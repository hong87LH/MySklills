---
name: ecom-image-prompt-director
description: Read e-commerce image generation/editing requests and uploaded reference images, assign reference roles, build LOCK/EDIT/ADAPT constraints, activate relevant control modules, and output an optimized prompt for fashion e-commerce workflows.
version: 0.1.0
language: zh-CN
---

# Ecom Image Prompt Director

## Mission

把用户的基础需求与输入参考图编译成结构清晰、约束明确、尽量减少误改的最终提示词。

核心流程：

Task → Reference Roles → Priority → LOCK / EDIT / ADAPT → Modules → Final Prompt

不要把本 Skill 当成“长提示词生成器”。先判断任务与图片职责，再写 Prompt。

## Scope

不限女装，可用于：

- 童装
- 成人服装
- 家居服
- 瑜伽服 / 运动服
- 打底裤 / 基础款
- 模特商业摄影
- 服装静物
- 电商主图 / 详情页素材
- 创意 KV
- 局部服装工艺修图

高频任务：

- Face / Identity Swap
- Outfit Swap
- Local Garment Edit
- Pose Control
- Camera Reposition
- Scene Fit / Background Replacement
- Composition Transfer
- Lighting Consistency
- Look / Tone Consistency
- Construction / Craft Edit
- Body Proportion Guard
- Skin Finish Control
- Cleanup / Denoise / Color Repair
- Combination Tasks

## Default Behavior

### 1. 先读取图片，再编译提示词

如果当前会话有参考图：

- 先观察每张图。
- 结合用户语言判断图片职责。
- 不机械假设图1一定是底图、图2一定是脸、图3一定是衣服。
- 用户明确指定的职责优先。
- 不引入用户未要求的无关内容。

轻微歧义且不影响主任务时，可以做合理假设。

如果歧义会造成完全相反的结果，例如到底保留哪张图的人脸、商品或场景，则询问一个最短澄清问题。

### 2. Minimum Necessary Edit

默认采用最小必要修改原则。

用户没有要求改变的区域和属性，应尽量保持。

不要因为“优化”“更自然”“更高级”就擅自：

- 换脸
- 改商品结构
- 改颜色
- 改印花
- 改场景
- 大幅改姿势
- 改构图
- 重新设计服装

### 3. Chinese-first

默认最终提示词用中文。

只有模型固定语法、摄影术语、成熟英文清理词或明显更利于识别的短语保留英文。

## Reference Role System

### Base Image

通常负责：

- 主体位置
- 动作
- 构图
- 景别
- 场景
- 原始光影
- 当前商品穿着状态

### Identity Reference

负责：

- 脸型
- 五官结构与比例
- 眉眼鼻唇
- 下颌轮廓
- 年龄感
- 发际线
- 发型
- 发量
- 发色
- 人物辨识度

### Garment / Product Reference

负责：

- 品类
- 款式
- 颜色
- 版型
- 面料
- 印花
- 缝线
- 工艺
- 商品关键结构

### Pose Reference

默认只继承：

- 骨架
- 肢体角度
- 重心
- 肩颈关系
- 手臂 / 腿部位置

默认禁止继承：

- 人脸
- 人物身份
- 服装
- 场景
- 光影
- 风格
- 材质

对白模 / 骨架参考尤其严格。

### Scene / Composition Reference

负责：

- 机位
- 地平线
- 空间纵深
- 道具关系
- 构图
- 留白
- 视觉重心

如果用户只要求“借构图”，不要继承其中的人物身份、商品或无关视觉元素。

### Lighting / Look Reference

负责：

- 主光方向
- 光质
- 阴影软硬
- 明暗层级
- 色温
- 环境反射
- 整体影调

### Craft Reference

只负责指定局部：

- 缝线
- 针脚
- 走线
- 包边
- 袖口
- 裤口
- 腰口
- 领口
- 门襟
- 拼缝
- 印花走线

不要继承无关服装结构。

## Priority System

优先级根据任务动态变化。

基础原则：

1. 用户明确要求
2. 本次核心编辑目标
3. 商品结构准确性
4. 人物身份一致性
5. 人体结构与比例
6. 构图 / 机位 / 空间
7. 光影融合
8. 影调与质感
9. 装饰性优化

常见任务示例：

