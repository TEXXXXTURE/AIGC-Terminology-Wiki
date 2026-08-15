---
term: Stability AI
full_name: Stability AI
aliases: [Stability, 英国 Stability]
category: 平台
dimension: 模型厂商
granularity: 厂商
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://stability.ai/
  - https://huggingface.co/stabilityai
relations:
  - target: Black Forest Labs
    note: BFL 是 Stability 核心成员出走创立的竞对
  - target: 阿里
    note: Stability 的开源生态地位被阿里等追赶
  - target: Stable Diffusion
    note: SD 是 Stability 的开源图像模型家族
  - target: Stable Audio
    note: Stable Audio 是 Stability 的音频模型
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Stability AI 是英国的开源生成模型公司，2020 年成立，**Stable Diffusion（SD）系列**的出品方——正是 SD 在 2022 年把文生图从云端 API 带到每个人的显卡上，引爆了整个 AIGC 创作生态。它是「开源图像生成」这一概念的缔造者，也是你 ComfyUI 里 SDXL 的娘家。

## 原理

Stability 的路线是「把前沿模型开源普惠」：基于 CompVis 小组的 Latent Diffusion 研究，把文生图模型做成普通人显卡能跑的大小，靠社区生态取胜。SD 系列走「基座模型 + 社区微调」路线——官方出基础模型（SD 1.5、SDXL），社区（CivitAI）在上面做海量 LoRA 和画风模型，形成巨大的生态飞轮。它同时探索音频（Stable Audio）、视频（SVD）等多模态。

## 由来与历史

2022 年 8 月，Stability AI 发布 Stable Diffusion v1，开源模型首次做到消费级显卡跑文生图，直接引爆 AIGC 时代，公司估值一度冲到 10 亿美元级别。2023 年发布 SDXL（目前仍是社区生态最繁荣的图像模型）。但公司内部一直动荡：创始团队（后来创立 BFL）出走、财务压力巨大、多次传出裁员和资金危机。到 FLUX 出现后，Stability 在画质上被 BFL 反超，开源图像王座易主。

## 应用

在 ComfyUI 里，Stability 的 SDXL 是**你的图类主力**：
- SDXL 基座 + 社区画风模型（Juggernaut-XL 写实、animagine-XL 二次元、Pony V6 特定画风）
- SDXL-Turbo 蒸馏版出图快一倍
- 12GB 显存舒适运行，LoRA 生态全行业最大，想要什么风格都有现成的

SVD（Stable Video Diffusion）是它的图生视频模型，但质量已被 Wan/LTX 超越，不推荐新用。

## 争议 / 讨论

Stability 是 AIGC 圈最戏剧性的公司：开创者、开源功臣，却因管理混乱和财务危机几度濒死，核心团队出走成竞对。社区对它的评价是「起了大早，赶了晚集」——理念伟大，执行崩坏。它也是版权诉讼的靶心（艺术家集体诉讼训练数据侵权）。

## 参见

- [Black Forest Labs](Black Forest Labs.md)
- [Stable Diffusion](../模型家族/Stable Diffusion.md)
- [SDXL](../模型家族/SDXL.md)
- [LoRA](微调/LoRA.md)
