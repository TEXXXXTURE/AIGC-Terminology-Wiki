---
term: GGUF
full_name: GPT-Generated Unified Format
aliases: [gguf]
category: 推理
dimension: 量化格式
granularity: 格式
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://github.com/ggml-org/llama.cpp
  - https://github.com/ggml-org/llama.cpp/pull/1684
  - https://github.com/Comfy-Org/ComfyUI/pull/15224
relations:
  - type: part_of
    target: 量化
    note: GGUF 是量化模型的打包格式，内含多种量化级别
  - type: similar_to
    target: safetensors
    note: 同为模型容器格式，GGUF 主打量化推理，safetensors 主打安全通用
  - target: bf16
    note: GGUF 计算时反量化回 fp16/bf16 级别精度，而非原生低比特计算
  - type: applies_to
    target: 神经网络
    note: GGUF 装的是神经网络的量化权重张量
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

GGUF（GPT-Generated Unified Format）是 llama.cpp 生态的模型打包格式，一句话说清：一个文件装下量化后的模型权重 + 全部元数据 + 分词器，拷过去就能跑。文件名里的 `Q4_K_M`、`Q5_K_M`、`Q8_0` 等后缀是量化级别——数字越大越保真、体积也越大。它最早是本地跑大语言模型的标配，现在也被引入图像生成（ComfyUI-GGUF 插件）。

## 原理

GGUF 的精髓是「存储量化、计算反量化」：权重以 4~8 bit 的低比特形式存在文件里（所以体积小、省显存），但加载计算时会先反量化回 fp16/bf16 级别的精度再做矩阵乘。这一点和原生 int8 计算有本质区别——也是它能在老硬件上跑的根本原因。详见[量化](../../01-底层原理/量化.md)。

## 由来与历史

GGUF 的前身是 GGML，由 Georgi Gerganov 为 llama.cpp 项目设计，目标是让大模型在消费级 CPU/显卡上跑起来。2023 年 8 月，GGUF 正式取代 GGML，解决了旧格式无法向后兼容的问题（每次模型结构变动都要重转一遍权重）。同年引入的 k-quants（llama.cpp PR #1684）确立了 `Q4_K_M` 这类现代量化级别，成为社区事实标准。

此后 GGUF 从语言模型扩展到更多领域：llama.cpp 持续加入对新架构的支持（Qwen3 Next、DiffusionGemma 等 PR 动辄数百个赞），ComfyUI 社区则通过 ComfyUI-GGUF 插件把它引入图像生成——Z-Image、H3 等新模型发布后不久就有社区制作的 GGUF 版本（H3 的官方 ComfyUI 支持见 Comfy-Org PR #15224）。

## 应用

在 ComfyUI 里用 GGUF 需要装 **ComfyUI-GGUF 插件**，然后把 Load Checkpoint 换成插件提供的 **UnetLoaderGGUF** 节点，模型文件放 `models/unet/`（或 `models/diffusion_models/`）。注意 GGUF 只包含主模型，文本编码器和 VAE 仍需单独加载。

量化级别怎么选：`Q8_0` 几乎无损但只省一半体积；`Q4_K_M` 是体积/画质的平衡点，社区最常用；`Q3` 以下画质肉眼可见地糙，只建议实在放不下时尝试。Z-Image/H3 工作流显存不足时，把 bf16 原版换成 Q4_K_M 是最常见的解法。

**RDNA2 用户的救星**：因为 GGUF 计算时反量化回 fp16，它绕开了 RDNA2 无 WMMA 指令集、原生 int8/fp8 必崩的硬件限制（见 [int8与fp8量化](int8与fp8量化.md)）。RX 6000 系想跑大模型，GGUF 基本是唯一选项。

## 争议 / 讨论

r/LocalLLaMA 等社区常年争论「最低可用量化级别」：有人认为 Q4_K_M 就是无损，有人坚持 Q6 起步。图像模型这边经验更明确——Q4_K_M 对出图的影响多数人难以察觉，但涉及文字渲染和精细纹理时低比特版本会先露馅。

## 参见

- [量化](../../01-底层原理/量化.md)
- [bf16](bf16.md)
- [int8与fp8量化](int8与fp8量化.md)
- [safetensors](safetensors.md)
