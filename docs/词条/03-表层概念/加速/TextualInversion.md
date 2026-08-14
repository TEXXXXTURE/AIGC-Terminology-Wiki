---
term: Textual Inversion
full_name: Textual Inversion (Embedding)
aliases: [文本反转, TI, embedding]
category: 模型微调
dimension: 语义注入技术
granularity: 具体技术
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/2208.01618
  - https://textual-inversion.github.io
  - https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/6700
relations:
  - type: contrast
    target: LoRA
    note: 常被对比的轻量个性化方案，TI 学「是什么」，LoRA 学「怎么画」
  - type: applies_to
    target: CLIP
    note: 反转的是文本编码器词表里的 embedding 向量
  - target: 文本编码器
    note: TI 训练产物直接挂在文本编码器的输入端
  - target: 风格模型
    note: TI 适合固定物体/角色，风格定制则更多交给 LoRA 或风格模型
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Textual Inversion（文本反转，简称 TI 或 embedding）是一种极轻量的个性化技术，一句话说清：用 3~5 张参考图，教会模型一个全新的「伪词」——以后在提示词里写下这个词，模型就会画出你教它的那个物体或角色。产物只有一个几十 KB 的小文件，是所有个性化方案里最小的一种。

## 原理

它不碰模型权重，只在文本编码器的词表里注册一个新 token，然后冻结其他一切、只优化这个新词对应的向量，直到「输入这个词 → 模型联想到你的参考图」。所以 TI 学到的本质上是一个指向模型概念空间的坐标。背景见[CLIP](../../02-组件/CLIP.md)与[文本编码器](../../02-组件/文本编码器.md)。

## 由来与历史

2022 年 8 月，Google Research 的 Nataniel Ruiz 等人发表 Textual Inversion 论文（arXiv:2208.01618），与同月亮相的 DreamBooth 并称两大个性化方案。SD 1.5 时代它是主流玩法，A1111 WebUI 内置了训练界面（社区还贡献过加权学习 TI 的改进，见 PR #6700）。随着 [LoRA](../微调/LoRA.md) 生态爆发，TI 因表达力有限而逐渐退居二线，但作为「几十 KB 就能固定一个角色」的方案仍有位置。

## 应用

ComfyUI 用法：把下载的 `.pt` 或 `.safetensors` 文件放进 `models/embeddings/`，然后在提示词里写 `embedding:文件名`（不带扩展名）即可触发。A1111 里直接写文件名就行。

使用建议：

- TI 最适合**固定一个具体物体或角色**（你家的猫、某个产品外观）；想学画风请用 LoRA——社区口诀是「TI 学是什么，LoRA 学怎么画」。
- embedding 同样绑定底模架构，SD1.5 的 embedding 在 SDXL 上不生效。
- 负面 embedding（如 EasyNegative）是 TI 的另一大用法：往负面提示词里一放，通用地压掉低质量特征。

## 参见

- [LoRA](../微调/LoRA.md)
- [CLIP](../../02-组件/CLIP.md)
- [文本编码器](../../02-组件/文本编码器.md)
- [风格模型](../微调/风格模型.md)
