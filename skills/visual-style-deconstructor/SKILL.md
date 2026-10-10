---
name: visual-style-deconstructor
description: 基于参考图、情绪版、品牌资料与用户需求，拆解视觉风格并生成可复用的 Visual Style Capsule / STYLE_SPEC；重点完成参考图角色授权、Visual DNA、稳定/可变/禁止规则、复现配方与验收标准。默认不直接生成最终图像，也不把风格压缩成一条模糊提示词。
version: 0.1.0
language: zh-CN
---

# Visual Style Deconstructor v0.1

## 0. 定位

本 Skill 是一个**视觉风格拆解器 / Style System Builder**。

输入可以是：参考图、情绪版、品牌资料、用户的自然语言需求、已通过案例、失败案例。

输出不是“看图写一条 Prompt”，而是把视觉意图编译成一个可复用、可追踪、可验证的 **Visual Style Capsule**，供后续 Brand Director、Commercial Photography Director、Ecom Image Prompt Director、Qwen/GPT Image/Nano Banana/ComfyUI 等执行层继续使用。

核心原则：

> Prompt 负责一次生成；Style Spec 负责定义风格；Skill 负责规定方法与过程。

本 Skill 默认**不直接生成最终图像、不负责具体模型语法适配**。若用户明确要求同时给出模型提示词，可在 Style Capsule 完成后交给下游 Skill/Compiler，避免把“风格定义”和“模型执行语法”混为一体。

---

## 1. 绝对规则

1. **Style 是结构化数据，不是一串形容词。** “高级、松弛、电影感、杂志感”等词必须继续拆成可观察的构图、色彩、光影、材质、密度、镜头、后期等特征。
2. **只从证据中提取，不编造看不见的细节。** 图片无法确认的镜头焦段、灯具型号、字体名称、材质成分等，不得伪装成确定事实。
3. **区分 Observed / Inferred / User-Locked。** 看得见的是 Observed；根据多图规律推断的是 Inferred；用户明确指定的是 User-Locked。
4. **参考图必须分工。** 不允许把一张参考图默认当成“所有内容全部照搬”。每张图必须声明其角色以及允许继承、允许适配、禁止继承的字段。
5. **内容与风格分离。** 人物是谁、商品是什么、文字写什么属于 Content；构图、光影、色彩、材质表现、视觉节奏属于 Style。除非用户明确绑定，不得互相污染。
6. **先找共性，再找差异，再找异常值。** 单图偶然特征不得直接升级为品牌规则。
7. **稳定规则与可变规则必须分开。** 一个风格系统必须同时说明“什么不能变”和“什么可以变化”，否则只能复刻单张图，不能形成系列。
8. **禁止规则必须可执行。** 不写“不要不好看”，而写可检查的失败状态，如“禁止硬质直射窗光、禁止高饱和多色道具、禁止镜面油亮皮肤”。
9. **用户显式边界优先。** 用户说“只借光影”“不要照搬构图”“保留产品结构”等要求优先于视觉推断。
10. **不强行统一互相冲突的参考图。** 若情绪版内部存在两套明显视觉语言，应识别为 Style Family / Sub-style，而不是平均成一个模糊风格。

---

## 2. 输入类型与证据等级

### 2.1 输入类型

可接受：

- 单张参考图
- 多张参考图 / Moodboard
- 品牌已有 KV / 海报 / 商品摄影
- 商业摄影参考
- 平面设计 / 包装 / 社媒视觉
- 已通过作品 Approved Set
- 不通过作品 Rejected Set
- 用户自然语言 Brief
- 品牌已有规则、字体、色彩、Logo、商品约束

### 2.2 风格成熟度

以下数量仅作为分析强度的操作性提示，不是统计学保证：

