---
term: CLIP
full_name: Contrastive Language-Image Pretraining
aliases: [对比语言-图像预训练]
category: 多模态
dimension: 模型组件
granularity: 组件
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/2103.00020
  - https://huggingface.co/Tongyi-MAI/Z-Image-Turbo
  - https://huggingface.co/Comfy-Org/z_image_turbo
relations:
  - type: part_of
    target: 文本编码器
    note: CLIP 是文本编码器家族中最有名的一员
  - type: applies_to
    target: 扩散模型
    note: 文生图扩散模型的提示词条件由 CLIP 这类文本编码器提供
  - target: 潜空间
    note: CLIP 把文本和图像映射到同一向量空间，与潜空间思想相通
  - type: part_of
    target: 神经网络
    note: CLIP 由两个神经网络编码器组成
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

CLIP（Contrastive Language-Image Pretraining，对比语言-图像预训练）是 OpenAI 在 2021 年发布的模型，做的事一句话说清：把文字和图片翻译成同一种「语言」——同一个向量空间里的数字向量，意思相近的图文，向量就靠得近。在文生图流程里它是「翻译官」：你写的提示词先经 CLIP 变成向量，扩散模型才「看得懂」该画什么。

## 原理

CLIP 由两个编码器组成：一个文本编码器吃句子，一个图像编码器吃图片，各自输出一个向量。训练方式叫对比学习：拿来海量「图片 + 图片说明」配对数据，要求模型把配对的图文向量拉近、把不配对的推远。OpenAI 用了 4 亿对图文做训练，模型因此学到了非常通用的视觉-语言对应关系——不用专门训练就能给图片分类（zero-shot），这是它当年最惊艳的能力。

在文生图里，CLIP 只用到文本那一半：提示词被编码成一串向量，作为「条件」注入去噪网络的每一步（通过交叉注意力机制），引导模型往文字描述的方向去噪。提示词写得越清楚，条件向量越明确，出图就越贴题——提示词工程之所以有效，根源就在这里。

值得注意的是，今天的「CLIP」更多是一个名字遗产。Stable Diffusion 1.x/2.x 用的确实是原版 CLIP 的文本编码器，但 SDXL 开始混用更大的 OpenCLIP，SD3、FLUX 换用 T5，Z-Image 则直接用 Qwen3 大语言模型当文本编码器。架构早已换了几轮，只是 ComfyUI 的加载节点还叫 CLIPLoader。详见[文本编码器](文本编码器.md)。

## 由来与历史

2021 年初，OpenAI 发表 CLIP 论文，和 DALL·E 同期亮相。它证明了「用互联网上的天然图文对做对比学习」这条路走得通：不需要人工标注，4 亿对网页图文就能训出通用的视觉理解能力，在 ImageNet 上不做专门训练就追平了当时的监督学习模型。CLIP 很快成为多模态研究的基础设施，从图像检索到内容审核处处可见。

2022 年，Stable Diffusion 把 CLIP 的文本编码器用作提示词条件模块，CLIP 从此走进每个文生图用户的电脑。随后几年，研究发现更大的语言模型（T5、Qwen、Gemma）当文本编码器理解力更强，CLIP 在新生成模型里逐步被替换，但它确立的「图文对齐到同一向量空间」范式至今仍是多模态的基石。

## 应用

在 ComfyUI 里，CLIP（广义地说，是文本编码器）由 **CLIPLoader** 节点加载，文件放在 `models/clip/` 或 `models/text_encoders/` 目录，输出 `CLIP` 接口，接到 CLIPTextEncode 节点——那个节点就是你写提示词（Prompt）的地方，正面、负面各一个。

Z-Image 文生图工作流里，CLIPLoader 加载的是 `qwen_3_4b_fp8_mixed.safetensors`——名字里虽有 CLIP，装的实际是 Qwen3-4B 语言模型，这是新架构的标准做法。加载时节点上的 `type` 选项要选对（如 z_image），选错了会直接报维度不匹配的错误。

实用建议：文本编码器文件也有 fp8 / fp16 / bf16 精度版本，显存紧张时选 fp8 影响很小（文本编码对精度不如 VAE 敏感）；换模型家族时务必同步更换文本编码器，Z-Image 的编码器装不进 SD 1.5 的工作流，反之亦然。

## 参见

- [文本编码器](文本编码器.md)
- [扩散模型](../01-底层原理/扩散模型.md)
- [潜空间](潜空间.md)
- [神经网络](../01-底层原理/神经网络.md)
