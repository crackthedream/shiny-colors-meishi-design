# 模板使用 / Using the templates

## 中文

此页随技能安装，使用模板时无需另外获取仓库示例页。四个模板位于 `assets/templates/`，分为 `flowing-summer`（流动斜切）和 `dress-bookplate`（洋装装帧），每组有 `front.svg` 与 `back.svg`。

1. 复制选中的 SVG 到自己的项目。样例成品为 **85.60 × 53.98 mm**，圆角参考 **R3.18 mm**；根据实际规格调整。
2. 正面的 `artwork-slot` 是原创几何占位图，`artwork-guide` 是图片位置提示。取得选定卡图后替换前者、移除后者，再判断裁切和留白。模板不包含官图、签名、组合标识或字体文件。
3. `data-field="name"` 是示例制作人姓名，其他文字也保持可编辑。联系字段默认不存在，需要时再加入。新姓名和长标题要重新检查字宽与文字区域；安全边距检查不会发现所有区域内的重叠。
4. 选择合适的字体，在编辑器中指定真实字重与样式。下表的别名用于附带检查工具，不保证与系统安装名称相同。若在浏览器或编辑器中预览，可将别名映射到对应字体或改成该软件识别的名称；转曲前保持映射一致。
5. 按 [SVG 工具说明](svg-tools.md)创建本地字体映射。对这些模板使用 `--require-field name`；转曲之后实际渲染，与可编辑版本核对。字体调整、图文对比、出血和印厂要求仍需分别检查。

## English

This guide is installed with the skill; the repository's example pages are optional. The four templates live in `assets/templates/`: `flowing-summer` and `dress-bookplate`, each with `front.svg` and `back.svg`.

1. Copy the selected SVGs into your project. The examples use **85.60 × 53.98 mm** finished dimensions and an **R3.18 mm** corner reference. Adapt them to the actual specification.
2. On the front, `artwork-slot` contains an original geometric stand-in and `artwork-guide` labels its intended use. Replace the former and remove the latter after obtaining the selected image, then reassess crop and negative space. No official art, signatures, unit logos, or font files are included.
3. `data-field="name"` identifies the sample producer name. Other text remains editable. Contact fields are absent until needed. Recheck text widths and available regions after inserting a new name or long title; safe-margin checks do not detect every overlap within those regions.
4. Choose fonts and specify actual weights and styles in your editor. The aliases below are intended for the helper and may differ from installed family names. Map them to real fonts or use names recognized by the renderer, keeping the helper's map consistent when outlining.
5. Create a local font map as described in the [SVG tool guide](svg-tools.md). Use `--require-field name` with these templates. Render and compare editable and outlined output. Review font changes, contrast, bleed, and printer requirements separately.

## 字体别名与来源 / Font aliases and sources

字体文件由使用者获取；可替换字体，但须重新核对布局。可变字体先生成对应轴值的静态实例。下列建议不构成字体文件的再分发。

Supply the font files yourself. Substitution is allowed but requires a new layout check. Instantiate variable fonts at the intended axis values before using the helper. These suggestions do not distribute font binaries.

| SVG alias | Actual font / 实际字体 | Weight / 字重 | Source / 来源 |
| --- | --- | --- | --- |
| `Noto Serif SC` | Noto Serif SC Regular | 400 | [Noto CJK](https://github.com/notofonts/noto-cjk) |
| `Shippori Mincho` | Shippori Mincho SemiBold | 600 | [Google Fonts](https://fonts.google.com/specimen/Shippori+Mincho) |
| `LXGW WenKai` | LXGW WenKai Regular | 400 | [LXGW WenKai](https://github.com/lxgw/LxgwWenKai) |
| `Cormorant Garamond Light Italic` | Cormorant Garamond Light Italic, static / 静态 | 300 | [Google Fonts](https://fonts.google.com/specimen/Cormorant+Garamond) |
| `Noto Serif SC Medium` | Noto Serif SC Medium | 500 | [Noto CJK](https://github.com/notofonts/noto-cjk) |
| `Source Han Sans JP Normal` | Source Han Sans Japanese Normal | 350 | [Source Han Sans](https://github.com/adobe-fonts/source-han-sans) |
| `Kaisei Tokumin Bold` | Kaisei Tokumin Bold | 700 | [Google Fonts](https://fonts.google.com/specimen/Kaisei+Tokumin) |

在自己的 `font-map.json` 中，以表中别名作键，以实际字体路径作值。只需包含当前 SVG 使用的字体；路径相对于映射文件。以下文件名仅作示意，需替换为实际取得的文件。

Use the aliases as keys in your own `font-map.json` and actual font paths as values. Include only the fonts used by the current SVG. Paths resolve relative to the map. The filenames below illustrate the format; replace them with the files you obtained.

```json
{
  "Noto Serif SC Medium": "fonts/noto-serif-sc-medium.ttf",
  "Source Han Sans JP Normal": "fonts/source-han-sans-jp-normal.otf",
  "Kaisei Tokumin Bold": "fonts/kaisei-tokumin-bold.ttf",
  "Cormorant Garamond Light Italic": "fonts/cormorant-light-italic-static.ttf"
}
```

这是洋装模板的字体组合。要实际完成转曲，应先确认每个文件的字重、字形覆盖和来源许可。

This is the font set used by the dress templates. Before outlining, verify each file's weight, glyph coverage, and source license.