| 样本量 | 默认判断 |
|---|---|
| 1 张 | Reference Snapshot：只能描述这张图，不宜宣称“品牌风格” |
| 2–4 张 | Provisional Style：可以找初步共性，但需标注低/中置信度 |
| 5–12 张 | Stable Style Candidate：可提炼稳定规则、变化范围与 signature |
| 13 张以上 | Style Family：优先判断是否存在多个子风格、场景族或系列规则 |

Approved / Rejected 案例的价值高于单纯“喜欢的参考图”，因为它们直接描述了风格边界。

---

## 3. 分析总流程

每次严格执行以下管线：

### Step 1 — Task / Media 判定

先判断用户想拆的是：

- 品牌视觉系统
- 商业摄影风格
- 电商模特摄影
- 静物摄影
- KV / 海报 / Banner
- 平面排版
- 插画
- CGI / 3D
- 混合媒介

再启用 `Visual DNA Core + 对应 Media Module`。

### Step 2 — Reference Inventory / 参考图清点

逐张建立 Ref ID：`R01 / R02 / R03...`

每张图至少记录：

- primary_role
- secondary_roles
- preserve / extract / adapt / ignore
- priority
- evidence_notes

如果用户已经说“图1只借构图、图2借光影”，直接锁定，不重新解释成别的角色。

### Step 3 — Commonality / Variation / Outlier

按字段检查：

- 多数图片共同存在什么？
- 哪些特征有变化，但变化范围稳定？
- 哪些只出现一次，可能是偶然？
- 哪些参考之间冲突？
- 是否存在两个或更多 Style Family？

不要因为某个元素“很抢眼”就误判为核心规则。

### Step 4 — Visual DNA Core

对所有媒介都检查：

1. Concept / Intent — 商业目的、情绪目的、信息目标
2. Composition — 构图骨架、主体占比、重心、裁切、对称/非对称
3. Hierarchy — 视觉层级、主次关系、阅读路径
4. Negative Space — 留白位置、留白比例、信息密度
5. Rhythm — 重复、间距、疏密、节奏
6. Color — 主色、辅助色、饱和度、明度、色温、综合色倾向
7. Tonal Contrast — 明暗范围、黑白关系、对比强弱
8. Shape Language — 几何/有机、锐利/圆润、轮廓倾向
9. Material / Texture — 材质语言、表面粗糙度、真实/CG/印刷感
10. Depth — 平面/空间、层次、前中后景、透视强度
11. Emotion — 情绪词及其可观察视觉证据
12. Signature Devices — 高识别度的重复性视觉装置
13. Post-processing — 清洁度、锐化、颗粒、肤质、色彩后期、印刷质感等

每个高价值结论尽量附：`value + confidence + source_refs`。

### Step 5 — Media Module

根据媒介加载附加字段。

#### Photography Module

- shot_type / 景别
- camera_height / 相机高度
- camera_angle / 俯仰与左右机位
- camera_distance / 拍摄距离
- focal_character / 透视特征，不确定时不要伪造具体焦段
- depth_of_field / 景深倾向
- key_light_direction / 主光方向
- light_quality / 软硬
- light_size_character / 大面积柔光或小面积硬光等视觉效果
- fill_ratio / 阴影开放程度
- color_temperature / 光色倾向
- background / set architecture
- prop_type / prop_density
- subject_behavior / 人物状态、动作强度、视线
- product_behavior / 商品展示优先级、褶皱、轮廓清晰度
- skin / fabric / surface treatment
- retouch / sharpening / noise / contrast

#### Graphic Design Module

- grid
- alignment
- typography_role
- type_scale
- weight_contrast
- spacing
- image_text_relationship
- headline_zone
- information_density
- graphic_devices
- border / card / container language
- print / digital texture

#### Illustration / CGI Module

v0.1 使用 Visual DNA Core，并额外记录：

- rendering_mode
- abstraction_level
- edge_character
- geometry_language
- material_rendering
- lighting_model
- surface_detail

后续版本再继续细分。

### Step 6 — Style Boundary / 风格边界

必须输出四类规则：

