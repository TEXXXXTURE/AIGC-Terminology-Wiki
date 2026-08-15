---
term: FLUX
full_name: FLUX.1 / FLUX.2
aliases: [FLUX.1, FLUX.2, FLUX 系列]
category: 模型
dimension: 模型家族
granularity: 家族
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://huggingface.co/black-forest-labs
  - https://blackforestlabs.ai/
relations:
  - target: Black Forest Labs
    note: FLUX 是 BFL 的旗舰模型家族
  - target: Stable Diffusion
    note: FLUX 是 SD 的画质替代者
  - target: Z-Image
    note: Z-Image 是 FLUX 在快速出图路线的对手
  - target: 蒸馏与Turbo
    note: schnell 是 FLUX 的蒸馏加速版
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

FLUX 是 Black Forest Labs 的旗舰图像生成模型家族，被公认为**当前开源文生图的画质天花板**。它用超大 DiT 架构 + 超强文本理解换来顶级画质、精准提示词跟随、可靠文字渲染，2024 年发布时直接以开源身份对标闭源 Midjourney。

## 原理

FLUX 基于扩散 Transformer（DiT）架构，不是传统 UNet——用 Transformer 做去噪网络，扩展性更好。它的画质优势来自三个叠加：超大参数量（FLUX.1 达 12B）、T5-XXL 文本编码器带来的顶级语义理解、精细的训练配方。家族分两条产品线：**dev**（完整版，画质最好）和 **schnell**（德语"快"，蒸馏加速版，4 步出图）。FLUX.2 又加了 klein 轻量分支（4B/9B）降低门槛。

## 由来与历史

2024 年 8 月，BFL 发布 FLUX.1 系列，直接成为开源图像新王：画质、文字渲染、人体结构全面超越 SDXL。2025 年 FLUX.2 发布，klein 分支让低显存用户也能体验。FLUX 的出现终结了 Stability 对开源图像的统治，社区工作流、LoRA 生态迅速转向 FLUX。它也是第一个让「开源模型画质超越闭源 Midjourney」成为共识的模型。

## 应用

在 ComfyUI 里，FLUX 的选型完全看显存：
- **FLUX.1 dev/schnell（12B）**：bf16 原版 24GB+，你的 12GB 卡放不下；量化版（int8/fp8/nvfp4）在 RDNA2 上必崩——基本无缘
- **FLUX.2-klein-4B**：轻量分支，bf16 ≈8GB，你 12GB 勉强能跑，是能摸到的最高画质，值得折腾
- 需要 T5-XXL 编码器 + CLIP，模型文件几十 GB

## 争议 / 讨论

FLUX 的「半开源」属性争议大：dev 版只开源权重、商用要付费；schnell 版才是真 Apache 2.0。社区批评 BFL「开源是营销，赚钱是目的」。另外 FLUX 参数量巨大，社区分化出「画质党」（坚持 FLUX）和「效率党」（转 Z-Image-Turbo 等快速模型）。

## 参见

- [Black Forest Labs](../模型厂商/Black Forest Labs.md)
- [Stable Diffusion](Stable Diffusion.md)
- [扩散模型](../../01-底层原理/扩散模型.md)
- [蒸馏与Turbo](../微调/蒸馏与Turbo.md)
