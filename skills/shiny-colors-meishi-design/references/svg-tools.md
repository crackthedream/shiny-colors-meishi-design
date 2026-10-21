# SVG 文字检查与转曲 / SVG text inspection and outlining

在需要检查成品尺寸、缺字、文字安全距离或交付转曲 SVG 时读取本页。工具仅处理明确的静态文字子集；审美、印厂要求与最终视觉效果仍需另行核对。

## 本地准备

Python 3.10 或更新版本。在技能目录运行：

```sh
python -m pip install -r requirements.txt
```

字体由使用者提供，不随技能分发，不会自动下载。为每个真实字体文件设置独立的 SVG `font-family` 名称；粗体应映射到实际粗体文件，不依赖合成粗体。建立本地 `font-map.json`：

```json
{
  "CardSerif": "fonts/card-serif-regular.ttf",
  "CardSans": "fonts/card-sans-regular.otf"
}
```

相对路径以这个 JSON 文件所在目录为基准。字体文件可为静态 TTF 或 OTF；可变字体需先在其他工具中生成所需轴值的静态实例。示例文件名仅说明结构，仓库不包含这些字体。

## 输入要求

SVG 根节点声明命名空间、正数 `width="85.6mm"`、`height="53.98mm"` 和比例一致的 `viewBox`；尺寸可以改为实际需要的值。在根节点以行内 CSS 明确关闭 kerning 和 ligatures，使文字继承；同名 SVG 属性不视为有效关闭：

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="85.6mm" height="53.98mm"
     viewBox="0 0 856 539.8"
     style="font-kerning:none;font-variant-ligatures:none">
  <text x="80" y="300" font-family="CardSans" font-size="30"
        data-field="producer">Sample Producer</text>
