# 微信公众号情感文章 Skill

这是一个面向公众号情感内容创作的可复用 Skill。它把读者投稿、树洞文字、聊天截图等素材，整理成有主题、有真人感、适合手机阅读的公众号文章。

## 主要能力

- 提取素材事实、人物关系和时间线
- 从案例中提炼单一情感主题
- 保留生活细节和口语感，减少 AI 痕迹
- 生成并检查钩子标题
- 检查隐私、版权、事实边界和平台风险
- 按中文语境处理阿拉伯数字与中文数字
- 输出适合微信公众号的手机端 HTML

## 文件位置

```text
skills/wechat-emotional-article/SKILL.md
```

## 安装

将 `skills/wechat-emotional-article` 文件夹复制到目标 Agent 的 skills 目录即可。例如 Codex（Windows）：

```text
C:\Users\你的用户名\.codex\skills\wechat-emotional-article\SKILL.md
```

也可以直接下载 [SKILL.md](skills/wechat-emotional-article/SKILL.md)，放入对应的 Skill 目录。

## 使用

直接向 Agent 发送素材，并说明需要生成微信公众号文章。默认流程为：

```text
提取素材 → 检查边界 → 确定主题 → 设计结构 → 写初稿 → 去 AI 味
→ 生成并检查钩子标题 → 内容风险检查 → 数字和字数复检
→ 手机端 HTML 排版 → 验证 → 输出文件
```

## 说明

Skill 会尽量降低隐私、版权和平台风险，但不能保证文章一定获得推荐或不会被限流。发布前请确认素材授权，并再次进行人工审核。

## License

MIT License

