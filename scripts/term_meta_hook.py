# -*- coding: utf-8 -*-
"""
MkDocs hook — 词条页终端风元信息注入

在词条页(.md 位于 docs/词条/ 下)正文开头,
自动注入一行终端风元信息: $ ai-kb term --dimension=X --granularity=Y
数据来自 page.meta(即 YAML frontmatter, MkDocs 已自动剥离)。

注意: on_page_markdown 事件触发时 frontmatter 已被剥离并放入 page.meta,
      因此不要再解析 markdown 里的 frontmatter。

启用: mkdocs.yml 增加
  hooks:
    - scripts/term_meta_hook.py
"""


def on_page_markdown(markdown, page, config, files):
    rel = page.file.src_path.replace("\\", "/")
    # 只处理词条目录下的 .md
    if not rel.startswith("词条/"):
        return markdown

    meta = getattr(page, "meta", {}) or {}
    dim = meta.get("dimension", "")
    gran = meta.get("granularity", "")
    cat = meta.get("category", "")
    mat = meta.get("maturity", "")

    parts = []
    if dim:
        parts.append(f"--dim={dim}")
    if gran:
        parts.append(f"--gran={gran}")
    if cat:
        parts.append(f"--cat={cat}")
    if mat:
        parts.append(f"--mat={mat}")
    if not parts:
        return markdown

    meta_line = (
        '<div class="term-meta">'
        '<span class="k">$</span> ai-kb term ' + " ".join(parts) +
        "</div>\n\n"
    )
    return meta_line + markdown
