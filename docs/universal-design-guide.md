# 通用设计指南

> 提炼自 Google Design、Material Design 3 Expressive、Jetpack Compose Glimmer 及 PAIR 等官方文章与研究。  
> 适用于产品、UX、UI 实现——**原则是通用的，落地需结合载体变通**。

---

## 一、设计哲学：从「好看」到「有意义」

### 1.1 形式追随感受（Form follows feeling）

Material Design 十年演进的核心转折：极简不等于最好。过度简化会让产品冰冷、难产生连接。

- **形状、颜色、动效** 应传达情绪与功能，而不只是装饰
- 表达式设计（Expressive）的目标：让用户**有感受**，同时**更快完成目标**
- 情感与可用性不是对立的——研究证实两者可以同时提升

### 1.2 原则可以进化

以下「常识」可以被重新审视：

| 旧原则 | 新认知 |
|--------|--------|
| 越简越好 | 有意义比极简更重要 |
| 先写完美 Brief 再动手 | 有时先画、先原型更能发现真问题 |
| 设计委员会必然失败 | 大规模协作可产生共识与创新 |
| 设计系统 = 绝对一致 | 用户需要个性化与灵活表达 |

### 1.3 隐形框架 vs 主动介入

以 Chrome 为代表的产品哲学：

- 日常状态：UI 是**画框**，让内容（网页、地图、事件）成为主角
- 关键时刻：产品可**接管注意力**——安全警告、紧急状态、关键操作
- 设计决策：持续权衡「隐形」与「可辨识」，尤其在安全、品牌辨识场景

---

## 二、Material 3 Expressive：高级感来自系统

### 2.1 五大表达要素

表达式设计通过以下维度同时影响**情绪**与**可用性**：

1. **Color** — 色彩
2. **Shape** — 形状
3. **Size** — 尺寸
4. **Motion** — 动效
5. **Containment** — 容器 / 分组

它们的作用不仅是好看，更是：**引导注意力、分组相关信息、突出关键操作**。

### 2.2 研究支撑（不是主观审美）

Google 对 M3 Expressive 的研究规模：

- 46 项独立研究，18,000+ 参与者
- 方法：眼动追踪、问卷、焦点小组、可用性测试

**关键发现：**

| 维度 | 结论 |
|------|------|
| 偏好 | 各年龄段偏好表达式设计；18–24 岁最高约 87% |
| 品牌感知 | 现代感 +34%、亚文化相关性 +32%、叛逆感 +30% |
| 可用性 | 关键 UI 元素识别最快提升约 4 倍；点击关键操作更快 |
| 年龄差异 | 表达式设计可缩小不同年龄段的视觉搜索差距 |
| 无障碍 | 更大按钮、高对比容器对所有用户更友好 |

### 2.3 高级用法：不是「更花」，是「更准」

**Send 按钮案例（邮件应用）：**

- 错误：小按钮藏在顶栏工具条里，与其他操作混在一起
- 正确：更大、靠近输入区域、用 secondary 色强调
- 结果：用户找到按钮的速度提升约 4 倍

**高级原则：**

- 表达服务于**核心用户旅程**，不是全局撒花
- 打破熟悉交互范式会损害可用性（如把歌曲列表换成散乱专辑封面）
- 去掉文字标签会降低可理解性
- **功能优先**：再好看也不能牺牲清晰度
- 需在**新鲜感**与**熟悉感**之间迭代平衡

### 2.4 M3 组件层级的「高级」特征

- **Tonal palette**：用 `primary-container` / `on-primary-container` 等语义色，而非硬编码 hex
- **State layer**：hover 8%、pressed 12% 叠层，而非渐变和重阴影伪装质感
- **Shape token**：`corner-small` → `corner-extra-large`，Expressive 可用更大圆角与非对称形状
- **Motion physics**：强调型缓动曲线，状态切换有物理感
- **Split button、Floating toolbar、Button groups**：相关操作分组，减少视线跳转

---

## 三、排版：高级感在字体的「适应性」

### 3.1 Google Sans Flex 的启示

