---
term: Stable Diffusion
full_name: Stable Diffusion
aliases: [SD, SDXL, Stable Diffusion XL]
category: 模型
dimension: 模型家族
granularity: 家族
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://huggingface.co/stabilityai
  - https://stability.ai/
relations:
  - target: Stability AI
    note: SD 是 Stability 的开源图像家族
  - target: FLUX
    note: FLUX 是 SD 的画质继任者
  - target: LoRA
    note: SDXL 的 LoRA 生态全行业最大
  - target: 潜空间
    note: SD 的潜空间扩散是其核心创新
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Stable Diffusion（SD）是 Stability AI 的开源图像生成模型家族，**2022 年把文生图从云端 API 带到每个人显卡上的那个模型**。它引爆了整个 AIGC 时代，开创了「开源基座 + 社区微调」的生态模式。你 ComfyUI 里的 SDXL 就是它的继任者，目前仍是社区生态最繁荣的图像模型。

## 原理

SD 的技术核心是**潜空间扩散**（Latent Diffusion）：不直接在像素上做扩散（太贵），而是先用 VAE 把图像压缩到小几十倍的潜空间，在潜空间里加噪去噪，最后解码回像素。这让消费级显卡跑文生图成为可能。架构上经典版本用 UNet 做去噪网络，SD3 之后转向 DiT。家族主线：SD 1.5（奠基）→ SDXL（生态巅峰）→ SD 3.x（转向 DiT）。

## 由来与历史

2022 年 8 月 SD v1 发布，开源模型首次做到消费级显卡跑文生图，引爆 AIGC 时代。2023 年 SDXL 发布，至今仍是社区生态最繁荣的图像模型——CivitAI 上几十万 LoRA 和画风模型都基于它。此后 Stability 内部动荡（核心团队出走创立 BFL），SD 3.x 画质被 FLUX 反超，开源图像王座易主，但 SDXL 的生态存量依然巨大。

## 应用

在 ComfyUI 里，**SDXL 是你的图类主力**（12GB 显存舒适运行）：
- 基座模型 + 社区画风模型：Juggernaut-XL（写实人像）、animagine-XL（二次元）、Pony V6（特定画风）、RealVisXL
- SDXL-Turbo 蒸馏版：出图快一倍
- LoRA 生态全行业最大：想要任何风格、角色、物体都有现成补丁
- 配套：CLIP 文本编码器 + SDXL VAE

## 争议 / 讨论

SD 的训练数据（LAION 爬取）引发大规模版权诉讼，是生成式 AI 版权问题的标志性案例。另外 SD 生态「模型碎片化」严重——几十万个社区模型质量参差，新手容易迷失。技术上 SDXL 已落后于 FLUX，但生态惯性让它短期内仍是主力。

## 参见

- [Stability AI](../模型厂商/Stability AI.md)
- [FLUX](FLUX.md)
- [LoRA](../微调/LoRA.md)
- [潜空间](../../02-组件/潜空间.md)
