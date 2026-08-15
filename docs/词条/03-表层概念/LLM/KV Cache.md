---
term: KV Cache
full_name: Key-Value Cache
aliases: [键值缓存]
category: 推理
dimension: 推理优化
granularity: 具体技术
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/1706.03762
  - https://arxiv.org/abs/1911.02150
  - https://arxiv.org/abs/2309.06180
relations:
  - type: applies_to
    target: 注意力机制
    note: 缓存的正是注意力计算中的 K/V 矩阵
  - type: applies_to
    target: 上下文窗口
    note: 长窗口的显存压力主要来自 KV Cache
  - type: applies_to
    target: 量化
    note: KV Cache 可量化压缩以省显存
  - type: part_of
    target: 推理优化
    note: KV Cache 是推理加速与显存优化的核心对象
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

KV Cache（Key-Value Cache，键值缓存）是大模型生成文本时用来「记住前面算了什么」的缓存：模型逐词生成，每生成一个新词都要回顾前文，如果每次重新算一遍，代价是平方级的浪费；把前文每个 token 在注意力层算出的 Key 和 Value 矩阵存下来复用，生成速度立刻快一个量级。它是现代 LLM 推理的标配，但也是显存的头号消耗者。

## 原理

自回归生成时，第 N 个 token 的注意力需要和前 N-1 个 token 的 Key/Value 做点积——这些是[注意力机制](../../01-底层原理/注意力机制.md)里的中间量，只依赖已有内容，算过一次就不会变，所以缓存起来直接查表即可。代价是显存：KV Cache 随序列长度线性增长（每层、每个 token 都要存一份 K 和 V），模型越大、层数越多、[上下文窗口](上下文窗口.md)越长，缓存越膨胀。压缩手段包括 MQA/GQA（多个注意力头共享一份 K/V）、KV Cache [量化](../../01-底层原理/量化.md)、以及 PagedAttention 的显存分页管理（arXiv:2309.06180）。

## 由来与历史

KV Cache 的思想随 2017 年 Transformer 论文（arXiv:1706.03762）的自回归解码而来——缓存已计算的 K/V 几乎是增量解码的自然做法。它从「实现细节」变成「研究热点」是在长上下文时代：2019 年的 MQA（Multi-Query Attention，arXiv:1911.02150）首次为省缓存牺牲一点模型容量，后来的 GQA 成为 Llama 等主流模型的标配；2023 年 vLLM 的 PagedAttention 借鉴操作系统虚拟内存的思想管理缓存碎片，把吞吐量提升数倍；此后 KV Cache 量化（压到 int8/int4 甚至更低）、稀疏化与逐出策略成为推理优化的主战场。

## 应用

对本地跑模型的用户，KV Cache 是实打实的显存账：以一张 12GB 显卡为例，模型权重占掉大半后，剩余显存能容纳多长的上下文，几乎完全由 KV Cache 决定——这就是为什么「上下文拉到 32K 就爆显存」。实用手段：在 llama.cpp、vLLM 等推理引擎里开启 KV Cache 量化（如 `--cache-type-k q8_0`），能把缓存显存减半甚至更多；多轮对话及时清理历史、长文档用 [RAG](RAG.md) 代替全文塞入，也能直接削减缓存占用。云端 API 侧则对应「prompt caching」计费项——命中缓存的历史部分便宜得多。

## 争议 / 讨论

- **压缩与效果的权衡**：KV Cache 量化、逐出旧 token 等压缩手段在长文本任务上或多或少掉点，「压到多狠才划算」没有统一答案，不同基准结论时有冲突。
- **线性注意力的替代路线**：Mamba 等状态空间模型试图用固定大小的状态彻底取代 KV Cache，省显存很诱人，但在需要精确回忆长程细节的任务上仍难撼动注意力，两条路线的竞争还在继续。

## 参见

- [注意力机制](../../01-底层原理/注意力机制.md)
- [上下文窗口](上下文窗口.md)
- [量化](../../01-底层原理/量化.md)
- [RAG](RAG.md)
