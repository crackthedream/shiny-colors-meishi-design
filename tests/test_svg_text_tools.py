"""Behavior checks for the portable SVG text helper; creates its own test font."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / 'skills/shiny-colors-meishi-design/scripts/svg_text_tools.py'
NS = '{http://www.w3.org/2000/svg}'


def build_font(path):
    chars = 'ABC123 '
    names = ['.notdef'] + ['space' if c == ' ' else c for c in chars]
    fb = FontBuilder(1000, isTTF=True)
    fb.setupGlyphOrder(names)
    fb.setupCharacterMap({ord(c): 'space' if c == ' ' else c for c in chars})
    glyphs = {}
    for name in names:
        pen = TTGlyphPen(None)
        if name != 'space':
            pen.moveTo((0, 0)); pen.lineTo((600, 0)); pen.lineTo((600, 700)); pen.lineTo((0, 700)); pen.closePath()
        glyphs[name] = pen.glyph()
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics({name: (300 if name == 'space' else 650, 0) for name in names})
    fb.setupHorizontalHeader(ascent=800, descent=-200)
    fb.setupNameTable({'familyName': 'SyntheticCardTest', 'styleName': 'Regular', 'uniqueFontIdentifier': 'SyntheticCardTest-Regular', 'fullName': 'SyntheticCardTest Regular', 'psName': 'SyntheticCardTest-Regular'})
    fb.setupOS2(sTypoAscender=800, sTypoDescender=-200, usWinAscent=800, usWinDescent=200, usWeightClass=400)
    fb.setupPost()
    fb.save(path)


SHAPING_STYLE = 'style="font-kerning:none;font-variant-ligatures:none"'
BASE = '''<svg xmlns="http://www.w3.org/2000/svg" width="85.6mm" height="53.98mm" viewBox="0 0 856 539.8" style="font-kerning:none;font-variant-ligatures:none" fill="#123456"><image x="0" y="0" width="10" height="10" href="data:image/png;base64,AAAA"/><text x="100" y="200" font-family="CardTest" font-size="40" data-field="producer">ABC 123</text></svg>'''


with tempfile.TemporaryDirectory(prefix='svg-tool-test-', dir=Path(__file__).parent) as temp:
    work = Path(temp)
    build_font(work / 'test.ttf')
    (work / 'fonts.json').write_text(json.dumps({'CardTest': 'test.ttf'}), encoding='utf-8')
    passed = []

    def run(name, svg=BASE, expected=0, command='inspect', extra=None):
        src = work / (name + '.svg'); src.write_text(svg, encoding='utf-8')
        before = hashlib.sha256(src.read_bytes()).hexdigest()
        args = [sys.executable, str(TOOL), command, str(src), '--font-map', str(work / 'fonts.json'), '--expect-size', '85.6', '53.98', '--require-field', 'producer']
        output = work / (name + '-outlined.svg')
        if command == 'outline': args += ['--output', str(output)]
        result = subprocess.run(args + (extra or []), capture_output=True, text=True, encoding='utf-8')
        assert result.returncode == expected, (name, result.returncode, result.stdout, result.stderr)
        assert hashlib.sha256(src.read_bytes()).hexdigest() == before
        report = json.loads(result.stdout) if result.stdout.strip() else None
        if expected and command == 'outline': assert not output.exists()
        passed.append(name)
        return report, output

    report, _ = run('simple_text')
    assert report['text_checks'][0]['bounds'] == [100.0, 172.0, 266.0, 200.0]
    report, output = run('outline_preserves_image', command='outline')
    root = ET.parse(output).getroot()
    assert not list(root.iter(NS + 'text'))
    original = ET.fromstring(BASE)
    assert [ET.tostring(e) for e in original.iter(NS + 'image')] == [ET.tostring(e) for e in root.iter(NS + 'image')]
    group = root.find(NS + 'g')
    assert group.get('aria-label') == 'ABC 123' and group.get('fill') == '#123456'
    assert len(list(group)) == 6
    report, _ = run('middle_anchor', BASE.replace('x="100" y="200"', 'x="400" y="200" text-anchor="middle"'))
    assert report['text_checks'][0]['bounds'] == [316.0, 172.0, 482.0, 200.0]
    report, output = run('middle_anchor_letter_spacing', BASE.replace('x="100" y="200"', 'x="400" y="200" text-anchor="middle" letter-spacing="4"'), command='outline')
    assert report['text_checks'][0]['bounds'] == [302.0, 172.0, 492.0, 200.0]
    assert ET.parse(output).getroot().find(NS + 'g').find(NS + 'path').get('transform').startswith('translate(302 ')
    report, _ = run('end_anchor_letter_spacing', BASE.replace('x="100" y="200"', 'x="400" y="200" text-anchor="end" letter-spacing="4"'))
    assert report['text_checks'][0]['bounds'] == [204.0, 172.0, 394.0, 200.0]
    report, _ = run('single_character_letter_spacing', BASE.replace('ABC 123</text>', 'A</text>').replace('x="100" y="200"', 'x="400" y="200" text-anchor="middle" letter-spacing="4"'))
    assert report['text_checks'][0]['bounds'] == [385.0, 172.0, 409.0, 200.0]
    run('text_inline_shaping', BASE.replace(' ' + SHAPING_STYLE, '').replace('<text ', '<text ' + SHAPING_STYLE + ' '))
    run('split_inherited_shaping', BASE.replace(SHAPING_STYLE, 'style="font-kerning:none"').replace('<text ', '<g style="font-variant-ligatures:none"><text ').replace('</text>', '</text></g>'))
    run('presentation_does_not_override_css', BASE.replace('<text ', '<text font-kerning="auto" font-variant-ligatures="normal" '))
    run('shaping_style_whitespace', BASE.replace(SHAPING_STYLE, 'style=" FONT-KERNING : NONE ; font-variant-ligatures : none ; "'))
    report, _ = run('presentation_only_rejected', BASE.replace(SHAPING_STYLE, 'font-kerning="none" font-variant-ligatures="none"'), 1, 'outline')
    assert any('presentation attributes alone' in error['error'] for error in report['errors'])
    report, _ = run('required_field_only_in_defs', BASE.replace('<text ', '<defs><text ').replace('</text>', '</text></defs>'), 1, 'outline')
    assert any('non-rendering definition' in error['error'] for error in report['errors'])
    assert any(error.get('field') == 'producer' and 'Required data-field is absent' in error['error'] for error in report['errors'])
    report, _ = run('required_overrides_decorative', BASE.replace('x="100" y="200"', 'x="0" y="200" data-decorative="true"'), 1, 'outline')
    assert any('safe area' in error['error'] for error in report['errors'])
    bad = {
        'unsafe_left': BASE.replace('x="100" y="200"', 'x="0" y="200"'),
        'missing_glyph': BASE.replace('ABC 123</text>', 'ABC 中</text>'),
        'missing_required': BASE.replace('data-field="producer"', 'data-field="other"'),
        'empty_field': BASE.replace('ABC 123</text>', '</text>'),
        'tspan': BASE.replace('ABC 123</text>', '<tspan>ABC</tspan></text>'),
        'text_transform': BASE.replace('<text ', '<text transform="translate(20 0)" '),
        'ancestor_transform': BASE.replace('<text ', '<g transform="translate(20 0)"><text ').replace('</text>', '</text></g>'),
        'definition_text_even_with_visible_field': BASE.replace('</svg>', '<defs><text x="100" y="200" font-family="CardTest" font-size="40">ABC</text></defs></svg>'),
        'css_stylesheet': BASE.replace('<text ', '<style>text { fill:red }</style><text '),
        'inline_style': BASE.replace('<text ', '<text style="fill:red" '),
        'font_weight_mismatch': BASE.replace('<text ', '<text font-weight="700" '),
        'wrong_dimensions': BASE.replace('width="85.6mm"', 'width="90mm"'),
        'unitless_dimensions': BASE.replace('width="85.6mm"', 'width="856"'),
        'text_stroke': BASE.replace('<text ', '<text stroke="red" '),
        'emoji': BASE.replace('ABC 123</text>', 'ABC 😀</text>'),
        'kerning_not_disabled': BASE.replace('font-kerning:none;', ''),
        'ligatures_not_disabled': BASE.replace(';font-variant-ligatures:none', ''),
        'inline_shaping_override': BASE.replace('<text ', '<text style="font-kerning:auto" '),
        'inline_shaping_extra_property': BASE.replace(SHAPING_STYLE, 'style="font-kerning:none;font-variant-ligatures:none;fill:red"'),
        'inline_shaping_malformed': BASE.replace(SHAPING_STYLE, 'style="font-kerning none;font-variant-ligatures:none"'),
        'inline_shaping_important': BASE.replace(SHAPING_STYLE, 'style="font-kerning:none!important;font-variant-ligatures:none"'),
        'duplicate_spaces': BASE.replace('ABC 123</text>', 'ABC  123</text>'),
        'unsupported_variant': BASE.replace('<text ', '<text font-variant="small-caps" '),
        'external_stylesheet': '<?xml-stylesheet type="text/css" href="anything.css"?>' + BASE,
        'dtd': '<!DOCTYPE svg []>' + BASE,
    }
    for name, svg in bad.items():
        report, _ = run(name, svg, 1, 'outline')
        assert not report['ok'] and report['errors']
    # Existing destination must remain byte-identical.
    destination = work / 'keep.svg'; destination.write_text('KEEP', encoding='utf-8')
    result = subprocess.run([sys.executable, str(TOOL), 'outline', str(work / 'simple_text.svg'), '--font-map', str(work / 'fonts.json'), '--output', str(destination)], capture_output=True)
    assert result.returncode == 2 and destination.read_text(encoding='utf-8') == 'KEEP'
    passed.append('exclusive_output')
    (work / 'bad-font-map.json').write_text('{broken', encoding='utf-8')
    result = subprocess.run([sys.executable, str(TOOL), 'inspect', str(work / 'simple_text.svg'), '--font-map', str(work / 'bad-font-map.json')], capture_output=True, text=True)
    assert result.returncode == 1 and not json.loads(result.stdout)['ok']
    passed.append('bad_font_map')
    print(json.dumps({'ok': True, 'count': len(passed), 'cases': passed}, indent=2))