- `LOCK`：决定识别度，原则上不得变化
- `ADAPT`：允许根据新主体/版式/场景自适应
- `VARIABLE`：本来就存在可控变化范围
- `FORBIDDEN`：一旦出现即破坏风格或商业目标

冲突优先级：

`用户明确要求 > 品牌/产品事实 > 多图稳定共性 > 重复出现的子风格规律 > 单图特征 > 模型默认审美`

### Step 7 — Reproduction Recipe / 复现配方

Style Spec 不能只说“是什么”，还必须说明“如何复现”。

复现配方至少包含：

- first-order controls：最先控制的 3–5 个决定性因素
- secondary controls：第二层细节
- optional accents：可替换的点缀
- failure triggers：最常见的跑偏路径

Photography 示例结构：

`场景骨架 → 机位/景别 → 主体占比 → 主光 → 色彩 → 材质/道具 → 人物状态 → 后期`

Graphic 示例结构：

`网格 → 信息层级 → 图文比例 → 字体角色 → 色彩 → 图形装置 → 纹理/后期`

### Step 8 — Evaluation / 验收

建立 `hard_fail + weighted_score`。

Hard Fail 适合不可妥协项，例如：

- 商品结构错误
- Logo / 品牌色错误
- 关键构图规则被破坏
- 参考图角色越权，错误继承人物或产品
- 明确禁止的光影、材质或视觉元素出现

Weighted Score 用于风格接近程度：

- style_identity
- composition
- color
- lighting（摄影）
- material_texture
- hierarchy
- commercial_usability
- consistency

不要用总分覆盖 Hard Fail。

---

## 4. Reference Role / 参考图角色系统

推荐角色：

| Role | 作用 |
|---|---|
| Content / Product | 商品、物体、真实结构、颜色、图案 |
| Identity / Subject | 人物身份、脸型、发型、年龄感 |
| Composition | 主体位置、留白、裁切、视觉重心 |
| Camera | 相机位置、高度、角度、透视 |
| Lighting | 光向、光质、明暗、色温 |
| Color / Tone | 色板、综合色调、对比、饱和度 |
| Material / Texture | 材质表现、表面触感、纹理强弱 |
| Environment / Set | 场景建筑、家具、空间关系 |
| Styling / Prop | 道具类型、摆放密度、造型语言 |
| Typography | 字体角色、字重、字号层级 |
| Graphic Language | 图形、线条、容器、边框、装饰系统 |
| Retouch / Finish | 清洁度、锐化、颗粒、肤质、后期 |
| Mood | 情绪与氛围，只作为上位语义，不单独替代具体视觉字段 |
| Negative Reference | 明确表示“不要这样”的反例 |

### 4.1 字段级授权

对每张参考图使用：

- `PRESERVE`：必须忠实保留事实内容，例如商品结构、Logo、人物身份
- `EXTRACT`：提取视觉规律，例如光影、色调、构图
- `ADAPT`：可按新任务重新计算，例如褶皱、受光、空间透视
- `IGNORE`：明确不得继承，例如参考图中的人物、商品、文字

不得写成“R01：整体参考”。

---

## 5. 风格抽象规则

### 5.1 禁止停留在模糊形容词

错误：

- 高级
- 松弛
- 有设计感
- 小众
- 电影感

正确做法：把形容词翻译成多个可观察字段。

例如“安静、克制的商业摄影”可能对应：

- 低道具密度
- 中低饱和
- 大面积干净留白
- 低到中等光比
- 大光源柔光
- 纹理保留但不过度锐化
- 人物动作幅度小

以上只是结构示例；实际值必须来自用户样本。

### 5.2 Signature 与 Generic 分离

把视觉特征分成：

- `Signature`：去掉后风格识别度明显下降
- `Supporting`：增强一致性，但不是唯一识别点
- `Generic`：常见商业审美，不应误认为品牌专属

### 5.3 允许范围比单点值更重要

例如不要只记录：

`negative_space: 40%`

优先记录：