</svg>
```

除上述两项排版开关使用行内 CSS 外，其余使用直接呈现属性，位置与字号采用单个 SVG 用户单位数值。工具按字符字形的实际墨迹范围检查安全距离，支持 `text-anchor`、字距、词距和 `dx`/`dy`。常见汉字、假名、基本拉丁字符、全角字符和标点可用；必须已存在于指定字体中。

给必须保留的信息添加 `data-field`，名称由使用者决定。用 `data-decorative="true"` 可将装饰文字排除在安全距离检查外；缺字检查仍会运行，命令明确要求的字段也始终检查安全距离。没有内容的字段应直接移除，不保留星号或空文本占位。

## 运行

```sh
python scripts/svg_text_tools.py inspect card.svg --font-map font-map.json --expect-size 85.6 53.98 --safe-mm 3 --require-field producer --report inspect-report.json
python scripts/svg_text_tools.py outline card.svg --font-map font-map.json --expect-size 85.6 53.98 --safe-mm 3 --require-field producer --output card-outlined.svg --report outline-report.json
```

需要联系信息时，再加 `--require-field contact`，并在实际联系文字上设置 `data-field="contact"`。不要强制所有名片都包含相同的联系项目。

通过时退出码为 0；检查失败为 1；参数或文件写入失败为 2。转曲只在全部检查通过后写出新 SVG，不覆盖已有文件。JSON 报告默认打印到终端，`--report` 可额外保存。报告不复制卡面的姓名和联系文本，但错误可能包含用户提供的文件路径；对外分享前仍需检查报告。

## 边界

- 这是逐字符轮廓工具，不是浏览器文字排版引擎。要求用行内 CSS 明确关闭 kerning 和 ligatures；不支持复杂文字塑形、合字、组合附加符号、emoji、竖排或双向文字。遇到这些内容，应在支持塑形的设计软件中转曲和检查。
- 不支持 `tspan`、`textPath`、定义容器中的文字、文本或祖先变换、嵌套视口、文字描边、裁剪、蒙版、滤镜、`textLength`、CSS 样式表、上述两项开关以外的行内样式、`use`、脚本或事件处理。将简单样稿整理为呈现属性，或改用完整设计工具；不要为了让检查通过而删掉必要的视觉效果。
- 图片元素的属性、引用和内嵌数据保留，工具不会读取、下载或上传图片资源。外链图片仍是外链；搬运文件时需另行处理其可移植性。XML 序列化可能改变排版与命名空间写法，保留的不是源文件逐字节格式。
- 转曲 SVG 的 `aria-label` 保留原文字，以便辅助技术读取。公开脱敏必须发生在转曲之前；转曲不是删除个人信息的方法。
- 安全范围以成品的矩形边界向内收缩计算。工具不计算圆角刀模、出血、打印机色彩、图片分辨率、字的最小可读尺寸或字体许可；这些项目需要真实预览与印厂规格。
- 对已有转曲稿运行检查，无法复原原始字段信息，因此不会将没有文字节点的稿件判为通过。保留可编辑源 SVG 和字体映射以便重新导出。

## English — local setup

Read this reference when checking final dimensions, missing glyphs, text safety margins, or producing outlined SVG. The utility handles an explicit static text subset. Design judgment, production requirements and final appearance require separate review.

Use Python 3.10 or newer. From the skill directory, run the same installation command shown above: `python -m pip install -r requirements.txt`.

Supply your own fonts; the utility neither bundles nor downloads them. Give each actual font file its own SVG `font-family` alias, including separate aliases for real bold variants. Create `font-map.json` using the JSON example above. Relative paths resolve from that JSON file's directory. Static TTF and OTF fonts are supported; use another tool to instantiate variable fonts at your intended axis values first. The example filenames explain the structure and do not identify bundled fonts.

## English — input contract

The SVG root must declare the SVG namespace, positive dimensions in millimeters, and a proportionally matching `viewBox`. The XML example above illustrates a card measuring 85.6 × 53.98 mm; use the dimensions appropriate to your task. Set `style="font-kerning:none;font-variant-ligatures:none"` on the root or each text node. The same-named SVG attributes alone do not establish effective browser settings.

Apart from the two inline CSS layout switches above, use presentation attributes, with position and size expressed as single SVG user-unit values. The utility measures actual glyph ink, supporting `text-anchor`, letter and word spacing, and single `dx`/`dy` values. Common Han, kana, basic Latin, fullwidth characters and punctuation are supported when covered by the supplied font. Normalize leading, trailing and repeated ASCII spaces before export.

Mark essential information using `data-field` names of your choice. `data-decorative="true"` excludes decorative text from safety-margin checks, but glyph checks still apply. Fields explicitly required on the command line are always checked for safety. Remove unused or empty fields rather than leaving asterisks or empty text placeholders.

## English — execution and results

Run the shared command examples above. `inspect` checks dimensions, glyph coverage and safety bounds; `outline` writes paths only after every check passes. `--expect-size WIDTH_MM HEIGHT_MM` verifies intended trim dimensions. `--safe-mm` defaults to 3 mm. Repeat `--require-field FIELD` for required text fields; for example, add `--require-field contact` only when a contact field belongs in this card, and mark that text with `data-field="contact"`.

Exit code 0 means checks passed, 1 means validation failed, and 2 means invalid arguments or a write failure. Outlining creates a new SVG and never overwrites an existing file. JSON reports print to the terminal; `--report` also saves a new report file. Reports do not copy the name or contact text, but errors may include supplied file paths. Review reports before sharing them publicly.

## English — limits and review obligations

- This is a per-codepoint outline utility, not a browser text-layout engine. Kerning and ligatures must be explicitly disabled using the supported inline CSS declarations. Complex shaping, combining marks, emoji, vertical and bidirectional text are unsupported. Use a shaping-capable design application to outline and inspect those cases.
- Unsupported inputs include `tspan`, `textPath`, text inside definition containers, text or ancestor transforms, nested viewports, text strokes, clipping, masks, filters, `textLength`, CSS stylesheets, inline style declarations other than the two supported switches, `use`, scripts and event handlers. Simplify straightforward drafts to presentation attributes or use a complete design tool; preserve necessary visual effects rather than deleting them to obtain a passing report.
- Image attributes, references and embedded payloads are preserved. The utility never reads, downloads or uploads image resources. Linked images remain linked and must be managed separately when moving files. XML serialization may change formatting and namespace spelling; source-file byte identity is not promised.
- Outlined groups retain the original text in `aria-label` for accessibility. Remove private information before outlining. Outlining does not anonymize a document.
- The safety box is a rectangular inset from the trim edge. Rounded cutting paths, bleed, print color, image resolution, minimum readable type size and font licensing are outside this utility's checks. Review a real rendering and the intended production specifications for those items.
- An already outlined document cannot prove its original field checks. Documents without editable text nodes fail validation. Keep editable SVG sources and the font map for future exports.

Passing these checks is not a print-readiness or design-quality certification. Render and visually compare the editable and outlined artwork, then verify the remaining production requirements.
