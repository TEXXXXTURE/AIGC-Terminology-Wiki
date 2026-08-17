---
term: GLM
full_name: GLM (General Language Model)
aliases: [ChatGLM, GLM-4, GLM-5]
category: 模型
dimension: 模型家族
granularity: 家族
maturity: stable
status: draft
contributors: [TEXXXXTURE]
sources:
  - https://huggingface.co/THUDM
  - https://github.com/THUDM/GLM-4
relations:
  - target: 智谱
    note: GLM 是智谱 AI 的模型家族
  - target: Qwen
    note: GLM 和 Qwen 是中文开源 LLM 的两大代表
  - target: Llama
    note: GLM 在中文领域的定位类似 Llama 在英文领域
created: 2026-08-17
updated: 2026-08-17
revisions: 1
---

## 定义

GLM(General Language Model)是智谱 AI 的大语言模型家族,清华大学技术背景。GLM 系列以中文能力见长,从 ChatGLM 开源爆火到 GLM-5.2 闭源旗舰,经历了从开源到闭源+部分开源的转变。最新 GLM-5.2 智能指数 52.64,开放度 44.44。

## 由来与历史

ChatGLM-6B(2023)是中文开源 LLM 的第一批爆款。GLM-4(2024)性能大幅提升,引入多模态。GLM-4.5/4.6(2025)迭代优化。GLM-5.2(2026)是当前旗舰,开放度 44.44 分(部分权重开源),输出速度 154.6 tok/s(同档位最快之一)。

## 应用

GLM-5.2 输出速度 154.6 tok/s、智能指数 52.64、输入 $1.40/M、输出 $4.40/M。在 50+ 分档位里速度最快、价格仅次于 DeepSeek。通过 zhipuai.cn 或 BigModel 平台调用。本地部署推荐 GGUF 量化版。

## AA 评测数据 (2026-08-17)

- 智能指数: 52.64
- 输出速度: 154.62 tok/s
- 输入价格: $1.4/M tokens
- 输出价格: $4.4/M tokens
- 上下文窗口: 1M
- 全知指数: 4.43
- 开放度: 44.44/100

## 参见

- [模型数据总览](../../04-LLM工程/模型数据总览.md)
- [模型评测](../../04-LLM工程/模型评测.md)
