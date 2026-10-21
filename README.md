# 闪耀色彩小偶像担当名片公式化设计

[English](README.en.md) · [技能正文](skills/shiny-colors-meishi-design/SKILL.md) · [两组示例](examples/README.zh-CN.md)

这份 skill 是从给风野灯织和杜野凛世做担当名片的过程中整理出来的。

官图选好了，接下来还有不少地方要琢磨：姓名放在哪里才自然，背面用什么图案，几张卡怎样放在一起好看，又各自保留角色和卡面的味道。这次制作里，这些地方都来回改过好几轮。

调研、选图、试排、看效果、再修改——把这段过程留下来，也许能给同样想做担当名片的人一个起点。你可以把这份 skill 装进自己的 Agent，带着喜欢的角色和想法，从选图开始慢慢做。

<!-- 作者补充（可选）：这里适合写为什么想做担当名片、想在什么场合使用，或这次制作中印象深的一件事。写自己的经历即可，不必写成项目介绍。 -->

名字里的“公式化”指的是这套可以重复使用的做法。至于用什么颜色、字体和构图，每次仍要看具体的角色与官图。

## 先看看做出来的样子

仓库里放了两组正反面，分别来自灯织和凛世的设计。姓名统一换成了「示例制作人」，联系方式也已移除。

### 灯织 · 流动斜切

![匿名流动斜切名片正反面](examples/flowing-summer/preview.png)

顺着人物、天空和发丝的方向，给姓名留出一块斜切的空间。背面继续用青蓝、浅薄荷和舒展的线条，延续正面的轻快感。

<!-- 作者补充（可选）：可以在这里写选这张灯织卡面的原因，或你最喜欢的一个画面细节。 -->

### 凛世 · 洋装装帧

![匿名洋装装帧名片正反面](examples/dress-bookplate/preview.png)

这组从服装和场景里取了蓝色与奶油白，再用细框、局部花饰和文字的疏密来组织背面。正面的姓名区也顺着画面的斜向安排，让信息和官图能放在一起读。

<!-- 作者补充（可选）：这里可以聊聊凛世这款的修改过程、喜欢的细节，或你还想继续调整的地方。 -->

效果图保留了官图，方便看完整的设计效果。另附的四张可编辑 SVG 使用原创图形和图片位置提示，不包含官图、签名或组合标识资产。图源、字体和替换方法放在[示例说明](examples/README.zh-CN.md)里，素材授权范围见[第三方素材说明](THIRD_PARTY_NOTICES.md)。

## 拿它做一套自己的名片

可以先告诉 Agent 你想做谁的担当名片，用来日常交换还是纪念某个日子。如果还没选好官图，就让它查资料、找图，整理成带编号的候选册，再由你挑选卡面和张数。已经有喜欢的图，也可以直接从那里开始。

选定之后，先做一组正反面看看。人物、环境、题字和制作人姓名要一起考虑；背面则从这张官图的色彩、服装或场景里找线索。看过样张，再说哪里太满、哪里太空、字体合不合适，或还差一点什么感觉。方向定下来后，再展开其余几张。

背面默认用文字、线条、矢量图案和留白来设计。想尝试 AI 插画时，需要明确提出。个人信息也可以最后再填；只保留你想放的项目，空着的联系方式会连同标签一起删掉，不留一排星号。

这份 skill 需要在能查资料、编辑文件和查看渲染结果的 Agent 中使用。它会保留可编辑文件，并整理正反面预览和约定的导出文件。素材可以由 Agent 查找，也可以由你提供；官方页面和实际下载地址会分别记录，来自社区镜像的图片也应注明来源。

## 怎么开始

### 安装到 Codex

如果你的 Agent 支持从 GitHub 安装 skill，可以直接发：

```text
使用 $skill-installer 安装：
https://github.com/crackthedream/shiny-colors-meishi-design/tree/main/skills/shiny-colors-meishi-design
```

也可以下载仓库，把完整的 `skills/shiny-colors-meishi-design` 文件夹复制到 Codex 的 `~/.codex/skills/`。配置过 `CODEX_HOME` 的话，放进它的 `skills/` 子目录。记得保留整个文件夹，里面的说明、模板和工具需要一起使用；下一轮对话再调用。

其他支持 `SKILL.md` 的 Agent，也可以按各自的方式安装这个文件夹。不同客户端能用的工具会有区别。

### 第一条消息可以这样写

```text
$shiny-colors-meishi-design
想给凛世做一套平时交换用的担当名片，还没选好官图。
先帮我找一些合适的卡面，编号给我挑。
背面用文字和图案来设计，先做一组正反面看看，个人信息晚点再填。
```

如果已经有一版，直接带着反馈继续：

```text
$shiny-colors-meishi-design
这版的配色可以保留，但姓名区看着有点像后来贴上去的。
帮我重新安排一下，让文字和画面更协调，顺便看看字体和留白。
没有填的联系方式就删掉。
```

## 想继续看细节

| 内容 | 位置 |
| --- | --- |
| 技能入口 | [SKILL.md](skills/shiny-colors-meishi-design/SKILL.md) |
| 完整中文流程 | [design-workflow.zh-CN.md](skills/shiny-colors-meishi-design/references/design-workflow.zh-CN.md) |
| 完整英文流程 | [design-workflow.en.md](skills/shiny-colors-meishi-design/references/design-workflow.en.md) |
| 四张可编辑 SVG 模板 | [assets/templates](skills/shiny-colors-meishi-design/assets/templates) |
| SVG 检查与文字转曲 | [工具说明](skills/shiny-colors-meishi-design/references/svg-tools.md) |
| 示例与来源 | [中文](examples/README.zh-CN.md) / [English](examples/README.en.md) |

## 导出和印刷前

模板的示例成品尺寸是 **85.60 × 53.98 mm**。准备印刷时，还要按实际印厂要求确认尺寸、圆角、安全区和出血。屏幕预览可以用来讨论设计，送印文件则需要按这些要求另行核对；把 DPI 数字调高，也不会增加原图的细节。

仓库附了一个可选的 SVG 文字工具，能检查尺寸、缺字和简单文字的边界，也能把支持的文字转成轮廓。它处理的文字结构有限，字体需要自己提供。检查通过后，仍要打开导出的图，看看文字和图片有没有跑位、缺失或被裁掉。

<details>
<summary>需要用检查工具时，展开这里</summary>

设计时不一定要运行脚本。需要使用时，先安装依赖，再查看命令说明：

```bash
python -m pip install -r skills/shiny-colors-meishi-design/requirements.txt
python skills/shiny-colors-meishi-design/scripts/svg_text_tools.py --help
```

支持范围和具体命令见[工具说明](skills/shiny-colors-meishi-design/references/svg-tools.md)。脚本会报告不支持的文字结构；它不能判断设计是否好看，也不能代替印厂检查。

修改脚本后，可以在仓库根目录运行 `python tests/test_svg_text_tools.py`。测试覆盖尺寸、缺字、边界、转曲时的图片保留，以及对不支持结构的处理；测试所用字形会临时生成，不需要下载字体。

</details>

## 关于素材和分享

这里原创的说明、脚本和无官图版式采用 [MIT License](LICENSE)，欢迎修改和分享。示例中的官图、游戏名称和标识仍属于各自权利方，具体说明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。本项目是《偶像大师 闪耀色彩》的非官方同好项目。

公开文件已经移除了原名片中的个人信息，也没有附上原始对话、本机路径、字体文件或完整卡面素材库。之后如果想分享自己改过的版本，也记得先检查姓名和联系方式有没有一起带进去。
