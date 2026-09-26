# Qwen Image 2.1｜提示词实测档案

> 阶段：研究 / 日常记录（非正式 Skill；不自动进入生产路由）  
> 建档日期：2026-09-26  
> 目标：先积累高频电商任务与实际生成样本，再与 Qwen 官方规则及官方案例交叉比对，最后决定是否凝练成正式 Skill。

## 文件索引

| 文件 | 用途 |
| --- | --- |
| [daily-prompt-tests.md](./daily-prompt-tests.md) | 日常有效提示词、测试状态、ComfyUI 参数与待验证任务 |
| [official/system_prompt_edit.txt](./official/system_prompt_edit.txt) | Qwen Image 2.1 官方 PE-I2I 系统提示词，原文留存 |
| [official/system_prompt_t2i.txt](./official/system_prompt_t2i.txt) | Qwen Image 2.1 官方 PE-T2I 系统提示词，原文留存 |
| [official/LICENSE](./official/LICENSE) | 官方材料的原始许可协议 |
| [official/NOTICE](./official/NOTICE) | 原始归属声明 |

## 本阶段研究方法

1. 用相同输入图、Seed、Steps、画布规格，对比**简短原始提示词 / 日常有效提示词 / 官方 PE 输出 / 未来 Skill 版本**。
2. 优先看：主体与商品不漂移、真实机位变化、空间结构连续、区域光影一致、扩图方向准确。
3. 记录失败例与生成结果链接；一个案例成功不等于已证明可普遍复用。
4. UI 参数与提示词分开：比例必须落到 ComfyUI 的 `custom_size / width / height`；仅写在 prompt 里不能保证生成画幅。
5. 本文件夹不包含正式 `SKILL.md`，不修改已有 `skills/ecom-image-prompt-director/` 的生产版本。

## 官方源文件信息

来源：[QwenLM/Qwen-Image-2.1 / prompt_rewrite](https://github.com/QwenLM/Qwen-Image-2.1/tree/main/prompt_rewrite)

- [PE-I2I 官方原文](https://github.com/QwenLM/Qwen-Image-2.1/blob/main/prompt_rewrite/prompts/system_prompt_edit.txt)
- [PE-T2I 官方原文](https://github.com/QwenLM/Qwen-Image-2.1/blob/main/prompt_rewrite/prompts/system_prompt_t2i.txt)
- [官方模型说明](https://github.com/QwenLM/Qwen-Image-2.1/blob/main/README.md)

两份 `official/*.txt` 保持原文，日常改写及英文输出偏好放在自己的测试档案里，不修改官方文件冒充原文。

**授权提示：** 官方仓库使用 Qwen RESEARCH LICENSE AGREEMENT，原文及派生材料的复制、分发和使用受许可条款约束；本目录为研究和评估归档，不表示获得商业使用授权。请阅读 `official/LICENSE` 和 `official/NOTICE`，后续用于公司生产工具前先核实授权范围。
