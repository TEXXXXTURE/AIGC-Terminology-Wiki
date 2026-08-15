---
term: DPO
full_name: Direct Preference Optimization
aliases: [直接偏好优化]
category: 对齐
dimension: 对齐技术
granularity: 具体技术
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/2305.18290
  - https://arxiv.org/abs/2203.02155
  - https://huggingface.co/blog/pref-tuning
relations:
  - type: contrast
    target: RLHF
    note: DPO 是 RLHF 的简化替代方案
  - type: applies_to
    target: 训练与微调
    note: DPO 是预训练之后的「训练后」对齐阶段
  - type: part_of
    target: 对齐
    note: 目标是让模型对齐人类偏好
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

DPO（Direct Preference Optimization，直接偏好优化）是一种「不用强化学习也能教模型做人」的对齐方法：传统 RLHF 要先训一个奖励模型、再跑复杂的强化学习，DPO 则直接用「同一个问题，回答 A 比回答 B 好」这样的偏好对数据，像做分类一样一步把模型调好。它把 RLHF 里最贵、最不稳的两步省掉了，效果却接近，因此迅速成为开源社区做对齐的主流选择。

## 原理

DPO 的巧妙在于一个数学发现：RLHF 想优化的目标（奖励最大化 + 不偏离原模型太远）存在一个闭式解，可以直接换算成「好回答的概率应该调高、差回答的概率应该调低」的简单损失函数。于是训练数据只需要偏好对（chosen / rejected），一次普通的梯度下降就完成对齐——它和 [RLHF](RLHF.md) 一样属于预训练之后的「训练后」阶段，见[训练与微调](../../01-底层原理/训练与微调.md)，这里不重复展开。

## 由来与历史

DPO 由斯坦福大学的 Rafailov 等人于 2023 年提出（arXiv:2305.18290），直接动机是 RLHF 的工程痛点：奖励模型可能被刷分（reward hacking）、PPO 训练出了名的难调、整套流水线又贵又慢。论文用数学推导证明奖励模型这一步理论上可以消掉。发布后开源社区几乎立刻拥抱：Zephyr、Llama 系列的部分版本、以及大量社区微调模型都用 DPO 或其变体做对齐。随后 DPO 家族不断扩展（KTO、ORPO、IPO 等），而 2024 年起 DeepSeek 的 GRPO 又让「轻量强化学习」路线回潮——今天的后训练通常是多种方法的组合。

## 应用

用 DPO 微调一个开源模型的典型流程：准备偏好对数据集（每条含 prompt、chosen 回答、rejected 回答），用 Hugging Face TRL 库的 `DPOTrainer` 训练，通常从一个已做过 SFT（监督微调）的模型出发。常见注意事项：偏好数据质量比数量重要，脏数据会直接教会模型坏品味；训练过度会让模型「学油」——回答变长、套路化、失去多样性；DPO 常与 [RLHF](RLHF.md) 系方法前后串联使用，而非非此即彼。

## 争议 / 讨论

- **DPO vs RLHF 上限之争**：DPO 简单稳定，但有研究指出它容易过拟合偏好数据、泛化不如带在线探索的强化学习；RLHF/GRPO 路线理论上限更高但工程门槛高。实践里两者并存，「离线偏好优化还是在线强化学习」仍是后训练的核心分歧之一。
- **偏好数据从哪来**：人类标注贵且慢，社区普遍用更强的模型生成偏好对（RLAIF 路线），这让「对齐」在某种程度上变成「用老师模型的品味教学生」，品味的来源与多样性问题被推到了上游。

## 参见

- [RLHF](RLHF.md)
- [训练与微调](../../01-底层原理/训练与微调.md)
- [神经网络](../../01-底层原理/神经网络.md)
