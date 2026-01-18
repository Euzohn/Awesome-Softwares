#!/usr/bin/env python3
"""
Awesome Softwares - 更新 GitHub Stars
从 GitHub API 获取最新的 Stars 数量
"""

import requests
import yaml
from pathlib import Path
import time

DATA_FILE = Path(__file__).parent.parent / "data" / "software.json"
GITHUB_API = "https://api.github.com/repos/{}"


def get_stars(owner: str, repo: str) -> int | None:
    """获取仓库的 Stars 数量"""
    try:
        url = GITHUB_API.format(f"{owner}/{repo}")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("stargazers_count", 0)
        elif response.status_code == 403:
            print(f"⚠️  Rate limited, skipping {owner}/{repo}")
            return None
        else:
            print(f"❌  Error getting {owner}/{repo}: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌  Exception: {e}")
        return None


def update_stars():
    """更新所有仓库的 Stars（统一写入 JSON）"""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        # 若文件为 JSON，使用 yaml.safe_load 也可解析，但建议明确使用 json
    # 改为显式 JSON 读写
    import json

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated_count = 0
    skipped_count = 0

    for software in data.get("software_list", []):
        github = software.get("github")
        if github and "/" in github:
            print(f"📡 Fetching stars for {github}...", end=" ")
            stars = get_stars(*github.split("/"))
            if stars is not None:
                old_stars = software.get("stars", 0)
                software["stars"] = stars
                if stars != old_stars:
                    print(f"✅ {old_stars} → {stars}")
                else:
                    print(f"✓ (no change)")
                updated_count += 1
            else:
                print("⏭ skipped")
                skipped_count += 1
            time.sleep(1)  # 避免 API 限制

    # 写回 JSON 文件
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n🎉 Updated {updated_count} repos, skipped {skipped_count}")


if __name__ == "__main__":
    update_stars()
