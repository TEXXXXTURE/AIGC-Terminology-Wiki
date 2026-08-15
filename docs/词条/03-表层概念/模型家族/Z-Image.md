---
term: Z-Image
full_name: Z-Image
aliases: [Z-Image-Turbo, Z-Image-Plus]
category: 模型
dimension: 模型家族
granularity: 家族
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://huggingface.co/Tongyi-MAI/Z-Image-Turbo
  - https://tongyi.aliyun.com/
relations:
  - target: 阿里
    note: Z-Image 是阿里通义实验室的图像模型
  - target: FLUX
    note: Z-Image-Turbo 是 FLUX 在快速出图路线的对手
  - target: 蒸馏与Turbo
    note: Turbo 版 4 步出图
  - target: 文本编码器
    note: 必须配 2560 维 Gemma2 编码器
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

Z-Image 是阿里通义实验室的图像生成模型家族，**最大的卖点是「快」**：Z-Image-Turbo 只需 4 步采样就能出图，速度是同类模型的数倍，是「快速出图」路线的代表。它是你 ComfyUI 里已经实测跑通的主力出图模型。

## 原理

Z-Image 基于 Lumina2 架构（DiT 的变体），核心创新是**极致的蒸馏加速**：通过 Turbo 蒸馏把常规 20-30 步的采样压到 4 步，画质损失很小。家族分两档：Z-Image-Turbo（~2.6B，快速）和 Z-Image-Plus（6B，画质更好）。它的文本编码器必须是 2560 维的 Gemma2 2B——架构绑定，不能换 Qwen（4096 维）否则报错。

## 由来与历史

阿里通义实验室 2025 年推出 Z-Image 系列，Z-Image-Turbo 凭借 4 步出图的极致速度迅速走红，成为「效率党」的首选——想要快速出图、快速迭代创意时，它比 FLUX 这类画质怪兽实用得多。ComfyUI 官方做了适配，bf16 版 11.5GB，12GB 卡轻松运行。

## 应用

在 ComfyUI 里，Z-Image-Turbo 是你的日常主力：
- 加载 `z_image_turbo_bf16` + `qwen_3_4b_fp8_mixed`（注意：虽然名字带 qwen，实际工作流用的是 Gemma2 2560 维编码器）+ `ae` VAE
- 参数：euler + simple + **4 步**（这是 Turbo 的标配，别用默认 20 步）
- ⚠️ 你的 RDNA2 卡：只能用 bf16 原版（int8_convrot 版必崩）

## 争议 / 讨论

Z-Image 的「快」是以画质上限为代价的——细节和构图不如 FLUX 顶级版。社区对「速度 vs 画质」的选择有争论：效率党选 Z-Image-Turbo，画质党选 FLUX。另外 Turbo 版的 4 步是硬约束，改大步数反而效果变差，新手容易踩坑。

## 参见

- [阿里](../模型厂商/阿里.md)
- [FLUX](FLUX.md)
- [蒸馏与Turbo](微调/蒸馏与Turbo.md)
- [文本编码器](../02-组件/文本编码器.md)
