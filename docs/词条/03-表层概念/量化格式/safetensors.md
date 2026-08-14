---
term: safetensors
full_name: Safe Tensors
aliases: [安全张量格式]
category: 推理
dimension: 量化格式
granularity: 格式
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://github.com/huggingface/safetensors
  - https://huggingface.co/docs/safetensors/index
relations:
  - type: similar_to
    target: GGUF
    note: 同为模型容器格式，safetensors 主打安全通用，GGUF 主打量化推理
  - target: 量化
    note: safetensors 只是容器，内部可装 fp32/bf16/fp8 任意精度的权重
  - type: applies_to
    target: 神经网络
    note: safetensors 存的就是神经网络的权重张量
  - target: LoRA
    note: LoRA 补丁文件如今也几乎全是 safetensors 格式
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

safetensors 是 Hugging Face 推出的模型权重存储格式，一句话说清：一个只装数据、装不下代码的模型文件格式。它取代的是老的 `.ckpt`（Python pickle 格式）——pickle 文件加载时可以执行任意代码，下载到别人动过手脚的模型就等于在自己电脑上运行病毒，safetensors 从结构上杜绝了这件事。今天 ComfyUI 里的模型文件几乎全是它。

## 原理

safetensors 文件 = 一个 JSON 头（记录每个张量的名字、形状、数据类型）+ 原始张量字节流，仅此而已。没有反序列化逻辑，结构上不可能藏可执行代码；同时因为张量按原始字节连续存放，加载时可以零拷贝内存映射（mmap），大模型加载速度比 pickle 快好几倍。文件内部的精度（fp32/bf16/fp16/fp8）与格式本身无关——它只是个安全的「集装箱」。权重张量的本质见[神经网络](../../01-底层原理/神经网络.md)。

## 由来与历史

2022 年，Hugging Face 针对 pickle 反序列化漏洞（恶意模型文件可远程执行代码，且多次被真实利用）开发了 safetensors，并在 2023 年把它定为 Hub 上模型的默认格式。Stable Diffusion 社区早期流传大量 `.ckpt` 文件，随着 WebUI、ComfyUI 全面转向 safetensors，老格式基本退出主流，只在一部分上古 LoRA 和 embedding（`.pt`）里还能见到。

## 应用

在 ComfyUI 里你不需要做什么特别的事——`models/checkpoints/`、`models/loras/`、`models/vae/`、`models/clip/` 里的文件几乎清一色 `.safetensors`，所有加载节点默认支持。文件名里的精度标注（`bf16`、`fp8_e4m3fn`）描述的是内部张量的数据类型，和容器格式互不绑定。

安全建议仍然成立：遇到来源不明的 `.ckpt`、`.pt`、`.pth` 文件要格外警惕，优先找同一模型的 safetensors 版本；ComfyUI 和 A1111 都默认对 pickle 类文件做安全检查，但那只是缓解而非根治。

## 参见

- [GGUF](GGUF.md)
- [量化](../../01-底层原理/量化.md)
- [神经网络](../../01-底层原理/神经网络.md)
- [LoRA](../微调/LoRA.md)
