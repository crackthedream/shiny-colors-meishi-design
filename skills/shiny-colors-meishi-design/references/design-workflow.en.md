# Design workflow: repeat the process, compose for the character and artwork

For producer and idol-support exchange cards for THE IDOLM@STER Shiny Colors. Chinese counterpart: [design-workflow.zh-CN.md](design-workflow.zh-CN.md). Use this method for a new design, a single-card revision, or a collection. When continuing an existing project, resume at the unfinished stage.

## 1. Define this assignment

Extract the character, purpose, selected artwork, quantity, front/back content, permitted composition changes, versions to preserve, and delivery formats from the current request and settled decisions. Purpose affects information density: everyday exchange cards, birthday editions, and event editions need their own content choices.

Ask only about decisions that change the design. When the user wants research before selection, deliver a selection sheet first. When the artwork is specified, verify it without repeating selection. One front/back prototype is the default way to test a method before expanding a set; honor existing authorization to proceed with a full set. Routine layout adjustments do not each need a new approval step.

Use the user's or printer's dimensions. Without specifications, propose 85.60 × 53.98 mm, a 3.18 mm corner radius, and a 3 mm text safety inset as the example starting point, explicitly making them adjustable. Address bleed, stock, color configuration, and duplex orientation against actual requirements when preparing production files.

**Done when:** the scope is actionable and the few outstanding user decisions are identified. An unanswered choice is not an approved choice.

## 2. Research to support a choice

The agent actively finds publicly accessible official character introductions, game/event pages, promotional material, and card information, and may retrieve available images. Do not make finding assets the user's default responsibility. Verify the character, original card title, variant, and franchise against specific sources. Search thumbnails help locate an image; inspect a clearer image for the actual analysis.

When only a community gallery provides the required variant, label it as a community mirror and separately record official evidence that confirms the title. The verification page and the downloaded image may come from different sites; record both. Mark inaccessible or unverified material accordingly rather than converting an inference into a fact. Preserve attribution and copyright marks supplied with the material.

Keep a lightweight record for each candidate:

| Field | Purpose |
| --- | --- |
| Stable ID, character, original card title, variant | Make a selection such as “02B” unambiguous; explain what A/B mean in the sheet |
| Page URL, image URL, source category, verification date | Distinguish official hosting, mirror hosting, and unverified provenance |
| Dimensions and actual inspection status | Explain whether resolution is adequate and whether analysis is based on the image |
| Main colors, mood, character/setting relationship | Explain suitability for this character and use |
| Crop risks and usable information areas | Protect the face, gestures, important props, and narrative relationships |
| Cues for the back | Derive graphics from clothing, light, flowers, architectural rhythm, or similar details |

Place images beside recommendations so the user can compare them directly. Compare complementary moods, compositions, and colors when proposing a set. Let quantity and themes emerge from selection rather than assigning every character to seasons or a uniform traditional-Japanese style.

**Done when:** candidate images have been inspected, IDs are accurate, source categories are clear, and the user can make a choice. Record the exact variant after selection.

## 3. Derive a visual language from the selected image

Write a short design intention: identify the most distinctive cue, how each face uses it, and how the name and contact information participate. Reinspect each image even for the same character; stage energy, everyday warmth, cool restraint, and playfulness may coexist.

| Image cue | Possible graphic treatment | What makes it work |
| --- | --- | --- |
| Wind, hair movement, diagonal light | Curves, color bands, a diagonal information area | Direction echoes the image while key information remains readable |
| Clothing trim, embroidery, fabric layers | Fine borders, local ornaments, spacing and layering | Details remain selective; an enlarged skirt silhouette does not carry the entire back |
| Architectural perspective or window frames | Receding borders, offset frames, rhythmic spacing | Proportion changes create depth instead of mechanical equal repetition |
| Water, rain, flowers, light spots | Groups of lines, abstract petals, restrained color accents | The result can be traced to this image rather than generic decoration |

These are derivation examples, not a menu. Connect a set through information hierarchy, typographic roles, margins, and production quality. Allow the main graphic, color proportions, negative space, and title direction to differ. When learning from another character's design, carry over the method and establish why the new composition fits this artwork.

## 4. Design the front as a whole

Test the crop at the finished aspect ratio before placing type. Arrange the visual focus of character and setting according to the selected direction: emphasize the character or let both share the composition. Keeping the face inside the frame does not guarantee a complete composition. A reflection, extended hand, or relationship to a light source can be essential.

Use existing negative space or reorganize the image through shaped color areas, side panels, fine frames, or local overlays. Their directions and proportions should relate to the movement in the image. A busy dark background may still be unsuitable for small type, and bright light spots are not stable negative space. Judge contrast from the rendered result.

