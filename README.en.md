# Shiny Colors Producer Card Design

**闪耀色彩小偶像担当名片公式化设计**

[简体中文](README.md) · [Skill entry point](skills/shiny-colors-meishi-design/SKILL.md) · [Examples](examples/README.en.md)

An installable Agent Skill for researching and designing character-focused producer exchange cards for **THE IDOLM@STER SHINY COLORS**. It covers artwork selection, front-and-back composition, typography, iteration, optional personal information, and export checks.

**“Formulaic” means a repeatable process.** The palette, motifs, type, and composition should come from the selected character and artwork. The same process should produce distinct designs.

## What it does

- Research character information and artwork sources, then present numbered candidates for the user to select.
- Analyze pose, environment, clothing, color, and available space; develop one complete front-and-back sample before expanding a collection.
- Integrate the producer name, character identity, and title into the composition. Default to typography, vector graphics, and negative space on the back.
- Include only personal details explicitly supplied by the user. Remove unfilled fields and rebalance their space.
- Deliver editable sources, previews, and appropriate exports, identifying what was checked and what still depends on a printer's specifications.

The agent may research and download artwork or use supplied images. Record the **official reference page** separately from the **actual download source**, and identify community mirrors accurately. AI illustration generation is an optional branch activated only by an explicit request.

## Two composition examples

### Flowing summer

![Anonymous flowing-summer card pair](examples/flowing-summer/preview.png)

The pose, sky, and flowing lines establish the composition. An angled identity area follows that movement, while the reverse carries its palette and rhythm forward.

### Dress bookplate

![Anonymous dress-bookplate card pair](examples/dress-bookplate/preview.png)

Blue, cream, delicate borders, and floral accents are drawn from the outfit and scene. Proportion and spacing establish the hierarchy.

Both previews use the generic Chinese label **示例制作人** (“Sample Producer”) and contain no contact details. **Third-party character artwork appears only in the demonstration previews. Editable templates use original graphics and image-placement guides; no official artwork, signature, or unit-logo assets are bundled.** See the [example notes](examples/README.en.md) and [third-party notices](THIRD_PARTY_NOTICES.md) for sources, font suggestions, and replacement instructions.

## Installation

### Codex

Ask an agent with GitHub skill installation support:

```text
Use $skill-installer to install:
https://github.com/crackthedream/shiny-colors-meishi-design/tree/main/skills/shiny-colors-meishi-design
```

Alternatively, download this repository and copy the complete `skills/shiny-colors-meishi-design` folder into `~/.codex/skills/`, or the `skills/` subdirectory of a configured `CODEX_HOME`. Keep the folder intact so that references, templates, and tools remain available through relative paths. Invoke it in the next conversation turn.

Other agents supporting `SKILL.md` can load this folder using their own installation mechanism. Tool availability varies by client; the skill does not depend on a particular browser plugin or a fixed local path.

### Start a project

```text
$shiny-colors-meishi-design
I want long-term producer exchange cards for Rinze Morino.
Research the character and present numbered artwork candidates first.
Let me select the artwork before designing. Use official artwork on the front
and typography with vector graphics on the back. Start with one front/back pair.
Leave personal information out for now.
```

For an existing design:

```text
$shiny-colors-meishi-design
Review whether the character, title, and producer identity form one composition.
Preserve the approved visual direction while improving type and spacing.
Remove any contact fields that have not been filled in.
```

## Contents

| Resource | Location |
| --- | --- |
| Skill entry point | [SKILL.md](skills/shiny-colors-meishi-design/SKILL.md) |
| Full Chinese workflow | [design-workflow.zh-CN.md](skills/shiny-colors-meishi-design/references/design-workflow.zh-CN.md) |
| Full English workflow | [design-workflow.en.md](skills/shiny-colors-meishi-design/references/design-workflow.en.md) |
| Four editable SVG templates | [assets/templates](skills/shiny-colors-meishi-design/assets/templates) |
| SVG inspection and text outlining | [Tool guide](skills/shiny-colors-meishi-design/references/svg-tools.md) |
| Examples and sources | [English](examples/README.en.md) / [中文](examples/README.zh-CN.md) |

## Optional checks

The design workflow does not require running scripts. The included Python utility can inspect SVG dimensions, font coverage, and safe margins for supported simple text:

```bash
python -m pip install -r skills/shiny-colors-meishi-design/requirements.txt
python skills/shiny-colors-meishi-design/scripts/svg_text_tools.py --help
```

The utility supports a documented subset of SVG text and uses fonts supplied by the user. Unsupported structures are reported. **Passing these checks does not establish visual quality or print readiness.** Render and compare outlined output to check glyphs, placement, cropping, and imagery. Exact commands are in the [tool guide](skills/shiny-colors-meishi-design/references/svg-tools.md).

The templates use an example finished size of **85.60 × 53.98 mm**. Confirm dimensions, corner radius, safe area, bleed, and printer specifications for each real project. A high DPI tag cannot add detail to an image. These templates are not universal press-ready files.

Maintainers can run `python tests/test_svg_text_tools.py` from the repository root to check dimensions, missing glyphs, margins, image preservation during outlining, and rejection of unsupported structures. Tests create their own temporary glyphs and require no font downloads.

## License and privacy

Original instructions, scripts, and artwork-free layouts are available under the [MIT License](LICENSE). Third-party character images, game names, and trademarks are excluded; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). This is an unofficial design-workflow reference and is not affiliated with the rights holders.

The repository contains no project participant's real name, contact information, original conversations, personal directories, font binaries, or complete artwork collection. Personal details entered while using the skill belong to that local project and should not accompany contributions to this public repository.
