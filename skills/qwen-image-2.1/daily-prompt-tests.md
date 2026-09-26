# Qwen Image 2.1｜日常有效提示词与样本测试日志

> v0.1 · 2026-09-26 · 持续追加，不是最终 Skill  
> 模型：Qwen Image 2.1 · ComfyUI Image Edit  
> 默认输出英文描述性提示词；中文保留为任务说明。**英文更好**是当前个人观察，不视为模型官方通用结论。

## 0. 状态及证据口径

- **已反馈成功（任务组）**：用户已反馈 B05 视角测试、B06 全景及 ComfyUI 自定义比例的整体测试成功；尚未附每条提示词对应的输出截图、Seed 和结果评分。
- **待逐条复测**：本文列出的单条 Prompt 尚需建立“一条提示词 ↔ 一张输入图 ↔ 一张结果图”的证据链；尤其向左扩图、长短版本和超宽全景不可仅凭整体反馈视为分别验证。
- **官方逐字案例**：只将下面「官方基础案例」标注为 README 原文。其余都是依据官方原则及本轮交流编写的**个人测试词**，不是 Qwen 官方逐字模板。

### 测试记录字段（每次可复制一行）

| 日期 | ID | 输入样本 | Prompt 版本 | Seed | Steps | custom_size | width × height | 输出样本链接 | 结果 / 失败点 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-26 | B05/B06 | 待补 | 本日志简版 / 长版 | 待补 | 待补 | 已成功测试开关 | 待补 | 待补 | 已反馈任务组成功，待逐条补图 | 待复核 |

## 1. B05｜更换场景机位

**共同测试原则：** 仅改变相机视角；保留原主体、场景中物体的身份与相对空间关系、材质、颜色及已有光照体系。因改变机位会自然改变物体投影轮廓、遮挡和画内布局，不应要求像素级“构图完全不变”。

### B05-01 更换角度—左—高角度

```text
Change only the camera viewpoint to a high-angle view from the left side. Preserve the subject, scene layout, materials, colors, lighting atmosphere, and all untargeted content. Make it look like the same scene photographed again from a left high-angle perspective.
```

- 中文任务：从场景左侧较高机位重拍；保持同一场景的材质、物体与光场。
- 画幅：默认跟随原图；`custom_size=false`。
- 观察：任务组已反馈成功；待补本条截图、具体机位和失败边界。

### B05-02 更换角度—右—高角度

```text
Change only the camera viewpoint to a high-angle view from the right side. Preserve the subject, scene layout, materials, colors, lighting atmosphere, and all untargeted content. Make it look like the same scene photographed again from a right high-angle perspective.
```

- 中文任务：从场景右侧较高机位重拍。
- 画幅：默认跟随原图；`custom_size=false`。
- 观察：任务组已反馈成功；待补逐条样本。

### B05-03 更换角度—背面—平视

```text
Change only the camera viewpoint to a back view at eye level. Preserve the subject, scene layout, materials, colors, lighting atmosphere, and all untargeted content. Make it look like the same scene photographed again from behind at eye level.
```

- 中文任务：相机绕至主体背面，以平视机位重新拍摄。
- 画幅：默认跟随原图；`custom_size=false`。
- 观察：任务组已反馈成功；待检查不可见背面是否出现虚构结构。

## 2. B06｜全景 / 扩图

**注意：** `custom_size=true` 并设置 `width/height` 才能明确控制输出比例。仅改变尺寸不等于把原图无损粘在扩大画布中；对于必须保留原始像素的扩图，需要预置扩图画布或后期回贴原图。

### B06-01 普通全景图（短版）

```text
Generate a panoramic version of this scene. Expand the environment into a coherent full panorama while preserving the core scene content, lighting atmosphere, materials, and overall visual style.
```

- 中文任务：将场景扩展为宽幅全景，延续材质、环境和光影。
- 建议测试画幅：`2:1`；ComfyUI 自定义宽高，不要仅在 prompt 中指定。
- 观察：B06 任务组已反馈成功；需补原图与输出对照。
- 限制：2:1 宽图不等于可无缝用于 HDRI 的 360° 球面全景。

### B06-02 超宽全景（待单独复测）

```text
Generate an ultra-wide panoramic version of this scene. Extend the scene into a broad, coherent panorama while preserving the core environment, lighting, materials, and overall style. The output should feel expansive and continuous, with strong panoramic width.
```

- 建议画幅：`3:1`，需验证当前 ComfyUI 工作流/显存是否支持该尺寸。
- 状态：测试候选，未记录独立样本。

### B06-03 向左扩图（短版）

```text
Outpaint the image toward the left, preserving the original image content, object placement, materials, colors, and lighting, while naturally extending the surrounding environment with seamless perspective and continuity.
```

### B06-03b 向左扩图（长版，对照测试）

