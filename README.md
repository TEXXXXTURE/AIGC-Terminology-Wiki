# AI 知识库

> **一线知识的沉淀与导航站** — 开源、Wiki 式、面向所有人的知识库。

## 这是什么

一个把知识讲清楚的地方。当前以 AI 领域为主体（机器学习、深度学习、NLP、多模态、LLM、Agent、AI 工程与安全伦理），架构支持扩展到任意知识领域。每个词条是独立节点，通过 relations 连接成知识网 下面的一个重要分支，不是全部。每个词条是一个独立页面，点击即可跳转，词条之间互相链接——就像一本不断生长的、开放给所有人编写的 AI Wiki。全站网状入口见 [AI 知识地图](docs/项目文档/map.md)。

**设计逻辑（四根柱子）**：

| 柱子 | 含义 | 机制 |
|------|------|------|
| 上限 | 内容能多深、多新、多一线 | 靠来源层级，每条带原始链接 |
| 标准 | 多规范、多可信、多一致 | 靠 Schema 校验 + 无源不收录 |
| 生态 | 内容产品活着 | 靠开放编写（四层贡献模型） |
| 信任 | 读者凭什么信 | 靠 git 留痕 + 来源标注 + 修订记录 |

## 双层结构

- **概念库（docs/）**：沉淀层。成熟词条独立成页，分类索引，互相链接。
- **雷达（雷达/）**：社区感知层。自动扫描 GitHub/arXiv/推文 抓新概念，生成「🟡 社区热词卡」——未经沉淀的一线信息，先进来、标注清楚、再慢慢转正。

## 目录结构

```
├── docs/                  概念库（MkDocs 站点）
│   ├── 词条/             词条本体，按领域分 6 大类
│   │   ├── 01-底层原理    Transformer/MoE/量化/训练...
│   │   ├── 02-组件        CLIP/VAE/Tokenizer...
│   │   ├── 03-表层概念    Agent/LLM/多模态/模型厂商...
│   │   ├── 04-LLM工程     推理优化/RAG/评测...
│   │   ├── 05-Agent工程   Agent 框架/工具调用/记忆...
│   │   └── 06-IT行业      基础设施/语言/框架...
│   ├── 文章与引用/        外部文章聚合与引用库
│   └── 项目文档/          项目规范（PRD/SPEC）+ 生产流程（词条生产单/kimi-prompts）
├── 雷达/                 社区感知层（采集原始素材 → 采集表 → 热词卡）
├── scripts/              采集与维护脚本（moke_collect/aa_collect/community_collect...）
├── mkdocs.yml            MkDocs 站点配置
```

## 内容规范

所有词条必须符合 [CONTENT-SPEC.md](docs/项目文档/CONTENT-SPEC.md)（词条 Schema + 写作风格 + 成熟度分级 + 校验清单）。

## 怎么贡献

欢迎任何人参与！详见 [CONTRIBUTING.md](docs/项目文档/CONTRIBUTING.md)。

四层贡献模型：
- **L1 读者**：提 Issue（纠错 / 补充 / 讨论）
- **L2 贡献者**：提 PR（提交词条草稿，过 Schema 校验后发布）
- **L3 维护者**：审校 / 合并 / 定稿
- **L4 机器**：雷达 Agent 自动抓热词卡

## 站点

GitHub Pages 自动部署：https://texxxxture.github.io/ai-knowledge-base/

## 关联项目

- [工具情报官 Wiki](https://github.com/TEXXXXTURE/tool-intel-wiki) — 工具拆解与情报日报
- [分布式 Agent 集群规则](https://github.com/TEXXXXTURE/distributed-agent-cluster-rules) — 集群运行规则