字体高级感不来自「换一个新字体」，而来自**解决一系列真实问题**：

- 产品锁标统一
- 小字号可读性
- 多语言书写系统
- 代码可读性（`a` / `o` 区分）
- 可变轴带来的表达范围

**Google Sans Flex 六轴：** Weight、Width、Optical Size、Slant、Grade、Roundedness

### 3.2 可变字体（Variable Fonts）

- 单文件替代整个字族，体积可减少约 70%
- 可在 Bold 与 Condensed 之间任意插值
- CSS：`font-weight`、`font-stretch`、`font-variation-settings`、`font-optical-sizing`
- **光学尺寸轴（opsz）**：字号变化时字腔、字距自动优化——高级感来源之一

### 3.3 排版高级原则

- 用 **M3 字阶角色**：display / headline / title / body / label，而非随意 px
- 关键数据用 **Expressive 大号数字**，次要信息降级
- 救援 / 安全 / 户外场景：**正文有下限**，关键指标放大
- 玻璃 / 叠层场景：文字加轻微 `text-shadow` 增强扫读性

---

## 四、透明叠层与 Glimmer：高级在于「克制」

> **重要：以下规则针对加色透明显示（AI 眼镜）。网页 / LCD 载体需变通，但「克制、层级、扫读」原则通用。**

### 4.1 物理约束塑造美学

| 现象 | 设计应对 |
|------|----------|
| 只能加光，不能发黑 | 黑 = 透明；用暗色底板作「容器」 |
| Halation（光晕） | 亮底会让相邻文字糊掉 → 暗底亮字 |
| 高饱和色在天空/沙滩下消失 | 界面默认中性，颜色仅用于强调 |
| 感知深度约 1 米 | 用户需主动切换焦点 → UI 必须值得这一瞥 |

### 4.2 排版用「视觉角度」思考

- 不以 px 为主，以**度（visual angle）** 衡量可读性
- 最小可读约 **0.6°**，正文应明显高于此
- Google Sans Flex + `opsz` 轴：增大字腔、拉远 i/j 上的点

### 4.3 纵深系统（depthEffect）

高级感不是 drop-shadow，而是：

- **Z 轴placement** + **深色遮挡阴影** 表达前后关系
- 按钮可叠在卡片上，建立层级
- 系统控件（如音量）可用更夸张的 depth 层级
- 聚焦时组件「靠近」用户，失焦时回落

### 4.4 动效：两种速度

| 场景 | 时长 | 目的 |
|------|------|------|
| Ambient 通知入场 | ~2s | 从外周缓慢引导注意力，不惊吓 |
| 用户操作反馈 | 即时（~0ms） | Focus ring / 高亮确认操作 |

### 4.5 载体变通（通用设计必读）

| 载体 | 材质策略 |
|------|----------|
| AI 眼镜（加色屏） | 暗底亮字，禁止大面积亮面 |
| 网页 / 手机 / 地图 HUD | 可用磨砂玻璃：低白度 + 强 blur + 环境色渗入 |
| 空间感卡片（Apple 式） | 多层纵深 + 边缘光 + 不同 blur 强度，非 1px 描边 |

**磨砂玻璃高级做法：**

- 背景透明度：**0.10–0.28**（不是 0.6+）
- `backdrop-filter: blur(40px+) saturate(1.6+)`
- 边缘：`inset` 上亮下暗 + `::after` 折射高光
- 禁止：去掉 blur 后仍像白底卡片

---

## 五、包容性设计：高级感包含「被看见」

### 5.1 与所有人一起构建

- 在构思、研究、设计、测试、营销各阶段纳入多元视角
- 承认偏见，让有生活经验的人引导方向
- 包容是**人道理由**，也是**商业理由**

### 5.2 全球无障碍

无障碍几乎总是**交叉性**的：残障、语言、识字率、经济、设备条件同时影响体验。

**策略摘要：**

- 研究样本包含残障用户（全球超 10 亿人）
- 插画与营销体现多元，而非 token 式点缀
- 简单英语 / 图形引导 / 减少层级菜单
- 隐私控制对弱势用户尤其重要

