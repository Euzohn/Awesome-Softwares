# 📁 项目结构说明

> 本文档说明 Awesome-Softwares 项目的技术架构和目录结构。

## 📂 目录结构

```
awesome-softwares/
├── 📄 README.md              # 软件列表（英文版）
├── 📄 README.zh.md           # 软件列表（中文版）
├── 📄 README_backup.md       # 旧版 README 备份
├── 📄 PROJECT_INFO.md        # 项目结构说明（本文档）
├── 📄 CONTRIBUTING.md        # 贡献指南
├── 📄 add_software_workflow.md # 添加软件工作流说明
├── 📄 LICENSE                # MIT 许可证
├── 📄 requirements.txt       # Python 依赖
│
├── 📁 data/
│   ├── software.json         # ✅ 结构化软件数据（核心数据源）
│   └── software.yaml         # YAML 备用格式
│
├── 📁 scripts/
│   ├── generate_readme.py    # 自动生成 README 文档
│   ├── add_software.py       # 添加新软件工具
│   ├── update_stars.py       # 更新 GitHub Stars
│   └── validate_schema.py    # 验证 JSON 数据结构
│
├── 📁 .github/workflows/
│   └── ci.yml                # GitHub Actions CI/CD
│
├── 📁 images/                # 软件 Logo 图片
│   ├── (各种 logo 文件...)
│   └── images.md             # 图片说明文档
│
└── 📁 docs/                  # 额外文档
    ├── tags.md               # 标签分类说明
    ├── cost.md               # 费用说明
    └── tmp.md                # 临时文档
```

## 🔄 数据流

```
data/software.json (单一数据源)
        ↓
  scripts/generate_readme.py
        ↓
  README.md + README.zh.md (自动生成)
```

## 🚀 快速开始

### 1. 安装 Python 3.x

```bash
# macOS
brew install python3

# Linux
sudo apt install python3
```

### 2. 克隆项目

```bash
git clone https://github.com/zohn/Awesome-Softwares.git
cd Awesome-Softwares
```

### 3. 生成 README 文档

```bash
python3 scripts/generate_readme.py
```

## 📝 添加新软件

### 方法一：直接编辑 JSON（推荐）

```bash
# 1. 编辑数据文件
nano data/software.json

# 2. 运行生成脚本
python3 scripts/generate_readme.py
```

### 方法二：使用模板

```bash
# 生成软件模板
python3 scripts/add_software.py --template
```

## 🔄 自动化工具

### 更新 GitHub Stars

```bash
python3 scripts/update_stars.py
```

**注意**: 设置 `GITHUB_TOKEN` 环境变量可避免 API 速率限制：

```bash
export GITHUB_TOKEN=your_github_token
python3 scripts/update_stars.py
```

## 🤖 GitHub Actions

项目包含以下自动化工作流：

| 工作流 | 触发条件 | 功能 |
|--------|----------|------|
| **CI** | push 到 main 分支 | 验证 JSON 格式 |
| **Generate README** | data/software.json 变更 | 自动更新文档 |
| **Update Stars** | 每周日 00:00 | 更新 Stars 数量 |

## 📊 软件分类

| 分类 | 图标 | 描述 |
|------|------|------|
| 播放器 | 🎬 | 视频和音频播放软件 |
| 文件传输 | 📡 | 文件分享和传输工具 |
| 文件管理 | 📁 | 文件压缩、重命名等 |
| 开发工具 | 💻 | 程序员必备开发软件 |
| 效率工具 | ⚡ | 提升工作效率的神器 |
| 音视频处理 | 🎥 | 视频录制、直播软件 |
| 数据分析 | 📊 | 数据处理和分析工具 |
| Markdown | 📝 | Markdown 编辑器 |
| 系统工具 | ⚙️ | 系统优化和管理工具 |
| 设计工具 | 🎨 | 设计和美化工具 |
| 图像处理 | 🖼️ | 图片编辑和压缩工具 |
| 截图工具 | 📸 | 截图和 OCR 工具 |
| 浏览器 | 🌐 | 网页浏览器 |
| 趣味工具 | 🎮 | 桌面宠物和娱乐工具 |

## 🏷️ 标签体系

### 平台标签
- `#macOS` - Apple macOS 系统
- `#Windows` - Microsoft Windows 系统
- `#Linux` - Linux 发行版
- `#Android` - Android 系统
- `#iOS` - Apple iOS 系统

### 类型标签
- `#开源软件` - 开源项目
- `#免费软件` - 完全免费
- `#付费软件` - 需要付费
- `#跨平台` - 支持多个平台

## 📄 许可证

MIT License

## ⭐ 统计

![GitHub stars](https://img.shields.io/github/stars/zohn/Awesome-Softwares?style=social)
![GitHub forks](https://img.shields.io/github/forks/zohn/Awesome-Softwares?style=social)

---

**提示**: 如需了解如何贡献代码，请查看 [CONTRIBUTING.md](CONTRIBUTING.md)