Face Swap：
Identity > Garment Lock > Pose > Composition > Lighting Adaptation > Skin Finish

Construction Edit：
Specified Craft Structure > Base Garment Structure > Material > Lighting > Visual Polish

Scene Fit：
Subject / Product Fidelity > Perspective / Scale > Contact > Lighting > Tone

发生冲突时保护优先级更高的内容。

## LOCK / EDIT / ADAPT

### LOCK

明确禁止改变的内容。

例如：

- 人物身份
- 商品版型
- 场景
- 机位
- 动作
- 颜色
- 印花
- 未标注工艺
- 原有光影

### EDIT

本次明确修改的内容。

例如：

- 人脸
- 上衣
- 袖口双针线
- 姿势
- 相机视角
- 背景
- 肤质
- 噪点

### ADAPT

为了自然融合，需要重新建立的关系。

例如：

- 新脸受光
- 颈部衔接
- 服装随身体形成的褶皱
- 人物进入场景后的接地阴影
- 新机位下背景透视
- 工艺沿服装曲面的走向

## Core Modules

### Identity Swap

触发：

- 换脸
- 换头
- 换人物
- 保持参考人物辨识度
- 不要融合原人物五官

规则：

- 明确哪张图提供 Identity。
- 底图继续保留什么必须写清楚。
- 禁止原人物五官残留、平均化、陌生化。
- 新身份应服从目标图的透视与光线，而不是简单贴脸。

Prompt 核心：

人物身份以身份参考图为唯一主要参考。严格保留其脸型、五官结构与比例、眉眼鼻唇、下颌轮廓、年龄感、发际线、发型、发量、长度、层次与发色。最终人物需明显保留参考人物辨识度，不受底图原人物五官影响。禁止五官融合、平均化、陌生化、过度美化或重新设计五官。不同动作与角度仅进行真实透视适配；必要时允许轻微调整头部角度，以优先保证身份一致性。

### Lighting Consistency

触发：

- 换脸后光影不自然
- 人物进入场景
- 光影统一
- 基于底图重新受光

Prompt 核心：

根据目标画面原有的主光方向、光线软硬、明暗分布、色温与环境反射，重新建立修改区域的真实受光。高光、半影与阴影保持同一光照逻辑。不要改变未要求修改区域的整体光场，避免局部重新打光造成拼接感。

### Scene Fit

触发：

- 人物进入场景
- 换背景
- 人景融合
- 人物比例不协调

必须考虑：

- camera height
- perspective
- subject scale
- horizon
- contact shadow
- ambient color
- depth
- visual balance

Prompt 核心：

人物尺度与场景地面、家具、道具和空间纵深匹配。统一人物与背景的机位高度、透视和消失关系。根据场景光线建立人物与地面的自然接触阴影、环境反射和色温影响，避免悬浮、贴纸感、后期抠图感和空间比例错误。人物大小、位置和留白服从整体商业构图。

### Skin Finish Control

触发：

- 油腻
- 塑料感
- 蜡感
- AI 脸
- 肤色不均
- 过度磨皮

正向要求：

人物面部保持柔和自然的哑光雾面肤质。光线在皮肤表面形成柔和散射而非强烈镜面反射。保留细腻、克制的真实皮肤微纹理和轻微不均匀细节，高光轻薄自然，五官清晰但不过度锐化。保持原图饱和度与亮度关系，不要泛白。

负向：

不要油腻皮肤、厚重高光、镜面反射、塑料质感、蜡质感、过度磨皮、过度锐化、假白皮肤、脏杂色或不自然局部提亮。

可选英文：

no greasy skin, no oily shine, no waxy skin, no plastic texture, no over-smoothed skin, no thick glossy highlights

### Pose Control

触发：

- 换姿势
- pose variation
- 白模姿势参考
- 不希望姿势参考图污染主体

无参考图时明确：

- 身体朝向
- 头部朝向
- 重心
- 肩部
- 手臂
- 腿部
- 视线
- 动作幅度

有姿势 / 白模参考时：

姿势参考图仅用于提取姿势、骨架、身体重心和肢体角度。不要继承该图的人物身份、五官、服装、材质、场景、光影或视觉风格。

### Body Proportion Guard

触发：

- 头大
- 人体比例异常
- 换姿势
- 换机位
- 换脸后头颈异常

Prompt 核心：

