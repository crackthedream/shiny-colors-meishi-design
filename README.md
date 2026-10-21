# 闪耀色彩小偶像担当名片公式化设计

[English](README.en.md) · [技能正文](skills/shiny-colors-meishi-design/SKILL.md) · [两组示例](examples/README.zh-CN.md)

把《偶像大师 闪耀色彩》（THE IDOLM@STER SHINY COLORS）的角色调研、卡面选择、正反面设计、个人信息填写与导出检查，整理成一个可安装的 Agent Skill。

**这里的“公式化”指可重复的工作流程。** 配色、图形、字体和构图需要从每次选定的角色与卡面出发；同一套流程应当产生有区别的设计。

## 能做什么

- 调研角色与官方资料，查找卡面来源，制作有编号的候选图册，由使用者选择主基调。
- 分析人物朝向、环境、服装、色彩和文字可用空间，先完成一组正反面样张，再迭代和展开整套。
- 将姓名、担当信息和标题纳入构图；背面默认使用文字、矢量图形与留白。
- 只放使用者主动提供的个人信息。未填写的项目直接移除，重新平衡版面。
- 交付可编辑源文件、预览与适当的导出文件，并说明已验证的项目和仍需印厂确认的事项。

Agent 可以自行查找和下载素材，也可以接收使用者提供的图片。记录**官方介绍页**与**实际下载来源**；社区镜像应如实标注。默认不生成 AI 插画，只有明确提出生图需求时才进入该分支。

## 两种构图参考

### 流动斜切 / Flowing summer

![匿名流动斜切名片正反面](examples/flowing-summer/preview.png)

以人物动态、天空与流动线条组织画面，姓名区沿构图方向进入正面。背面延续色彩和运动感。

### 洋装装帧 / Dress bookplate

![匿名洋装装帧名片正反面](examples/dress-bookplate/preview.png)

从服装和场景提取蓝色、奶油白、细框与花饰，以比例和疏密建立文字层级。

两组效果图使用「示例制作人」，没有联系方式。**效果图中的第三方角色图片用于展示；可编辑模板已替换为原创图形和图片位置提示，不附官图、签名或组合标识资产。** 图源、字体建议和替换方法见[示例说明](examples/README.zh-CN.md)及[第三方素材说明](THIRD_PARTY_NOTICES.md)。

## 安装

### 在 Codex 中安装

可以对支持安装 GitHub 技能的 Agent 说：

```text
使用 $skill-installer 安装：
https://github.com/crackthedream/shiny-colors-meishi-design/tree/main/skills/shiny-colors-meishi-design
```

也可以下载仓库，将完整的 `skills/shiny-colors-meishi-design` 文件夹复制到 Codex 的 `~/.codex/skills/`。配置了 `CODEX_HOME` 时使用其 `skills/` 子目录。保留整个文件夹，使说明、模板和工具的相对链接仍然有效；下一轮对话再调用技能。

其他支持 `SKILL.md` 的 Agent 可按自身的技能安装方式加载这个文件夹。不同客户端的工具能力各不相同，本仓库不依赖某个浏览器插件或本机固定路径。

### 开始使用

```text
$shiny-colors-meishi-design
我想做杜野凛世的长期担当名片。先调研并给出编号卡面候选，
让我选图后再设计。默认使用官图正面和文字、矢量图案背面。
先做一组正反面样张，个人信息暂不填写。
```

修改现有设计也可以：

```text
$shiny-colors-meishi-design
检查这组名片的人物、题字和姓名区是否形成整体。
保留已确认的视觉方向，优化字体和留白；未填写的联系项直接删除。
```

## 文件导航

| 内容 | 位置 |
| --- | --- |
| 技能入口 | [SKILL.md](skills/shiny-colors-meishi-design/SKILL.md) |
| 完整中文流程 | [design-workflow.zh-CN.md](skills/shiny-colors-meishi-design/references/design-workflow.zh-CN.md) |
| Full English workflow | [design-workflow.en.md](skills/shiny-colors-meishi-design/references/design-workflow.en.md) |
| 四张可编辑 SVG 模板 | [assets/templates](skills/shiny-colors-meishi-design/assets/templates) |
| SVG 检查与文字转曲 | [工具说明](skills/shiny-colors-meishi-design/references/svg-tools.md) |
| 示例与来源 | [中文](examples/README.zh-CN.md) / [English](examples/README.en.md) |

## 可选检查工具

设计流程不要求执行脚本。需要检查 SVG 尺寸、字体覆盖或简单文字的安全边距时，可使用附带的 Python 工具：

```bash
python -m pip install -r skills/shiny-colors-meishi-design/requirements.txt
python skills/shiny-colors-meishi-design/scripts/svg_text_tools.py --help
```

工具只支持文档中说明的 SVG 文字子集，字体由使用者提供。它会对不支持的文字结构报告问题；**脚本通过不等于视觉质量合格，也不等于已完成印前检查。** 转曲后仍需渲染对照，确认缺字、位置、裁切和图片表现。具体命令见[工具说明](skills/shiny-colors-meishi-design/references/svg-tools.md)。

模板使用 **85.60 × 53.98 mm** 的示例成品尺寸。实际项目需确认尺寸、圆角、安全区、出血和印厂要求；高 DPI 标签不能增加原图的细节。当前模板并非适用于所有印厂的交付文件。

维护者可在仓库根目录运行 `python tests/test_svg_text_tools.py`，验证尺寸与缺字检测、边界、转曲图片保留和拒绝不支持结构等行为。测试会临时生成自己的字形，不需要下载字体。

## 许可与隐私

原创技能说明、脚本及无官图版式采用 [MIT License](LICENSE)。第三方角色图像、游戏名称、商标等不在该授权范围内，详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。这是非官方的设计流程参考，与作品权利方无隶属关系。

仓库不包含项目参与者的真实姓名、联系方式、原始对话、个人目录、字体文件或完整卡面素材库。使用时填写的私人信息属于各自项目，不应随着技能改进一起提交到公共仓库。
