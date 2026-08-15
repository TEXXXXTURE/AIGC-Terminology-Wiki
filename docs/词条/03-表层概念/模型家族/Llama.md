---
term: Llama
full_name: Llama
aliases: [Llama 2, Llama 3, Meta Llama]
category: 模型
dimension: 模型家族
granularity: 家族
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://huggingface.co/meta-llama
  - https://ai.meta.com/llama/
relations:
  - target: Meta
    note: Llama 是 Meta 的 LLM 家族
  - target: Qwen
    note: Llama 是 Qwen 在开源 LLM 的主要对标
  - target: GGUF
    note: Llama 是 GGUF 量化最经典的载体
  - target: Ollama
    note: Ollama 以跑 Llama 起家
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Llama 是 Meta 的开源大语言模型家族，**定义了开源 LLM 的事实标准**。从 Llama 1 到 Llama 3，它一直是开源大模型的标杆——无数下游模型（微调版、中文版、Agent 版）都基于它构建，本地跑 LLM 的首选基座。

## 原理

Llama 是标准的 Decoder-only Transformer，靠高质量数据 + 工程优化取胜，没有花哨的架构创新但极其扎实。家族规格齐全：7B/8B（消费级）、13B/70B（工作站）、405B（旗舰）。Llama 3 引入了改进的 tokenizer 和更大规模的预训练数据，8B 版本在单卡就能跑，是本地部署性价比之王。

## 由来与历史

2023 年 2 月 Meta 发布 Llama 1（65B 级开源），7 月 Llama 2 允许商用，引爆开源 LLM 生态；2024 年 Llama 3 系列（8B/70B/405B）成为开源标杆，405B 一度是最大开源模型。Llama 的开源让「人人可跑大模型」成为现实，也是 GGUF 量化格式和 Ollama 等本地工具兴起的直接推手。

## 应用

在本地 AI 里，Llama 是跑 LLM 的标准选择：
- 配合 **Ollama** 一键部署：`ollama run llama3.1`
- 配合 **GGUF 量化**：12GB 卡能跑 8B（Q8）甚至 70B（Q4，慢）
- 生态：HuggingFace 上成千上万的 Llama 微调版（中文、代码、角色扮演）

## 争议 / 讨论

Llama 许可证（Llama Community License）对超大月活（7 亿+）商用有限制，被批「不够开源」；405B 虽开源但本地部署成本极高，社区实际多用 8B/70B。

## 参见

- [Meta](../模型厂商/Meta.md)
- [Qwen](Qwen.md)
- [GGUF](量化格式/GGUF.md)
- [Ollama](../工具/Ollama.md)
