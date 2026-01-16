# 贡献指南

感谢您对 Awesome-Softwares 项目的兴趣！本指南将帮助您了解如何为项目做出贡献。

## 📋 目录

- [如何贡献](#如何贡献)
- [添加新软件](#添加新软件)
- [软件信息格式](#软件信息格式)
- [提交规范](#提交规范)
- [自动化工具](#自动化工具)

## 如何贡献

1. **Fork** 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingSoftware`)
3. 提交您的更改 (`git commit -m 'Add AmazingSoftware'`)
4. 推送到分支 (`git push origin feature/AmazingSoftware`)
5. 创建 **Pull Request**

## 添加新软件

### 方式一：手动编辑（推荐）

1. 编辑 `data/software.json` 文件
2. 在 `software_list` 数组中添加新软件条目
3. 运行 `python3 scripts/generate_readme.py` 更新 README

### 方式二：使用脚本

```bash
# 生成新软件模板
python3 scripts/add_software.py --template

# 交互式添加（需要手动编辑 JSON）
# 1. 运行 generate_readme.py 重新生成 README
python3 scripts/generate_readme.py
```

## 软件信息格式

```json
{
  "name": "软件名称",
  "description": "一句话描述软件功能",
  "website": "https://example.com/",
  "platforms": ["macOS", "Windows", "Linux"],
  "category": "分类名称",
  "open_source": true,
  "free": true,
  "github": "owner/repo",
  "price": "$99 (可选)",
  "stars": 10000,
  "tags": ["标签1", "标签2"],
  "highlights": [
    "亮点1",
    "亮点2"
  ]
}
```

### 字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| `name` | ✅ | 软件名称 |
| `description` | ✅ | 一句话描述 |
| `website` | ✅ | 官网链接 |
| `platforms` | ✅ | 支持的平台列表 |
| `category` | ✅ | 从现有分类中选择 |
| `open_source` | ✅ | 是否开源 (true/false) |
| `free` | ✅ | 是否免费 (true/false) |
| `github` | ❌ | GitHub 仓库 (如 owner/repo) |
| `price` | ❌ | 价格 (如 $99) |
| `stars` | ❌ | GitHub Stars 数量 |
| `tags` | ✅ | 标签列表 |
| `highlights` | ✅ | 功能亮点列表 |

### 支持的平台

- `macOS` - Apple macOS
- `Windows` - Microsoft Windows
- `Linux` - Linux 发行版
- `Android` - Android 系统
- `iOS` - Apple iOS

### 现有分类

- 播放器
- 文件传输
- 文件管理
- 开发工具
- 效率工具
- 音视频处理
- 数据分析
- Markdown
- 系统工具
- 设计工具
- 图像处理
- 截图工具
- 浏览器
- 趣味工具

## 提交规范

### Commit Message 格式

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Type 类型

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `perf`: 性能优化
- `chore`: 其他更新

### 示例

```
feat(software): Add Visual Studio Code

- Add new development tool
- Cross-platform support
- Open source with large community

Closes #123
```

## 自动化工具

### 生成 README

```bash
python3 scripts/generate_readme.py
```

此脚本会：
1. 读取 `data/software.json`
2. 生成 `README.md` 和 `README.zh.md`
3. 自动添加更新时间戳

### 更新 Stars

```bash
python3 scripts/update_stars.py
```

此脚本会：
1. 获取所有开源软件的最新 Stars 数量
2. 更新 `data/software.json`
3. 需要 GitHub API Token（避免速率限制）

### 环境变量

```bash
export GITHUB_TOKEN=your_token_here
python3 scripts/update_stars.py
```

## 代码规范

- 使用 **4 空格** 缩进
- JSON 文件使用 **UTF-8** 编码
- 链接必须以 `https://` 开头
- 描述保持简洁，不超过 100 字
- 亮点不超过 6 条

## 建议

在提交 PR 之前，请检查：

- [ ] 软件信息完整准确
- [ ] JSON 格式正确（可使用 `python3 -m json.tool data/software.json` 验证）
- [ ] README 已更新
- [ ] 没有拼写或语法错误

## 联系方式

- 提交 Issue: https://github.com/zohn/Awesome-Softwares/issues
- 项目主页: https://github.com/zohn/Awesome-Softwares

感谢您的贡献！ 🎉