Give character name, card title, producer identity, and decorative lettering distinct roles. When identity is central to the card, give the producer name and idol-support line sufficient weight. A long title can become a rhythmic group of lines. A shared bottom strip is one possible treatment, not a default solution for every image.

Cropping, scaling, and separate information layers can alter the composition; retain the original image and its source marks. When the user requests an unchanged illustration, separate it from the new layout and check that its content survives export.

## 5. Design the back and typography together

Default to editable type, lines, color fields, and vector patterns. Abstract selected image cues into a composition with clear priorities, letting type and graphics share the focus. Use an official signature or unit mark sparingly when relevant and available, and record its source.

Choose the reading order of name, idol-support line, title, and contacts before choosing fonts. Information type and display type have different jobs; Chinese and Japanese text require the actual corresponding glyphs. Inspect thin or pale text near physical size so a design that looks delicate on a large screen remains readable when small. Check italic, script, and special weights against real font files rather than trusting system fallback.

Handle font files, subsets, outlines, and embedding under their respective licenses. Keep live text in the editable SVG. Save a separate outlined copy when fixed appearance is needed, preserving the editable original.

Add an AI-image branch only after an explicit user request. Record which assets are generated and which are official, and distinguish an illustrated variant from the primary graphic edition. Generated imagery does not automatically become the default for future cards.

## 6. Review and iterate a prototype

Choose one front/back pair that tests the current design difficulty: the busiest artwork, the hardest placement for type, or the strongest expression of the user's taste. Show both faces at the same size each round, with one or two sentences identifying the image cue and the concrete change.

Translate feedback into observable revisions:

- For “mechanical,” inspect proportions, alignment, repeated spacing, and whether the type is merely attached. Adjust hierarchy and composition instead of adding decoration as a patch.
- For “rough,” inspect graphic completeness, curve endings, density, and detail scale. Retain necessary cues and reduce arbitrary geometric clutter.
- For “not like this character,” return to this image's clothing, expression, setting, and colors, then derive the design again rather than importing the previous character's treatment.
- For “soft but striking,” create emphasis through hierarchy, light/dark relationships, shape rhythm, and space; lowering saturation alone is insufficient.

Record which faces are retained and which change in each round. After the prototype is accepted, expand the set while handling every crop and text placement individually. Revising one face should not silently change another approved face.

**Done when:** the user has accepted the prototype direction or authorized the corresponding full-set work, and each face has an explainable relationship to its source image.

## 7. Apply personal information and assemble delivery

Allow name, idol-support line, contacts, social accounts, and short statements according to the request. Contact count and platform are not fixed. If a field is absent or intentionally omitted, remove its label, placeholder, and redundant separators, then reposition remaining content. Do not fill space with asterisks, ellipses, or invented account numbers. Teaching examples may use an explicit sample identity and reserved domains.

After applying real information, check the longest strings, missing glyphs, and contrast. Regenerate SVGs, outlined copies, PNGs, overview sheets, and delivery inventories together. Editing and saving an HTML preview does not update previously exported images; make that distinction clear.

For public reference editions, export again from clean example data. Inspect visible text and SVG `aria-label`/`title`/`desc`, HTML templates, script constants, JSON reports, raster pixels, and metadata. Actual contacts, producer nicknames, private paths, and conversation logs must stay outside the public package. A text scan alone cannot establish that a raster image has been anonymized.

## 8. Export and verification limits

Preserve editable sources and front/back review images at minimum. Provide outlined SVG, PNG, PDF, imposed sheets, or other formats according to the agreement. Compute pixel dimensions from physical dimensions and the target resolution. Increasing export DPI does not recover detail absent from the source image.

Inspect every face for consistent identity/contact data, no empty labels or placeholders, complete glyph coverage, no overflowing text, no unintended crop of important anatomy or objects, sufficient text/background contrast, and correct front/back pairing. A collection overview reveals relationships; enlarged individual faces reveal details. Review both.

The bundled [SVG text tool](svg-tools.md) can inspect or outline supported horizontal single-run text, using an explicit font map to report glyph coverage and actual glyph bounds. Unsupported features such as `tspan`, complex shaping, text/ancestor transforms, CSS stylesheets, or additional inline styles must produce an unsupported-layout result. For those layouts, use an editor/renderer that shapes them accurately, or simplify the structure without changing the design intention, then render and inspect again. Do not report a partial check as a complete pass.

An inset such as 3 mm is a setting for the current design. The tool does not establish visual balance, decorative quality, background contrast, or compliance with a printer's requirements. Disclose browser interactions that were not actually tested. An RGB proof at finished dimensions is not automatically a print file with bleed, color conversion, and duplex imposition.

**Finally done when:** delivery points to the latest files, all fronts and backs are visible, personal fields agree, sources and third-party boundaries are clear, and tested/untested aspects are stated. Preserve approved originals and keep historical iterations separate from the current delivery.