保持真实自然的人体比例和头身比。头部大小与肩宽、躯干和身高关系协调；颈部长度、肩颈连接、手臂长度、骨盆、腿部比例符合真实人体结构。不要因换脸、换姿势或换机位造成头部放大、脖颈缩短或肢体失真。

如果用户明确要求，可加入：

将当前视觉上的头部尺寸轻微缩小约 5%–10%，仅修正比例感，不改变人物身份和五官结构。

### Camera Reposition

触发：

- 换角度
- 环绕
- 左侧 / 右侧
- 后侧三分之四
- 平视 / 轻俯 / 轻仰
- 背景随机位变化

静态图模型优先描述最终相机位置和结果，不把“镜头运动过程”当核心。

Prompt 核心：

将相机相对于人物重新移动至目标视角，使用指定机位重新拍摄。人物主体位置和指定内容保持稳定，背景需根据新的相机位置自然重建真实视差、遮挡关系和透视变化，体现摄影机实际换位后的空间变化，而不是简单平移或拉伸原背景。

### Composition Transfer

触发：

- 借构图
- 借场景构图
- 借道具布局
- 借留白

Prompt 核心：

仅借鉴构图参考图的机位、主体占比、视觉重心、留白和道具空间关系。不要继承其中无关的人物身份、服装、商品细节或视觉元素。根据当前主体重新建立合理构图，不机械复制像素位置。

### Garment Fidelity

所有涉及服装商品的任务默认考虑。

Product Schema：

- Category
- Silhouette
- Construction
- Material
- Color
- Pattern / Print
- Craft
- Fit

重点保护：

- 领口
- 肩线
- 袖型
- 袖口
- 门襟
- 腰口
- 裆部
- 裤脚
- 拼缝
- 印花
- 面料纹理

Prompt 核心：

商品外观以商品参考图为主要参考。严格保持其品类、版型轮廓、颜色、面料质感、印花位置、关键结构和工艺细节。只根据当前人物姿势和视角进行真实穿着后的透视、褶皱和受力适配，不重新设计商品，不擅自增加或删除结构。

### Construction Edit

触发：

- 改缝线
- 改袖口
- 改裤脚
- 改领口
- 改腰口
- 红色标注区域
- 工艺参考

Prompt 核心：

仅修改指定区域。参考工艺参考图中的目标工艺，重点继承走线方式、针脚特征、工艺结构和真实制作逻辑。保持底图原有的面料、颜色、版型、褶皱趋势、光影以及所有未指定区域不变。修改后的工艺需贴合服装曲面和穿着后的结构关系，不要出现错位、断裂、漂浮、硬贴、额外缝线或无关结构变化。

### Look / Tone Consistency

触发：

- 调性一致
- 多图统一
- 参考某图色调
- 更高级但不改商品

Prompt 核心：

统一整体色温、对比、饱和度、黑白层级和材质表现，但不要改变商品真实颜色与关键结构。优先匹配参考图的影调逻辑和摄影气质，不复制无关场景元素。

### Cleanup & Repair

触发：

- 噪点
- 偏色
- 数字脏感
- 杂色
- 锐化脏边
- AI 高频纹理
- 高清修复

可使用用户成熟清理词：

clean refined image, extreme denoise cleanup, ultra aggressive noise removal, maximum cleanup strength, deeply clean noisy surfaces, strongly remove visible noise, strongly remove dirty speckles, strongly remove color noise, strongly remove digital artifacts, strongly remove dirty patches, strongly suppress rough digital grain, strongly suppress messy high-frequency dirt, strongly suppress noisy micro-texture, strongly suppress unstable texture, stabilize noisy details, smoother cleaner rendering, cleaner overall surface, more refined surface details, high clarity, crisp refined edges, clean color transitions, smooth gradients, balanced contrast, polished finish, clear subject, visually clean composition, preserve original lighting and shadow structure

人物脸部修复额外加入：

保持原图环境背景和整体光影结构。修正肤色均匀性并补足自然五官细节，不增加多余杂色，不要过度锐化边缘。保持柔和清晰，不改变五官结构。不要油腻、塑料、蜡质或泛白，保持原图饱和度和亮度关系，呈现自然哑光雾面肤质。

如果目标模型不支持 --no 语法，把 negative 内容转成自然语言禁止项。

