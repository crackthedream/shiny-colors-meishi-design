#!/usr/bin/env python3
"""Inspect and outline a deliberately small, offline SVG text subset.

No renderer or font discovery is involved. Fonts are supplied in a JSON map.
Use a shaping-capable design tool for text outside the documented subset.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

SVG = "{http://www.w3.org/2000/svg}"
ET.register_namespace("", SVG[1:-1])
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
NUMBER = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?"
CSS_ONLY = {"font-kerning", "font-variant-ligatures"}
DEFINITION_CONTAINERS = {SVG + name for name in ("defs", "clipPath", "mask", "pattern", "marker", "symbol", "filter")}
INHERITED = {
    "font-family", "font-size", "font-weight", "font-style", "font-stretch",
    "font-kerning", "font-variant-ligatures", "letter-spacing", "word-spacing",
    "text-anchor", "fill", "stroke", "stroke-width", "fill-opacity",
    "stroke-opacity", "dominant-baseline", "alignment-baseline", "writing-mode",
    "direction", "unicode-bidi", "visibility", "display",
}
FONT_KEYS = {k for k in INHERITED if k.startswith("font-")} | {
    "letter-spacing", "word-spacing", "text-anchor", "dominant-baseline",
    "alignment-baseline", "writing-mode", "direction", "unicode-bidi",
}


def number(value: str | None, default: float = 0) -> float:
    if value is None:
        return default
    if not re.fullmatch(NUMBER + r"(?:px)?", value.strip()):
        raise ValueError(f"Expected a single SVG user-unit value, got {value!r}")
    result = float(value.strip().removesuffix("px"))
    if not math.isfinite(result):
        raise ValueError("Numeric values must be finite")
    return result


def millimeters(value: str | None) -> float:
    if value is None or not re.fullmatch(NUMBER + "mm", value.strip()):
        raise ValueError("Root width and height must be explicit positive mm values")
    result = float(value.strip()[:-2])
    if not math.isfinite(result) or result <= 0:
        raise ValueError("Physical dimensions must be positive and finite")
    return result


def properties(element: ET.Element, inherited: dict) -> dict:
    result = dict(inherited)
    # These two CSS properties are not effective SVG presentation attributes in
    # browsers. Only inherited inline declarations can satisfy their contract.
    result.update({k: v for k, v in element.attrib.items() if k in INHERITED - CSS_ONLY})
    for declaration in element.get("style", "").split(";"):
        if not declaration.strip():
            continue
        key, separator, value = declaration.partition(":")
        key, value = key.strip().lower(), value.strip().lower()
        if not separator or key not in CSS_ONLY or value != "none":
            raise ValueError("Inline CSS only supports font-kerning:none and font-variant-ligatures:none; use presentation attributes for other supported properties")
        result[key] = value
    unsupported_layout = {
        "font", "font-variant", "font-feature-settings", "font-variation-settings",
        "font-variant-caps", "font-variant-numeric", "font-variant-east-asian",
        "font-variant-position", "font-language-override", "text-decoration",
        "text-transform", "baseline-shift", "kerning", "glyph-orientation-vertical",
        "glyph-orientation-horizontal", "text-orientation", "white-space",
    }
    if unsupported_layout.intersection(element.attrib):
        raise ValueError("Unsupported text-layout attribute: " + ", ".join(sorted(unsupported_layout.intersection(element.attrib))))
    return result


def image_fingerprints(root: ET.Element) -> list[str]:
    return [hashlib.sha256(ET.tostring(e, encoding="utf-8")).hexdigest()
            for e in root.iter(SVG + "image")]


def load_fonts(mapping_path: Path) -> dict[str, TTFont]:
    mapping = json.loads(mapping_path.read_text(encoding="utf-8-sig"))
    if not isinstance(mapping, dict) or not mapping:
        raise ValueError("Font map must be a nonempty family-to-file JSON object")
    fonts = {}
    try:
        for family, filename in mapping.items():
            if not isinstance(family, str) or not isinstance(filename, str):
                raise ValueError("Each font map key and filename must be a string")
            font = TTFont(mapping_path.parent / filename)
            fonts[family] = font
            if "fvar" in font:
                raise ValueError(f"{family}: use a static font instance, not a variable font")
            if any(table in font for table in ("COLR", "CBDT", "sbix", "SVG ")):
                raise ValueError(f"{family}: color glyph fonts are unsupported")
    except Exception:
        for font in fonts.values():
            font.close()
        raise
    return fonts


def supported_characters(text: str) -> None:
    for char in text:
        cp = ord(char)
        # Basic Latin, CJK punctuation, kana, Han, fullwidth forms, and punctuation.
        ranges = ((0x20, 0x7E), (0x2000, 0x206F), (0x3000, 0x30FF),
                  (0x31F0, 0x31FF), (0x3400, 0x4DBF), (0x4E00, 0x9FFF),
                  (0xF900, 0xFAFF), (0xFF01, 0xFFEF), (0x20000, 0x323AF))
        if unicodedata.category(char).startswith(("M", "C")) or not any(a <= cp <= b for a, b in ranges):
            raise ValueError(f"U+{cp:04X} needs unsupported shaping or script handling")


def text_geometry(element: ET.Element, props: dict, fonts: dict) -> tuple:
    if len(element):
        raise ValueError("Use single text nodes; tspan and textPath are unsupported")
    if any(key in element.attrib for key in ("rotate", "textLength", "lengthAdjust")):
        raise ValueError("rotate and textLength/lengthAdjust are unsupported")
    text = element.text or ""
    if not text.strip():
        raise ValueError("Empty text fields must be removed before export")
    if text.startswith(" ") or text.endswith(" ") or "  " in text:
        raise ValueError("Normalize leading, trailing and repeated ASCII spaces before export")
    supported_characters(text)
    if props.get("font-kerning") != "none" or props.get("font-variant-ligatures") != "none":
        raise ValueError('Set style="font-kerning:none;font-variant-ligatures:none" on text or an ancestor; presentation attributes alone do not disable browser kerning and ligatures')
    for key, allowed in {
        "font-style": {"normal"}, "font-stretch": {"normal"},
        "dominant-baseline": {"auto", "alphabetic"},
        "alignment-baseline": {"auto", "baseline", "alphabetic"},
        "writing-mode": {"horizontal-tb", "lr-tb"}, "direction": {"ltr"},
        "unicode-bidi": {"normal"}, "visibility": {"visible"},
        "display": {"inline", "block"},
    }.items():
        if key in props and props[key] not in allowed:
            raise ValueError(f"Unsupported {key}: {props[key]}")
    if props.get("stroke", "none") != "none":
        raise ValueError("Text strokes are unsupported for exact ink-bound checks")
    families = [s.strip().strip("\"'") for s in props.get("font-family", "").split(",")]
    family = next((f for f in families if f in fonts), None)
    if family is None:
        raise ValueError("No supplied font matches this text's font-family")
    font = fonts[family]
    if "font-weight" in props:
        weight = {"normal": 400, "bold": 700}.get(props["font-weight"])
        if weight is None:
            weight = number(props["font-weight"])
        actual = font["OS/2"].usWeightClass if "OS/2" in font else None
        if weight != actual:
            raise ValueError(f"{family}: font-weight {weight:g} does not match supplied font weight {actual}")
    cmap = font.getBestCmap() or {}
    missing = sorted(set(char for char in text if ord(char) not in cmap))
    if missing:
        raise ValueError("Missing glyphs: " + ", ".join(f"U+{ord(c):04X}" for c in missing))
    size = number(props.get("font-size"), 16)
    if size <= 0:
        raise ValueError("font-size must be positive")
    scale = size / font["head"].unitsPerEm
    spacing = number(props.get("letter-spacing") if props.get("letter-spacing") != "normal" else None)
    word_spacing = number(props.get("word-spacing") if props.get("word-spacing") != "normal" else None)
    glyph_set = font.getGlyphSet()
    names = [cmap[ord(char)] for char in text]
    advances = [font["hmtx"][name][0] * scale + (word_spacing if char == " " else 0)
                for char, name in zip(text, names)]
    # SVG anchoring includes the trailing letter-spacing after the final glyph.
    length = sum(advances) + spacing * len(text)
    anchor = props.get("text-anchor", "start")
    if anchor not in {"start", "middle", "end"}:
        raise ValueError(f"Unsupported text-anchor: {anchor}")
    cursor = number(element.get("x")) + number(element.get("dx"))
    cursor -= length if anchor == "end" else length / 2 if anchor == "middle" else 0
    baseline = number(element.get("y")) + number(element.get("dy"))
    boxes, paths = [], []
    for name, advance in zip(names, advances):
        glyph = glyph_set[name]
        pen, bounds_pen = SVGPathPen(glyph_set), BoundsPen(glyph_set)
        glyph.draw(pen)
        glyph.draw(bounds_pen)
        if pen.getCommands():
            paths.append({"d": pen.getCommands(), "transform":
                          f"translate({cursor:.10g} {baseline:.10g}) scale({scale:.10g} {-scale:.10g})"})
        if bounds_pen.bounds:
            x0, y0, x1, y1 = bounds_pen.bounds
            boxes.append((cursor + x0 * scale, baseline - y1 * scale,
                          cursor + x1 * scale, baseline - y0 * scale))
        cursor += advance + spacing
    bounds = None if not boxes else [min(b[0] for b in boxes), min(b[1] for b in boxes),
                                     max(b[2] for b in boxes), max(b[3] for b in boxes)]
    return family, bounds, paths


def process(args: argparse.Namespace) -> tuple[dict, ET.Element | None]:
    report = {"ok": False, "layout_model": "per-codepoint; no shaping or kerning",
              "safe_margin_mm": args.safe_mm, "text_checks": [], "errors": []}
    fonts = {}
    try:
        source = args.svg.read_bytes()
        if any(marker in source.upper() for marker in (b"<!DOCTYPE", b"<!ENTITY", b"<?XML-STYLESHEET")):
            raise ValueError("DTD, entity declarations and external stylesheets are unsupported")
        root = ET.fromstring(source)
        if root.tag != SVG + "svg":
            raise ValueError("Expected a namespaced SVG root")
        for element in root.iter():
            if element.tag in {SVG + "style", SVG + "script", SVG + "foreignObject", SVG + "use"}:
                raise ValueError("CSS stylesheets, script, foreignObject and use are unsupported")
            if any(k.split("}")[-1].lower().startswith("on") for k in element.attrib):
                raise ValueError("Event-handler attributes are unsupported")
        width, height = millimeters(root.get("width")), millimeters(root.get("height"))
        vb = [number(n) for n in re.split(r"[ ,]+", root.get("viewBox", "").strip())]
        if len(vb) != 4 or vb[2] <= 0 or vb[3] <= 0:
            raise ValueError("A valid viewBox is required")
        vx, vy, vw, vh = vb
        if not math.isclose(vw / vh, width / height, rel_tol=1e-4):
            raise ValueError("viewBox aspect ratio does not match physical dimensions")
        if args.expect_size and not all(math.isclose(a, b, abs_tol=.01) for a, b in zip((width, height), args.expect_size)):
            raise ValueError("Physical dimensions do not match --expect-size")
        if not math.isfinite(args.safe_mm) or not 0 <= args.safe_mm < min(width, height) / 2:
            raise ValueError("safe-mm must be nonnegative and smaller than half the short edge")
        sx, sy = args.safe_mm * vw / width, args.safe_mm * vh / height
        safe = [vx + sx, vy + sy, vx + vw - sx, vy + vh - sy]
        report.update(size_mm=[width, height], safe_box=safe)
        original_images = image_fingerprints(root)
        fonts = load_fonts(args.font_map)
        seen_fields = set()
        replacements = []

        def walk(parent: ET.Element, inherited: dict, blocked: bool = False, decorative: bool = False, in_definition: bool = False):
            props = properties(parent, inherited)
            blocked = blocked or any(parent.get(k) for k in ("transform", "clip-path", "mask", "filter"))
            decorative = decorative or parent.get("data-decorative") == "true"
            in_definition = in_definition or parent.tag in DEFINITION_CONTAINERS
            for element in parent:
                if element.tag != SVG + "text":
                    walk(element, props, blocked or element.tag == SVG + "svg", decorative, in_definition)
                    continue
                field = element.get("data-field")
                if field and not in_definition:
                    seen_fields.add(field)
                item = {"id": element.get("id"), "field": field}
                try:
                    if in_definition:
                        raise ValueError("Text inside non-rendering definition containers is unsupported")
                    p = properties(element, props)
                    if blocked or any(element.get(k) for k in ("transform", "clip-path", "mask", "filter")):
                        raise ValueError("Text transforms, clips, masks, filters and nested viewports are unsupported")
                    family, bounds, paths = text_geometry(element, p, fonts)
                    is_decorative = (decorative or element.get("data-decorative") == "true") and field not in args.require_field
                    inside = bounds is not None and all((bounds[0] >= safe[0] - 1e-6, bounds[1] >= safe[1] - 1e-6,
                                                         bounds[2] <= safe[2] + 1e-6, bounds[3] <= safe[3] + 1e-6))
                    item.update(font=family, bounds=bounds, decorative=is_decorative,
                                within_safe_area=None if is_decorative else inside)
                    if not inside and not is_decorative:
                        raise ValueError("Text ink lies outside the safe area")
                    attrs = {k: v for k, v in element.attrib.items() if k not in FONT_KEYS | {"x", "y", "dx", "dy"}}
                    attrs["aria-label"] = element.text or ""
                    for key in ("fill", "fill-opacity", "stroke", "stroke-opacity"):
                        if key in p:
                            attrs[key] = p[key]
                    group = ET.Element(SVG + "g", attrs)
                    group.tail = element.tail
                    for path in paths:
                        ET.SubElement(group, SVG + "path", path)
                    replacements.append((parent, element, group))
                except (ValueError, KeyError, TypeError) as exc:
                    item["error"] = str(exc)
                    report["errors"].append({"id": item["id"], "field": field, "error": str(exc)})
                report["text_checks"].append(item)

        walk(root, {})
        if not report["text_checks"]:
            report["errors"].append({"error": "No editable text nodes found; outlined artwork cannot prove original field checks"})
        for missing in sorted(set(args.require_field) - seen_fields):
            report["errors"].append({"field": missing, "error": "Required data-field is absent"})
        if not report["errors"]:
            if args.command == "outline":
                for parent, old, new in replacements:
                    index = list(parent).index(old)
                    parent.remove(old)
                    parent.insert(index, new)
            report["images_preserved"] = original_images == image_fingerprints(root)
            report["image_count"] = len(original_images)
            if not report["images_preserved"]:
                raise ValueError("Image elements changed unexpectedly")
        report["ok"] = not report["errors"]
        return report, root
    except Exception as exc:
        report["errors"].append({"error": str(exc)})
        return report, None
    finally:
        for font in fonts.values():
            font.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("inspect", "outline"))
    parser.add_argument("svg", type=Path)
    parser.add_argument("--font-map", type=Path, required=True, help="JSON family-to-file map; paths relative to map")
    parser.add_argument("--safe-mm", type=float, default=3.0)
    parser.add_argument("--expect-size", nargs=2, type=float, metavar=("WIDTH_MM", "HEIGHT_MM"))
    parser.add_argument("--require-field", action="append", default=[], help="Require a nonempty text data-field; repeat as needed")
    parser.add_argument("--output", type=Path, help="New SVG file, required for outline; existing files are never overwritten")
    parser.add_argument("--report", type=Path, help="Optional new JSON report file")
    args = parser.parse_args()
    if args.command == "outline" and not args.output:
        parser.error("outline requires --output")
    if args.command == "inspect" and args.output:
        parser.error("inspect does not accept --output")
    for destination in (args.output, args.report):
        if destination and destination.exists():
            parser.error("Output already exists; choose a new filename")
    if args.output and args.report and args.output.resolve() == args.report.resolve():
        parser.error("Output SVG and report must use different paths")
    report, root = process(args)
    try:
        if report["ok"] and args.command == "outline":
            # Exclusive creation also prevents overwriting a file created after validation.
            with args.output.open("xb") as stream:
                ET.ElementTree(root).write(stream, encoding="utf-8", xml_declaration=True)
        rendered = json.dumps(report, ensure_ascii=True, indent=2)
        if args.report:
            with args.report.open("x", encoding="utf-8") as stream:
                stream.write(rendered + "\n")
        print(rendered)
    except OSError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 2
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
