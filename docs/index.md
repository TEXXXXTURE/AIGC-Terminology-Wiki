---
title: AI 知识库
---

<div class="hero">
  <h1>AI 知识库</h1>
  <div class="subtitle">一线知识的沉淀与导航站 — 开源、Wiki 式、面向所有人的知识库</div>
  <div class="pillars">
    <span class="pillar">📚 上限靠来源</span>
    <span class="pillar">🧪 标准靠校验</span>
    <span class="pillar">🤗 生态靠开放</span>
    <span class="pillar">🔖 信任靠留痕</span>
  </div>
</div>

---

## 🌳 知识树

每个词条是一个节点，关系是边。从根往下读是一条完整的学习路径，从叶子跳入是速查。

```
AI 知识树
├── AI 基础          — AI 是什么、机器学习/深度学习基础、数学与统计
├── 深度学习          — 神经网络/Transformer/CNN/训练与微调
├── 生成与多模态       — 扩散模型/Stable Diffusion/ComfyUI/图像视频音频生成
├── LLM 与语言模型    — LLM 工程/RAG/提示词/评测/微调
├── Agent 与智能体    — Agent/Function Calling/MCP/多Agent协作
├── AI 工程与基础设施  — 推理引擎/MLOps/数据工程/部署
└── 计算机基础        — 编程语言/操作系统/数据库/框架与库
```

> 说明：Wiki 的知识结构是网状的——每个词条是独立节点，通过 relations 互相连接。当前仓库物理目录沿用早期分类（01-底层原理 … 06-IT行业），这只是文件夹层面的便利，知识结构在 relations 里。详细地图见 [AI 知识地图](项目文档/map.md)。

## 📚 词条导航

- [AI 知识地图 →](项目文档/map.md) — 全站网状入口
- [底层原理 →](词条/01-底层原理/神经网络.md) — 理解一切的根
- [组件 →](词条/02-组件/UNet.md) — 模型的零件
- [表层概念 →](词条/03-表层概念/量化格式/bf16.md) — 具体技术/格式/参数
- [LLM 工程 →](词条/04-LLM工程/推理引擎.md) — LLM 落地
- [Agent 工程 →](词条/05-Agent工程/Agent 框架.md) — Agent 开发
- [IT 行业 →](词条/06-IT行业/编程语言/Python.md) — 语言/系统/框架

## 🟡 前沿雷达

机器自动扫描社区（GitHub / arXiv / 讨论）生成的热词卡，未经沉淀、先看先得。见 `雷达/` 目录。

## 📖 项目文档

| 文档 | 是什么 |
|------|--------|
| [AI 知识地图](项目文档/map.md) | 全站网状入口：广义 AI 知识树 + 当前目录对应 |
| [PRD（人类版）](项目文档/PRD-人类版.md) | 项目是什么、框架、进度——快速了解 |
| [PRD（Agent 版）](项目文档/PRD-Agent版.md) | 完整设计决策 + 技术细节 + 踩坑记录 |
| [内容规范](项目文档/CONTENT-SPEC.md) | 词条长什么样、怎么写、怎么连线、怎么校验 |
| [贡献指南](项目文档/CONTRIBUTING.md) | 四层贡献模型：读者 / 贡献者 / 维护者 / 机器 |
| [维护流程](项目文档/MAINTENANCE.md) | 审校 / 发布 / 雷达 / 升降级 / 回滚 |
| [设计定案](项目文档/DESIGN-SPEC.md) | 项目设计决策的唯一事实源 |

## ✍️ 贡献

欢迎任何人参与！提 Issue 纠错、提 PR 写词条。仓库：[TEXXXXTURE/AIGC-Terminology-Wiki](https://github.com/TEXXXXTURE/AIGC-Terminology-Wiki)（历史命名，已扩展为通用知识库）
