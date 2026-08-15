---
term: Lightricks
full_name: Lightricks
aliases: [LTX, Lightricks 以色列]
category: 平台
dimension: 模型厂商
granularity: 厂商
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://www.lightricks.com/
  - https://huggingface.co/Lightricks
relations:
  - target: MiniMax
    note: 同为视频模型厂商，LTX 主攻效率、H3 主攻质量
  - target: 阿里
    note: Wan 是 LTX 在视频领域的主要竞品
  - target: Stability AI
    note: 同有消费级工具产品线
  - target: LTX
    note: LTX 是 Lightricks 的视频模型家族
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Lightricks 是以色列的公司，老牌移动端图片/视频编辑工具开发商（知名产品有 Facetune、Videoleap），2024 年杀入 AI 视频生成，开源了 **LTX 系列视频模型**。它的差异化标签是「**快**」——LTX-Video 是当时最快的开源视频生成模型，主打效率而非单纯画质。

## 原理

Lightricks 的视频模型走「效率优先」路线：LTX-Video（2B）采用精简架构 + 潜空间扩散，生成速度比同期竞品快一个数量级，中端显卡就能实时预览；后续 LTX-2 升级为 MoE（混合专家）架构，LTX-2.3 把质量做到接近第一梯队。它的理念是「让视频生成像打字一样流畅」——速度是体验的核心。

## 由来与历史

Lightricks 2013 年成立，靠手机修图 App 起家（Facetune 曾是现象级产品）。2024 年底开源 LTX-Video，凭借速度优势在开源视频社区迅速出圈；2025 年迭代 LTX-2（MoE 架构）、LTX-2.3/2.5，逐步补齐画质短板。它把「消费级工具公司」的基因带进了 AI 视频——非常在意生成速度和用户体验。

## 应用

在 ComfyUI 里，LTX 系列的选择逻辑：
- **LTX-Video 2B**：12GB 卡能跑，速度快，适合先跑通视频工作流、快速预览想法
- **LTX-2/2.3/2.5**：质量提升但体积暴涨（8B→22B），fp8 量化版都要 22GB，你的 12GB 卡放不下，建议 GGUF 低量化或放弃

一句话：你的卡上 LTX 只适合当「快速预览工具」，追求画质还是看 MiniMax H3 或 Wan。

## 争议 / 讨论

LTX 早期模型有「快但糊」的口碑——速度换来的是细节不足，社区曾戏称「LTX 出的是短视频预览而非成片」。后续版本质量追上来，但「效率 vs 质量」的路线之争在社区一直存在。另外 LTX 的模型迭代过快，老版本（LTX-1）很快被社区遗忘。

## 参见

- [MiniMax](MiniMax.md)
- [LTX](../模型家族/LTX.md)
- [MoE](01-底层原理/MoE.md)
- [GGUF](量化格式/GGUF.md)
