---
term: UNet
full_name: U-Net
aliases: [U-Net, U型网络]
category: 架构
dimension: 模型组件
granularity: 组件
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/1505.04597
  - https://arxiv.org/abs/2006.11239
  - https://arxiv.org/abs/2212.09748
relations:
  - type: part_of
    target: 扩散模型
    note: 经典扩散模型的去噪网络
  - type: part_of
    target: 神经网络
    note: UNet 是卷积神经网络的一种结构
  - type: applies_to
    target: 训练与微调
    note: UNet 的参数靠扩散训练得来，也是 LoRA 等微调的主要作用对象
  - target: 潜空间
    note: Stable Diffusion 里 UNet 在潜空间上做去噪
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

UNet（U-Net）是一种长得像字母「U」的神经网络结构：左半边把图片一层层压缩、提取特征（编码器），右半边再一层层放大还原（解码器），中间用「跳跃连接」把左半边的细节直接抄近路送到右半边。它最早是给医学图像分割用的，后来被扩散模型相中，成了 Stable Diffusion 等经典文生图模型里的去噪主力——你在 ComfyUI 里加载的那个大模型文件，很长一段时间里装的就是一个 UNet。

## 原理

UNet 的编码器一路下采样：图片尺寸逐层减半，通道数逐层增加。越往下，网络看到的「视野」越大，抓住的是构图、物体这类全局信息；越往上，保留的是边缘、纹理这类局部细节。这种多尺度结构让网络既能理解「画的是什么」，又能管好「线条长什么样」。

跳跃连接（skip connection）是它的灵魂：编码器每一层的输出，直接拼接到解码器对应层。普通编码器-解码器结构压到底部时细节会丢光，跳跃连接相当于把原图的细节「备份」了一份送过去，解码器据此还原出锐利的结果。这也是它当年在医学图像分割上胜出的原因——画细胞轮廓，细节一条都不能丢。

在扩散模型里，UNet 的输入是一张带噪声的图（在 Stable Diffusion 里是潜空间里的噪声），外加两个条件：当前是第几步（时间步嵌入）和提示词向量（通过交叉注意力注入）。输出是「这张图里的噪声是什么」。减噪一步步进行，图片逐渐显形——详细过程见[扩散模型](../01-底层原理/扩散模型.md)。

UNet 也有短板：卷积结构对全局关系的建模能力有限，模型做大之后扩展性不如 Transformer。2022 年 DiT（Diffusion Transformer）论文证明可以用纯 Transformer 做去噪网络，效果更好、更能堆规模。此后 FLUX、SD3、Wan、Z-Image 等新一代模型全部转向了 DiT，UNet 正在逐步退场——但存量生态（SD 1.5、SDXL 的海量模型和 LoRA）让它仍是今天最常用的组件之一。

## 由来与历史

2015 年，弗莱堡大学的 Ronneberger 等人发表 U-Net 论文，原本目标很具体：生物医学图像分割。当时的痛点是医学数据标注稀少，UNet 靠数据增强和跳跃连接，用几十张训练图就能准确分割细胞结构，在当年的 ISBI 细胞追踪挑战赛上大幅领先。此后它迅速成为图像分割领域的标准结构。

2020 年 DDPM 论文把扩散模型带回主流视野时，选择了 UNet 的改进版作为去噪网络：加入自注意力层、时间步嵌入和 GroupNorm。这个「DDPM 版 UNet」随后被 Stable Diffusion（2022）继承，成为之后两三年几乎所有开源文生图模型的标配，也催生了围绕它的庞大微调生态——绝大多数 LoRA 调的就是 UNet 的权重。

2022 年底 DiT 论文发表，2024 年起 SD3、FLUX、Wan 等新模型陆续换成 Transformer 去噪网络。你在 ComfyUI 里加载 Z-Image 时，UNETLoader 节点里装的其实已经是一个 DiT，只是节点名字沿用至今——名字没换，内核换了。

## 应用

在 ComfyUI 里，UNet 对应 **UNETLoader** 节点（加载模型用，文件放在 `models/diffusion_models/` 目录），输出一个 `MODEL` 接口，接到 KSampler 上参与采样。Z-Image 文生图工作流加载的 `z_image_turbo_bf16.safetensors` 走的就是这个节点——虽然 Z-Image 的去噪内核已是 DiT，但节点名仍叫 UNETLoader。

三个实用注意点：一是去噪模型、文本编码器、VAE 三件套必须配套，拿 SD 1.5 的 VAE 去配 Z-Image 会直接报错或出废图；二是模型文件有精度版本之分（fp8 / fp16 / bf16），fp8 省显存但略有质量损失，选择逻辑见[浮点数与精度](../01-底层原理/浮点数与精度.md)；三是给 UNet 挂 LoRA 时（LoraLoaderModelOnly 节点），LoRA 必须和底模同架构，SDXL 的 LoRA 装不到 Z-Image 上。

## 参见

- [扩散模型](../01-底层原理/扩散模型.md)
- [神经网络](../01-底层原理/神经网络.md)
- [训练与微调](../01-底层原理/训练与微调.md)
- [潜空间](潜空间.md)
- [采样器](采样器.md)
