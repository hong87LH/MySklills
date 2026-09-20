# AI 电商服装生图｜日常生产 SOP

此目录独立维护电商生图日常 SOP，与 `skills/` 下的 Ecom Image Prompt Director 分开管理。

## 版本规则

- 每个发布版按实际交付形态保留 HTML / Markdown 快照：`sop/versions/ecom-image-sop-vX.Y.Z.html` 与 `sop/versions/ecom-image-sop-vX.Y.Z.md`；发布后不覆盖历史版本。
- `sop/index.html`（交互版）与 `sop/index.md`（静态阅读版）为当前稳定入口，后续发布时与对应版本快照同步更新。
- `sop/CHANGELOG.md` 记录版本差异、时间、修复原因及对应快照。
- 回退时将指定版本快照的完整内容复制回相应的 `sop/index.html` / `sop/index.md`；旧版仍保留，Git 提交历史可追溯。

## 最新版本

**v0.4.1**：修复“异常修复与商业精修工具箱”提示词代码框文字不清晰的问题；深色提示词块使用高对比度浅色文字，打印时采用白底深字。保留 v0.4 的全部 SOP 主流程及七条常用提示词。

## 手册入口

- **[当前交互版 HTML（v0.4.1）](./index.html)**：离线页面，含勾选与章节交互。
- **[当前阅读版 Markdown（v0.4.1）](./index.md)**：适合 GitHub 直接阅读、编辑和复制提示词。
- **[v0.4.1 Markdown 完整快照](./versions/ecom-image-sop-v0.4.1.md)**：与 HTML 同步的 SOP 内容，静态清单无本地持久化。
- **[v0.4.1 完整快照](./versions/ecom-image-sop-v0.4.1.html)**：修复提示词文字可读性，正常打印也使用高对比度文字。
- **[v0.4.0 完整快照](./versions/ecom-image-sop-v0.4.0.html)**：修复前版本，完整保留，便于回退或比对。
- **[更新日志](./CHANGELOG.md)**：记录变更。

**一致性核验：**`index.html` 与 v0.4.1 版本快照是同一份内容，Git Blob SHA 均为 `bfc291b9a94729fd3135586ac8b9f15596c495ba`。v0.4.0 SHA 为 `222b50c1411aa566920d65310e07ac543756cc72`。`index.md` 与 v0.4.1 Markdown 快照亦为相同 Git Blob：`815688428b35b44877dbdce2720f4edc52cf658c`。

GitHub 的 `blob` 页面默认展示 HTML 源码；阅读或运行交互功能时请打开 `Raw` 并保存为 .html，在浏览器中打开。