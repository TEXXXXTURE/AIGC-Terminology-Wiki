---
term: int8与fp8量化
full_name: 8-bit Integer / Floating Point Quantization
aliases: [int8, fp8, 8位量化, E4M3, E5M2]
category: 推理
dimension: 量化格式
granularity: 格式
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/2209.05433
  - https://github.com/ROCm/ROCm/issues/1714
  - https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/14031
relations:
  - type: part_of
    target: 量化
    note: int8/fp8 是把权重与计算压到 8bit 的量化实现
  - type: part_of
    target: 浮点数与精度
    note: fp8 是 8 位浮点格式（E4M3/E5M2），int8 是 8 位整数
  - type: contrast
    target: bf16
    note: 对比非量化的 16 位原版精度，省一半显存
  - target: GGUF
    note: GGUF 存储量化但计算时反量化，与原生 int8 计算路线本质不同
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

int8 和 fp8 是把模型权重（甚至计算过程）从 16 位压缩到 8 位的两套量化方案，一句话说清：显存占用直接减半，代价是精度损失。区别在于用什么装这 8 个比特——int8 用整数，fp8 用微型浮点（E4M3/E5M2 两种规格）。下载模型时文件名里的 `int8`、`fp8`、`fp8_e4m3fn` 指的就是它们。

## 原理

量化的基本思想是把高精度数值映射到低比特表示：int8 把浮点数按比例缩放成 -128~127 的整数，fp8 则用 8 位拼出一个迷你浮点格式（指数位+尾数位的缩水版），保留了浮点的动态范围，对大模型的激活值更友好。省显存、提速度，代价是每个数值都变「糙」了。详见[量化](../../01-底层原理/量化.md)与[浮点数与精度](../../01-底层原理/浮点数与精度.md)。

## 由来与历史

int8 量化源自移动端推理时代——手机芯片只有整数算力，逼出了「训练后量化」一整套方法。大模型时代，8bit 推理由 bitsandbytes 等库普及开来。

fp8 则是 2022 年由 NVIDIA、Arm、Intel 联合提出的新标准（论文 arXiv:2209.05433），定义了 E4M3（4 位指数+3 位尾数，推理主力）和 E5M2 两种格式。NVIDIA 从 Hopper（H100）开始原生支持，AMD 到 RDNA3 才加入对应的 WMMA 指令集。WebUI 社区也跟进实现了 fp8 存储类型以节省显存（A1111 PR #14031）。

## 应用

在 ComfyUI 里，fp8 最常见的用法是「混合精度」文件：Z-Image 工作流的文本编码器 `qwen_3_4b_fp8_mixed.safetensors` 就是 fp8 版本，显存紧张时换它对画质影响很小（文本编码对精度不如 VAE 敏感）。部分大模型（FLUX、H3）也有社区 fp8 版 checkpoint，显存直接减半。

**RDNA2（RX 6000 系）警告**：RDNA2 没有 WMMA（矩阵乘加速）指令集，原生 int8/fp8 计算内核在你的卡上必崩——这是硬件代际限制，装什么驱动都没用，ROCm 官方支持列表里也没有它（见 ROCm issue #1714）。替代方案是用 [GGUF](GGUF.md)：它存储时是量化的，但计算前反量化回 fp16，所以 RDNA2 能跑。NVIDIA 显卡和 RDNA3（RX 7000 系）以上则可正常使用 int8/fp8。

## 争议 / 讨论

社区对 8bit 量化的画质损伤程度一直有分歧：一方认为 fp8 几乎无损、是显存紧张时的免费午餐；另一方（尤其是 llama.cpp 社区）持续讨论量化引入的误差，并探索激活值旋转等技巧来压低损失（llama.cpp PR #21038）。实际建议是：文本编码器放心用 fp8，VAE 和主模型能不用就不用。

## 参见

- [量化](../../01-底层原理/量化.md)
- [浮点数与精度](../../01-底层原理/浮点数与精度.md)
- [bf16](bf16.md)
- [GGUF](GGUF.md)
- [safetensors](safetensors.md)
