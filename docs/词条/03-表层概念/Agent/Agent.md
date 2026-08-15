---
term: Agent
full_name: AI Agent
aliases: [智能体, AI 智能体]
category: Agent
dimension: Agent 生态
granularity: 概念
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://huggingface.co/learn/agents-course/unit1/what-are-agents
  - https://arxiv.org/abs/2210.03629
  - https://arxiv.org/abs/2302.04761
relations:
  - type: applies_to
    target: Function Calling
    note: Agent 调用工具的方式
  - type: applies_to
    target: 上下文窗口
    note: Agent 的多轮循环受窗口限制
  - type: applies_to
    target: RAG
    note: Agent 的长期记忆常借助 RAG
  - type: applies_to
    target: Transformer
    note: Agent 的大脑是 Transformer 类 LLM
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Agent（智能体）是一种「能自己干活」的大模型应用：普通的 LLM 只会一问一答，而 Agent 在 LLM 这个「大脑」外面套了一个循环——它能自己规划步骤、调用工具（搜索、代码执行、API 等）、记住中间结果，直到把任务做完。你让它「帮我订明天去上海的机票」，它不会只回一句建议，而是真的去查航班、比价格、走下单流程。你日常用的 Claude Code、Manus 这类工具，本质上都是 Agent。

## 原理

Agent 的核心是一个「思考—行动—观察」（Thought / Action / Observation）循环：LLM 先输出一段思考决定下一步做什么，然后发起一个动作（通常是[Function Calling](Function%20Calling.md)，即调用一个工具），工具执行后把结果作为「观察」喂回模型，模型再决定下一步，直到任务完成。这个模式来自 ReAct 论文（arXiv:2210.03629）。循环每转一轮，思考和结果都占[上下文窗口](../LLM/上下文窗口.md)，所以 Agent 的实际能力受窗口大小和工具质量两头制约；需要记住的长期信息则常靠 [RAG](../LLM/RAG.md) 检索补充。大脑本身仍是 [Transformer](../../01-底层原理/Transformer.md)，这里不重复展开。

## 由来与历史

让语言模型「会用工具」的想法在 2023 年初集中爆发：Meta 的 Toolformer（arXiv:2302.04761）证明模型可以自学何时调用计算器、搜索引擎；几乎同时，LangChain 等框架把「LLM + 工具 + 循环」工程化，AutoGPT 一度成为现象级开源项目。2023 年中 OpenAI 推出 [Function Calling](Function%20Calling.md)，把工具调用从「提示词技巧」变成模型的原生能力；2024 年 Anthropic 推出 [MCP](MCP.md)，进一步把「接什么工具」标准化。到 2025 年，Claude Code、Manus、各家 Deep Research 让 Agent 从演示走向日常生产力工具。

## 应用

实践中分单 Agent 和多 Agent：单 Agent 一个大脑跑完整循环，简单可靠，适合写代码、查资料这类线性任务；多 Agent 把任务拆给多个角色（规划者、执行者、评审者）协作，能力上限更高但更难调试、token 消耗成倍。搭建上手可以走 Hugging Face 的 Agents Course，用 smolagents、LangGraph、LlamaIndex 等框架；接外部工具优先考虑现成 MCP 服务器。常见坑：循环失控（死循环刷 token）、工具描述写得太含糊导致模型选错工具、以及长任务把窗口撑爆——需要主动做上下文压缩。

## 争议 / 讨论

- **Agent 是不是新瓶装旧酒**：批评者认为多数 Agent 只是「LLM + while 循环 + 一堆 prompt」，没有理论上的新东西；支持者则指出工具调用和长程规划带来的能力跃迁是实打实的，工程复杂度本身也是护城河。
- **可靠性天花板**：单步准确率 95% 的模型，连走 20 步只剩三成多成功率，这让「长程自主任务」至今不稳。多数生产级 Agent 仍然需要人在关键环节确认，「全自动」更多是营销话术而非现状。

## 参见

- [Function Calling](Function%20Calling.md)
- [MCP](MCP.md)
- [上下文窗口](../LLM/上下文窗口.md)
- [RAG](../LLM/RAG.md)
- [Transformer](../../01-底层原理/Transformer.md)
