#!/usr/bin/env python3
"""
Awesome Softwares - 添加新软件工具
用于快速添加新软件到 data/software.yaml
"""

import sys
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "software.json"


def add_software(
    name: str,
    description: str,
    website: str,
    platforms: list,
    category: str,
    open_source: bool,
    free: bool,
    github: str | None = None,
    price: str | None = None,
    tags: list | None = None,
    highlights: list | None = None,
):
    """添加新软件到数据文件 (JSON)"""
    # 读取现有数据
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 创建新软件条目
    new_software = {
        "name": name,
        "description": description,
        "website": website,
        "platforms": platforms,
        "category": category,
        "open_source": open_source,
        "free": free,
    }

    if github:
        new_software["github"] = github

    if price:
        new_software["price"] = price

    if tags:
        new_software["tags"] = tags

    if highlights:
        new_software["highlights"] = highlights

    # 添加到列表
    data.setdefault("software_list", []).append(new_software)

    # 写回文件 (JSON)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Added {name} to {DATA_FILE}")


def generate_template():
    """生成新软件模板 (JSON 字段示例)"""
    template = """
{
  "name": "软件名称",
  "description": "一句话描述",
  "website": "官网地址",
  "platforms": ["macOS", "Windows"],
  "category": "分类名称",
  "open_source": true,
  "free": true,
  "github": "GitHub用户名/仓库名",
  "price": "价格",
  "tags": ["标签1", "标签2"],
  "highlights": ["亮点1", "亮点2"]
}
"""
    print(template)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python add_software.py --template    # Show template")
        print("  python add_software.py --add <name>  # Add new software (interactive TODO)")
        sys.exit(1)

    if sys.argv[1] == "--template":
        generate_template()
    elif sys.argv[1] == "--add":
        if len(sys.argv) < 3:
            print("Error: Software name required")
            sys.exit(1)
        name = sys.argv[2]
        print(f"Interactive mode for adding {name} (TODO)...")
        print("Please edit data/software.json manually following the template and run scripts/generate_readme.py")
    else:
        print(f"Unknown argument: {sys.argv[1]}")


if __name__ == "__main__":
    main()
