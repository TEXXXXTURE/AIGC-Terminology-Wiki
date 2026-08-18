# 第四批词条生产单 B — Agent 与推理方向（6 条）

> 依据：CONTENT-SPEC.md v2.1（先完整读它！）
> 产出位置：D:/AIGC术语库/docs/词条/
> 素材库（必读参考）：D:/AIGC术语库/雷达/采集/hf-courses/agents-course/（HF 官方 Agent 课程）

## 总要求

- 严格按 CONTENT-SPEC v2.1 模板：frontmatter + 正文（定义/原理/由来与历史/应用/争议（如有）/参见）
- 渲染原则：frontmatter 是坐标，正文是干净人话文章，不渲染标签
- 人话优先，术语首次出现带英文全称
- sources 真实 URL（HF 课程/论文/官方文档）
- relations ≥3 条，target+note 必填，闭合已有 28 词条（含本批 A 的 Transformer/注意力/RAG/上下文窗口 等）及本批互链
- created/updated = 2026-08-14，contributors: [TEXXXXTURE]

## 词条清单

### 1. Agent（智能体，放 03-表层概念/Agent/）
- 文件：docs/词条/03-表层概念/Agent/Agent.md
- category: Agent ｜ dimension: Agent 生态 ｜ granularity: 概念
- 要点：能自主规划+调用工具+记忆的 LLM 应用；ReAct 循环（思考-行动-观察）；工具调用是核心；单 Agent vs 多 Agent；你日常用的 Hermes/Claude Code 就是 Agent
- relations: Function Calling（note: Agent 调用工具的方式）、上下文窗口（note: Agent 的循环受窗口限制）、RAG（note: 记忆常借助 RAG）、Transformer

### 2. Function Calling（函数调用，放 03-表层概念/Agent/）
- 文件：docs/词条/03-表层概念/Agent/Function Calling.md
- category: Agent ｜ dimension: Agent 生态 ｜ granularity: 具体技术
- 要点：模型输出结构化 JSON 调用外部函数；tool schema 定义；OpenAI 2023 年开创；MCP 是它的标准化演进；Agent 的行动能力来源
- relations: Agent（note: Agent 靠它执行动作）、MCP（note: MCP 标准化了工具调用）、LLM 推理（note: 模型需专门训练此能力）

### 3. MCP（Model Context Protocol，放 03-表层概念/Agent/）
- 文件：docs/词条/03-表层概念/Agent/MCP.md
- category: Agent ｜ dimension: Agent 生态 ｜ granularity: 具体技术
- 要点：Anthropic 2024 推出的开放协议；工具/资源/提示的统一接口；"AI 的 USB-C"；客户端-服务器架构；Hermes 支持 MCP 服务器
- relations: Function Calling（note: MCP 是工具调用的标准化）、Agent（note: Agent 通过 MCP 接外部工具）、平台

### 4. DPO（Direct Preference Optimization，放 03-表层概念/对齐/）
- 文件：docs/词条/03-表层概念/对齐/DPO.md
- category: 对齐 ｜ dimension: 对齐技术 ｜ granularity: 具体技术
- 要点：2023 年 Stanford 提出；跳过奖励模型和强化学习，直接优化偏好；RLHF 的简化替代；数据=偏好对（chosen/rejected）；训练更稳更省
- relations: RLHF（note: DPO 是 RLHF 的替代方案）、训练与微调（note: DPO 是训练后对齐）、对齐（note: 目标是对齐人类偏好）

### 5. 越狱（Jailbreak，放 03-表层概念/对齐/）
- 文件：docs/词条/03-表层概念/对齐/越狱.md
- category: 对齐 ｜ dimension: 对齐技术 ｜ granularity: 概念
- 要点：绕过模型安全对齐的提示词/方法；DAN、角色扮演等经典手法；对抗训练 vs 越狱的攻防；为什么越狱不可避免（对齐是概率性的）
- relations: 对齐（note: 越狱是对齐的对抗面）、RLHF（note: RLHF 是防御手段）、上下文工程（note: 越狱本质是提示词工程）

### 6. KV Cache（键值缓存，放 03-表层概念/LLM/）
- 文件：docs/词条/03-表层概念/LLM/KV Cache.md
- category: 推理 ｜ dimension: 推理优化 ｜ granularity: 具体技术
- 要点：注意力计算中缓存的 K/V 矩阵；避免重复计算；长上下文显存大户（O(n) 每层）；量化/剪枝 KV Cache 是优化方向；与显存的关系（你 12GB 卡跑长上下文的关键瓶颈）
- relations: 注意力机制（note: 缓存的是注意力的 K/V）、上下文窗口（note: 长窗口显存来自 KV Cache）、量化（note: KV Cache 可量化压缩）、推理优化

## 完成标准
- 6 个文件在指定位置
- 全部 frontmatter 完整 + 正文五区 + relations≥3
- 报告：每个文件路径 + 一句话概括
