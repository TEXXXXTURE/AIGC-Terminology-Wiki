---
term: Tokenizer
full_name: Tokenizer
aliases: [分词器, 分词, Tokenization]
category: 架构
dimension: 模型组件
granularity: 组件
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/1508.07909
  - https://huggingface.co/docs/transformers/tokenizer_summary
  - https://huggingface.co/learn/llm-course/chapter1/5
relations:
  - type: applies_to
    target: 文本编码器
    note: 分词是文本编码的第一步
  - type: applies_to
    target: Transformer
    note: token 是 Transformer 的输入
  - type: applies_to
    target: 上下文窗口
    note: 上下文窗口按 token 计
  - type: applies_to
    target: RAG
    note: RAG 流程里文档要先分词再切块
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Tokenizer（分词器）是文本进入模型的第一道门：它把一句人话切成一个个模型认识的「token」（词元），再把每个 token 映射成一个数字 id。模型其实不认识字，只认识这些 id——所以「分词」是理解文本前的必经预处理。对使用者来说，token 还是计费、限长、测速的基本单位。

## 原理

分词 + 查表两步走：先按一定规则把文本切成片段，再查词汇表（vocabulary，一张 token→id 的对照表）得到一串整数。这串整数再交给[文本编码器](文本编码器.md)变成向量。真正进入 Transformer 的，是这串 token id。

现代分词器的主流算法是 BPE（Byte Pair Encoding，字节对编码）：从一个字符一个字符开始，统计语料里最常相邻出现的字符对，把它们合并成一个新 token，反复合并直到词汇表达到预设大小。结果是高频词作为整词保留（「the」是一个 token），低频词和生造词被拆成子词（「tokenization」可能拆成「token」+「ization」），既能控制词汇表大小，又不怕遇到没见过的词。BERT 系的 WordPiece 是思路相近的变体。

为什么 token 数这么重要？因为大模型的计费、上下文长度、生成速度全都按 token 算——同样一段话，被切得越碎，token 就越多，价格越贵、占用的[上下文窗口](../03-表层概念/LLM/上下文窗口.md)越大、生成越慢。中文和英文的切分差异很大：英文天然按空格分词、常用词往往 1 token；中文没有空格，常按字或词切，同等语义的中文通常比英文 token 数更多——这也是很多模型中文「变贵、变短」的原因之一。

## 由来与历史

早期 NLP 按空格或整词分词，遇到没见过的词（OOV, out-of-vocabulary）就抓瞎。2016 年 Sennrich 等人把 BPE 从数据压缩引入机器翻译（arXiv:1508.07909），用「子词」解决了 OOV 问题，此后成为标配。GPT 系用 BPE，BERT 系用 WordPiece，各自演化出配套的 tokenizer。如今 tokenizer 和模型绑定发布——换模型必须换对应的 tokenizer，否则 id 对不上，输出全是乱码。

## 应用

实用中你最常接触 tokenizer 的三个场景：一是看上下文预算——想知道一段文字会不会超长，先数 token 而不是数字数（Hugging Face 有在线的 tokenizer 演示页可查）；二是估算成本——API 计费按 token，中文场景要留意 token 膨胀；三是理解「为什么同一个词在不同模型里 token 数不同」——词汇表不同。在 RAG 等工程里，文档也是先分词再切块、向量化的。

## 参见

- [文本编码器](文本编码器.md)
- [Transformer](../01-底层原理/Transformer.md)
- [上下文窗口](../03-表层概念/LLM/上下文窗口.md)
- [RAG](../03-表层概念/LLM/RAG.md)
