# 📝 Article Gen — 公众号文章生成器

一个 Claude Code 技能（Skill），让你通过一句话指令自动生成公众号文章。

支持任意类目（情感/科技/职场/育儿/美食/故事...），自定义字数和风格。

## ✨ 功能

- ✍️ 自动生成文章（4种风格可选）
- ✅ 自动合规审查（避免限流）
- 🏷️ 自动生成爆款标题
- 🎨 自动 HTML 排版（适配公众号）
- 🖼️ 自动配图（Unsplash 免费商用）
- 🔍 可选：自动抓取小红书/知乎素材（需额外安装）

## 📦 安装

### 基础安装（零依赖，推荐）

只需要 Claude Code，不需要安装任何额外工具：

```bash
# 1. 克隆本仓库
git clone https://github.com/sun162957-glitch/article-gen.git

# 2. 复制技能文件到 Claude Code 技能目录
# Windows
copy article-gen\skills\gen-article.md %USERPROFILE%\.claude\skills\

# macOS/Linux
# cp article-gen/skills/gen-article.md ~/.claude/skills/
```

完成！现在可以直接使用了。

### 高级安装（可选，支持爬虫抓取）

如果需要从真实平台（小红书/知乎）抓取素材：

```bash
# 1. 克隆 ForgeRSS（素材抓取工具）
git clone https://github.com/tmwgsicp/ForgeRSS.git
cd ForgeRSS

# 2. 安装依赖
python -m venv venv
venv\Scripts\pip install -r requirements.txt   # Windows
# venv/bin/pip install -r requirements.txt     # macOS/Linux

# 3. 登录平台（首次需要扫码）
venv\Scripts\python.exe -m generators.social.xiaohongshu.scraper --login  # 小红书
venv\Scripts\python.exe -m generators.social.zhihu.scraper --login         # 知乎
```

## 🚀 使用方法

### 快捷指令

```
/gen-article 情感 300字 倾诉型
/gen-article 科技 500字 干货型
/gen-article 职场 800字 观点型
/gen-article 故事 600字 故事型
```

### 交互模式

```
/gen-article
```

然后 Claude 会问你：
- 写什么类目？
- 多少字？
- 什么风格？
- 素材来源？（AI生成 / 爬虫抓取）

## 📋 支持的参数

| 参数 | 可选值 |
|------|--------|
| **类目** | 情感、科技、职场、育儿、美食、故事、生活、财经、健康、教育... |
| **字数** | 任意数字（如 300、500、800、1000） |
| **风格** | 倾诉型、故事型、干货型、观点型 |
| **素材** | AI生成（默认）、爬虫抓取（需安装ForgeRSS） |

## 🎨 四种文章风格

### 倾诉型（情感号常用）
- 第一人称"我"，口语化
- 有具体场景、对话、细节
- 短段落，手机阅读友好

### 故事型（故事号常用）
- 完整故事线：起因→经过→高潮→结局
- 有人物、事件、冲突
- 有转折或反转

### 干货型（知识号常用）
- 条理清晰，分点论述
- 有数据、案例支撑
- 实用性强

### 观点型（评论号常用）
- 有明确立场
- 有论据支撑
- 结尾抛出问题引发讨论

## 📁 输出结构

```
output/
├── images/
│   ├── 文章标题1.jpg
│   └── 文章标题2.jpg
├── 文章标题1.html
├── 文章标题1.txt
├── 文章标题2.html
└── 文章标题2.txt
```

## ⚠️ 注意事项

1. **基础模式**（AI生成）不需要安装任何工具，开箱即用
2. **爬虫模式**需要安装 ForgeRSS，且首次需要扫码登录
3. 爬虫模式的登录态会过期，过期后需要重新扫码
4. 素材仅供创作参考，请确保最终内容的原创性
5. 发布前请再次检查内容是否符合平台规范

## 🛠️ 自定义

### 修改排版样式

编辑 `skills/gen-article.md` 中的 HTML 排版规范部分。

### 修改合规规则

编辑 `skills/gen-article.md` 中的合规审查部分。

### 修改搜索关键词

编辑 `skills/gen-article.md` 中的关键词表格。

## 📄 License

MIT License

## 🙏 致谢

- [ForgeRSS](https://github.com/tmwgsicp/ForgeRSS) — 素材抓取工具（可选）
- [Unsplash](https://unsplash.com) — 免费商用图片
- [Claude Code](https://claude.ai/code) — AI 编程助手
