---
term: Transformer
full_name: Transformer
aliases: [Transformer 架构, 变换器]
category: 架构
dimension: 底层原理
granularity: 原理
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/1706.03762
  - https://huggingface.co/learn/llm-course/chapter1/4
  - https://arxiv.org/abs/2212.09748
relations:
  - type: part_of
    target: 注意力机制
    note: 自注意力是 Transformer 的核心组件
  - type: part_of
    target: 神经网络
    note: Transformer 是神经网络的一种架构
  - type: applies_to
    target: 扩散模型
    note: DiT 用 Transformer 做去噪网络
  - type: applies_to
    target: 文本编码器
    note: 文本编码器本质上是 Transformer 网络
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Transformer 是 Google 在 2017 年论文《Attention Is All You Need》里提出的一种神经网络架构，一句话概括：它用「注意力机制」取代了之前主流的循环神经网络（RNN），让模型能并行地处理整段文字，同时看清每个词和其他所有词的关系。今天的大语言模型（GPT、Llama、DeepSeek）、文生图的扩散模型（DiT）、以及各种多模态模型，底层几乎全是 Transformer——说它「统治一切」不算夸张。

## 原理

Transformer 的核心思想是「自注意力」（self-attention）：输入的一句话先被切成 token，每个 token 都同时「看向」句子里所有其他 token，算出一个加权后的表示。这样无论两个词离得多远，关系都能一步直达，而不是像 RNN 那样必须按顺序一步步传。具体机制见[注意力机制](注意力机制.md)词条。

原始论文是一个「编码器-解码器」（encoder-decoder）结构：编码器负责读懂输入、把它压缩成一组表示，解码器再根据这组表示一步步生成输出。这个结构后来演化出三大流派：只用编码器的 BERT 系（适合分类、理解类任务）、只用解码器的 GPT 系（适合生成，今天几乎所有 LLM 都是它）、以及两者都用上的 T5/BART 系（适合翻译、摘要）。

为什么 Transformer 能「统治一切」？关键在两点：一是并行——RNN 必须一个词一个词地算，Transformer 整段一起算，能在 GPU 上高效扩展，于是模型可以堆得巨大；二是通用——它只要求输入能排成一串「token」，文字、图像切成小块、音频切成片段，通通都能进。这套扩展性直接催生了「规模法则」（scaling law）：模型越大、数据越多，能力越强。

## 由来与历史

2017 年 6 月，Vaswani 等人在 Google 发表《Attention Is All You Need》（arXiv:1706.03762），最初是为机器翻译设计的，但很快被证明是一套通用架构。2018 年 BERT 和 GPT 相继问世，分别确立「理解」和「生成」两条路线；2020 年的 GPT-3 展示了超大模型的零样本能力。

2022 年 InstructGPT/ChatGPT 把 Transformer 语言模型推到大众面前，2023 年 Llama 等开源模型点燃了本地部署生态。Transformer 也走出了文本：2023 年的 DiT（Diffusion Transformer，arXiv:2212.09748）用 Transformer 取代 UNet 做扩散模型的去噪网络，FLUX、SD3、Wan 等新一代文生图/文生视频模型都是这一路线——Transformer 由此同时统治了语言和视觉生成两个世界。

## 应用

对使用者来说，Transformer 就是你手里所有模型的内核：和 GPT 对话、让 ComfyUI 里的 FLUX 出图、让 Wan 生成视频，底层跑的都是它。理解它的两个基本事实就够了：一是「注意力让它看清全局」，这解释了为什么模型能理解复杂描述；二是「token 是它的基本单位」，这解释了为什么输入长度、计费和速度都按 token 算（见 [Tokenizer](../02-组件/Tokenizer.md)）。

## 参见

- [注意力机制](注意力机制.md)
- [神经网络](神经网络.md)
- [扩散模型](扩散模型.md)
- [文本编码器](../02-组件/文本编码器.md)
