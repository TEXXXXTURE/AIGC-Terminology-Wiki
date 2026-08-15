---
term: MCP
full_name: Model Context Protocol
aliases: [模型上下文协议]
category: Agent
dimension: Agent 生态
granularity: 具体技术
maturity: hot
status: published
contributors: [TEXXXXTURE]
sources:
  - https://www.anthropic.com/news/model-context-protocol
  - https://modelcontextprotocol.io/
  - https://github.com/modelcontextprotocol/servers
relations:
  - type: evolved_from
    target: Function Calling
    note: MCP 是工具调用的标准化
  - type: applies_to
    target: Agent
    note: Agent 通过 MCP 接外部工具
  - type: applies_to
    target: 上下文窗口
    note: MCP 注入的工具描述与结果都占用上下文窗口
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

🟡 社区热词，未经沉淀，信息可能快速过时

MCP（Model Context Protocol，模型上下文协议）是 Anthropic 于 2024 年底推出的开放协议，目标是统一「AI 应用怎么连接外部数据和工具」。在 MCP 之前，每接一个数据源或工具都要写一套定制对接代码；MCP 把这个接口标准化，就像「AI 界的 USB-C」——工具提供方写一个 MCP 服务器，任何支持 MCP 的客户端（Claude Desktop、Cursor、各类 IDE 和 Agent 框架）都能即插即用。

## 原理

MCP 采用客户端—服务器架构：宿主应用（如 Claude Desktop）里的 MCP 客户端，通过标准协议连到一个个 MCP 服务器；每个服务器对外暴露三类能力——工具（Tools，可执行的动作）、资源（Resources，可读的数据）、提示模板（Prompts）。连接建立后，服务器把工具描述交给宿主，宿主再经 [Function Calling](Function%20Calling.md) 让模型决定何时调用——也就是说 MCP 不取代函数调用，而是把「工具从哪来、长什么样」标准化。这些工具描述和返回结果最终都进[上下文窗口](../LLM/上下文窗口.md)，所以接的服务器越多、窗口压力越大。

## 由来与历史

2024 年 11 月 25 日，Anthropic 发布 MCP 并开源协议规范与一批参考服务器（GitHub、Slack、文件系统、数据库等），动机很明确：彼时每家公司、每个框架都在各搞一套工具接口，生态碎片化严重。发布后采纳速度超预期：2025 年 OpenAI 宣布在自家产品支持 MCP，Google、微软跟进，Cursor、Windsurf 等 IDE 全面接入，社区服务器数量爆炸式增长。从「Anthropic 一家的协议」变成事实上的行业标准，MCP 只用了一年左右——这也是它目前仍被视为快速演进中的热词的原因。

## 应用

个人用户最直接的用法：在 Claude Desktop 或 Cursor 的配置文件里加几行 JSON，挂上现成的 MCP 服务器（文件系统、浏览器、数据库……），应用立刻获得对应能力。开发者则可以用官方 SDK（TypeScript/Python 等）给自己的服务写 MCP 服务器，一次开发、处处可用。注意事项：服务器质量参差不齐，安装第三方服务器等于给它开了访问本地数据和执行命令的权限，来源不明的服务器有供应链与提示注入风险；另外挂太多服务器会把工具描述塞满上下文，影响模型选择工具的准确率。

## 争议 / 讨论

- **安全风险**：MCP 服务器能读写本地资源、执行命令，恶意或被投毒的工具描述可以诱导模型执行危险操作（工具投毒攻击）。协议自身的鉴权与安全模型仍在快速补齐，生产环境使用需谨慎审计。
- **标准之争**：MCP 虽占先机，但围绕「协议该多复杂」「是否过度依赖 LLM 自主决策」一直有争论，也有团队选择更轻量的自研接口。它能否像 USB-C 那样真正统一生态，尚需时间检验。

## 参见

- [Function Calling](Function%20Calling.md)
- [Agent](Agent.md)
- [上下文窗口](../LLM/上下文窗口.md)
