# AI 电商服装生图｜日常生产 SOP

此目录独立维护电商生图日常 SOP，与 `skills/` 下的 Ecom Image Prompt Director 分开管理。

## 版本规则

- 每个发布版保留独立 HTML 快照：`sop/versions/ecom-image-sop-vX.Y.Z.html`，发布后不覆盖历史版本。
- `sop/index.html` 为当前稳定版副本，后续发布时与版本快照同步更新。
- `sop/CHANGELOG.md` 记录版本差异、时间、修复原因及对应快照。
- 回退时将指定版本快照的完整内容复制回 `sop/index.html`；旧版仍保留，Git 提交历史可追溯。

## 最新版本

**v0.4.1**：修复“异常修复与商业精修工具箱”提示词代码框文字不清晰的问题；深色提示词块使用高对比度浅色文字，打印时采用白底深字。保留 v0.4 的全部 SOP 主流程及七条常用提示词。

## 手册入口

- **[当前稳定版（v0.4.1）](./index.html)**：便于固定访问。
- **[v0.4.1 完整快照](./versions/ecom-image-sop-v0.4.1.html)**：修复提示词文字可读性，正常打印也使用高对比度文字。
- **[v0.4.0 完整快照](./versions/ecom-image-sop-v0.4.0.html)**：修复前版本，完整保留，便于回退或比对。
- **[更新日志](./CHANGELOG.md)**：记录变更。

**一致性核验：**`index.html` 与 v0.4.1 版本快照是同一份内容，Git Blob SHA 均为 `bfc291b9a94729fd3135586ac8b9f15596c495ba`。v0.4.0 SHA 为 `222b50c1411aa566920d65310e07ac543756cc72`。

GitHub 的 `blob` 页面默认展示 HTML 源码；阅读或运行交互功能时请打开 `Raw` 并保存为 .html，在浏览器中打开。