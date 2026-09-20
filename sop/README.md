# AI 电商服装生图｜日常生产 SOP

此目录独立维护电商生图日常 SOP，与 `skills/` 下的 Ecom Image Prompt Director 分开管理。

## 版本规则

- 每个发布版保留独立 HTML 快照：`sop/versions/ecom-image-sop-vX.Y.Z.html`，发布后不覆盖历史版本。
- `sop/index.html` 为当前稳定版副本，后续发布时与版本快照同步更新。
- `sop/CHANGELOG.md` 记录版本差异、时间、修复原因及对应快照。
- 回退时将指定版本快照的完整内容复制回 `sop/index.html`；旧版仍保留，Git 提交历史可追溯。

## 最新版本

**v0.4.1**：修复“异常修复与商业精修工具箱”提示词代码框文字不清晰的问题；深色提示词块使用高对比度浅色文字，打印时采用白底深字。保留 v0.4 的全部 SOP 主流程及七条常用提示词。

> 注：手册 HTML 发布后，`sop/index.html` 与 `sop/versions/ecom-image-sop-v0.4.1.html` 应保持内容一致。