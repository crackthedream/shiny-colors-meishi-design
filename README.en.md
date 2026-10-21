# Shiny Colors Producer Card Design

**闪耀色彩小偶像担当名片公式化设计**

[简体中文](README.md) · [Skill](skills/shiny-colors-meishi-design/SKILL.md) · [Examples](examples/README.en.md)

This project grew out of designing producer exchange cards for Hiori Kazano and Rinze Morino from **THE IDOLM@STER SHINY COLORS**. Several questions kept coming back during revisions: does the producer's name actually belong in the composition? Does each card feel like its character and chosen artwork? Are the type and spacing doing enough?

<!-- Optional personal note: add why you wanted to make these cards or share this project. -->

The useful parts of that process are collected here as an installable Agent Skill, with two examples and editable starting points. The “formula” in the Chinese title is the sequence of research, selection, design, and revision. The colors, shapes, type, and layout still need to come from each card.

## Two examples from the project

### Flowing summer · Hiori Kazano

![Anonymous flowing-summer card pair](examples/flowing-summer/preview.png)

The sky, pose, and flowing lines give the front its direction. The angled name area follows that movement; the back carries the color and rhythm into a composition of its own.

<!-- Optional personal note: add your favorite detail in this pair or a change that made it work for you. -->

### Dress bookplate · Rinze Morino

![Anonymous dress-bookplate card pair](examples/dress-bookplate/preview.png)

This pair takes its blue and cream palette, fine borders, and small floral accents from the outfit and scene. The spacing and proportions give the name, title, and decorative details their places on the card.

<!-- Optional personal note: add what you wanted to express about Rinze or why this artwork appealed to you. -->

Both previews use **示例制作人** (“Sample Producer”) and have no contact details. The previews include third-party character artwork. The four editable SVGs use original graphics and image-placement guides, with no official artwork, signatures, or unit-logo assets bundled. Sources, font suggestions, and replacement notes are in the [example guide](examples/README.en.md) and [third-party notices](THIRD_PARTY_NOTICES.md).

## How a project usually goes

Start with the character and what you want the cards for. The agent researches the character and artwork, looks at the images, and prepares numbered candidates. You choose the artwork and how many cards to make. If those choices are already settled, it carries them forward.

The agent can find and download publicly accessible artwork, or work with images you supply. It records both the official reference page and the actual download source, including whether an image came from a community mirror.

The first design is usually one front-and-back pair. Pose, clothing, environment, color, and available space guide the layout. The producer name, character identity, and title are part of that composition. The back uses typography, vector graphics, and space by default; AI illustration is only used when you explicitly ask for it.

From there, you give feedback and the agent revises the pair before extending the collection. Each card keeps its own visual character. Only personal details you supply and want displayed are added; empty fields and their labels disappear, and the spacing is adjusted. The final handoff includes editable sources, previews, the agreed exports, and a record of sources and checks.

The skill supplies instructions, examples, and a small optional checking tool. Research, editing, and rendering use the capabilities of the agent running it.

## Try it

In Codex, ask an agent with GitHub skill installation support:

```text
Use $skill-installer to install:
https://github.com/crackthedream/shiny-colors-meishi-design/tree/main/skills/shiny-colors-meishi-design
```

You can also download the repository and copy the complete `skills/shiny-colors-meishi-design` folder into `~/.codex/skills/`, or the `skills/` subdirectory of your configured `CODEX_HOME`. Keep that folder intact so its references, templates, and tools remain available. Invoke it in the next conversation turn.

Other agents that support `SKILL.md` can load the same folder through their own installation method. Tool availability varies by client; there is no dependency on a particular browser plugin or fixed local path.

For a new project:

```text
$shiny-colors-meishi-design
I want long-term producer exchange cards for Rinze Morino.
Research the character and show me numbered artwork candidates first.
Let me choose before you design. Use official artwork on the front
and typography with vector graphics on the back. Start with one front/back pair.
Leave personal information out for now.
```

Or bring an existing design:

```text
$shiny-colors-meishi-design
Check whether the character, title, and producer name work together.
Keep the agreed visual direction, but improve the type and spacing.
Remove any contact fields I haven't filled in.
```

## Where to find things

| If you want to… | Open… |
| --- | --- |
| Read the skill's instructions | [SKILL.md](skills/shiny-colors-meishi-design/SKILL.md) |
| Follow the full process | [English workflow](skills/shiny-colors-meishi-design/references/design-workflow.en.md) / [中文流程](skills/shiny-colors-meishi-design/references/design-workflow.zh-CN.md) |
| Edit one of the four SVG starting points | [Templates](skills/shiny-colors-meishi-design/assets/templates) |
| Check an SVG or outline its text | [Tool guide](skills/shiny-colors-meishi-design/references/svg-tools.md) |
| Look up example sources and fonts | [English notes](examples/README.en.md) / [中文说明](examples/README.zh-CN.md) |

## Before printing

The examples use a finished size of **85.60 × 53.98 mm**. For an actual order, confirm the size, corner radius, safe area, bleed, and export requirements with your printer. These are editable design examples; printer-specific preparation and a visual check of every face are still needed. A high DPI setting cannot add detail missing from the source image.

The optional Python tool checks SVG dimensions, font coverage, and safe margins for supported text, and can convert that text to outlines. It does not assess the design's appearance or certify a file for print. After outlining, render the result and compare the text, positions, cropping, and images with the source.

<details>
<summary>Running the optional SVG tool</summary>

The design process works without these scripts. To use the tool:

```bash
python -m pip install -r skills/shiny-colors-meishi-design/requirements.txt
python skills/shiny-colors-meishi-design/scripts/svg_text_tools.py --help
```

It supports a documented subset of SVG text, reports unsupported structures, and uses fonts you supply. See the [tool guide](skills/shiny-colors-meishi-design/references/svg-tools.md) for commands and limits.

For maintenance, run `python tests/test_svg_text_tools.py` from the repository root. The tests cover dimensions, missing glyphs, margins, image preservation during outlining, and rejection of unsupported structures. They create temporary test glyphs and need no font downloads.

</details>

## Reusing and contributing

The original instructions, scripts, and layouts without official artwork are available under the [MIT License](LICENSE). Third-party character images, game names, and trademarks remain outside that license; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). This is an unofficial project with no affiliation to the rights holders.

The public package leaves out participants' real names, contact details, original conversations, personal directories, font binaries, and the complete artwork collection. Personal information you add belongs to your own card project. Please remove it before sharing files or contributing changes here.