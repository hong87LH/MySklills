# Visual Style Deconstructor v0.1

把参考图、情绪版、品牌资料和历史案例，从“感觉像”拆成**可复用、可版本化、可验收的视觉风格系统**。

## 它解决什么问题

传统做法通常是：

`参考图 → 看图描述 → 写 Prompt → 出图`

Visual Style Deconstructor 的目标是：

`参考图 / Moodboard / Brand Assets → Reference Role → Visual DNA → Style Boundary → Reproduction Recipe → STYLE_SPEC → 下游执行 Skill / Model Compiler`

核心不是“写得更像参考图”，而是回答：

- 哪些视觉特征是真正稳定的？
- 哪些只是单张图的偶然因素？
- 每张参考图到底负责什么？
- 什么必须保持，什么允许变化？
- 换商品、换模特、换画幅后，怎样仍然保持同一种视觉语言？
- 一张新结果为什么符合 / 不符合目标风格？

---

## 当前文件

```text
visual-style-deconstructor/
├── SKILL.md
├── README.md
├── STYLE_SPEC.template.yaml
└── REFERENCE_ROLE_SCHEMA.md
```

### `SKILL.md`

定义拆解方法、分析顺序、Visual DNA、风格边界、复现配方和验收逻辑。

### `STYLE_SPEC.template.yaml`

机器可读的 Visual Style Capsule 模板。后续可以由其它 Skill、Agent、插件或模型 compiler 直接读取。

### `REFERENCE_ROLE_SCHEMA.md`

定义每张参考图的职责，以及 `PRESERVE / EXTRACT / ADAPT / IGNORE` 字段级授权方法。

---

## 推荐第一次怎么测试

准备一组你认为“属于同一视觉方向”的图片，推荐 5–12 张。

同时告诉 Skill：

1. 这组图要服务什么任务，例如儿童家居服模特摄影、静物摄影、品牌 KV。
2. 哪些是你真正认可的核心参考。
3. 如果有的话，哪些图只是借构图 / 光影 / 色彩 / 排版。
4. 哪些元素明确不要。
5. 是否有已经通过和已经否定的历史案例。

示例请求：

```text
使用 Visual Style Deconstructor 拆解这组 8 张参考图。
目标：建立儿童家居服秋冬商业摄影风格。
R01-R03 主要参考空间和构图；R04-R05 主要参考光影；R06-R08 主要参考人物状态和后期质感。
商品版型、颜色和真实面料不属于参考图风格，后续必须由真实商品图控制。
输出完整 STYLE_SPEC。
```

---

## 默认输出

1. 任务与媒介判定
2. 参考图角色地图
3. 风格核心概括
4. Visual DNA
5. LOCK / ADAPT / VARIABLE / FORBIDDEN
6. 复现配方
7. 验收标准
8. STYLE_SPEC YAML

---

## Visual DNA v0.1

### Core

适用于所有媒介：

- Concept / Intent
- Composition
- Hierarchy
- Negative Space
- Rhythm
- Color
- Tonal Contrast
- Shape Language
- Material / Texture
- Depth
- Emotion
- Signature Devices
- Post-processing

### Photography Module

额外拆：

- 景别
- 相机高度 / 角度 / 距离
- 透视特征
- 景深
- 主光方向 / 光质 / 光比 / 色温
- 场景结构
- 道具类型与密度
- 人物状态
- 商品展示关系
- 肤质 / 面料 / 清洁 / 锐度

### Graphic Design Module

额外拆：

- Grid
- Alignment
- Typography Role
- Type Scale
- Spacing
- Image/Text Relationship
- Headline Zone
- Information Density
- Graphic Devices
- Container Language
- Texture Finish

---

## 与现有 Ecom Image Prompt Director 的关系

两者不要合并成一个 Skill。

```text
Visual Style Deconstructor
        ↓
STYLE_SPEC
        ↓
Ecom Image Prompt Director
        ↓
具体任务提示词
```

Visual Style Deconstructor 回答：

> “我们想要的视觉语言到底是什么？”

Ecom Image Prompt Director 回答：

> “这一次具体该改什么、保留什么、怎样组织成执行提示词？”

后续还可以增加：

```text
STYLE_SPEC
   ├── Commercial Photography Director
   ├── Brand Visual Director
   ├── GPT Image Compiler
   ├── Qwen Image Compiler
   ├── Nano Banana Compiler
   └── ComfyUI Workflow Mapper
```

---

## v0.1 设计原则

### 1. 不追求一次“描述得很漂亮”

追求的是可重复调用、可判断、可迭代。

### 2. 不把 Mood 当规则

“高级、松弛、温暖、克制”必须继续拆成可观察的视觉变量。

### 3. 不把单图偶然特征升级为品牌规范

先找多图共性，再定义 Style Signature。

### 4. 不要求所有参考图意见一致

发生冲突时，识别 Style Family 或保留 unresolved question。

### 5. Approved / Rejected 都是资产

最终风格系统应该越来越依赖真实的通过 / 不通过案例，而不是越来越长的 Prompt。

---

## 下一步建议

v0.1 先不要继续堆字段。

第一阶段更值得做的是拿真实项目测试 2–3 轮，例如：

- 儿童家居服模特商业摄影
- 电商静物摄影
- 品牌 KV / 促销视觉

测试后重点记录：

- 哪些字段经常没用？
- 哪些字段缺失？
- 哪些判断最容易漂？
- 哪些 Style 规则真正能跨主体复现？
- 哪些东西必须交给下游模型 compiler，而不应该留在 Style Spec？

再据此升级 v0.2。
