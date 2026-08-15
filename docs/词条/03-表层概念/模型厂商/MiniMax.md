---
term: MiniMax
full_name: MiniMax
aliases: [稀宇科技, MiniMax 稀宇科技]
category: 平台
dimension: 模型厂商
granularity: 厂商
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://www.minimaxi.com/
  - https://huggingface.co/MiniMaxAI
relations:
  - target: 阿里
    note: 同为中国大厂，都有视频模型（H3 vs Wan）
  - target: Black Forest Labs
    note: 同为厂商，BFL 主攻图像、MiniMax 主攻视频
  - target: Stability AI
    note: 同为生成模型厂商，路线不同
  - target: MiniMax H3
    note: H3 是 MiniMax 的视频生成模型
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

MiniMax（稀宇科技）是中国的一家 AI 公司，2021 年成立于上海，主打多模态大模型。它在 AIGC 圈里最出名的身份是 **MiniMax H3 视频模型**的出品方——H3 是 2025 年开源的最强视频生成模型之一，能直接生成带声音的视频。公司旗下还有自己的对话产品「海螺 AI」（Hailuo）。

## 原理

MiniMax 的技术路线是「多模态大一统」：用统一的架构同时处理文字、图像、视频、音频。H3 是这个思路的集大成者——它不是单纯的文生视频，而是「视频+音频联合生成」：你给一句话或一张图，它直接产出带画面、带人声、带背景音的视频，生成阶段就把声音和画面一起规划，而不是后期拼接。这也是它和阿里 Wan、BFL 视频路线的核心区别。

## 由来与历史

MiniMax 成立于 2021 年，创始人闫俊杰出身商汤科技，公司早期专注对话模型（海螺 AI 的前身）。2023-2024 年它在中文大模型市场站稳脚跟，随后把重心转向多模态。2025 年开源 H3 是它的标志性动作：H3 以视频+音频联合生成能力震惊社区，成为开源视频模型的 Top 选择，ComfyUI 官方很快做了适配，用户在自己显卡上就能跑。

## 应用

在 ComfyUI 里，MiniMax H3 是视频生成的高端选择：加载 H3 主模型 + 32B 文本编码器 + 视频/音频双 VAE，就能文生视频（T2V）、图生视频（I2V）、参考视频引导（R2V）。它的动态效果（物体运动、物理合理性）在开源模型里是第一梯队，但显存门槛高——你的 RX 6750 XT（12GB）需要 bf16 原版配 UniBlockSwap 换显存，或直接用社区 GGUF 量化版。有 H3-Turbo LoRA 可以显著提速。

## 争议 / 讨论

H3 的许可证是「社区许可证」（Community License Agreement），商用有附加条款，不是纯 MIT——社区对开源程度的质疑一直存在。另外 32B 的文本编码器体积巨大（bf16 版 48GB），被戏称为「买显卡送编码器」。

## 参见

- [阿里](阿里.md)
- [Black Forest Labs](Black Forest Labs.md)
- [MiniMax H3](../模型家族/MiniMax H3.md)
- [GGUF](量化格式/GGUF.md)