### 5.3 无障碍即高级感

- 颜色 + 图标**双编码**（色盲友好）
- 对比度达标，紧急色不能只在白底上「看起来够亮」
- 触控目标 ≥ 48dp，户外 / 湿手场景加大
- `prefers-reduced-motion` 提供静态降级

---

## 六、对话与 AI 设计

### 6.1 对话设计六原则（VUI）

1. 给界面明确**人格**
2. 推动对话**向前**（信息量原则）
3. **简短且相关**
4. 利用**上下文**
5. 用词序与**重音**引导注意力（尾焦点原则）
6. 不要教「命令」——说话是直觉的

### 6.2 以人为中心的 AI（PAIR）

- **Fair is not the default**：包容需要刻意设计
- ML 应让用户「不用多想」（Predictably smart）
- 原型阶段用 **Wizard of Oz** 模拟智能，验证后再投入工程
- 关注误识别路径：用户如何发现错误、如何恢复
- 先回答「该不该做」，再回答「能不能做」

---

## 七、高级感对照：常见低级 vs 高级做法

| 维度 | 低级做法 | 高级做法 |
|------|----------|----------|
| 颜色 | 硬编码 hex + 渐变 | 语义 token + tonal palette |
| 质感 | 白底 + 轻 blur | 低透明度 + 强 blur + 环境色渗入 |
| 边框 | `1px solid #fff` | 边缘光（inset 亮暗）+ 折射高光 |
| 阴影 | 统一 drop-shadow | 纵深分档，远近不同虚实 |
| 按钮 | 放大 + 换橙色 | State layer + 字阶 + 容器分组 + 位置优化 |
| 动效 | 全局 300ms fade | Ambient 慢、交互快，两套节奏 |
| 排版 | 随意 px | 字阶角色 + opsz 轴 |
| 设计系统 | 死板照搬文档 | 提取原则，按载体变通 |
| 信息密度 | 仪表盘堆满 | 极简，只留当前旅程必要信息 |

---

## 八、落地检查清单

动手前（Agent / 设计师自检）：

- [ ] **载体是什么？** 网页 / 手机 / 地图叠层 / 真眼镜？
- [ ] **参考是什么？** 项目现有系统 or 明确产品参照？
- [ ] **验收标准是什么？** 3 条以内、可观察

交稿前：

- [ ] 去掉 blur 后是否仍像白卡片？
- [ ] 背景环境色能否透出？
- [ ] 多层 UI 是否在同一平面？
- [ ] 边框是否只是 1px 描边？
- [ ] 关键操作是否够大、够近、够分组？
- [ ] 是否为了「有出处」而牺牲「适合用户」？

---

## 九、参考来源

| 主题 | 来源 |
|------|------|
| M3 Expressive 研究 | [Expressive Design: Google's UX Research](https://design.google/library/expressive-material-design-google-research) |
| 设计原则进化 | [From Minimal to Meaningful](https://design.google/library/minimal-meaningful) |
| 透明屏幕 / Glimmer | [Designing for Transparent Screens](https://design.google/library/transparent-screens) |
| 字体系统 | [Making Google Sans Flex](https://design.google/library/google-sans-flex-font) |
| 可变字体 | [Variable Fonts Are Here to Stay](https://design.google/library/variable-fonts-are-here-to-stay) |
| 包容性 | [Building for Everyone](https://design.google/library/building-for-everyone) |
| 全球无障碍 | [Designing for Global Accessibility](https://design.google/library/designing-global-accessibility-part-1) |
| 对话设计 | [Speaking the Same Language](https://design.google/library/speaking-the-same-language-vui) |
| AI 原型 | [Simulating Intelligence](https://design.google/library/simulating-intelligence) |
| 浏览器哲学 | [Refreshing Chrome](https://design.google/library/refreshing-chrome) |
| Glimmer 开发文档 | [Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer) |

---

*本文档随 Google Design 更新可迭代。原则通用，实现因项目而异。*
