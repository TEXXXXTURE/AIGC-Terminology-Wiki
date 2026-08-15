---
term: LTX
full_name: LTX 视频模型
aliases: [LTX-Video, LTX-2, LTX-2.3, LTX-2.5]
category: 模型
dimension: 模型家族
granularity: 家族
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://huggingface.co/Lightricks
  - https://www.lightricks.com/
relations:
  - target: Lightricks
    note: LTX 是 Lightricks 的视频模型家族
  - target: Wan
    note: Wan 质量优先，LTX 效率优先
  - target: MiniMax H3
    note: H3 是 LTX 在质量路线上的对手
  - target: MoE
    note: LTX-2 起采用 MoE 架构
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

LTX 是 Lightricks 的视频生成模型家族，主打「**快**」：LTX-Video（2B）曾是开源最快的视频生成模型，中端显卡即可快速出片。家族从 LTX-Video 迭代到 LTX-2（MoE 架构）、LTX-2.3/2.5（质量补强），是「效率优先」路线的代表。

## 原理

LTX 系列的技术核心是「精简架构换速度」：LTX-Video 用紧凑的潜空间扩散设计，把生成速度做到同期竞品的数量级优势；LTX-2 转向 MoE（混合专家）架构——总参数大但每次只激活一部分专家，兼顾速度与容量；LTX-2.3 进一步优化质量。它的理念是视频生成应该「像打字一样流畅」，速度即体验。

## 由来与历史

Lightricks 2013 年靠手机修图 App 起家（Facetune 是现象级产品），2024 年底开源 LTX-Video，凭速度出圈；2025 年迭代 LTX-2（MoE）、LTX-2.3/2.5，逐步补齐画质短板。它是「消费级工具公司转型 AI 视频」的代表案例——产品基因决定了它更在意速度和易用性，而非堆参数。

## 应用

在 ComfyUI 里，LTX 的选型看显存和用途：
- **LTX-Video 2B**：12GB 卡能跑，速度快，适合快速预览想法、跑通视频工作流
- **LTX-2/2.3/2.5**：质量提升但体积暴涨（8B→22B），fp8 都要 22GB，你的 12GB 卡放不下，GGUF 低量化才勉强
- 定位：你的卡上 LTX 是「快速预览工具」，追求画质看 MiniMax H3 或 Wan

## 争议 / 讨论

LTX 早期有「快但糊」口碑——速度换细节，社区戏称「短视频预览器而非成片工具」。迭代过快导致老版本（LTX-1）被遗忘。「效率 vs 质量」的路线之争在视频生成社区持续存在，LTX 是效率派的旗帜。

## 参见

- [Lightricks](../模型厂商/Lightricks.md)
- [Wan](Wan.md)
- [MoE](../../01-底层原理/MoE.md)
- [GGUF](../量化格式/GGUF.md)
