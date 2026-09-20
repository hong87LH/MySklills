# AI 电商服装生图 SOP｜版本更新记录

> 存放目录：`sop/`。稳定入口：`sop/index.html`。不可改写已发布的 `sop/versions/` 历史快照。

## v0.4.1 · 2026-09-20｜提示词文本可读性修复

- 修复修复工具箱的深色代码框中，通用 `code` 标签浅色背景覆盖父级深色背景，导致浅色文字不明显的问题。
- 为 `.prompt-box pre code` 显式设置透明背景、浅色文字、字号与行距；打印时调整为白底深色字，兼容打印或存 PDF。
- 保持完整 SOP 内容、七条提示词、修复工具箱、八阶段流程和交互验收清单。
- **稳定入口：** [index.html](./index.html)
- **版本快照：** [ecom-image-sop-v0.4.1.html](./versions/ecom-image-sop-v0.4.1.html)
- **Git Blob SHA：** `bfc291b9a94729fd3135586ac8b9f15596c495ba`

## v0.4.0 · 2026-09-20｜修复工具箱提示词增强版

- 在日常 SOP 上增加七组常用修复提示词：降噪、马赛克人脸高清修复、GPT Image 2.5 均匀肤色、Nano Banana 3.1 Flash 缝线修复（两种）、GPT Image 2.5 印花比例修复、相机视角 Orbit 视差调整。
- 保留新款种子图流程、旧品快速翻单、场景母图、姿势裂变、商品工艺/色彩/面部修复和导出归档内容。
- **版本快照：** [ecom-image-sop-v0.4.0.html](./versions/ecom-image-sop-v0.4.0.html)
- **Git Blob SHA：** `222b50c1411aa566920d65310e07ac543756cc72`

## 如何回退

1. 在 `sop/versions/` 选择目标版本快照；
2. 将快照的**完整文本内容**恢复到 `sop/index.html`；
3. 记录回退原因、目标版本和 Commit SHA 于本日志；
4. 不要覆盖历史快照；不需要改动 `skills/` 目录。
