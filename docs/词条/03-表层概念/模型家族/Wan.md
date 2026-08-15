---
term: Wan
full_name: Wan 视频模型
aliases: [Wan2.1, Wan2.2, 通义万相, Wan-AI]
category: 模型
dimension: 模型家族
granularity: 家族
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://huggingface.co/Wan-AI
  - https://tongyi.aliyun.com/wanxiang
relations:
  - target: 阿里
    note: Wan 是阿里通义万相的视频模型
  - target: MiniMax H3
    note: Wan 是 H3 在开源视频领域的主要竞品
  - target: LTX
    note: Wan 质量优先，LTX 效率优先
  - target: 扩散模型
    note: Wan 用 DiT 架构做潜空间扩散
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Wan（通义万相）是阿里的视频生成模型家族，覆盖文生视频、图生视频、视频编辑等能力，是开源视频模型的第一梯队选手。家族从 Wan2.1 迭代到 Wan2.2，提供从 1.3B 轻量版到 14B 旗舰版的完整梯度——**从小显卡到专业卡都有对应版本**，这是它最大的生态优势。

## 原理

Wan 用 DiT（Diffusion Transformer）架构做潜空间扩散，质量与效率平衡得好。家族的关键特性是「版本梯度」：1.3B（轻量，480p 快速预览）、5B（质量与资源平衡）、14B（旗舰，质量最佳，分 T2V 文生视频和 I2V 图生视频）。Wan2.2 的 TI2V 5B 支持图文混合输入。官方提供 ComfyUI 完整适配和蒸馏 LoRA。

## 由来与历史

阿里通义万相团队 2024 年开源 Wan 系列，Wan2.1 让国产视频模型进入第一梯队；2025 年 Wan2.2 发布，在运动质量和一致性上进一步提升。Wan 的策略是「全梯度覆盖 + 官方生态适配」，让任何显卡的用户都能找到合适版本——这让它成为开源视频社区用户量最大的家族之一。

## 应用

在 ComfyUI 里，Wan 的选型看你的显存（12GB）：
- **Wan2.1 T2V 1.3B**：轻量可靠，480p 短视频主力，你的日常选择
- **Wan2.2 TI2V 5B**：质量高一档，bf16 ≈10GB 有点悬，配 GGUF 稳跑；文生+图生都能干
- **Wan2.1 I2V 14B 480P**：图生视频质量好，GGUF Q4 ≈8GB 能跑就是慢
- Wan2.2 T2V A14B：激活 14B，bf16 28GB+，你放不下（16GB 档 GGUF 勉强）

## 争议 / 讨论

Wan 早期版本许可证有商用限制，社区有微词；迭代过快（1.1→2.2 不到一年）导致老版本快速过气，下载时要认准最新版。另外 14B 版本实际显存需求虚高，社区常用 GGUF 量化降门槛。

## 参见

- [阿里](../模型厂商/阿里.md)
- [MiniMax H3](MiniMax H3.md)
- [扩散模型](../../01-底层原理/扩散模型.md)
- [GGUF](../量化格式/GGUF.md)