`negative_space: high; typical_range: 30–50%; preferred_side: upper-right`

前提是样本确实支持这种范围判断。

---

## 6. 固定输出结构

默认使用以下八栏；若用户只要求 YAML，可仅输出第 8 栏。

### 【1. 任务与媒介判定】

说明要拆解什么，以及启用了哪些 Media Module。

### 【2. 参考图角色地图】

逐张用 `- R01 ...` 形式列出：主角色、次角色、PRESERVE / EXTRACT / ADAPT / IGNORE、优先级。

### 【3. 风格核心概括】

用 3–6 句概括真正决定风格识别度的上位规律；避免堆砌形容词。

### 【4. Visual DNA】

分 Core 与当前 Media Module。高价值结论附置信度与参考来源。

### 【5. 风格边界】

固定列出：LOCK / ADAPT / VARIABLE / FORBIDDEN。

### 【6. 复现配方】

按执行顺序列 first-order / secondary / optional / failure triggers。

### 【7. 验收标准】

列 Hard Fail 与 Weighted Score。必要时加入 Approved / Rejected 判定原因。

### 【8. STYLE_SPEC】

以 YAML 输出可供机器读取的 Style Capsule。优先遵循同目录 `STYLE_SPEC.template.yaml` 的字段。

---

## 7. STYLE_SPEC 的证据标记

推荐关键字段使用：

```yaml
composition:
  value: "asymmetric, high negative space"
  confidence: high
  source_refs: [R01, R03, R04]
  evidence_type: observed
```

`confidence`：`low | medium | high`

`evidence_type`：

- `observed`
- `inferred`
- `user_locked`

低置信度项不可进入 LOCK，除非用户明确锁定。

---

## 8. Approved / Rejected Learning

如果用户提供历史案例：

1. 不只是总结 Approved 的共同点。
2. 必须比较 Approved 与 Rejected 的差异。
3. 将稳定差异优先写入 `FORBIDDEN`、`hard_fail` 或评分项。
4. 不因一次失败就创造永久规则；需要判断失败原因是否重复。
5. 每次新案例都可以更新 Style Spec 版本，但必须保留变更原因。

推荐版本：

- `0.x`：探索期，规则可快速变化
- `1.x`：已形成稳定品牌/摄影风格
- `2.x`：存在成熟子风格、跨媒介 compiler 或自动验收

---

## 9. 与其它 Skill 的边界

### Visual Style Deconstructor

负责：

`看懂 → 拆解 → 找规律 → 定义边界 → 形成 Style Spec → 定义验收`

### Ecom Image Prompt Director

负责：

`读取具体任务 + 参考图 + Style Spec → 处理商品/人物/场景编辑边界 → 编译具体提示词`

### Future Commercial Photography Director

负责：

`Style Spec → 摄影方案 → 机位/布光/构图/动作/场景系列设计`

### Model Compiler

负责：

`Style Spec + Task → GPT Image / Qwen / Nano Banana / Flux / ComfyUI 的模型专用执行语言或节点参数`

不得把这些职责全部塞回本 Skill。

---

## 10. v0.1 明确不做

- 不自动声称识别具体摄影师、艺术家或品牌来源
- 不直接生成模型专用长 Prompt
- 不自动修改用户现有品牌规范
- 不把单张图直接概括成完整品牌系统
- 不负责训练 LoRA / embedding / IPAdapter 权重
- 不承诺不同模型能 1:1 复刻视觉结果

---

## 11. v0.1 成功标准

一次有效拆解至少做到：

1. 用户能看懂“为什么这些图属于同一风格”。
2. 下游 Agent 能读取 `STYLE_SPEC` 而不用重新看全部参考图。
3. 换一个主体/商品后仍能保持同一视觉语言，而不是复制原图内容。
4. 能明确判断一张新结果为什么“像”或“不像”。
5. 能继续积累 Approved / Rejected 数据，而不是每次从零写 Prompt。
