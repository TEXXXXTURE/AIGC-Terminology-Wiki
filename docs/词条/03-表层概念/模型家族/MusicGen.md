---
term: MusicGen
full_name: MusicGen
aliases: [AudioCraft, MusicGen Medium, MusicGen Large]
category: 模型
dimension: 模型家族
granularity: 家族
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://huggingface.co/facebook/musicgen-medium
  - https://github.com/facebookresearch/audiocraft
relations:
  - target: Meta
    note: MusicGen 是 Meta 的音乐生成模型
  - target: Stable Audio
    note: Stable Audio 是 MusicGen 的主要竞品
  - target: ACE-Step
    note: ACE-Step 是更新的端到端歌曲模型
  - target: 训练与微调
    note: MusicGen 基于音频 token 建模训练
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

MusicGen 是 Meta（AudioCraft 项目）的音乐生成模型，**输入一句文字描述直接生成完整音乐**，是本地音乐生成的经典选择。家族分 small（300M）/ medium（1.5B）/ large（3.3B）三档，还有 melody 版（支持哼一段旋律让它续写）。12GB 显存全家族无压力。

## 原理

MusicGen 的工作方式是「先压缩再生成」：用音频编码器把声音压成离散 token（类似文本的分词），再用 Transformer 按文字条件自回归生成 token 序列，最后解码成音频。它支持文字描述（"lofi hip hop"）、旋律参考（melody 版）、以及二者的组合。medium 以上版本质量可用，large 质量最好但生成慢些。

## 由来与历史

Meta 2023 年发布 AudioCraft（含 MusicGen），是当时质量最好的开源音乐生成模型之一，凭借「一句描述出完整音乐」的能力迅速成为社区标配。之后同类模型（Stable Audio、ACE-Step 等）陆续出现，但 MusicGen 凭借生态成熟度和 Meta 持续维护，至今仍是本地音乐生成的主流选择。

## 应用

在本地 AI 里，MusicGen 的使用：
- 用 Audiocraft 库或 ComfyUI 节点：输入"lofi hip hop, rainy night"之类描述，生成 10-30 秒音乐
- 三档选择：small 快但糙，medium 平衡（推荐），large 最好
- melody 版：哼一段旋律（wav 文件），它据此续写完整编曲
- 12GB 显存全家族可跑，medium 约需 6GB

## 争议 / 讨论

MusicGen 的生成时长有限（默认 10-30 秒，需拼接做长曲），且版权问题敏感——训练数据含受版权保护的歌曲，Meta 未完全披露。社区常用它做背景音乐/灵感草稿，而非成品发布。

## 参见

- [Meta](../模型厂商/Meta.md)
- [Stable Audio](../模型家族/Stable Audio.md)
- [ACE-Step](../模型家族/ACE-Step.md)
- [训练与微调](../01-底层原理/训练与微调.md)