```text
Outpaint the image toward the left. Extend the existing scene naturally into the newly added area on the left, completing the surrounding environment and spatial structure. Preserve the original image content, object placement, materials, colors, and lighting, and keep all untargeted content unchanged. Ensure seamless continuity in perspective, scale, and environmental illumination.
```

- 中文任务：仅在左侧增加环境；原画面保持，补全墙地面、原有物体的合理延续。
- 推荐：源图 `3:4` 时分别试 `1:1` / `4:3` 等更宽画幅；不要把“向左”理解为从左侧机位重拍。
- 状态：已有提示词，待比较简版与长版；暂不标注某一版必然更好。

### B06-04 左右扩图

```text
Outpaint the image to the left and right, naturally extending the existing environment and completing the surrounding spatial structures, walls, floor, and visible objects. Preserve the original central image, object placement, materials, colors, and lighting. Maintain consistent perspective, environmental illumination, and seamless continuity. Do not introduce unrelated objects or redesign the existing scene.
```

- 中文任务：左右扩展商业摄影场景、保留中心主体和原环境区域光影。
- 推荐：`4:3` / `16:9`，根据原始画幅选真正更宽的比例。
- 状态：待补逐条对照图。

### B06-05 全景扩图（商业摄影详细版）

```text
Perform panoramic outpainting by extending the original scene widely to both the left and right, completing the surrounding environment into a coherent wide panoramic composition. Preserve the original central image, object placement, materials, colors, and lighting structure. Extend the environment according to the existing spatial logic, perspective, and soft ambient illumination. Do not introduce additional window beams, light spots, clutter, or unrelated objects. Create a clean, realistic, seamless panoramic view of the same commercial photography environment.
```

- 中文任务：以原场景为基准向左右延展，避免额外窗光、光斑和无关道具。
- 建议测试画幅：`2:1`。
- 状态：待与 B06-01 短版进行同图、同 Seed 对照。

## 3. Qwen 官方 README 的两条「逐字基础案例」

下面两条为**官方原文**，非本人的强化版模板。用于比较“极短指令”与本日志较长编辑指令的差别。

### OFFICIAL-01｜单图编辑 / 背景替换

```text
Change the background to a sunset beach
```

来源：[官方 README · Image Editing (Single Image)](https://github.com/QwenLM/Qwen-Image-2.1/blob/main/README.md)。

### OFFICIAL-02｜多参考图合成

```text
These three characters are sitting around a campfire in a forest
```

来源：[官方 README · Image Editing (Multiple Reference Images)](https://github.com/QwenLM/Qwen-Image-2.1/blob/main/README.md)。

## 4. 官方 PE 规则与本人的测试假设

- 官方编辑 PE 的核心：只改目标属性、其余保持；尽量指向身份参考图，少用冗长五官重述。
- 多图需逐张声明角色；官方 PE 使用 `<image1>`、`<image2>` 等编号，编号必须与输入顺序对应。
- 画幅规则：`wh_ratio` 和 `ratio_follow` 二选一；实际在 ComfyUI 仍须落地为底层宽高参数。
- 官方 PE-I2I 对中文输入默认产出中文描述；**本档案采用英文生图提示词是用户基于本地测试提出的实验偏好**，不要把它标成官方强制规则。
- 全景：官方 PE 的标准全景建议 `2:1`，超宽 `3:1`；需要区分“场景横向扩图”和真正 360° 环境贴图。

来源：[official/system_prompt_edit.txt](./official/system_prompt_edit.txt)、[official/system_prompt_t2i.txt](./official/system_prompt_t2i.txt)。

## 5. 待补的高频电商任务

| ID（暂定） | 任务 | 核心评估 |
| --- | --- | --- |
| FACE | 换脸 / 换头 | 五官身份相似、发型与头身比例、服装与背景不漂移 |
| CHAR | 同角色不同姿势 / 机位 | 人脸、体型、服装印花与结构一致 |
| CLOTH | 换装 | 领口、袖口、缝线、裤脚、印花还原 |
| SCENE | 人物入场景 | 场景画布、人物比例、接触阴影、区域光影 |
| BG | 替换背景 | 主体不改、透视与受光协调 |
| OUTPAINT | 单边 / 双边扩图 | 原画面完整、方向准确、空间与光影连续 |

## 6. 凝练正式 Skill 前的验收条件

- 至少跨不同输入图复测，不凭一张图判断成功。
- 保存输入图/输出图链接、Prompt 原文、Seed、Steps、参考图排序、`custom_size`、尺寸和失败描述。
- 将官方基础案例、官方 PE 输出、现有 Ecom Image Prompt Director 与英文测试模板放在同条件下比较。
- 确认高频任务中哪些用简短词足够、哪些必须加入 LOCK / EDIT / ADAPT，才考虑转入生产 Skill。

<!-- 维护规则：只追加带日期的新观察；不要静默覆盖已参与测试的 Prompt 原文。 -->
