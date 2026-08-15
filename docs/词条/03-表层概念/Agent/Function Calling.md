---
term: Function Calling
full_name: Function Calling
aliases: [函数调用, 工具调用, Tool Calling]
category: Agent
dimension: Agent 生态
granularity: 具体技术
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://openai.com/index/function-calling-and-other-api-updates/
  - https://huggingface.co/learn/agents-course/unit1/actions
  - https://arxiv.org/abs/2302.04761
relations:
  - type: applies_to
    target: Agent
    note: Agent 靠它执行动作
  - type: evolved_from
    target: MCP
    note: MCP 把工具调用进一步标准化
  - type: applies_to
    target: 训练与微调
    note: 模型需专门训练才能可靠输出函数调用
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Function Calling（函数调用，也常叫 Tool Calling，工具调用）是让大模型「调用外部函数」的能力：开发者把可用函数的名字、参数、用途以结构化的描述（tool schema）告诉模型，模型在需要时不再输出自然语言，而是输出一段结构化的 JSON——「调用 search 函数，参数 query=北京天气」。真正的执行由外部程序完成，结果再喂回模型继续生成。它是 LLM 从「聊天机器人」变成「能办事的 Agent」的关键一跃。

## 原理

Function Calling 本质上是让模型学会输出「格式严格受约束」的文本：tool schema 以 JSON 形式随提示词一起进入[上下文窗口](../LLM/上下文窗口.md)，模型生成的函数名和参数必须是合法 JSON，程序解析后执行、把返回值拼回对话。这种能力不是凭空来的——模型要在[训练与微调](../../01-底层原理/训练与微调.md)阶段专门用工具调用数据训练（如 Toolformer 的自监督方式，arXiv:2302.04761），否则参数格式错误率会很高。

## 由来与历史

2023 年初，Toolformer 和 ReAct 等工作证明「LLM + 工具」的巨大潜力，但当时工具调用靠提示词约定格式，脆弱且各家不通用。转折点在 2023 年 6 月：OpenAI 在 GPT-3.5/4 的 API 中原生支持 Function Calling，模型经过专门训练能稳定输出结构化调用，随后各家模型（Claude、Gemini、Qwen、DeepSeek）纷纷跟进，「tool calling 支持」成为模型标配。2024 年 Anthropic 推出 [MCP](MCP.md)，把「工具怎么描述、怎么发现、怎么连接」统一成开放协议，Function Calling 从「单家 API 特性」演进为生态标准的地基。

## 应用

在 API 里使用 Function Calling 通常是三步：定义 tool schema（函数名、JSON Schema 参数、描述）、把 schema 随请求发给模型、收到模型的调用请求后在本地执行并回传结果。写好 schema 是门手艺：描述含糊模型会选错工具，参数约束不严会生成非法调用。面向 Agent 开发时，建议优先接 MCP 服务器而不是手写每个 schema；Hugging Face Agents Course 的第一单元就有用普通 Python 函数当工具的完整示例。

## 争议 / 讨论

- **可靠性仍不完美**：参数幻觉（编造不存在的参数值）、该调用时不调用、并发调用顺序错误等问题依然存在，生产系统普遍需要 schema 校验、重试和人工兜底。
- **各家方言问题**：OpenAI、Anthropic、Google 的 tool schema 格式细节长期不一致，跨模型迁移有成本——这正是 MCP 出现要解决的问题之一。

## 参见

- [Agent](Agent.md)
- [MCP](MCP.md)
- [训练与微调](../../01-底层原理/训练与微调.md)
- [上下文窗口](../LLM/上下文窗口.md)
