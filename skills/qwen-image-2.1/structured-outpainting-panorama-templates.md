# Qwen Image 2.1｜扩图与全景结构化提示词资料

> 状态：候选模板资料 v0.2；不构成正式 Skill、不进入生产路由。  
> 记录日期：2026-09-28  
> 来源区分：**官方规则**来自 `official/system_prompt_edit.txt`；**英文模板**是从 [daily-prompt-tests.md](./daily-prompt-tests.md) 中本人的候选/有效记录抽取变量后形成，不是官方逐字提示词。  
> 保留原始实验提示词全文，以便后续同图同 Seed 对比；本页只放复用模板及替换字典。

## 一、官方规则定位（原文不改）

- [官方 PE-I2I：明确将画布向外延展的操作称为 outpainting，L49](./official/system_prompt_edit.txt#L49)
- [官方 PE-I2I：Outpainting 扩图方向、比例与 30%–50% 估计，L136–146](./official/system_prompt_edit.txt#L136-L146)
- [官方 PE-I2I：Panoramic generation，L148–157](./official/system_prompt_edit.txt#L148-L157)
- [官方 PE-I2I：`wh_ratio` 与 `ratio_follow` 的互斥规则，L63–65](./official/system_prompt_edit.txt#L63-L65)

注意：官方提供的是**操作、方向、比例规则**，不是下面的完整英文模板；下列模板由个人提示词实验归纳，不能标记为官方原文。

## 二、OUTPAINT-BASE-v1｜通用方向扩图母句

**原始基准：** [B06-03b｜向左扩图（长版）](./daily-prompt-tests.md#b06-03b-向左扩图长版对照测试)。下面只将原句中与方向有关的两处词组变量化，其余保持原句原样。

```text
Outpaint the image {DIRECTION_PHRASE}. Extend the existing scene naturally into the newly added area {AREA_PHRASE}, completing the surrounding environment and spatial structure. Preserve the original image content, object placement, materials, colors, and lighting, and keep all untargeted content unchanged. Ensure seamless continuity in perspective, scale, and environmental illumination.
```

**替换字典（只替换这两处变量）：**

| 任务 | DIRECTION_PHRASE | AREA_PHRASE | 未明确指定比例时的官方比例处理 |
| --- | --- | --- | --- |
| 仅向左 | `toward the left` | `on the left` | 变宽 |
| 仅向右 | `toward the right` | `on the right` | 变宽 |
| 左右同时 | `to the left and right` | `on both sides` | 更大幅度变宽 |
| 仅向上 | `upward` | `at the top` | 变高 |
| 仅向下 | `downward` | `at the bottom` | 变高 |
| 上下同时 | `upward and downward` | `at the top and bottom` | 更大幅度变高 |
| 向四周 | `in all directions` | `on all sides` | 保持原宽高比，同时扩大实际画布 |

**母句恢复为左侧基准时应完全等于：**

```text
Outpaint the image toward the left. Extend the existing scene naturally into the newly added area on the left, completing the surrounding environment and spatial structure. Preserve the original image content, object placement, materials, colors, and lighting, and keep all untargeted content unchanged. Ensure seamless continuity in perspective, scale, and environmental illumination.
```

> 研究注意：向四周扩图时，不能只“保持原比例”而不增加实际宽高；单侧扩图也不能假设仅修改输出比例就能像素级锁定原图位置。提示词方向与底层画布定位要分别测试。

### 官方给出的比例示例（未指定目标比例的情况）

| 原始比例 | 扩图方向 | 官方示例输出比例 |
| --- | --- | --- |
| 1:1 | 左或右 | 3:2 |
| 3:4 | 左或右 | 1:1 / 4:3 |
| 1:1 | 左右 | 16:9 / 2:1 |
| 1:1 | 上或下 | 2:3 |
| 16:9 | 上或下 | 4:3 / 1:1 |
| 1:1 | 上下 | 9:16 |
| 任意 | 四周 | 原始比例（画布均匀扩大） |

若用户明确指定目标比例，以其指定值为准。官方在未指定扩展幅度时，用指定方向增加约 30%–50% 空间作为一般估计，不是固定的工作流输出尺寸。

## 三、PANORAMA-BASE-v1｜普通全景 / 超宽全景

**原始候选来源：** [B06-01 普通全景短版](./daily-prompt-tests.md#b06-01-普通全景图短版) 与 [B06-02 超宽全景](./daily-prompt-tests.md#b06-02-超宽全景待单独复测)。本节是便于统一替换的**新候选结构**，不等于两条原始提示词逐字相同，实际效果需要与原版对照。

```text
Generate a {PANORAMA_STYLE} version of this scene. Expand the environment into a coherent {PANORAMA_WIDTH} panorama while preserving the core scene content, lighting atmosphere, materials, and overall visual style.
```

| 类型 | PANORAMA_STYLE | PANORAMA_WIDTH | 官方 wh_ratio |
| --- | --- | --- | --- |
| 标准全景 | `panoramic` | `full` | `2:1` |
| 超宽全景 | `ultra-wide panoramic` | `ultra-wide` | `3:1` |

**标准全景代入后**与既有 B06-01 原文完全一致：

```text
Generate a panoramic version of this scene. Expand the environment into a coherent full panorama while preserving the core scene content, lighting atmosphere, materials, and overall visual style.
```

超宽代入版需与 B06-02 原始长句用相同输入图和参数作 A/B 测试，不能先假定它比原版更好。

## 四、PANORAMIC-OUTPAINT-BASE-v1｜既有画面的左右全景扩图

普通全景生成与全景扩图在研究档案中保留为**两项不同任务**：
- `Generate a panoramic version`：从原场景概念生成宽幅全景版，可能重新安排原有构图。
- `Perform panoramic outpainting`：强调向原画面两侧增加区域、尽量保留原中心内容。

**原始来源：** [B06-05 商业摄影全景扩图（详细版）](./daily-prompt-tests.md#b06-05-全景扩图商业摄影详细版)。

```text
Perform panoramic outpainting by extending the original scene {EXTENSION_SCOPE}, completing the surrounding environment into a coherent {PANORAMA_WIDTH} panoramic composition. Preserve the original central image, object placement, materials, colors, and lighting structure. Extend the environment according to the existing spatial logic, perspective, and soft ambient illumination. Do not introduce additional window beams, light spots, clutter, or unrelated objects. Create a clean, realistic, seamless panoramic view of the same commercial photography environment.
```

| 类型 | EXTENSION_SCOPE | PANORAMA_WIDTH | 官方 wh_ratio |
| --- | --- | --- | --- |
| 标准全景扩图 | `widely to both the left and right` | `wide` | `2:1` |
| 超宽全景扩图（待测试） | `farther to both the left and right` | `ultra-wide` | `3:1` |

标准全景扩图代入后恢复既有 B06-05 原文；超宽版仅为结构化候选，**尚无单独样本证明**。这段包含商业场景特定的禁新增窗光和光斑限制，不适合不加判断地复制到所有题材。

## 五、PANORAMA-360｜官方第三类：360° / VR panorama

官方在 [Panoramic generation 章节 L148–157](./official/system_prompt_edit.txt#L148-L157) 将全景分为三种，研究档案应全部保留：

| 官方类型名称 | 官方 `wh_ratio` | 目前记录方式 |
| --- | --- | --- |
| `Standard panorama / 全景` | `2:1` | B06-01 原句 + 结构化候选 |
| `Wide panorama / 超宽全景` | `3:1` | B06-02 原句 + 结构化候选 |
| `360° / VR panorama` | `2:1` | 独立待验证候选；不可直接与普通全景合并 |

### 为什么第三类不能只替换全景宽度？

360° / VR 的 `2:1` 与普通全景 `2:1` 相同，但任务并不相同。对于希望用于 3D 场景环绕的结果，除了宽高比，通常还需要说明球面等距柱状投影（equirectangular）、环绕连续性与左右边缘衔接。**官方系统提示词在这一段只规定比例，并未提供这些几何属性的逐字成品提示词，也没有保证模型能稳定生成可用的 360° 环境贴图。**

### PANORAMA-360-CANDIDATE-v1（个人新拟，未实测，非官方提示词）

该实验候选独立于已有 B06 普通全景结构，**不标注“有效模板”**，仅为后续对照试验存档：

```text
Generate a 360-degree equirectangular panorama of the existing environment. Extend the visible scene into a coherent full-surround view, completing the unseen surroundings consistently with the original spatial structure, materials, colors, and lighting. Maintain a continuous environment around the entire horizontal field of view, with seamless continuity between the left and right edges.
```

| 测试变量 | 作用 | 暂定值 |
| --- | --- | --- |
| `PANORAMA_PROJECTION` | 目标全景投影 | `360-degree equirectangular panorama` |
| `PANORAMA_COVERAGE` | 场景补全范围 | `full-surround view` |
| `EDGE_CONTINUITY` | 边缘连续性 | `seamless continuity between the left and right edges` |
| 官方 `wh_ratio` | 画面比例 | `2:1` |

需额外验证：左右接缝、上下极区畸变、完整 360° 环绕、场景结构真实度。普通单张照片无法提供背后空间的真实证据，新增区域只能由模型推断；不能把 2:1 输出或生成成功直接认定为合格 HDRI。这里记录的是 LDR 图像生成候选，不代表自动得到 HDR 格式。

## 六、ComfyUI 参数与提示词分离记录

| 变量 / 控制 | 作用 |
| --- | --- |
| `DIRECTION_PHRASE` / `AREA_PHRASE` | 表达扩图方向与新增区域 |
| `PANORAMA_STYLE` / `PANORAMA_WIDTH` | 表达全景类型 |
| 官方 PE `wh_ratio` | 语义层的目标比例 |
| 官方 PE `ratio_follow` | 跟随某一参考图；扩图和全景明确选目标比例时为空 |
| ComfyUI `custom_size / width / height` | 实际生成画布；需把目标比例和需要增加的面积落实到像素尺寸 |

**后续比对：** 同图、同 Seed、同 Steps、同宽高，对比原始长句与结构化派生句；记录商品与场景保持、方向准确、透视、光影连续性。不要因为模板可复用就把所有派生方向自动标记为“实测成功”。
