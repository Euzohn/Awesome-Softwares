# 贡献指南

感谢您对 Awesome-Softwares 项目的兴趣！本指南将帮助您了解如何为项目做出贡献。

## 📋 目录

- [如何贡献](#如何贡献)
- [添加新软件](#添加新软件)
- [软件信息格式](#软件信息格式)
- [提交规范](#提交规范)
- [自动化工具](#自动化工具)
- [CI/CD 工作流](#cicd-工作流)

## 如何贡献

1. **Fork** 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingSoftware`)
3. 提交您的更改 (`git commit -m 'Add AmazingSoftware'`)
4. 推送到分支 (`git push origin feature/AmazingSoftware`)
5. 创建 **Pull Request**

**注意**：推送后，CI 会自动验证数据格式并生成 README。如果验证失败，请检查错误信息并修复。

## 添加新软件

### 方式一：手动编辑（推荐）

1. 编辑 `data/software.json` 文件
2. 在 `software_list` 数组中添加新软件条目
3. 运行 `python3 scripts/validate_schema.py` 验证数据格式
4. 运行 `python3 scripts/generate_readme.py` 更新 README

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
  "description": "一句话描述软件功能（中文）",
  "description_en": "A brief description of the software (English)",
  "website": "https://example.com/",
  "platforms": ["macOS", "Windows", "Linux"],
  "category": "分类名称",
  "open_source": true,
  "free": true,
  "github": "owner/repo (可选)",
  "stars": 10000,
  "tags": ["标签1", "标签2"],
  "tags_en": ["Tag1", "Tag2"],
  "highlights": [
    "亮点1",
    "亮点2"
  ],
  "highlights_en": [
    "Highlight1",
    "Highlight2"
  ],
  "logo": "https://example.com/logo.png 或 ./images/logo.png (可选)",
  "price": "$99 (可选)"
}
```

### 字段说明

| 字段            | 必填 | 说明                                      |
| --------------- | ---- | ----------------------------------------- |
| `name`          | ✅    | 软件名称                                  |
| `description`   | ✅    | 一句话描述（中文）                        |
| `description_en`| ❌    | 一句话描述（英文）                        |
| `website`       | ✅    | 官网链接                                  |
| `platforms`     | ✅    | 支持的平台列表                            |
| `category`      | ✅    | 从现有分类中选择                          |
| `open_source`   | ✅    | 是否开源 (true/false)                     |
| `free`          | ✅    | 是否免费 (true/false)                     |
| `github`        | ❌    | GitHub 仓库 (如 owner/repo)               |
| `stars`         | ❌    | GitHub Stars 数量                         |
| `tags`          | ✅    | 标签列表（中文）                          |
| `tags_en`       | ❌    | 标签列表（英文）                          |
| `highlights`    | ✅    | 功能亮点列表（中文）                      |
| `highlights_en` | ❌    | 功能亮点列表（英文）                      |
| `logo`          | ❌    | Logo 图片 URL 或相对路径                  |
| `price`         | ❌    | 价格 (如 $99)                             |

### 支持的平台

- `macOS` - Apple macOS
- `Windows` - Microsoft Windows
- `Linux` - Linux 发行版
- `Android` - Android 系统
- `iOS` - Apple iOS
- `Web` - Web 应用

### 现有分类

- 多媒体与音视频
- 文件管理与传输
- 网络工具与浏览器
- 系统工具与优化
- 开发与编程
- 办公与生产力
- 笔记、知识与写作管理
- 设计与图像处理
- 远程协作与通讯
- 娱乐与趣味

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

### 验证数据格式

```bash
python3 scripts/validate_schema.py
```

此脚本会：
1. 验证 `data/software.json` 的数据格式
2. 检查必需字段、有效平台和分类
3. 验证 GitHub 仓库格式和 URL

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
- [ ] 运行 `python3 scripts/validate_schema.py` 验证数据格式
- [ ] 没有拼写或语法错误

## CI/CD 工作流

项目使用 GitHub Actions 进行持续集成和自动化：

- **触发条件**：
  - 推送 `data/software.json` 时触发数据验证和 README 生成
  - 每周定时更新 GitHub Stars（通过 PR）

- **自动化任务**：
  - 数据格式验证（`validate_schema.py`）
  - README 生成（`generate_readme.py`）
  - Stars 更新（`update_stars.py`）

- **所需密钥**：
  - `GITHUB_TOKEN`：用于访问 GitHub API（自动提供）

贡献者无需手动运行大部分脚本，CI 会处理验证和生成。

## 联系方式

- 提交 Issue: https://github.com/Euzohn/Awesome-Softwares/issues
- 项目主页: https://github.com/Euzohn/Awesome-Softwares

感谢您的贡献！ 🎉
