#!/usr/bin/env python3
"""
Awesome Softwares - README Generator
Generates README.md and README.zh.md from data/software.json
"""

import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

DATA_FILE = Path(__file__).parent.parent / "data" / "software.json"
OUTPUT_DIR = Path(__file__).parent.parent

COST_BADGES = {
    (True, False): ("Free", "brightgreen"),
    (True, True): ("Freemium", "orange"),
    (False, False): ("Paid", "red"),
}

PLATFORM_BADGES = {
    "macOS": ("macOS", "000000", "apple", "white"),
    "Windows": ("Windows", "0078D6", "windows", "white"),
    "Linux": ("Linux", "FCC624", "linux", "black"),
    "Android": ("Android", "3DDC84", "android", "white"),
    "iOS": ("iOS", "000000", "apple", "white"),
    "Web": ("Web", "4285F4", "chrome", "white"),
}




def get_cost_badge(free: bool, freemium: bool) -> str:
    key = (free, freemium)
    text, color = COST_BADGES.get(key, ("Unknown", "grey"))
    return f"![{text}](https://img.shields.io/badge/Cost-{text}-{color})"


def get_platform_badges(platforms: list) -> str:
    badges = []
    for platform in platforms:
        if platform in PLATFORM_BADGES:
            name, color, logo, logo_color = PLATFORM_BADGES[platform]
            badge = f"![{name}](https://img.shields.io/badge/{name}-{color}?logo={logo}&logoColor={logo_color}&style=for-the-badge)"
            badges.append(badge)
    return " ".join(badges)


def get_open_source_badge(open_source: bool) -> str:
    if open_source:
        return "![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen)"
    return "![Proprietary](https://img.shields.io/badge/Open%20Source-No-lightgrey)"


def generate_github_link(github: str | None) -> str:
    if github:
        return f"[GitHub Link](https://github.com/{github})"
    return "N/A"


def generate_stars_badge(github: str | None) -> str:
    if github:
        return f"![Stars](https://img.shields.io/github/stars/{github}?style=social)"
    return "N/A"





def generate_software_section(software: dict, is_chinese: bool) -> str:
    name = software["name"]
    website = software["website"]
    platforms = software.get("platforms", [])
    open_source = software.get("open_source", False)
    free = software.get("free", True)
    freemium = software.get("freemium", False)
    github = software.get("github")

    if is_chinese:
        description = software.get("description", "")
        tags = software.get("tags", [])
        highlights = software.get("highlights", [])
    else:
        description = software.get("description_en", software.get("description", ""))
        tags = software.get("tags_en", software.get("tags", []))
        highlights = software.get("highlights_en", software.get("highlights", []))

    cost_badge = get_cost_badge(free, freemium)
    os_badge = get_open_source_badge(open_source)
    platform_badges = get_platform_badges(platforms)
    github_link = generate_github_link(github)
    stars_badge = generate_stars_badge(github)
    logo_path = software.get("logo", f"./images/{name.lower().replace(' ', '')}-logo.png")

    tag_str = " ".join([f"#{tag}" for tag in tags])
    highlights_list = "<br>".join([f"- {h}" for h in highlights])
    highlights_label = "✨ 亮点" if is_chinese else "✨ Highlights"
    anchor = name.lower().replace(" ", "-").replace("_", "-")

    if is_chinese:
        section = f"""<a id="{anchor}"></a>
## {name}

| 信息项 | 详情 |
| :------------------ | :----------------------------------------------------------------------------------------------------------------------------------------- |
| **🖼 Logo** | <img src="{logo_path}" alt="{name} Logo" width="120"/> |
| **🌐 官网** | [点击访问]({website}) |
| **🖥 适用系统** | {platform_badges} |
| **🛠 功能用途** | {description} |
| **🔓 是否开源** | {os_badge} |
| **📦 GitHub 源代码** | {github_link} |
| **⭐ GitHub Stars** | {stars_badge} |
| **💰 是否免费** | {cost_badge} |
| **{highlights_label}** | {highlights_list} |
| **🏷 分类** | {tag_str}

"""
    else:
        section = f"""<a id="{anchor}"></a>
## {name}

| Item | Details |
| :------------------ | :----------------------------------------------------------------------------------------------------------------------------------------- |
| **🖼 Logo** | <img src="{logo_path}" alt="{name} Logo" width="120"/> |
| **🌐 Website** | [Visit]({website}) |
| **🖥 Platforms** | {platform_badges} |
| **🛠 Description** | {description} |
| **🔓 Open Source** | {os_badge} |
| **📦 GitHub Repository** | {github_link} |
| **⭐ GitHub Stars** | {stars_badge} |
| **💰 Cost** | {cost_badge} |
| **{highlights_label}** | {highlights_list} |
| **🏷 Tags** | {tag_str}

"""

    return section


