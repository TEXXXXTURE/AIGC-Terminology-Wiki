---
term: MiniMax H3
full_name: MiniMax H3
aliases: [H3, minimax-h3]
category: 模型
dimension: 模型家族
granularity: 具体模型
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://huggingface.co/MiniMaxAI/MiniMax-H3
  - https://huggingface.co/Comfy-Org/MiniMax-H3
relations:
  - target: MiniMax
    note: H3 是 MiniMax 的视频生成旗舰
  - target: Wan
    note: Wan 是 H3 在开源视频领域的主要竞品
  - target: LTX
    note: LTX 主打效率，H3 主打质量
  - target: 蒸馏与Turbo
    note: 有 H3-Turbo LoRA 加速方案
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

MiniMax H3 是 MiniMax 公司 2025 年开源的视频生成大模型，最大特点是**视频+音频联合生成**——给它一句话或一张图，直接产出带声音的视频（人声、音乐、音效一步到位），而不是先出画面再单独配音。它在开源视频模型里是质量第一梯队，动态效果（物体运动、物理合理性）尤其突出。

## 原理

H3 是扩散模型家族的成员，核心创新在于「音画同源」：训练时让视频和音频共享同一个潜空间表征，生成阶段一起规划画面和声音的时序，保证音画同步。架构上它用超大 DiT 主干 + 32B 文本编码器（Qwen3-VL-32B）理解提示词，配合视频 VAE + 音频 VAE 双解码器。参数量大（主模型 ~30B 级），这也是它质量高的原因。

## 由来与历史

MiniMax 在 2025 年发布 H3，一举奠定国产开源视频模型的高端地位。它的出现让「开源视频模型」从「能动就行」提升到「能商用」水平。H3 发布后 Comfy-Org 官方做了完整适配（含量化变体、GGUF 社区版、Turbo LoRA），生态迅速成熟。它支持三种生成模式：文生视频（T2V）、图生视频（I2V）、参考视频引导（R2V）。

## 应用

在 ComfyUI 里，H3 的完整阵容是「主模型 + 32B 编码器 + 视频 VAE + 音频 VAE」四件套：
- **显存**：bf16 全套约 85GB 文件，12GB 显卡靠 UniBlockSwap 换显存能跑但慢；更推荐社区 GGUF 量化版（Q4_K_M ≈20GB 主模型）
- **⚠️ RDNA2 注意**：官方 int8_convrot 量化版在你的 RX 6750 XT 上必崩（无 WMMA），只能选 bf16/fp16 原版或 GGUF
- 加速：挂 H3-Turbo LoRA 可显著减少步数

## 争议 / 讨论

H3 的社区许可证商用有附加条款，不是纯开源；32B 编码器体积被吐槽「比主模型还占地方」。另外它对显存的苛刻要求让低配用户望而却步，社区普遍期待更轻量的版本。

## 参见

- [MiniMax](../模型厂商/MiniMax.md)
- [Wan](Wan.md)
- [扩散模型](../../01-底层原理/扩散模型.md)
- [GGUF](../量化格式/GGUF.md)
