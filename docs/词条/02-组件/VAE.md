---
term: VAE
full_name: Variational Autoencoder
aliases: [变分自编码器, Variational Autoencoder]
category: 多模态
dimension: 模型组件
granularity: 组件
maturity: stable
status: published
contributors: [TEXXXXTURE]
sources:
  - https://arxiv.org/abs/1312.6114
  - https://arxiv.org/abs/2112.10752
  - https://huggingface.co/Comfy-Org/z_image_turbo
relations:
  - type: part_of
    target: 潜空间
    note: 潜空间就是 VAE 编码器的输出
  - type: applies_to
    target: 扩散模型
    note: Stable Diffusion 用 VAE 提供潜空间，扩散全程在其中进行
  - type: part_of
    target: 生成模型
    note: VAE 本身就是生成模型的三大流派之一
  - type: applies_to
    target: 浮点数与精度
    note: VAE 对精度敏感，解码发黑发灰常是 fp16 溢出所致
created: 2026-08-14
updated: 2026-08-14
revisions: 1
---

## 定义

VAE（Variational Autoencoder，变分自编码器）是一个「先压缩、再还原」的神经网络：编码器把一张大图压成很小的一组数字（潜空间表示），解码器再把这组数字还原回图。在今天的文生图流程里它扮演「暗房」的角色——扩散模型全程在压缩后的潜空间里干活，最后由 VAE 解码器把结果「冲洗」成你看到的图片。

## 原理

普通自编码器（Autoencoder）是「压缩-重建」的确定性网络：图进、向量出、再还原。VAE 在此基础上多走一步：编码器输出的不是一个固定向量，而是一个概率分布（均值和方差），解码时从这个分布里采样。这样学到的是一片连续、平滑的潜空间——两个相近的向量解码出来是两张相近的图，中间的向量解码出来是自然的过渡。这一性质让潜空间可以「插值」和「采样」，是它能当生成模型用的根本原因。

训练 VAE 要平衡两个目标：重建损失（还原出来的图要足够像原图）和 KL 散度（学出来的分布要规整、不能乱跑）。压得越狠越省算力，但细节丢得越多；这个权衡直接决定了下游生成模型的画质上限。

在 Stable Diffusion 这类潜空间扩散模型里，VAE 把 512×512×3 的图像压成 64×64×4 的潜空间张量，数据量缩小约 48 倍，扩散去噪全程在这个小空间里进行，最后一步才解码回像素——这是消费级显卡能跑文生图的关键。视频和音频模型同理：视频 VAE 还要压缩时间维度，音频 VAE 压缩波形频谱，所以 MiniMax H3 这类视频工作流里会同时挂视频 VAE 和音频 VAE 两个解码器。

## 由来与历史

VAE 由 Diederik Kingma 和 Max Welling 于 2013 年提出，首次把变分推断（一种近似概率计算的经典方法）和神经网络结合起来，让「学一个可采样的潜空间」变得可训练、可扩展。它与次年诞生的 GAN（生成对抗网络）一起，开启了深度生成模型的时代。

2014 到 2020 年间，VAE 生成图片的清晰度一直被 GAN 压制，更多活跃在表示学习、异常检测等场景。真正的翻身仗在 2022 年：Stable Diffusion 的潜空间扩散（Latent Diffusion）设计让 VAE 从「主角」转型为「最佳配角」——它不再负责生成，只负责压缩和解码，把最难的生成任务交给扩散模型。这个分工大获成功，从此「扩散模型 + VAE」成为文生图、文生视频的标准架构。

## 应用

在 ComfyUI 里，VAE 对应 **VAELoader** 节点（文件放在 `models/vae/` 目录），输出 `VAE` 接口，通常接给 **VAEDecode** 节点：KSampler 采样出来的还是潜空间数据，必须经 VAEDecode 解码成像素图才能保存预览。图生图场景则反过来用 VAEEncode 把输入图压进潜空间。

Z-Image 文生图工作流里，VAELoader 加载随模型配套的 VAE 文件；而在 H3 视频工作流里你会看到两个 VAELoader 并排：`minimax_h3_video_vae_fp16` 负责视频帧、`audio_vae_fp32` 负责音轨——视频模型带声音输出时，音画各走各的解码器。

两个实用注意点：一是 VAE 对数值精度比主模型敏感，部分模型用 fp16 解码会溢出导致整图发黑或发灰，遇到黑图先把 VAE 换成 fp32 版本试试（原理见[浮点数与精度](../01-底层原理/浮点数与精度.md)）；二是 VAE 与主模型必须配套，不同模型家族的潜空间布局不同，混用 VAE 轻则色彩发灰、细节糊掉，重则直接报错。

## 参见

- [潜空间](潜空间.md)
- [扩散模型](../01-底层原理/扩散模型.md)
- [生成模型](../01-底层原理/生成模型.md)
- [浮点数与精度](../01-底层原理/浮点数与精度.md)
- [UNet](UNet.md)
