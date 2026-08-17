---
term: DiT
full_name: Diffusion Transformer
aliases: [扩散Transformer, 扩散 Transformer]
category: 架构
dimension: 底层原理
granularity: 原理
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/2212.09748
relations:
  - type: part_of
    target: 扩散模型
    note: DiT 把扩散模型的去噪网络从 UNet 换成 Transformer
  - type: evolved_from
    target: Transformer
    note: DiT 是 Transformer 架构进入扩散去噪网络的产物
  - type: applies_to
    target: 神经网络
    note: DiT 本质是一个 Transformer 架构的神经网络
  - type: applies_to
    target: FLUX
    note: FLUX / SD3 / Wan 等新一代模型都采用 DiT 架构
created: 2026-08-17
updated: 2026-08-17
revisions: 1
---

## 定义

DiT（Diffusion Transformer，扩散 Transformer）是用 Transformer 取代 UNet 来充当扩散模型「去噪网络」的一种架构。一句话说清：扩散模型的核心任务是「看噪声图、预测该去掉哪部分噪声」，过去这个活儿由 UNet 干，DiT 让它交给 Transformer 干——而 Transformer 恰恰最擅长在大规模数据上「看清全局关系」，于是新一代文生图、文生视频模型几乎清一色转向 DiT。

## 原理

标准扩散模型（如 Stable Diffusion）在[潜空间](../02-组件/潜空间.md)里一步步去噪，去噪网络原本是 [UNet](../02-组件/UNet.md)。DiT 的做法是把 UNet 换成 [Transformer](Transformer.md)：把潜空间特征切成一个个「图块 token」，像文字 token 一样送进 Transformer 做自注意力，再预测噪声。由于 Transformer 的扩展性强、能堆很大，它比 UNet 更能吃下规模红利——这正好契合[缩放法则](缩放法则.md)的逻辑。具体机制见[扩散模型](扩散模型.md)与[Transformer](Transformer.md)。

## 由来与历史

DiT 由 Peebles 和 Xie 在 2022 年论文《Scalable Diffusion Models with Transformers》（arXiv:2212.09748）中提出，最初在类 ImageNet 生成上验证了「Transformer 去噪网络 + 规模扩展」的有效性。2024 年成为分水岭：Stable Diffusion 3、FLUX、以及文生视频的 Wan、LTX 等全部采用 DiT 路线，标志着视觉生成正式进入「Transformer 统一架构」时代——语言生成（GPT 系）和视觉生成由此共用同一套底层范式。

## 应用

对使用者来说，DiT 是「为什么新模型又强又能扩」的底层答案：FLUX 出图质感、Wan 出视频的连贯度，都直接受益于 DiT 的可扩展性。它在 ComfyUI 里并不会单独出现，而是藏在 FLUX / Wan 等[模型家族](../03-表层概念/模型家族/FLUX.md)的内部结构里——你加载的是整个 DiT 模型，调节的仍是采样步数、CFG 等老参数。理解 DiT 的价值在于：它解释了「为什么模型越新越大、但同一套工作流还能继续用」。

## 参见

- [扩散模型](扩散模型.md)
- [Transformer](Transformer.md)
- [神经网络](神经网络.md)
- [FLUX](../03-表层概念/模型家族/FLUX.md)
- [Wan](../03-表层概念/模型家族/Wan.md)
