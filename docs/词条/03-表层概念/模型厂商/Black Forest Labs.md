---
term: Black Forest Labs
full_name: Black Forest Labs
aliases: [BFL, 黑森林实验室]
category: 平台
dimension: 模型厂商
granularity: 厂商
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://blackforestlabs.ai/
  - https://huggingface.co/black-forest-labs
relations:
  - target: Stability AI
    note: BFL 创始团队出自 Stability，直接对标
  - target: MiniMax
    note: BFL 主攻图像，MiniMax 主攻视频
  - target: 阿里
    note: FLUX 是阿里 Z-Image/Wan 在画质上的对手
  - target: FLUX
    note: FLUX 是 BFL 的旗舰模型家族
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Black Forest Labs（黑森林实验室，简称 BFL）是德国的 AI 生成模型公司，2024 年成立于弗莱堡，创始团队来自 Stable Diffusion 的发明地——他们就是 Stability AI 早期核心成员出走后另立的门户。BFL 的招牌是 **FLUX 系列图像模型**，被视为当前开源文生图的画质天花板。

## 原理

BFL 的技术核心是「大模型暴力美学」：FLUX 系列不走轻量路线，而是用超大的 DiT（Diffusion Transformer）架构 + 超强的文本理解（T5-XXL 编码器），换来对提示词的精准跟随和顶级画质。FLUX.1 有 12B 参数，FLUX.2 更大，还细分了 dev（开发版）和 schnell（德语"快"，蒸馏加速版）两条产品线。它的理念是：与其优化小模型，不如把大模型做到极致。

## 由来与历史

2024 年 8 月，BFL 发布 FLUX.1 系列，直接以开源模型身份对标闭源的 Midjourney，凭借画面质量、文字渲染、人体结构三大优势迅速封神，成为社区「画质天花板」。2025 年迭代 FLUX.2，并推出 klein 轻量分支（4B/9B）让低显存用户也能用。BFL 同时为闭源巨头提供底层能力，是开源图像领域影响力最大的新势力。

## 应用

在 ComfyUI 里，FLUX 系列是「想要最好画质」的选择，但对显存极其苛刻：
- **FLUX.1 dev/schnell（12B）**：bf16 原版 24GB+，量化版在 RDNA2 上必崩（无 WMMA），你的 12GB 卡基本无解
- **FLUX.2-klein-4B**：轻量分支，bf16 ≈8GB，你 12GB 勉强能跑，是目前能摸到的最高画质
- 配套需要 T5-XXL 文本编码器 + CLIP，模型文件动辄几十 GB

## 争议 / 讨论

FLUX 的开源程度一直有争议：FLUX.1-dev 只开源权重不开源训练代码，商用要付费许可证；schnell 版才是真正 Apache 2.0。社区普遍认为 BFL 是「半开源」——看得见摸得着，但核心配方保密。

## 参见

- [Stability AI](Stability AI.md)
- [FLUX](../模型家族/FLUX.md)
- [GGUF](量化格式/GGUF.md)
- [bf16](量化格式/bf16.md)
