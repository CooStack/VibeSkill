# 美术

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [AR001 · Art direction; 美术指导; Style guide](../concepts/AR001.md) | 统一画风、艺术方向 |
| [AR002 · Moodboard; Reference board](../concepts/AR002.md) | 氛围参考、参考拼板 |
| [AR003 · Concept art; 概念设计; Key art](../concepts/AR003.md) | 世界观设定、宣传主视觉 |
| [AR004 · Model sheet; Turnaround; 角色设定三视图](../concepts/AR004.md) | 角色前侧后、造型一致 |
| [AR005 · Shape language; 形状语言](../concepts/AR005.md) | 角色看起来强壮或危险 |
| [AR006 · Silhouette; 剪影; Readability](../concepts/AR006.md) | 缩小后认不出、轮廓糊 |
| [AR007 · 比例 Proportion; 解剖 Anatomy; Gesture](../concepts/AR007.md) | 人体不对、动作僵硬 |
| [AR008 · Composition; 构图; Focal point](../concepts/AR008.md) | 画面散、不知道看哪里 |
| [AR009 · Negative space; 负形; Tangency](../concepts/AR009.md) | 轮廓粘连、空间拥挤 |
| [AR010 · Perspective; Vanishing point; Foreshortening](../concepts/AR010.md) | 透视不对、近大远小 |
| [AR011 · Atmospheric perspective; 空气透视](../concepts/AR011.md) | 远景没层次 |
| [AR012 · Value; 明度; Value grouping](../concepts/AR012.md) | 黑白看不清、亮暗混乱 |
| [AR013 · Hue; Saturation; Value; 色相/饱和度/明度](../concepts/AR013.md) | 调颜色、太艳、灰 |
| [AR014 · 色彩协调 Color harmony; 冷暖关系](../concepts/AR014.md) | 配色乱、冷暖对比 |
| [AR015 · 色域 Gamut; 色彩空间 Color space; ICC](../concepts/AR015.md) | 导出变色、屏幕色差 |
| [AR016 · sRGB; Linear light; Gamma](../concepts/AR016.md) | 混色发暗、光照不对 |
| [AR017 · Bit depth; Banding; Dithering](../concepts/AR017.md) | 渐变断层、颜色数量 |
| [AR018 · Key/Fill/Rim light; 主光/补光/轮廓光](../concepts/AR018.md) | 立体感、主体分离 |
| [AR019 · Form shadow; Cast shadow; Terminator](../concepts/AR019.md) | 阴影不对、明暗交界线 |
| [AR020 · Occlusion; 接触阴影; Ambient occlusion](../concepts/AR020.md) | 接触面漂浮、缝隙暗 |
| [AR021 · Specular; Roughness; Reflection](../concepts/AR021.md) | 太塑料、太亮、金属感 |
| [AR022 · Subsurface scattering; SSS; 次表面散射](../concepts/AR022.md) | 皮肤蜡感、透光耳朵 |
| [AR023 · Edge control; 硬边/软边/失边](../concepts/AR023.md) | 画面死板、焦点不清 |
| [AR024 · Brushwork; 笔触; Painterly](../concepts/AR024.md) | 油画感、手绘感 |
| [AR025 · Stylization; Realism; Exaggeration](../concepts/AR025.md) | 风格化、写实、夸张 |
| [AR026 · Cel shading; Toon shading](../concepts/AR026.md) | 卡通分层阴影、描边 |
| [AR027 · Pixel art; 像素画; Pixel grid](../concepts/AR027.md) | 8 位、复古小图、像素角色 |
| [AR028 · Pixel cluster; Selective outline; Hue shifting](../concepts/AR028.md) | 像素轮廓僵、阴影脏 |
| [AR029 · Raster; Vector; Resolution; PPI/DPI](../concepts/AR029.md) | 图片放大糊、印刷清晰度 |
| [AR030 · Alpha; Straight/Premultiplied alpha](../concepts/AR030.md) | 透明边缘黑边、抠图 |
| [AR031 · Layer; Mask; Clipping mask](../concepts/AR031.md) | 非破坏修改、局部调整 |
| [AR032 · Blend mode; Multiply; Screen](../concepts/AR032.md) | 叠色、光效合成 |
| [AR033 · Texture; Seamless; Tileable](../concepts/AR033.md) | 平铺纹理、边缘接缝 |
| [AR034 · Albedo/Base color; Normal; Roughness; Metallic](../concepts/AR034.md) | 材质贴图一套、PBR 贴图 |
| [AR035 · Trim sheet; Decal; Atlas](../concepts/AR035.md) | 共用细节、贴花、合图 |
| [AR036 · Sprite; Sprite sheet; Atlas](../concepts/AR036.md) | 二维角色帧、切图 |
| [AR037 · Keyframe; In-between; Timing; Spacing](../concepts/AR037.md) | 动画节奏、动作生硬 |
| [AR038 · Squash/stretch; Anticipation; Follow-through](../concepts/AR038.md) | 动作没重量、缺预备动作 |
| [AR039 · Smear; Motion blur; 拖影](../concepts/AR039.md) | 高速动作读不清 |
| [AR040 · VFX shape/timing; 特效层次](../concepts/AR040.md) | 爆炸没重点、技能不好读 |
| [AR041 · Compositing; Color grading; LUT](../concepts/AR041.md) | 后期合成、统一色调 |
| [AR042 · Look development; Lookdev](../concepts/AR042.md) | 材质灯光一起调、外观开发 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为美术领域基线，将风格、构图和材质概念落实为可交付资产及实际使用场景中的视觉验收。

### 关键特征

- 先确定主体、用途和展示尺寸，风格选择服从可辨认性与内容目标。
- 分别控制轮廓、明暗、色彩和细节密度，避免以术语堆叠代替视觉取舍。
- 沿用项目资产规范与参考方向，未经要求不扩展角色设定或改换整体美术风格。

### 如何落实

- 明确主体必须保留的特征、构图焦点、背景关系及禁止变化的内容。
- 先用轮廓和大面积明暗建立层级，再加入与观看距离匹配的材质和细节。
- 按目标用途处理尺寸、透明边缘、色彩与导出格式；序列资产同时约束视角、比例和光照一致性。
- 把资产放回实际界面或场景，与相邻素材比较辨识度、边缘融合和视觉权重。

### 如何验收

- 在实际展示尺寸及缩略尺寸下辨认主体，核对关键特征未被细节或背景淹没。
- 对照参考检查轮廓、配色和光照方向，区分有意变化与不一致。
- 检查导出后的透明边缘、裁切和色彩表现，序列资产核对比例与位置跳动。

### 常见误用

- 只在放大画布上评价细节，忽略最终尺寸下的可读性。
- 将低多边形、像素化或某种配色当作所有风格化需求的默认答案。
