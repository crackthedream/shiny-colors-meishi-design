# 闪耀色彩小偶像担当名片公式化设计

[English](README.en.md) · [技能正文](skills/shiny-colors-meishi-design/SKILL.md) · [两组示例](examples/README.zh-CN.md)

用于《偶像大师 闪耀色彩》（THE IDOLM@STER SHINY COLORS）担当名片设计的 Agent Skill，覆盖角色调研、官图选择、正反面构图、字体排版、反馈修改和导出检查。

适合日常交换、纪念主题名片，以及已有设计的继续修改。“公式化”指可重复使用的工作流程；每张卡的配色、图案和构图仍从具体角色与官图出发。

## 主要功能

| 功能 | 具体内容 |
| --- | --- |
| 调研与选图 | 查找角色资料和卡面来源，查看实际图片，整理带编号的候选册 |
| 正反面设计 | 将人物、环境、题字和姓名区共同构图，背面默认使用文字与矢量图形 |
| 反馈迭代 | 先完成一组样张，再根据反馈调整构图、字体和细节，展开整套 |
| 信息填写 | 仅显示用户要求的个人字段；空缺项连同标签、占位符一起移除 |
| 文件交付 | 保留可编辑源文件，整理正反面总览、约定的导出文件和素材来源 |
| 辅助检查 | 提供可选的 SVG 尺寸、缺字、文字边界检查与文字转曲工具 |

需要在具备资料检索、文件编辑和渲染能力的 Agent 中使用。官图可以由 Agent 查找，也可以由用户提供；AI 插画只在用户明确要求时使用。

## 效果示例

两组正反面展示不同的构图方式。姓名统一使用「示例制作人」，不含联系方式。

### 灯织 · 流动斜切

![匿名流动斜切名片正反面](examples/flowing-summer/preview.png)

正面以人物和画面的方向安排斜切姓名区；背面使用青蓝、浅薄荷与舒展的线条，延续正面的色彩和动感。

### 凛世 · 洋装装帧

![匿名洋装装帧名片正反面](examples/dress-bookplate/preview.png)

从服装与场景提取蓝色、奶油白、细框和局部花饰，通过文字层级与留白组织背面；正面姓名区呼应画面的斜向。

效果图含第三方官图。四张可编辑 SVG 使用原创图形和图片位置提示，不附官图、签名或组合标识资产。图源、字体和替换方法见[示例说明](examples/README.zh-CN.md)，素材授权范围见[第三方素材说明](THIRD_PARTY_NOTICES.md)。

## 安装

### Codex

对支持从 GitHub 安装 skill 的 Agent 发送：

```text
使用 $skill-installer 安装：
https://github.com/crackthedream/shiny-colors-meishi-design/tree/main/skills/shiny-colors-meishi-design
```

也可以下载仓库，将完整的 `skills/shiny-colors-meishi-design` 文件夹复制到 Codex 的 `~/.codex/skills/`。配置了 `CODEX_HOME` 时，使用其 `skills/` 子目录。保留整个文件夹，让说明、模板和工具的相对链接仍然有效；下一轮对话再调用。

其他支持 `SKILL.md` 的 Agent 可按各自的方式加载该文件夹。实际可用的检索、设计和导出工具取决于客户端。

## 使用方法

### 新建一套名片

```text
$shiny-colors-meishi-design
想给凛世做一套平时交换用的担当名片，还没选好官图。
先帮我找一些合适的卡面，编号给我挑。
背面用文字和图案来设计，先做一组正反面看看，个人信息晚点再填。
```

### 修改已有设计

```text
$shiny-colors-meishi-design
这版的配色可以保留，但姓名区看着有点像后来贴上去的。
帮我重新安排一下，让文字和画面更协调，顺便看看字体和留白。
没有填的联系方式就删掉。
```

## 工作流程

**确认需求 → 调研选图 → 一组正反面样张 → 反馈修改 → 展开整套 → 填写信息 → 导出检查**

用户决定角色、卡面、张数和要显示的信息；Agent 负责资料查找、构图排版和文件处理。已有明确选图或已确认的设计方向时，从对应阶段继续；已授权整套执行时，也可直接展开。

素材记录区分官方介绍页与实际下载地址，社区镜像应如实注明。每次修改后查看实际渲染结果，再核对文字、裁切和个人信息。具体步骤见[完整设计流程](skills/shiny-colors-meishi-design/references/design-workflow.zh-CN.md)。

## 文件导航

| 内容 | 位置 |
| --- | --- |
| 技能入口 | [SKILL.md](skills/shiny-colors-meishi-design/SKILL.md) |
| 完整中文流程 | [design-workflow.zh-CN.md](skills/shiny-colors-meishi-design/references/design-workflow.zh-CN.md) |
| 完整英文流程 | [design-workflow.en.md](skills/shiny-colors-meishi-design/references/design-workflow.en.md) |
| 四张可编辑 SVG 模板 | [assets/templates](skills/shiny-colors-meishi-design/assets/templates) |
| SVG 检查与文字转曲 | [工具说明](skills/shiny-colors-meishi-design/references/svg-tools.md) |
| 示例与来源 | [中文](examples/README.zh-CN.md) / [English](examples/README.en.md) |

## 导出与印刷

模板使用 **85.60 × 53.98 mm** 的示例成品尺寸。实际送印前，需按印厂要求确认尺寸、圆角、安全区、出血和导出格式。高 DPI 标签不能增加原图细节，模板也不能直接视为已通过印厂检查的文件。

附带的 SVG 工具支持部分文字结构，可检查尺寸、缺字和文字边界，并将支持的文字转成轮廓。字体由使用者提供。转曲后仍需渲染对照，检查文字位置、图片和裁切；工具检查不代替视觉审阅或印前检查。

<details>
<summary>可选 SVG 工具：安装与使用</summary>

设计流程不要求运行脚本。需要工具检查时，安装依赖并查看命令说明：

```bash
python -m pip install -r skills/shiny-colors-meishi-design/requirements.txt
python skills/shiny-colors-meishi-design/scripts/svg_text_tools.py --help
```

支持范围和具体命令见[工具说明](skills/shiny-colors-meishi-design/references/svg-tools.md)。脚本会报告不支持的文字结构；它不能判断设计是否好看，也不能代替印厂检查。

修改脚本后，可以在仓库根目录运行 `python tests/test_svg_text_tools.py`。测试覆盖尺寸、缺字、边界、转曲时的图片保留，以及对不支持结构的处理；测试所用字形会临时生成，不需要下载字体。

</details>

## 许可与隐私

原创说明、脚本和无官图版式采用 [MIT License](LICENSE)。第三方官图、游戏名称和标识不在该授权范围内，详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。本项目是非官方的同好设计工具，与作品权利方无隶属关系。

公开文件不含项目参与者的真实姓名、联系方式、原始对话、本机路径、字体文件或完整卡面素材库。使用时填写的私人信息留在各自项目中；分享文件或提交修改前，请移除个人信息。

## 写在最后

这是我尝试用 Codex 简单制作担当名片后的副产物。说不上有多好看，或是设计性多强，但基本水准应该还是有的，希望能一定程度上帮到各位 Producer。当然，如果有足够的设计天赋，还是可以自己先搓着。

如果您在使用的时候发现什么问题，也可以联系我（不过，想自己修改也完全没问题，这也并不是什么有技术含量的东西；如果是更劲、更强的 Claude 模型，搓得更好看也说不定）。
