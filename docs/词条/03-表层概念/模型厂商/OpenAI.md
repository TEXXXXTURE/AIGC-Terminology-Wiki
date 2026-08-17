---
term: OpenAI
full_name: OpenAI
aliases: [OpenAI Inc.]
category: 模型
dimension: 模型厂商
granularity: 厂商
maturity: stable
status: draft
contributors: [TEXXXXTURE]
sources:
  - https://openai.com
  - https://platform.openai.com/docs
relations:
  - target: MiniMax
    note: OpenAI 和 MiniMax 是中外闭源模型的代表
created: 2026-08-17
updated: 2026-08-17
revisions: 1
---

## 定义

OpenAI 是全球最大的 AI 模型厂商,GPT 系列的创造者。从 GPT-3 到 GPT-5.6,它定义了大模型的主流形态——闭源 API、按 token 付费。最新 GPT-5.6 系列分三个档位:Luna(速度快、性价比高)、Sol(旗舰推理)、Terra(平衡档),均支持百万级上下文。

## 由来与历史

2015 年成立,初期以非营利 AI 研究实验室自居。2020 年 GPT-3 一战成名,2022 年 ChatGPT 引爆全球 AI 热潮。2024 年转型营利公司,估值突破千亿美元。2025-2026 年密集发布 GPT-5 系列(5.0→5.5→5.6),同时推出开源模型 gpt-oss 系列,回应 Meta 和 DeepSeek 的开源竞争。

## 应用

在 API 层面,OpenAI 的 GPT-5.6 Luna 是当前性价比最高的旗舰级模型之一(输入 $0.20/M、输出 $1.20/M、速度 175 tok/s)。本地部署不适用(闭源),但 gpt-oss-120b 是 OpenAI 的开放权重版本,速度 179 tok/s,适合本地推理。

## 参见

- [模型数据总览](../../04-LLM工程/模型数据总览.md)
- [模型评测](../../04-LLM工程/模型评测.md)
