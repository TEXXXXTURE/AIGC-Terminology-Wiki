---
term: ComfyUI
full_name: ComfyUI
aliases: [节点式工作流, ComfyUI 工作流]
category: 工具
dimension: 本地工具
granularity: 工具
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://github.com/comfyanonymous/ComfyUI
  - https://docs.comfy.org/
  - https://github.com/Comfy-Org/ComfyUI
  - https://huggingface.co/learn/diffusion-course
relations:
  - type: applies_to
    target: 扩散模型
    note: ComfyUI 最核心的用途就是把扩散模型拆成节点图来跑
  - type: applies_to
    target: 采样器
    note: KSampler 等节点直接对应采样器/调度器参数
  - type: applies_to
    target: LoRA
    note: 通过 LoraLoader 节点加载 LoRA 并控制强度
  - type: applies_to
    target: GGUF
    note: 通过 GGUF 插件加载量化模型，降低显存门槛
  - type: applies_to
    target: PyTorch
    note: ComfyUI 底层依赖 PyTorch 执行所有模型计算
  - type: applies_to
    target: Wan
    note: 新一代开源视频模型大多有 ComfyUI 官方/社区工作流
  - type: applies_to
    target: MiniMax H3
    note: H3 的 Comfy-Org 官方适配就是 ComfyUI 节点生态的一部分
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

ComfyUI 是一款开源、节点式（Node-based）的 AIGC 工作流工具，主要用来跑 Stable Diffusion、FLUX、Wan、MiniMax H3 等图像/视频/音频生成模型。它把“模型加载、提示词编码、潜空间采样、VAE 解码、图像保存”等步骤拆成一个个小节点，用连线把数据流串起来。相比一键式 WebUI，ComfyUI 更透明、更灵活，也因此成为社区研究新模型和新工作流的事实标准。









## 原理

ComfyUI 的核心是一个“节点图”：每个节点是一个功能块，输入经过处理后产生输出，再通过连线传给下一个节点。整个图既描述了数据流，也决定了执行顺序。以文生图为例，一条最简链路是：

`Load Checkpoint → CLIP Text Encode → Empty Latent Image → KSampler → VAEDecode → Save Image`

这里的 Checkpoint 是底模，CLIP 负责把提示词转成条件向量，Empty Latent Image 生成空白潜空间，KSampler 在潜空间里迭代去噪，VAEDecode 把潜空间变回像素图。因为中间状态是 Latent（潜空间），所以可以在不损失太多信息的情况下做重绘、放大、局部修改。

ComfyUI 能成为“学习入口”，正是因为它把模型生成中的各种参数和配置都暴露成了可见的节点：`steps`、`cfg`、`sampler_name`、`scheduler`、`denoise`、`seed` 等。用户不再面对黑盒，而是能直接看到每一步发生了什么。

## 由来与历史

ComfyUI 由开发者 comfyanonymous 在 2022 年 Stable Diffusion 开源后推出，最初是为了给 SD 提供一种更可控、更适合批量/复杂工作流的界面。随着 ControlNet、LoRA、视频生成等生态爆发，ComfyUI 逐渐从“极客工具”变成社区主流：Comfy-Org 作为官方组织持续维护，并为 Wan、MiniMax H3、LTX 等新模型提供官方节点适配。今天它已经不只是画图工具，而是整个开源 AIGC 生态的“工作流操作系统”。

## 应用

ComfyUI 的典型使用方式：

- **文生图 / 图生图 / 局部重绘**：通过不同的节点组合实现。
- **LoRA / 风格模型**：用 LoraLoader 节点加载并调节强度。
- **ControlNet / IP-Adapter**：给生成过程加结构控制或参考图条件。
- **文生视频 / 图生视频**：Wan、LTX、MiniMax H3 等都有对应工作流。
- **音画联合生成**：H3 的 FL2VA 主模型 + 视频 VAE + 音频 VAE 可以在 ComfyUI 里一次生成带声音的视频。
- **低显存方案**：通过 GGUF、fp8、pruned 模型、UniBlockSwap 等节点/设置降低显存需求。

常用目录：`models/checkpoints`、`models/diffusion_models`、`models/text_encoders`、`models/vae`、`models/loras`、`models/controlnet`、`custom_nodes/`。安装自定义节点通常用 ComfyUI-Manager。

## 争议 / 讨论

- **学习曲线陡**：节点图对新手不友好，但社区普遍认为“学会节点图才算真正理解生成流程”。
- **WebUI vs ComfyUI**：WebUI 上手快、适合简单出图；ComfyUI 灵活、可复现、适合研究和复杂工作流。两者不是替代关系。
- **自定义节点依赖地狱**：装太多插件容易冲突、报错，需要管理 Python 包和版本。
- **硬件兼容性**：AMD RDNA2 等老架构缺少 WMMA，跑 int8_convrot 量化可能崩溃，需要用 bf16/fp16 或 GGUF。

## 参见

- [扩散模型](../../01-底层原理/扩散模型.md)
- [采样器](../../02-组件/采样器.md)
- [LoRA](../微调/LoRA.md)
- [GGUF](../量化格式/GGUF.md)
- [PyTorch](../../06-IT行业/框架与库/PyTorch.md)
- [Wan](../模型家族/Wan.md)
- [MiniMax H3](../模型家族/MiniMax H3.md)

