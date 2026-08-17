---
term: ControlNet
full_name: ControlNet
aliases: [控制网, 条件控制网络]
category: 多模态
dimension: 条件注入技术
granularity: 具体技术
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/2302.05543
  - https://github.com/lllyasviel/ControlNet
relations:
  - type: applies_to
    target: 扩散模型
    note: ControlNet 给文生图扩散模型加精确的结构控制
  - type: contrast
    target: IP-Adapter
    note: 两者都是条件注入，ControlNet 管结构、IP-Adapter 管语义
  - type: applies_to
    target: 潜空间
    note: ControlNet 把控制图编码成与图像同尺寸的潜空间条件
  - type: applies_to
    target: ComfyUI
    note: ComfyUI 里 ControlNetLoader + 应用节点是标准用法
created: 2026-08-17
updated: 2026-08-17
revisions: 1
---

## 定义

ControlNet 是 2023 年提出的一种给文生图模型「加精确控制」的神经网络结构。一句话说清：普通提示词只能说「画一个站在街上的女孩」，ControlNet 让你额外塞一张线稿、一张姿态骨架或一张深度图，模型就会严格按这张图的结构去生成——「画什么」由提示词决定，「长什么样、什么姿势」由你的控制图决定。

## 原理

ControlNet 的核心技巧是「锁定原模型、外挂一个可训练副本」：它把预训练扩散模型（通常是[扩散模型](../../01-底层原理/扩散模型.md)的 UNet）复制一份，用「零卷积」连接，只在训练时让这份副本学习「从控制图到生成结果」的映射，原模型权重几乎不动、推理时叠加生效。控制图（边缘、姿态、深度、分割等）先被编码成和图像[潜空间](../../02-组件/潜空间.md)同样尺寸的张量，作为额外的条件注入去噪过程。这样既能精确控制构图，又不破坏底模原有的画质与泛化能力。

## 由来与历史

ControlNet 由 Lvmin Zhang 等人在 2023 年论文《Adding Conditional Control to Text-to-Image Diffusion Models》（arXiv:2302.05543）中提出，很快成为 Stable Diffusion 生态里最重要的控制手段之一。它解决的正是纯提示词「说不清空间布局」的痛点——从漫画描线、产品图换背景到角色固定姿态，社区发展出十几类预处理器（OpenPose、Canny、Depth、Scribble 等），并通过 [ComfyUI](../../03-表层概念/工具/ComfyUI.md) 的节点化工作流普及到普通用户。

## 应用

在 ComfyUI 里标准用法是：**ControlNetLoader** 加载控制模型 → 用对应预处理器节点把输入图转成控制条件 → 通过 **Apply ControlNet** 节点接到正/负采样条件上，再进 KSampler。可以并联多个 ControlNet（一个管姿态、一个管边缘）叠加控制。注意控制模型必须匹配底模架构（SD1.5 / SDXL / FLUX 各自有不同的 ControlNet），接错会直接失效或报错。

## 参见

- [扩散模型](../../01-底层原理/扩散模型.md)
- [潜空间](../../02-组件/潜空间.md)
- [IP-Adapter](../加速/IP-Adapter.md)
- [ComfyUI](../工具/ComfyUI.md)
