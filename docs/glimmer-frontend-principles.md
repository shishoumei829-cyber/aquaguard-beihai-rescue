# Glimmer 设计原则 · 前端可迁移版

> 提炼自 Google Jetpack Compose Glimmer（AI 眼镜透明显示）设计研究与文章。  
> **核心观点：Glimmer 解决的是「注意力经济」和「叠层可读性」问题，这些问题在网页、地图 HUD、移动端同样存在。**

---

## 一、什么该迁移，什么不该迁移

| Glimmer 原文规则 | 眼镜载体 | 前端可迁移 |
|------------------|----------|------------|
| 黑 = 透明，暗底亮字 | ✅ 必须 | ⚠️ 仅地图/视频叠层场景 |
| 禁止高饱和色大面积使用 | ✅ 必须 | ✅ 动态背景上的 UI |
| 视觉角度排版（度） | ✅ 必须 | ✅ 转化为「扫读字号」策略 |
| 纵深 depthEffect | ✅ 必须 | ✅ 空间卡片、浮层 |
| Ambient 2s 缓入 | ✅ 必须 | ✅ 通知、告警条 |
| 交互 0ms 反馈 | ✅ 必须 | ✅ 按钮 focus/active |
| 极简信息密度 | ✅ 必须 | ✅ 所有端 |
| 去掉 blur 用纯黑底 | ✅ 必须 | ❌ 网页用磨砂 + 低白度 |

---

## 二、七条可迁移原则

### 1. Earn the Glance（值得看一眼）

用户注意力是稀缺资源——无论眼镜还是手机。

**前端做法：**
- 一屏只回答一个问题
- 地图 HUD 只显示当前任务关键数（距离、状态）
- 指挥端让地图做主角，侧栏可折叠
- 删掉「好看但非当前旅程必要」的元素

**反模式：** 仪表盘堆满指标、每个角都有信息

---

### 2. Ambient vs Interactive 双速动效

Glimmer 发现：通知 500ms 太快像「闪一下」；用户操作反馈必须即时。

| 类型 | 时长 | 场景 |
|------|------|------|
| Ambient | 1.5–2s | SOS 告警、新事件推入、状态变化提示 |
| Interactive | 0–120ms | 按钮按下、focus ring、选中态 |

**CSS 变量：**
```css
--ag-duration-ambient: 2000ms;
--ag-duration-fast: 120ms;
```

**反模式：** 所有动效统一 300ms fade

---

### 3. Depth as Hierarchy（纵深即层级）

高级感来自前后关系，不是 drop-shadow 统一糊一层。

**三档纵深（已在 `ag-glass--far/mid/near` 实现）：**

| 档位 | 场景 | 特征 |
|------|------|------|
| far | 背景通知、次要提示 | 更透明、更模糊、更小、阴影更虚 |
| mid | 主信息卡片 | 中等透明度 |
| near | 主操作按钮 | 更不透明、更近、阴影更实、可叠在卡片上 |

**前端做法：**
- 按钮叠在卡片右上角，而不是塞在卡片内部角落
- 浮层工具条独立于内容卡
- `transform: translateY + scale` 微调纵深感

---

### 4. Glanceable Typography（扫读排版）

Glimmer 用视觉角度（0.6° 最小）；前端转化为字号策略：

| 角色 | 用途 | 建议 |
|------|------|------|
| Display | 关键数字（距离、待派遣数） | 32–42px |
| Title | 事件标题 | 18px+ |
| Body | 正文 | 16px 下限（现场端） |
| Label | 次要标签 | 11–12px，仅在有足够对比衬托时用 |

**原则：** 数字要大、标签要小、层级靠尺寸不靠颜色堆砌

---

### 5. Restrained Color（克制用色）

高饱和色在复杂背景（地图、照片、渐变）上会「消失」或刺眼。

**前端做法：**
- 界面默认中性（白/磨砂/深灰）
- 橙色 / 红色**只**用于：紧急、待处理、SOS
- 强调色面积 < 15%
- 状态必须 **颜色 + 图标** 双编码

**AquaGuard token：**
- `--ag-secondary` 仅用于紧急行动
- `--ag-primary` 用于稳定结构

---

### 6. Material as Environment（材质即环境）

Glimmer 的「黑=容器」在网页上映射为：**材质随场景切换**

| 场景 | 材质 |
|------|------|
| 指挥端侧栏、弹层 | `ag-panel` 实心磨砂 |
| 地图 / 照片叠层 | `ag-glass` 低白度磨砂 |
| 卫星图 HUD | `ag-hud-dark` 暗底亮字 |

**判断标准：** 背后是什么？动态复杂 → 磨砂或暗底；静态浅色 → 实心面板

---

### 7. Focus Ring Instant（即时确认）

用户操作后必须立刻知道「系统收到了」。

**前端做法：**
```css
.ag-btn:focus-visible {
  outline: 2px solid var(--ag-secondary);
  outline-offset: 2px;
  transition: outline 0ms; /* 不要延迟 */
}
```

- 不用 ripple 延迟代替确认
- 选中态变化 < 120ms
- 湿手 / 户外场景按钮 ≥ 48px，紧急 ≥ 56px

---

## 三、组件映射表

| Glimmer 概念 | AquaGuard 组件 | 文件 |
|--------------|----------------|------|
| Ambient 通知 | `.ag-alert` + `.ag-glass--far` | `feedback.css` |
| 信息卡片 | `.ag-hud__card` + `.ag-glass--mid` | `hud.css` |
| 主操作 | `.ag-btn--emergency` + `.ag-glass--near` | `button.css` |
| 纵深材质 | `.ag-glass--far/mid/near` | `glass.css` |
| 状态芯片 | `.ag-chip--*` | `chip.css` |
| 暗底 HUD | `.ag-hud-dark` | `hud.css` |

---

## 四、场景决策树

```
UI 叠在什么上？
├─ 静态浅色背景 → ag-panel / ag-card
├─ 地图 / 照片 / 视频 → ag-glass（低白度磨砂）
└─ 卫星图 / 高对比动态 → ag-hud-dark（暗底亮字）

这个信息有多紧急？
├─ 背景感知 → ag-glass--far + ambient 2s 入场
├─ 当前任务 → ag-glass--mid
└─ 立即行动 → ag-btn--emergency + ag-glass--near

用户需要多快看到？
├─ 扫一眼 → display 大号数字
├─ 读一句 → title 18px+
└─ 操作 → 56px 按钮
```

---

## 五、自检清单（从 Glimmer 迁移）

- [ ] 一屏是否只传达一个核心信息？
- [ ] 通知是否用 ambient 慢速入场？
- [ ] 按钮反馈是否即时？
- [ ] 浮层是否有 far/mid/near 纵深？
- [ ] 强调色是否克制？
- [ ] 状态是否有图标？
- [ ] 地图叠层是否透出背景色？
- [ ] 是否误用了眼镜专用黑底（在普通网页上）？

---

*参考：[Designing for Transparent Screens](https://design.google/library/transparent-screens) · [Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer)*
