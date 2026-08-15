---
term: Meta
full_name: Meta Platforms
aliases: [Meta AI, Facebook AI, 元公司]
category: 平台
dimension: 模型厂商
granularity: 厂商
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://ai.meta.com/
  - https://huggingface.co/facebook
relations:
  - target: 阿里
    note: 同为 LLM 开源主力，Llama 对标 Qwen
  - target: Stability AI
    note: Meta 的生成模型与 Stability 生态互补
  - target: MusicGen
    note: MusicGen 是 Meta 的音乐生成模型
  - target: Llama
    note: Llama 是 Meta 的 LLM 家族
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Meta（Facebook 母公司）是开源 AI 的最大玩家之一，靠**两大开源家族**出名：**Llama**（大语言模型）和 **MusicGen / AudioCraft**（音乐生成）。在 AIGC 词条库里，它是「开源 LLM 事实标准」的缔造者——Llama 系列定义了开源大模型的规格，无数下游模型（包括中国的很多开源模型）都基于它微调。

## 原理

Meta 的开源策略是「开放生态换话语权」：把模型权重开源（Llama 系列从 7B 到 405B），让全世界的开发者基于它构建，形成事实标准。技术上 Llama 是标准的 Decoder-only Transformer 架构，靠规模和数据取胜，没有花哨创新但工程极其扎实。音频方向，AudioCraft/MusicGen 用类似扩散+Transformer 的混合架构做音乐生成，MusicGen 的 medium/large 版本至今仍是本地音乐生成的主流选择。

## 由来与历史

Meta 2023 年 2 月发布 Llama 1，首次把 65B 级大模型开源；2023 年 7 月 Llama 2 允许商用，引爆开源 LLM 生态；2024 年 Llama 3 系列（8B/70B/405B）成为开源标杆，405B 一度是最大开源模型。同时期的 MusicGen（2023）也一直保持更新。Meta 的开源模型是「被下游引用最多」的模型家族，无数中文开源模型（如各种 Llama 微调版）都建立在它之上。

## 应用

在 ComfyUI 和本地 AI 里，Meta 模型的两个常见用法：
- **MusicGen**：本地音乐生成首选，medium（1.5B）质量可用、large（3.3B）质量更好，12GB 显存无压力，还能哼一段旋律让它续写（melody 模式）
- **Llama**：本地跑 LLM 的基础模型（配合 Ollama/llama.cpp），GGUF 量化后 12GB 卡能跑 8B 甚至 70B（Q4）

## 争议 / 讨论

Llama 的许可证（Llama Community License）对商用有月活限制（7 亿+用户需申请），被一些开发者诟病「不够开源」；Meta 因此也承受着「开源作秀」的批评。另外 405B 模型虽开源，但本地部署成本极高，实际社区多用 8B/70B 版本。

## 参见

- [Llama](../模型家族/Llama.md)
- [MusicGen](../模型家族/MusicGen.md)
- [GGUF](量化格式/GGUF.md)
- [Ollama](../工具/Ollama.md)
