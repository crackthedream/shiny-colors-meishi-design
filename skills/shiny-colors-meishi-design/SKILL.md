---
name: shiny-colors-meishi-design
description: Design and iterate THE IDOLM@STER Shiny Colors producer and idol-support meishi cards, from researched card-art selection to coordinated fronts, vector backs, typography, personal fields, and checked exports. Use for Shiny Colors fan-exchange cards and revisions to them; this is not a general corporate business-card template.
---

# 闪耀色彩小偶像担当名片公式化设计

# Shiny Colors Producer Meishi Design

## 中文

把调研、选择、样张、迭代和交付变成可复用流程；让每张的构图继续由角色和所选卡面决定。

开始设计时读 [中文方法](references/design-workflow.zh-CN.md)。该文与 [English workflow](references/design-workflow.en.md) 内容对应，按工作语言选读一份。

需要可编辑的起点时，查看流动斜切的 [正面](assets/templates/flowing-summer/front.svg) / [背面](assets/templates/flowing-summer/back.svg)，或洋装装帧的 [正面](assets/templates/dress-bookplate/front.svg) / [背面](assets/templates/dress-bookplate/back.svg)，并读[模板与字体指南](references/template-guide.md)。模板不含官图，展示的是构图关系；替换素材后重新判断裁切、字体和留白，不能只换姓名套版。

1. **恢复范围。** 核对角色、使用场景、已选卡面、已有反馈和交付规格。已有明确选择就沿用；需要补充的事实由 agent 调研，只向用户询问会改变设计的决定。
2. **调研与选图。** Agent 可查找并获取公开可访问的官方素材。记录具体页面、图像地址、卡名、版本和来源性质；社区镜像与官网获取分开标明。实际看图后制作稳定编号的候选册，由用户决定选图与张数。用户已经指定时直接核验指定素材。
3. **先做一套正反面样张。** 从画面提取色彩、方向、服装或环境线索，选择最能验证本次设计方法的一款。正面把人物、环境、题字和身份区一起构图；背面默认以文字与矢量图形回应正面。只有用户明确要求时才进入 AI 生图分支，并标明生成内容。
4. **迭代再展开。** 展示样张与简短设计理由，按用户反馈修改。样张认可或用户已授权整套执行后展开；各款保持自己的图形语言，通过字体角色、信息层级和规格形成套装关系。
5. **填写与整理。** 只显示用户提供并要求显示的字段。未提供或删除的字段连同标签、占位符一起消失，重新平衡留白。真实信息写入后重新导出全部交付面；公开参考版使用明确的示例身份，彻底移除原个人信息。
6. **导出与核验。** 保留可编辑源文件，按用户/印厂规格输出。逐面看渲染结果，再检查文字、字体、边界与来源。使用附带的 [SVG 文字工具](scripts/svg_text_tools.py) 前读 [工具说明](references/svg-tools.md)；工具报告不代替审美检查，也不等同印厂验收。

素材署名与版权标记应保留。官方图、标识和字体遵循各自来源条件；本项目原创文件的 MIT 许可不改变第三方素材的许可。保留现有批准版本，明确本轮改动和未实测项。

完成时交付最新正反面总览、约定的编辑/导出文件和来源说明；个人信息一致、删除字段无残留、图像与文字无意外裁切，用户能清楚区分效果校样与已按印厂要求制作的文件。

## English

Make research, selection, prototyping, iteration, and delivery repeatable. Let each character and selected artwork determine the composition.

For design work, read the [English workflow](references/design-workflow.en.md). It corresponds to the [Chinese workflow](references/design-workflow.zh-CN.md); read the version matching the working language.

For an editable starting point, inspect the flowing diagonal [front](assets/templates/flowing-summer/front.svg) / [back](assets/templates/flowing-summer/back.svg), or the dress-inspired bookplate [front](assets/templates/dress-bookplate/front.svg) / [back](assets/templates/dress-bookplate/back.svg), and read the [template and font guide](references/template-guide.md). These templates contain no official artwork and demonstrate compositional relationships. Reassess crop, type, and space after replacing the artwork rather than only substituting a name.

1. **Recover the scope.** Check the character, use, selected artwork, existing feedback, and delivery specifications. Carry forward settled choices. Research facts yourself and ask the user only for decisions that affect the design.
2. **Research and select.** The agent may locate and retrieve publicly accessible official artwork. Record the page, image URL, card title, variant, and source category; distinguish community mirrors from downloads hosted by an official source. Inspect images before presenting a consistently numbered selection sheet. The user selects the artwork and quantity; verify directly when these are already specified.
3. **Prototype one front/back pair.** Extract colors, directions, and clothing or environmental cues. Choose a pair that tests the relevant design decisions. Compose the character, setting, title, and identity area together on the front. Default to typography and vector graphics on the back. Enter an AI-image branch only when explicitly requested, and identify generated content.
4. **Iterate, then expand.** Show the pair with a short design rationale and revise from feedback. Expand after acceptance or when the user has already authorized a full-set workflow. Give every card its own visual language; connect the set through typographic roles, information hierarchy, and physical specifications.
5. **Apply information and assemble.** Display only fields supplied and requested by the user. Remove absent fields, their labels, and their placeholders, then rebalance the space. Regenerate every deliverable after applying actual information. Use clearly labeled sample identities and remove all original personal data from public examples.
6. **Export and inspect.** Keep editable sources and export to the agreed user/printer specifications. Visually review each rendered face, then check text, fonts, boundaries, and provenance. Read the [SVG tool guide](references/svg-tools.md) before using the bundled [SVG text helper](scripts/svg_text_tools.py). A machine pass is neither an aesthetic assessment nor printer acceptance.

Preserve attribution and copyright marks. Official art, marks, and fonts remain subject to their source terms; MIT coverage of original project files does not relicense third-party material. Preserve approved versions and report what changed and what was not tested.

Deliver the current front/back overview, agreed editable/export files, and source notes. Personal information must agree across outputs, removed fields must leave no residue, and images/text must have no unintended clipping. Distinguish design proofs from files prepared to a specific printer's requirements.
