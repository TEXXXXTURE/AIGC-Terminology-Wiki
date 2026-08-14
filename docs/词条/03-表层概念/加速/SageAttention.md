---
term: SageAttention
full_name: SageAttention (Quantized Attention Acceleration)
aliases: [Sage注意力, sage_attn]
category: 推理
dimension: 加速技术
granularity: 具体技术
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/2411.10958
  - https://github.com/thu-ml/SageAttention
  - https://github.com/Comfy-Org/ComfyUI/issues/14735
relations:
  - type: part_of
    target: 量化
    note: SageAttention 用 int8 量化近似注意力计算
  - target: 浮点数与精度
    note: 其精度取舍依赖对低比特浮点/整数表示的理解
  - type: applies_to
    target: UNet
    note: 加速对象是扩散骨干网络（UNet/DiT）里的注意力层
  - target: 采样器
    note: 注意力加速直接缩短每一步采样耗时
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

SageAttention 是清华大学 thu-ml 团队开源的注意力加速技术，一句话说清：把注意力计算里的矩阵乘换成 int8 量化版本来算，速度比广泛使用的 FlashAttention 还快约 2~5 倍，而出图画质几乎看不出差别。在 ComfyUI 里它以 PatchSageAttentionKJ 节点（KJNodes 插件包）的形式存在。

## 原理

扩散模型每一步去噪，骨干网络里的注意力层都是耗时大头。SageAttention 的做法是把注意力中的两次矩阵乘（QK^T 和 PV）量化到 int8 来执行，并配合对 Q、K 做平滑预处理来压住量化误差——int8 的吞吐远高于 fp16，于是整体提速。量化背景见[量化](../../01-底层原理/量化.md)，注意力层所在的位置见[UNet](../../02-组件/UNet.md)。

## 由来与历史

2024 年 11 月，thu-ml 团队发布 SageAttention 论文（arXiv:2411.10958）并开源代码，很快成为视频/图像扩散模型加速的标配之一；随后推出的 SageAttention2 进一步把精度下探到 int4/int8 混合。ComfyUI 社区迅速跟进，KJNodes 插件提供了一键 patch 节点，ComfyUI 官方仓库的相关加速讨论（如 issue #14735）也热度不低。

## 应用

ComfyUI 用法：安装 KJNodes 插件和 sageattention 的 Python 包后，在工作流里把 **PatchSageAttentionKJ** 节点接在模型加载器之后、采样器之前即可，不需要改其他参数。视频生成（Wan 等长序列模型）收益最大，图像生成也能省下一截时间。

**RDNA2（RX 6000 系）必须禁用此节点**：SageAttention 的 int8 内核依赖 WMMA 类矩阵加速指令，RDNA2 没有这套指令集，patch 之后不是变慢而是直接崩溃——和原生 int8/fp8 模型是同一种硬件代际限制（见 [int8与fp8量化](../量化格式/int8与fp8量化.md)）。NVIDIA 显卡与 RDNA3（RX 7000 系）以上可正常使用。装完插件出图报错时，第一嫌疑人就是它。

## 参见

- [量化](../../01-底层原理/量化.md)
- [浮点数与精度](../../01-底层原理/浮点数与精度.md)
- [UNet](../../02-组件/UNet.md)
- [int8与fp8量化](../量化格式/int8与fp8量化.md)
