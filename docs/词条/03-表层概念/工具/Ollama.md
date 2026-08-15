---
term: Ollama
full_name: Ollama
aliases: [ollama run, ollama pull]
category: 工具
dimension: 本地工具
granularity: 工具
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://ollama.com/
  - https://github.com/ollama/ollama
relations:
  - target: llama.cpp
    note: Ollama 底层基于 llama.cpp
  - target: Llama
    note: Ollama 以跑 Llama 系列起家
  - target: GGUF
    note: Ollama 的模型都是 GGUF 格式
  - target: Qwen
    note: 也支持 Qwen 等中文模型
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Ollama 是本地跑大语言模型（LLM）的一键工具：装好之后，`ollama run llama3.1` 就能在你自己电脑上跑起一个聊天模型，像用 Docker 一样简单。它把「下载模型 → 准备环境 → 启动服务 → 对话」整个过程压缩成一条命令，是本地 LLM 部署的事实标准工具。

## 原理

Ollama 的底层是 **llama.cpp**（一个纯 C++ 的高效推理库），它负责把模型文件加载进显存/内存并高效计算。Ollama 在上面包了一层极简的工程壳：模型仓库管理（`ollama pull` 下载）、模型格式统一（全是 GGUF 量化格式）、API 服务（启动后暴露 OpenAI 兼容的 `/v1/chat/completions` 接口）、模型文件定制（Modelfile 可以自定义系统提示词/参数）。这层壳让「本地跑模型」从折腾变成一键。

## 由来与历史

Ollama 2023 年发布，正值 Llama 2 开源引爆本地 LLM 需求。它凭借「一键运行」的极致简单迅速成为社区标配——之前跑本地模型要自己编译 llama.cpp、下载权重、写推理脚本，Ollama 把这些全藏起来了。2024 年起支持 OpenAI 兼容 API，让本地模型能直接接入各种工具（LangChain、Open WebUI 等）。目前是本地 LLM 部署最流行的工具，有官方的 Windows/macOS/Linux 桌面应用。

## 应用

本地跑 LLM 的标准姿势：
- 安装后 `ollama pull qwen3:8b` 下载模型，`ollama run qwen3:8b` 开聊
- 12GB 显卡（你的 RX 6750 XT）能流畅跑 7-8B 模型（Q4 量化），14B 勉强（慢）
- 启动后本地 API：`http://localhost:11434/v1`，任何 OpenAI 兼容客户端都能接
- Modelfile 定制：改系统提示词、温度、上下文长度

## 争议 / 讨论

Ollama 的「开箱即用」背后是封装——它不支持所有模型（尤其新架构要等适配），高级推理参数（sampler 微调）暴露得少，硬核用户嫌它「不够自由」转用 llama.cpp 或 vLLM 直连。另外它是商业公司（非纯开源社区项目），虽然本体开源但生态逐步封闭的担忧存在。

## 参见

- [llama.cpp](llama.cpp.md)
- [GGUF](量化格式/GGUF.md)
- [Llama](../模型家族/Llama.md)
- [vLLM](vLLM.md)
