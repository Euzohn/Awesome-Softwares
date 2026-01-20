#!/usr/bin/env python3
"""
Awesome Softwares - 更新 GitHub Stars
从 GitHub API 获取最新的 Stars 数量
"""

import requests
import os
from pathlib import Path
import time

DATA_FILE = Path(__file__).parent.parent / "data" / "software.json"
GITHUB_API = "https://api.github.com/repos/{}"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def get_stars(owner: str, repo: str, retry_count: int = 0) -> int | None:
    """获取仓库的 Stars 数量，支持重试"""
    try:
        url = GITHUB_API.format(f"{owner}/{repo}")
        headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return data.get("stargazers_count", 0)
        elif response.status_code == 403:
            if "X-RateLimit-Remaining" in response.headers:
                remaining = int(response.headers["X-RateLimit-Remaining"])
                reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
                if remaining == 0 and reset_time > 0:
                    wait_time = max(reset_time - int(time.time()), 60)  # 至少等待60秒
                    print(f"⚠️  Rate limited, waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                    if retry_count < 1:  # 只重试一次
                        return get_stars(owner, repo, retry_count + 1)
            print(f"⚠️  Rate limited, skipping {owner}/{repo}")
            return None
        elif response.status_code == 404:
            print(f"❌  Repository not found: {owner}/{repo}")
            return None
        else:
            print(f"❌  Error getting {owner}/{repo}: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌  Exception: {e}")
        return None


def update_stars():
    """更新所有仓库的 Stars（统一写入 JSON）"""
    import json

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated_count = 0
    skipped_count = 0
    rate_limited = False

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
                rate_limited = True

            # 如果遇到速率限制，增加等待时间
            sleep_time = 3 if rate_limited else 1
            time.sleep(sleep_time)

    # 写回 JSON 文件
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n🎉 Updated {updated_count} repos, skipped {skipped_count}")

    if rate_limited:
        print("💡 Tip: Set GITHUB_TOKEN environment variable to increase rate limits")
        print("   export GITHUB_TOKEN=your_github_token")


if __name__ == "__main__":
    print("🚀 Starting GitHub stars update...")
    if not GITHUB_TOKEN:
        print("💡 No GITHUB_TOKEN found. Using anonymous requests (60/hour limit)")
        print("   Set GITHUB_TOKEN for higher limits (5000/hour)")
    else:
        print("✅ Using GitHub token for higher rate limits")
    print()
    update_stars()
