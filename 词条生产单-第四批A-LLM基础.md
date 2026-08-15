# 第四批词条生产单 A — LLM 基础层（6 条）

> 依据：CONTENT-SPEC.md v2.1（先完整读它！）
> 产出位置：D:/AIGC术语库/docs/词条/
> 素材库（必读参考）：D:/AIGC术语库/雷达/采集/hf-courses/llm-course/（HF 官方 LLM 课程，权威定义）

## 总要求

- 严格按 CONTENT-SPEC v2.1 模板：frontmatter + 正文（定义/原理/由来与历史/应用/争议（如有）/参见）
- 渲染原则：frontmatter 是坐标，正文是干净人话文章，不渲染标签
- 人话优先，术语首次出现带英文全称
- sources 真实 URL（HF 课程/论文/官方文档）
- relations ≥3 条，target+note 必填，闭合已有 22 词条（神经网络/训练与微调/扩散模型/采样器/文本编码器/CLIP 等）及本批互链
- created/updated = 2026-08-14，contributors: [TEXXXXTURE]

## 词条清单

### 1. Transformer（架构，放 01-底层原理/）
- 文件：docs/词条/01-底层原理/Transformer.md
- category: 架构 ｜ dimension: 底层原理 ｜ granularity: 原理
- 要点：2017 "Attention Is All You Need"；自注意力取代 RNN；编码器-解码器；并行训练；为什么统治一切（LLM/扩散/多模态全是它）；扩散模型里的 DiT 也是 Transformer
- relations: 注意力机制（note: 核心组件是自注意力）、神经网络（note: Transformer 是神经网络的一种架构）、扩散模型（note: DiT 用 Transformer 做去噪网络）、文本编码器

### 2. 注意力机制（Attention，放 01-底层原理/）
- 文件：docs/词条/01-底层原理/注意力机制.md
- category: 架构 ｜ dimension: 底层原理 ｜ granularity: 原理
- 要点：QKV 三件套；缩放点积注意力；多头注意力；"关注哪里"的机制；从 RNN 到 Transformer 的转折；SageAttention 加速的就是它
- relations: Transformer（note: Transformer 的核心机制）、神经网络、SageAttention（note: SageAttention 加速注意力计算）、文本编码器

### 3. Tokenizer（分词器，放 02-组件/）
- 文件：docs/词条/02-组件/Tokenizer.md
- category: 架构 ｜ dimension: 模型组件 ｜ granularity: 组件
- 要点：文本→token id；BPE 算法；词汇表；为什么 token 数影响价格和速度；中英文分词差异
- relations: 文本编码器（note: 分词是编码的第一步）、Transformer（note: token 是 Transformer 的输入）、上下文窗口（note: 上下文按 token 计）

### 4. RAG（检索增强生成，放 03-表层概念/LLM/）
- 文件：docs/词条/03-表层概念/LLM/RAG.md
- category: 上下文工程 ｜ dimension: LLM 技术 ｜ granularity: 具体技术
- 要点：Retrieval-Augmented Generation；外部知识检索+生成；解决幻觉和知识过期；向量数据库；流程：文档切块→embedding→检索→拼进 prompt
- relations: 上下文窗口（note: 检索结果注入上下文）、文本编码器（note: embedding 由编码器生成）、Prompt（note: 检索内容拼进提示词）

### 5. 上下文窗口（Context Window，放 03-表层概念/LLM/）
- 文件：docs/词条/03-表层概念/LLM/上下文窗口.md
- category: 上下文工程 ｜ dimension: LLM 技术 ｜ granularity: 概念
- 要点：一次能看多少 token；从 2K 到 128K/1M 的演进；长上下文的意义与代价（注意力 O(n²)）；KV Cache 与上下文的关系
- relations: Tokenizer（note: 窗口按 token 计）、RAG（note: RAG 是应对窗口限制的手段）、KV Cache（note: 长上下文显存占用来自 KV Cache）、注意力机制

### 6. RLHF（人类反馈强化学习，放 03-表层概念/对齐/）
- 文件：docs/词条/03-表层概念/对齐/RLHF.md
- category: 对齐 ｜ dimension: 对齐技术 ｜ granularity: 具体技术
- 要点：三阶段（SFT→奖励模型→PPO）；让模型对齐人类偏好；OpenAI InstructGPT 首创；代价与替代方案（DPO）；DeepSeek 的 GRPO
- relations: 训练与微调（note: RLHF 是训练后阶段）、对齐（note: 核心目标是对齐人类偏好）、DPO（note: DPO 是 RLHF 的简化替代）

## 完成标准
- 6 个文件在指定位置
- 全部 frontmatter 完整 + 正文五区 + relations≥3
- 报告：每个文件路径 + 一句话概括
