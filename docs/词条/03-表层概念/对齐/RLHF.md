---
term: RLHF
full_name: Reinforcement Learning from Human Feedback
aliases: [基于人类反馈的强化学习, 人类反馈强化学习]
category: 对齐
dimension: 对齐技术
granularity: 具体技术
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/2203.02155
  - https://arxiv.org/abs/2305.18290
  - https://huggingface.co/blog/rlhf
relations:
  - type: applies_to
    target: 训练与微调
    note: RLHF 是预训练之后的「训练后」阶段
  - type: part_of
    target: 对齐
    note: RLHF 是实现价值观对齐的核心技术之一
  - type: contrast
    target: DPO
    note: DPO 是 RLHF 的简化替代方案
  - type: applies_to
    target: 神经网络
    note: 奖励模型和策略模型都是神经网络
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

RLHF（Reinforcement Learning from Human Feedback，基于人类反馈的强化学习）是一种「用人类偏好训练模型」的方法：不再只让模型预测下一个词，而是让人类对模型的回答打分、排序，再用这些偏好信号去训练模型，让它学会「说人爱听的话」。ChatGPT 之所以「听话、有礼貌、拒绝有害请求」，背后就是这套技术——它把「能说会道」的语言模型，调教成了「好用」的助手。

## 原理

RLHF 通常分三步走：先做监督微调（SFT），用人类示范教模型基本的问答格式；再训练一个「奖励模型」（reward model），让人类对同一问题的多个回答排序，奖励模型学会「给好回答打高分」；最后用强化学习（早期是 PPO 算法）去更新语言模型，目标是让奖励模型给的分数尽可能高。这套「训练后」流程建立在预训练和[训练与微调](../../01-底层原理/训练与微调.md)的基础之上，奖励模型与策略模型本身也都是[神经网络](../../01-底层原理/神经网络.md)。

## 由来与历史

用人类反馈训练智能体的想法 2017 年就有了雏形（Christiano 等）。真正的引爆点是 2022 年 OpenAI 的 InstructGPT（arXiv:2203.02155）：他们证明用 RLHF 微调 GPT-3，能让模型更好地遵循指令、更少说有害的话，而参数量小得多的版本甚至比更大的原版更受欢迎——ChatGPT 正是这条路线的产品化。

RLHF 虽好但贵且难训（要训奖励模型、跑强化学习，训练不稳定）。2023 年 Rafailov 等人提出 DPO（Direct Preference Optimization，arXiv:2305.18290），把偏好学习变成一次简单的分类式训练，省掉了奖励模型和强化学习两步，效果接近、工程简单得多。2024 年起，DeepSeek 的 GRPO 等新算法进一步降低了 RL 阶段的成本，让「强化学习后训练」重新成为各家模型的热门战场。

## 应用

RLHF（及其后继者）几乎是所有商用对话助手的标准工序：ChatGPT、Claude、Gemini、DeepSeek 都经过某种形式的偏好对齐。它带来的是「软能力」——遵循指令、拒绝有害请求、语气得体、少编瞎话。代价也明确：需要大量人类标注（贵）、奖励模型可能被「钻空子」（reward hacking，模型学会刷分而不是真的变好）、而且「什么叫好回答」本身由标注者群体的价值观决定。

## 争议 / 讨论

- **RLHF vs DPO**：RLHF 理论上限更高、但实现复杂、训练不稳；DPO 简单稳定、但有人认为它容易过拟合偏好数据、上限更低。实践里两者和各自的变体（GRPO、KTO 等）并存，没有定论。
- **谁来定义「好」**：对齐本质是把某群标注者的价值观注入模型。不同文化、不同厂商对「安全」和「正确」的边界判断并不一致，这让「对齐」本身成为持续争论的话题，而不只是技术问题。

## 参见

- [训练与微调](../../01-底层原理/训练与微调.md)
- [神经网络](../../01-底层原理/神经网络.md)