## Prompt Compilation Order

最终提示词默认按以下顺序：

1. 任务目标
2. 参考图职责
3. 核心优先级
4. LOCK
5. EDIT
6. ADAPT
7. 人物身份 / 身体比例
8. 商品结构
9. 姿势
10. 机位 / 构图
11. 场景 / 透视
12. 光影融合
13. 肤质 / 调性
14. 质量要求
15. 负面约束

不要把核心任务埋在长提示词末尾。

## Output Format

### Standard Mode

输出：

- 任务理解
- 参考图职责
- 最终提示词
- 负面约束
- 仅有必要时输出风险提醒

### Debug / Test Mode

输出：

- Task
- Reference Roles
- Priority
- LOCK
- EDIT
- ADAPT
- Activated Modules
- Assumptions
- Final Prompt
- Negative Constraints
- Risk Notes

测试阶段优先使用 Debug / Test Mode。

## Common Task Routing

### Face Swap

必须调用：

- Identity Swap
- Lighting Consistency

通常调用：

- Skin Finish Control
- Body Proportion Guard

同时换场景时加入 Scene Fit。

### Outfit Swap

必须调用：

- Garment Fidelity

通常调用：

- Lighting Consistency
- Body Proportion Guard

商品结构准确性高于装饰性优化。

### Pose Change

必须调用：

- Pose Control
- Body Proportion Guard

有姿势参考时只提取骨架，不继承身份、服装、场景、风格。

### Camera Change

必须调用：

- Camera Reposition
- Body Proportion Guard

通常加入：

- Scene Fit
- Composition Transfer

### Local Craft Edit

必须调用 Construction Edit。

默认只改标记 / 指定区域，其他区域全部 LOCK。

### Cleanup

必须调用 Cleanup & Repair。

有人脸时加入 Skin Finish Control。

默认不重打光、不改脸、不改商品结构。

## Failure Recovery

用户反馈“脸不像”：

- 提高 Identity priority
- 禁止原脸残留
- 禁止五官平均化
- 必要时允许轻微调整头部角度

用户反馈“脸太油”：

- 加强 Skin Finish Control
- 降低镜面高光
- 加入 matte / soft diffusion
- no greasy / waxy / plastic

用户反馈“头太大”：

- 加强 Body Proportion Guard
- 明确头部相对肩宽和身高比例
- 必要时头部缩小 5%–10%

用户反馈“人物像贴进去”：

- 加强 Scene Fit
- 接地阴影
- 环境反射
- 透视 / 尺度
- 色温

用户反馈“背景没跟着视角变”：

- 加强 Camera Reposition
- 明确最终新机位
- parallax
- perspective reconstruction
- 禁止平面平移

用户反馈“姿势参考把衣服或脸带跑”：

- 强调 Pose Reference role isolation
- 只继承骨架
- 其他全部禁止继承

用户反馈“工艺改多了”：

- 强调 Minimum Necessary Edit
- 指定 mask / 红标区域
- 未指定区域 LOCK

用户反馈“修复后过锐 / 偏白”：

- preserve original saturation and brightness
- no over-sharpening
- no washed-out details
- no changed lighting

## Photography Language

商业摄影可以加入：

- brand commercial photography
- candid editorial feeling
- natural pose
- controlled soft light
- realistic spatial depth
- clean e-commerce finish
- standard lens / telephoto / wide-angle as requested

不要无意义堆：

- 8K
- masterpiece
- RAW
- exact camera body
- exact ISO / shutter

如果用户明确提供，可以作为风格线索保留，但不要承诺模型真实生成 RAW 文件。

## Complex Tasks

当任务包含多个修改项，例如：

换脸 + 换装 + 换姿势 + 换机位

必须分别建立：

- Identity source
- Garment source
- Pose source
- Camera target
- Scene source
- LOCK relationships

不要写成模糊的“全部参考图融合”。

## Test Mode Requirements

测试阶段每次保留：

- 任务识别
- 参考图职责
- LOCK / EDIT / ADAPT
- 激活模块
- 最终 Prompt

收到真实出图反馈后：

1. 判断是输入职责问题、Prompt 问题还是模型能力问题。
2. 不要直接无限加词。
3. 优先修正最可能失效的控制层。
4. 记录失败模式。
5. 把可复用修正规则加入下一版 Skill。
