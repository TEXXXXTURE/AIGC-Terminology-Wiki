---
term: RAG
full_name: Retrieval-Augmented Generation
aliases: [检索增强生成]
category: 上下文工程
dimension: LLM 技术
granularity: 具体技术
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/2005.11401
  - https://arxiv.org/abs/2312.10997
relations:
  - type: applies_to
    target: 上下文窗口
    note: 检索到的内容被注入上下文窗口
  - type: applies_to
    target: 文本编码器
    note: 文档与查询的向量由文本编码器生成
  - type: applies_to
    target: Tokenizer
    note: 文档切块前先被分词
  - target: 提示词工程
    note: 检索结果最终拼进提示词
  - type: applies_to
    target: 注意力机制
    note: 生成端靠注意力整合检索内容与问题
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

RAG（Retrieval-Augmented Generation，检索增强生成）是一种让大模型「先查资料再回答」的方法：在模型生成之前，先从外部知识库检索出和问题最相关的内容，把查到的资料拼进提示词，再让模型据此作答。它要解决的是 LLM 的两大老毛病——幻觉（一本正经地胡说）和知识过期（训练数据有截止日期）。给模型一本「随时可查的书」，比指望它把什么都背下来更靠谱。

## 原理

流程可以概括成「切块→向量化→检索→拼接→生成」：先把文档切成小块，用[文本编码器](../../02-组件/文本编码器.md)把每块和用户问题都转成向量，存入向量数据库；提问时找出与问题向量最相似的若干块，拼进 prompt 交给 LLM 生成答案。这里的向量化和生成分别依赖编码器与 [Transformer](../../01-底层原理/Transformer.md)，检索注入的内容则占用[上下文窗口](上下文窗口.md)——所以 RAG 本质是「用外部检索换有限的窗口」。

## 由来与历史

2020 年，Meta（当时 Facebook AI）的 Lewis 等人发表论文《Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks》（arXiv:2005.11401），正式提出 RAG 框架。真正让它爆火的是 2022 年底 ChatGPT 之后：大家发现 LLM 虽然会说话，但私有数据不知道、最新知识没有、还爱编造，RAG 恰好是成本最低的补救方案。2023 年起，向量数据库（FAISS、Milvus、pgvector 等）和编排框架（LangChain、LlamaIndex 等）把 RAG 做成了一套成熟工程，成为企业落地 LLM 的默认姿势。

## 应用

典型场景：企业知识库问答、客服机器人、私有文档助手——把公司手册、产品文档切块入库，用户提问时检索作答，让模型「只基于给定资料说话」。工程上有几个关键旋钮：切块大小（chunk size，太大检索不准、太小丢了上下文）、检索条数（top-k）、以及要不要加「重排序」（rerank）提升命中率。检索质量直接决定答案质量——喂给模型的资料错了，生成再漂亮也是错的。

## 争议 / 讨论

RAG 常被拿来和「长上下文」对比：上下文窗口越做越大（百万 token），有人质疑「干脆把整本书塞进窗口，还要检索吗」。目前的主流观点是两者互补——长上下文适合精读小规模材料，RAG 适合海量文档里大海捞针；而且检索能省 token、降成本。另一个争议点是「lost in the middle」：模型对拼在中间的检索片段容易忽略，所以片段顺序和数量仍需精心设计。

## 参见

- [上下文窗口](上下文窗口.md)
- [文本编码器](../../02-组件/文本编码器.md)
- [Tokenizer](../../02-组件/Tokenizer.md)
- [注意力机制](../../01-底层原理/注意力机制.md)
