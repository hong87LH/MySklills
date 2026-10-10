# Visual Style Deconstructor — Reference Role Schema v0.1

本文件定义参考图在视觉拆解中的职责与字段授权，避免“整体参考”导致人物、商品、场景、构图与风格互相污染。

## 1. 核心原则

每张参考图都必须回答四个问题：

1. **它主要提供什么？**
2. **它次要提供什么？**
3. **哪些字段允许继承或提取？**
4. **哪些字段必须明确忽略？**

禁止只写：

- 图1整体参考
- 参考图风格
- 按图2感觉做

推荐结构：

```yaml
ref_id: R01
primary_role: Lighting
secondary_roles:
  - Color/Tone
priority: 90
authorization:
  preserve: []
  extract:
    - lighting.key_direction
    - lighting.quality
    - color.temperature
  adapt:
    - shadow_position
    - subject_exposure
  ignore:
    - subject.identity
    - product
    - composition
```

---

## 2. 标准 Role

### Content / Product

用于：

- 商品结构
- 商品颜色
- 图案
- Logo
- 真实材质
- 产品比例

默认行为：

- 事实字段优先 `PRESERVE`
- 不自动继承背景、人物、构图、光影

### Identity / Subject

用于：

- 人物身份
- 脸型与五官
- 发型
- 年龄感
- 身体比例

默认行为：

- 身份事实优先 `PRESERVE`
- 新场景下受光、透视、姿势可以 `ADAPT`

### Composition

用于：

- 主体位置
- 主体占比
- 留白
- 裁切
- 对称 / 非对称
- 视觉重心

默认行为：

- `EXTRACT` 构图关系
- 不自动继承人物、商品、文字

### Camera

用于：

- 相机高度
- 左右机位
- 俯仰
- 拍摄距离
- 透视强弱

注意：

人物转身 ≠ 相机换位。

### Lighting

用于：

- 主光方向
- 光质
- 阴影开放程度
- 明暗关系
- 色温

默认行为：

- 光照规律 `EXTRACT`
- 新主体上的具体高光与阴影位置必须 `ADAPT`

### Color / Tone

用于：

- 主色板
- 辅助色
- 色温
- 饱和度
- 明度
- 综合色调
- 色彩关系

商品真实颜色与品牌标准色若被锁定，优先级高于参考图综合色调。

### Material / Texture

用于：

- 表面粗糙度
- 织物触感
- 木材 / 金属 / 玻璃等材质语言
- 印刷 / CG / 手工质感

不要把“参考图里的具体物体”误当成必须复刻的材质系统。

### Environment / Set

用于：

- 空间结构
- 家具关系
- 背景建筑
- 场景深度

### Styling / Prop

用于：

- 道具类别
- 道具数量
- 摆放方式
- 陈列节奏

建议同时记录 `prop_density`，避免只复制具体道具。

### Typography

用于：

- 字体角色
- 字重对比
- 字号层级
- 字距 / 行距倾向

无法确认具体字体时，不要伪造字体名称。

### Graphic Language

用于：

- 线条
- 几何图形
- 卡片
- 边框
- 图标
- 装饰系统

### Retouch / Finish

用于：

- 清洁度
- 锐度
- 颗粒
- 肤质
- 面料表现
- 对比
- 色彩后期

### Mood

Mood 是上位语义，不应该单独作为最终执行规则。

例如：

`calm / quiet / premium`

必须继续拆成可观察项：

- 低道具密度
- 柔和光比
- 中低饱和
- 高留白
- 低动作幅度

### Negative Reference

专门用于“不要这样”。

例如：

```yaml
primary_role: Negative Reference
extract:
  - failure_pattern
ignore:
  - all_positive_style_fields
```

---

## 3. 四种授权状态

### PRESERVE

忠实保留事实。

适合：

- 产品结构
- Logo
- 人物身份
- 品牌标准色

### EXTRACT

提取规律，不复制内容本身。

适合：

- 构图
- 光影
- 色彩关系
- 视觉节奏
- 字体角色

### ADAPT

继承原则，但允许根据新任务重新计算。

适合：

- 新姿势下的褶皱
- 新场景下的阴影
- 新比例下的排版间距
- 新机位下的透视

### IGNORE

明确禁止继承。

适合：

- 参考图里无关人物
- 参考图里的商品
- 无关文字
- 不属于目标风格的偶然道具

---

## 4. Priority

建议范围：`0–100`

- 90–100：用户明确指定 / 品牌硬规则 / 商品事实
- 70–89：主要风格参考
- 40–69：辅助参考
- 10–39：灵感来源，只允许弱影响
- 0：Negative / Ignore

Priority 不是“复制强度”，而是**冲突时的裁决优先级**。

---

## 5. 冲突裁决

默认顺序：

1. 用户明确要求
2. 品牌 / 商品事实
3. Approved Set 的稳定规律
4. 多张参考图共同规律
5. 单张参考图
6. 模型默认审美

若两张主要参考图在同一字段强冲突：

- 不做平均
- 标记 conflict
- 判断是否属于两个 Style Family
- 若无法判断，保留为 `unresolved_questions`

---

## 6. 推荐输出格式

```text
【参考图角色地图】
- R01｜Primary: Composition｜Secondary: Camera｜Priority: 85
  - EXTRACT: 主体左偏、右侧留白、中景裁切
  - ADAPT: 新商品尺寸下的主体占比
  - IGNORE: 人物身份、服装、背景材质

- R02｜Primary: Lighting｜Secondary: Color/Tone｜Priority: 90
  - EXTRACT: 左前侧大面积柔光、低光比、暖中性色温
  - ADAPT: 新主体的高光/阴影位置
  - IGNORE: 原场景、原人物、原构图
```

最终目标不是让模型“参考更多”，而是让每一张参考图**只在被授权的字段上生效**。
