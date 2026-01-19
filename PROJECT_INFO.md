# 📁 项目结构说明

> 本文档说明 Awesome-Softwares 项目的技术架构和目录结构。

## 📂 目录结构

```
awesome-softwares/
├── 📄 index.html             # 🌐 交互式网页版本
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
│   ├── generate_html.py      # 生成带嵌入数据的 HTML 网页
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
   ├── scripts/generate_readme.py
   │         ↓
   │   README.md + README.zh.md (自动生成)
   │
   └── scripts/generate_html.py
             ↓
       index.html (嵌入数据网页)
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

### 3. 生成文档和网页

```bash
# 生成 README 文档
python3 scripts/generate_readme.py

# 生成 HTML 网页
python3 scripts/generate_html.py
```

## 📝 添加新软件

### 方法一：直接编辑 JSON（推荐）

```bash
# 1. 编辑数据文件
nano data/software.json

# 2. 运行生成脚本
python3 scripts/generate_readme.py
python3 scripts/generate_html.py
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
| **Generate README** | data/software.json 变更 | 自动更新 README 和 HTML |
| **Update Stars** | 每周日 00:00 | 更新 Stars 数量 |

## 📊 软件分类

当前共有 **13个分类**，涵盖40个软件：

| 分类 | 图标 | 描述 |
|------|------|------|
| 多媒体与音视频 | 🎥 | 视频、音频播放和处理软件 |
| 文件管理与传输 | 📁 | 文件传输、压缩和管理工具 |
| 网络工具与浏览器 | 🌐 | 浏览器、下载器、FTP/SFTP、网络工具、RSS、协作 |
| 系统工具与优化 | ⚙️ | 系统监控、剪贴板、输入法、菜单栏工具、美化、资源管理 |
| 开发与编程 | 💻 | 编辑器、终端、IDE、数据库管理、接口调试、开发辅助 |
| 办公与生产力 | ⚡ | 办公套件、启动器、桌面搜索、效率工具、自动化、日历、待办、流程图、PDF、截图工具 |
| 笔记、知识与写作管理 | 📝 | 笔记、知识库、个人Wiki、大纲、写作、Markdown笔记 |
| 设计与图像处理 | 🎨 | 图像处理、原型设计、矢量/位图编辑、图标、UI设计 |
| 远程协作与通讯 | 🖥️ | 远程桌面、协作、终端控制、会议、团队通讯 |
| 娱乐与趣味 | 🎮 | 桌宠、小游戏、趣味工具、虚拟宠物 |
| 人工智能与机器学习 | 🤖 | AI助手、代码生成、数据分析、机器学习工具 |
| 安全与隐私 | 🔒 | 密码管理、加密工具、安全扫描、隐私保护 |
| 云计算与基础设施 | ☁️ | 云服务管理、容器化、DevOps工具、基础设施即代码 |

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

- **软件数量**: 40个开源软件
- **分类数量**: 13个主要分类
- **支持平台**: macOS, Windows, Linux, Android, iOS, Web

![GitHub stars](https://img.shields.io/github/stars/zohn/Awesome-Softwares?style=social)
![GitHub forks](https://img.shields.io/github/forks/zohn/Awesome-Softwares?style=social)

---

**提示**: 如需了解如何贡献代码，请查看 [CONTRIBUTING.md](CONTRIBUTING.md)
