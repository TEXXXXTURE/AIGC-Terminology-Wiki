---
term: DeepSeek
full_name: DeepSeek (深度求索)
aliases: [深度求索, DeepSeek AI]
category: 模型
dimension: 模型厂商
granularity: 厂商
maturity: stable
status: draft
contributors: [TEXXXXTURE]
sources:
  - https://deepseek.com
  - https://huggingface.co/deepseek-ai
relations:
  - target: Qwen
    note: DeepSeek 和 Qwen 是中文开源 LLM 的双雄
  - target: 阿里
    note: DeepSeek 与阿里是中文大模型的主要竞争者
created: 2026-08-17
updated: 2026-08-17
revisions: 1
---

## 定义

DeepSeek(深度求索)是中国头部 AI 模型厂商,以极致性价比和开源策略闻名。DeepSeek V4 Pro 是其最新旗舰,智能指数 53.2,价格仅 $1.32/$3.96——比 GPT-5.6 Terra 便宜一半以上。DeepSeek 的技术路线强调 MoE(混合专家)架构,用更少的激活参数实现更强能力。

## 由来与历史

2023 年由量化基金幻方量化创立。DeepSeek V2(2024)引入 MoE+MLA 架构,在中文社区一战成名。DeepSeek V3(2025)进一步优化推理效率。DeepSeek R1(2025)是开源推理模型标杆。V4 Pro(2026)是当前版本,价格持续下探,成为中国 AI 基础设施的关键供应商。

## 应用

DeepSeek V4 Pro 在 AA 评测中智能指数 53.2,输出速度 80 tok/s,输入 $1.32/M、输出 $3.96/M。在同档位(50+ 分)里价格最低。适合需要中文能力的高性价比推理场景。DeepSeek 也提供缓存命中 $0.044/M 的极低复读价。

## 参见

- [模型数据总览](../../04-LLM工程/模型数据总览.md)
- [模型评测](../../04-LLM工程/模型评测.md)