def generate_readme_zh(data: dict) -> str:
    software_list = data["software_list"]
    categories = data.get("categories", [])

    software_by_category = {}
    for software in software_list:
        cat = software.get("category", "未分类")
        if cat not in software_by_category:
            software_by_category[cat] = []
        software_by_category[cat].append(software)

    category_titles = {c["id"]: c["icon"] for c in categories}

    software_links = []

    readme = f"""# 📚 软件列表

🔗 [中文版本](README.zh.md) | [English Version](README.md)

> 本仓库整理并收录常用软件的信息，包括官网地址、支持平台、主要用途、开源与否、GitHub 仓库链接、功能亮点及分类标签等，旨在作为一个清晰、可查阅的软件清单索引。

> 📅 最后更新: {datetime.now().strftime("%Y-%m-%d")}

## 📖 目录

- [📚 软件列表](#-软件列表)
  - [📖 目录](#-目录)
  - [说明](#说明)
    - [💰 是否免费](#-是否免费)
  - [软件列表](#软件列表)
"""

    for cat, icon in category_titles.items():
        cat_id = cat.lower().replace(" ", "-")
        readme += f"  - [{icon} {cat}](#{cat_id})\n"

    readme += """
## 说明

### 💰 是否免费

| 类别                           | 描述                                                 | 徽章                                                           |
| ------------------------------ | ---------------------------------------------------- | -------------------------------------------------------------- |
| 🟢 **完全免费（Free）**         | 所有功能开放，无需注册或付费即可使用全部功能。       | ![Free](https://img.shields.io/badge/Cost-Free-brightgreen)    |
| 🟠 **部分功能付费（Freemium）** | 提供基本功能的免费版本，高级功能需订阅或一次性付费。 | ![Freemium](https://img.shields.io/badge/Cost-Freemium-orange) |
| 🔴 **完全付费（Paid）**         | 所有功能需付费使用。                                 | ![Paid](https://img.shields.io/badge/Cost-Paid-red)            |

## 软件列表

""" + "\n".join([f"- [{s['name']}](#{s['name'].lower().replace(' ', '-').replace('_', '-')})" for s in sorted(software_list, key=lambda x: x['name'].lower())]) + "\n\n"

    for cat in categories:
        cat_id = cat["id"]
        icon = cat["icon"]
        software_list = software_by_category.get(cat_id, [])

        readme += f"\n<a id=\"{cat_id.lower().replace(' ', '-')}\"></a>\n## {icon} {cat_id}\n\n"

        for software in software_list:
            readme += generate_software_section(software, is_chinese=True)

    return readme


def generate_readme_en(data: dict) -> str:
    software_list = data["software_list"]
    categories = data.get("categories", [])

    software_by_category = {}
    for software in software_list:
        cat = software.get("category", "Uncategorized")
        if cat not in software_by_category:
            software_by_category[cat] = []
        software_by_category[cat].append(software)

    category_titles = {c.get("id_en", c["id"]): c["icon"] for c in categories}

    readme = f"""# 📚 Awesome Softwares

🔗 [中文版本](README.zh.md) | [English Version](README.md)

> A curated list of awesome software tools with their websites, platforms, descriptions, open source status, GitHub links, features, and tags.

> 📅 Last Updated: {datetime.now().strftime("%Y-%m-%d")}

## 📖 Table of Contents

- [📚 Awesome Softwares](#-awesome-softwares)
  - [📖 Table of Contents](#-table-of-contents)
  - [Overview](#overview)
    - [💰 Cost](#-cost)
  - [Software List](#software-list)
"""

    for cat, icon in category_titles.items():
        cat_id = cat.lower().replace(" ", "-")
        readme += f"  - [{icon} {cat}](#{cat_id})\n"
        if cat in software_by_category:
            for software in software_by_category[cat]:
                software_name = software["name"]
                software_anchor = software_name.lower().replace(" ", "-").replace("_", "-")
                readme += f"    - [{software_name}](#{software_anchor})\n"

    readme += """
## Overview

### 💰 Cost

| Category | Description | Badge |
|----------|-------------|-------|
| 🟢 **Free** | All features are open, no registration or payment required. | ![Free](https://img.shields.io/badge/Cost-Free-brightgreen) |
| 🟠 **Freemium** | Free basic version, premium features require subscription. | ![Freemium](https://img.shields.io/badge/Cost-Freemium-orange) |
| 🔴 **Paid** | All features require payment. | ![Paid](https://img.shields.io/badge/Cost-Paid-red) |

## Software List

""" + "\n".join([f"- [{s['name']}](#{s['name'].lower().replace(' ', '-').replace('_', '-')})" for s in sorted(software_list, key=lambda x: x['name'].lower())]) + "\n\n"

    for cat in categories:
        cat_id = cat.get("id_en", cat["id"])
        icon = cat["icon"]
        original_cat_id = cat["id"]
        software_list = software_by_category.get(original_cat_id, [])

        readme += f"\n<a id=\"{cat_id.lower().replace(' ', '-')}\"></a>\n## {icon} {cat_id}\n\n"

        for software in software_list:
            readme += generate_software_section(software, is_chinese=False)

    return readme


def main():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    readme_zh = generate_readme_zh(data)
    with open(OUTPUT_DIR / "README.zh.md", "w", encoding="utf-8") as f:
        f.write(readme_zh)
    print("Generated README.zh.md")

    readme_en = generate_readme_en(data)
    with open(OUTPUT_DIR / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_en)
    print("Generated README.md")

    print("\nSuccessfully generated both README files!")


if __name__ == "__main__":
    main()
