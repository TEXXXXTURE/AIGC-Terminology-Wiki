---
term: Qwen
full_name: Qwen（通义千问）
aliases: [Qwen2, Qwen3, 通义千问]
category: 模型
dimension: 模型家族
granularity: 家族
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://huggingface.co/Qwen
  - https://qwenlm.github.io/
relations:
  - target: 阿里
    note: Qwen 是阿里通义千问的 LLM 家族
  - target: Llama
    note: Qwen 是 Llama 在中文开源 LLM 的主要对手
  - target: 文本编码器
    note: Qwen 常被用作多模态模型的文本编码器
  - target: Z-Image
    note: Qwen-Image 是阿里的图像模型，Z-Image 是另一条线
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Qwen（通义千问）是阿里的大语言模型家族，从 0.5B 到 236B 全覆盖，是**中文开源 LLM 的事实标准**。它不只是聊天模型——Qwen 系列还包括多模态版本（Qwen-VL 视觉、Qwen-Audio 音频）和代码版本，还常被其他厂商借用作多模态模型的文本编码器（比如 MiniMax H3 就用 Qwen3-VL-32B）。

## 原理

Qwen 是标准的 Decoder-only Transformer 架构，靠高质量数据和工程取胜。家族按能力分多条线：Qwen（纯文本）、Qwen-VL（视觉语言）、Qwen-Audio、Qwen-Coder（代码）。它的多模态版本在「理解+生成」上能力强，被大量第三方模型借用作文本编码器——因为它语义理解好、输出维度适合扩散模型做条件注入。

## 由来与历史

阿里 2023 年发布 Qwen，此后高频迭代：Qwen2（2024，性能跃升）、Qwen2.5（生态成熟，成为社区主力）、Qwen3（2025，混合推理）。Qwen 家族在中文开源 LLM 上长期压制 Llama 的本地化版本，全球下载量位居开源模型前列。它的多模态版本 Qwen-VL 系列被 MiniMax、各种文生图模型选为编码器，影响力超出 LLM 本身。

## 应用

在 ComfyUI 和本地 AI 里，Qwen 的两个常见角色：
- **LLM**：本地跑中文对话/Agent，配合 Ollama/llama.cpp + GGUF 量化，12GB 卡能跑 Qwen3 8B/14B
- **文本编码器**：Qwen 的视觉语言版（如 Qwen3-VL-32B）被 H3 等视频模型用作提示词理解器；注意 Z-Image 不用 Qwen 而是用 Gemma2（维度 2560 vs 4096，架构绑定）

## 争议 / 讨论

Qwen 迭代太快，老版本（Qwen1/Qwen2）快速过气，社区有「追新疲劳」；另外 Qwen 的「全尺寸覆盖」策略让选择困难（0.5B~236B 几十个版本）。技术上 Qwen 深度绑定阿里云生态，本地部署的官方支持略弱于 Llama。

## 参见

- [阿里](../模型厂商/阿里.md)
- [Llama](Llama.md)
- [文本编码器](../../02-组件/文本编码器.md)
- [MiniMax H3](MiniMax H3.md)
- [模型数据总览](../../04-LLM工程/模型数据总览.md)

## AA 评测数据 (2026-08-17)

Qwen3.8 Max 在 Artificial Analysis 评测中的数据:

- 智能指数: 58.08
- 输出速度: 46.2 tok/s
- 输入价格: $2.00/M tokens
- 输出价格: $6.00/M tokens
- 缓存命中: $0.25/M tokens
- 上下文窗口: 1M tokens
- 全知指数: 3.4
