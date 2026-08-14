---
term: 蒸馏与Turbo
full_name: Knowledge Distillation / Turbo Models
aliases: [知识蒸馏, Turbo 模型, Lightning, schnell]
category: 训练
dimension: 加速技术
granularity: 具体技术
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/2311.17042
  - https://arxiv.org/abs/2311.05556
  - https://huggingface.co/Tongyi-MAI/Z-Image-Turbo
  - https://huggingface.co/learn/diffusion-course/unit2/1
relations:
  - type: part_of
    target: 训练与微调
    note: 蒸馏是一种训练范式，让老师模型教学生模型
  - type: applies_to
    target: 采样器
    note: 蒸馏模型专为低步数采样设计，steps 降到个位数
  - target: LoRA
    note: 蒸馏成果常打包成加速 LoRA（Turbo-LoRA、LCM-LoRA）分发
  - type: applies_to
    target: 生成模型
    note: 蒸馏是生成模型提速的主流路线之一
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

知识蒸馏（Knowledge Distillation）是让「老师模型」教「学生模型」的训练范式；在图像生成领域，它的产物就是各种 **Turbo / Lightning / schnell** 模型——一句话说清：把原本要跑 20~30 步的去噪过程压缩到 1~8 步，出图速度快一个数量级，代价是画质和可控性略降。Z-Image-Turbo（4 步出图）就是典型产物。

## 原理

普通扩散模型靠采样器一步步去噪，步数多才细腻。蒸馏让学生模型直接学习「老师多步计算后的最终结果」，一步到位地模仿出来——老师跑 30 步才到的终点，学生 4 步就能跳到附近。不同方案（LCM、ADD 等）在「怎么定义这个模仿目标」上各有巧思。训练与采样背景见[训练与微调](../../01-底层原理/训练与微调.md)和[采样器](../../02-组件/采样器.md)。

## 由来与历史

蒸馏概念最早由 Hinton 等人在 2015 年提出，用于压缩分类模型。图像生成领域的蒸馏潮在 2023 年爆发：清华大学团队的 LCM（Latent Consistency Models，arXiv:2311.05556）先把 50 步压到 4 步；同年 Stability AI 发布 SDXL-Turbo，使用 ADD（Adversarial Diffusion Distillation，arXiv:2311.17042）实现 1~4 步出图。随后 Black Forest Labs 的 FLUX.1-schnell、阿里的 Z-Image-Turbo 相继跟进，「官方标配一个蒸馏加速版」成了新模型的惯例。

## 应用

用蒸馏模型的关键是**同步改采样参数**，这是新手最常踩的坑：

- Z-Image-Turbo 工作流：steps 设为 4~8，CFG（guidance）降到 1 左右——很多蒸馏模型根本不吃负面提示词和 CFG，照抄普通模型的 20 步 / CFG 7 只会得到过曝的废图。
- 不想换底模可以用加速 LoRA（如 H3-Turbo-Lora、LCM-LoRA）：挂在原版模型上，配合低步数采样器（lcm / dpmpp_sde 等）使用，见 [LoRA](LoRA.md)。
- ComfyUI 里 Z-Image-Turbo 的现成工作流和量化版本见 Hugging Face 的 Tongyi-MAI/Z-Image-Turbo 与 Comfy-Org/z_image_turbo 仓库。

代价要说清：低步数下细节、纹理和构图多样性都有可见损失，且蒸馏模型上再训练 LoRA 的效果通常不如在原版上训练。

## 争议 / 讨论

社区对蒸馏的态度分两派：实用派认为 4 步出图让批量出图和实时预览成为可能，画质损失可以接受；画质派坚持「步数换质量」，把 Turbo 版当草稿机、终稿仍用原版多步渲染。r/StableDiffusion 上「LoRA 微调 vs 直接换蒸馏模型」的讨论也反复出现——结论普遍是：想快用蒸馏，想精调风格还是在原版上做 LoRA。

## 参见

- [训练与微调](../../01-底层原理/训练与微调.md)
- [采样器](../../02-组件/采样器.md)
- [LoRA](LoRA.md)
- [扩散模型](../../01-底层原理/扩散模型.md)
