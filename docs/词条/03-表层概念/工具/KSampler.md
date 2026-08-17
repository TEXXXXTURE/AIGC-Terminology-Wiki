---
term: KSampler
full_name: KSampler
aliases: [采样节点, KSampler 节点]
category: 工具
dimension: ComfyUI 节点
granularity: 节点
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://comfyui-wiki.com/zh/comfyui-nodes/sampling/k-sampler
  - https://github.com/comfyanonymous/ComfyUI
  - https://docs.comfy.org/
relations:
  - type: part_of
    target: ComfyUI
    note: KSampler 是 ComfyUI 最常用的采样节点
  - type: applies_to
    target: 采样器
    note: 节点的 sampler_name 参数对应具体的采样算法
  - type: applies_to
    target: 扩散模型
    note: KSampler 负责在潜空间里执行扩散模型的去噪采样
  - type: applies_to
    target: LoRA
    note: LoRA 加载后通常通过 KSampler 与底模一起参与采样
  - type: applies_to
    target: GGUF
    note: GGUF 低显存方案也通过 KSampler 完成生成
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

KSampler 是 ComfyUI 中最核心的采样节点：它接收模型、提示词条件、潜空间图像和一组采样参数，在潜空间里执行扩散模型的去噪过程，最终输出新的潜空间图像。几乎所有 ComfyUI 工作流（文生图、图生图、视频生成）都会经过它。

## 原理

KSampler 的工作流程可以概括为：先根据 `seed` 和 `denoise` 给原始潜空间加入噪声，然后由 `model` 结合 `positive`（正向条件）和 `negative`（负向条件）逐步去噪，经过 `steps` 步后得到结果。其中：

- `seed` 控制随机噪声，固定 seed 可复现结果。
- `steps` 控制去噪步数，步数越多通常越精细。
- `cfg` 控制生成结果与提示词的贴合程度，太高容易过曝/失真。
- `sampler_name` 选择具体采样算法（euler、dpmpp_2m 等）。
- `scheduler` 选择噪声去除策略（normal、karras、simple 等）。
- `denoise` 控制重绘强度：`1.0` 表示完全重绘，`0.x` 表示在输入图上做轻度修改。

## 由来与历史

KSampler 是 ComfyUI 早期就存在的核心节点，随着 Stable Diffusion 生态一起普及。它的设计把“采样器”和“调度器”显式拆开，让用户能精细控制生成过程。后来 ComfyUI 又增加了 KSampler (Advanced)、SamplerCustom 等高级节点，但 KSampler 仍是默认最常用、最适合入门的一个。

## 应用

在 ComfyUI 里，一条最简文生图链路通常是：

`Load Checkpoint → CLIP Text Encode → Empty Latent Image → KSampler → VAEDecode → Save Image`

常见参数组合：

- SD1.5：`steps=20-30`，`cfg=7`，`euler/dpmpp_2m + normal/karras`
- SDXL：`steps=20-30`，`cfg=5-8`
- FLUX：`steps=4/8/20`，`cfg=1` 或不需要
- Z-Image-Turbo：`steps=4`，`cfg=1`，`euler + simple`
- H3-Turbo LoRA：低步数 + 低 CFG

## 争议 / 讨论

- **steps 不是越多越好**：超过模型建议步数后收益递减，甚至可能引入伪影。
- **cfg 过高会“烧图”**：细节过锐、颜色过饱和，社区普遍建议从 6-8 开始调。
- **sampler/scheduler 组合很多**：不同模型有不同“标准答案”，需要看模型卡或社区工作流。

## 参见

- [ComfyUI](ComfyUI.md)
- [采样器](../../02-组件/采样器.md)
- [扩散模型](../../01-底层原理/扩散模型.md)
- [LoRA](../微调/LoRA.md)
- [GGUF](../量化格式/GGUF.md)
