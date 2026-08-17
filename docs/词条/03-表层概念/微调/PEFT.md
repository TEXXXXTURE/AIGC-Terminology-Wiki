---
term: PEFT
full_name: Parameter-Efficient Fine-Tuning
aliases: [参数高效微调]
category: 模型微调
dimension: 微调技术
granularity: 概念
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/2303.15647
  - https://huggingface.co/docs/peft
relations:
  - type: part_of
    target: 训练与微调
    note: PEFT 是微调的一个大类，与全量微调相对
  - type: peer
    target: 全量微调
    note: PEFT 与全量微调是微调的两条路线
  - type: part_of
    target: LoRA
    note: LoRA 是 PEFT 家族里最常用的方法
created: 2026-08-17
updated: 2026-08-17
revisions: 1
---

## 定义

PEFT（Parameter-Efficient Fine-Tuning，参数高效微调）是一类「只训练模型中极少数参数、冻结绝大部分」的微调方法的统称。一句话说清：与其把几十亿参数全改一遍（[全量微调](全量微调.md)），不如只动其中一小撮——既省显存、又防遗忘、产物还小到能随手分享。LoRA 就是 PEFT 里最出圈的代表。

## 原理

大模型微调的痛点在于：全量更新所有参数又贵又容易「灾难性遗忘」（把预训练学到的通用能力冲掉）。PEFT 的思路是「四两拨千斤」——冻结底座，只在特定位置插入或调整极少量参数。家族里的方法各有招式：[LoRA](LoRA.md) 在低秩矩阵里学变化量、Adapter 在层间插小模块、Prompt Tuning 只调输入软提示、Prefix Tuning 调注意力前缀。它们共享一个判断：大模型适配新任务时，真正需要的「改动量」其实很小。原理细节见[训练与微调](../../01-底层原理/训练与微调.md)。

## 由来与历史

PEFT 作为一个研究方向的命名在 2019 年 Adapter 之后逐渐成形，2021 年 LoRA 把「低秩」这招做到极简好用，2023 年 Lialin 等人的综述《Scaling Down to Scale Up》（arXiv:2303.15647）把它系统化为一门「参数高效微调大观」。同年 Hugging Face 推出 PEFT 库，把 LoRA、AdaLoRA、IA³ 等方法统一成一套 API，让它从论文走进每个普通开发者的工作流。

## 应用

对使用者来说，PEFT 是「低成本定制模型」的代名词：用消费级显卡就能训出几十 MB 的适配补丁，还能一个底模挂多个 PEFT 权重按需切换。在图像社区它对应 LoRA 文件（见[风格模型](风格模型.md)）；在 NLP 里它对应 Hugging Face PEFT 的 LoRA / QLoRA。代价是：对「需要学全新概念」的重任务，PEFT 的表达力上限仍不如[全量微调](全量微调.md)。

## 参见

- [训练与微调](../../01-底层原理/训练与微调.md)
- [LoRA](LoRA.md)
- [全量微调](全量微调.md)
- [蒸馏与Turbo](蒸馏与Turbo.md)
- [风格模型](风格模型.md)
