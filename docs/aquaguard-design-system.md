# AquaGuard 设计系统（Lumina DS）

> 北海银滩智能救援系统前端设计资产。  
> 载体：网页 HTML 四端（指挥 / 平板 / 手机 / 游客），非 AR 眼镜。

---

## 文件结构

```
design-system/
  index.css              ← 统一入口，页面只需引这一个
  tokens.css             ← 颜色、字体、间距、动效 token
  material/glass.css     ← 磨砂材质 + 纵深三档
  components/
    button.css           ← 按钮、分割按钮
    chip.css             ← 状态徽章
    card.css             ← 卡片、指标、进度条
    feedback.css         ← 告警、导航、工具条
    hud.css              ← 地图透明叠层

docs/
  aquaguard-design-system.md     ← 本文档
  glimmer-frontend-principles.md ← Glimmer/AI眼镜 → 前端迁移（重点）
  universal-design-guide.md      ← Google 设计通用指南
  cursor-design-rules.md         ← Cursor Agent 规则
```

## 快速开始

```html
<link rel="stylesheet" href="design-system/index.css">
```

```html
<button class="ag-btn ag-btn--emergency">
  <span class="material-symbols-outlined fill">directions_run</span>
  出发救援
</button>
```

---

## 品牌

| Token | 值 | 用途 |
|-------|-----|------|
| `--ag-primary` | #182E7D | 星夜紫 · 导航、结构 |
| `--ag-secondary` | #F79F47 | 活力橙 · 紧急、警告 |
| `--ag-error` | #BA1A1A | 危险、SOS |
| `--ag-safe` | #16A34A | 安全、进行中 |

---

## 字体

| 场景 | 字体 |
|------|------|
| 正文 | Hanken Grotesk |
| 标题 / 数字 | Google Sans Flex |
| 图标 | Material Symbols Outlined |

字阶类：`.ag-type-display-lg` · `.ag-type-headline` · `.ag-type-body` · `.ag-type-label-sm`

---

## 材质选择

| 类名 | 场景 |
|------|------|
| `.ag-panel` | 指挥端侧栏、实心磨砂卡片 |
| `.ag-glass` | 地图/照片叠层基础材质 |
| `.ag-glass--far` | 背景通知（远层） |
| `.ag-glass--mid` | 主信息卡（中层） |
| `.ag-glass--near` | 主操作按钮（近层） |
| `.ag-hud-dark` | 卫星图暗底 HUD |

详见 [Glimmer 前端迁移原则](./glimmer-frontend-principles.md)

---

## 组件清单

### 按钮 `ag-btn`
- `ag-btn--primary` 主操作
- `ag-btn--emergency` 紧急（56px 全宽）
- `ag-btn--outline` 次要
- `ag-btn--ghost` 幽灵
- `ag-btn--icon` 图标
- `ag-btn-group` 分割按钮

### 徽章 `ag-chip`
- `--emergency` `--waiting` `--active` `--danger` `--live`

### 卡片 `ag-card`
- `--emergency` 左侧橙条
- `--active` 左侧绿条
- `ag-metric` / `ag-progress` 指标与进度

### 反馈 `ag-alert` · `ag-nav-step` · `ag-toolbar`

### 地图 HUD `ag-hud`
完整叠层组件，见 `aquaguard-ds-demo.html`

---

## 间距与圆角

- 间距：8px 基准，`--ag-space-1` (4px) 到 `--ag-space-7` (48px)
- 圆角：`--ag-radius-sm` (8px) 到 `--ag-radius-pill`

---

## 动效

| Token | 值 | 用途 |
|-------|-----|------|
| `--ag-duration-ambient` | 2000ms | 通知缓入 |
| `--ag-duration-fast` | 120ms | 交互反馈 |
| `--ag-ease` | cubic-bezier(0.2,0,0,1) | 强调缓动 |

---

## 无障碍

- 触控目标 ≥ 48px，紧急 ≥ 56px
- 状态色 + 图标双编码
- `prefers-reduced-motion` 已内置降级
- 现场端正文 ≥ 16px

---

## 与旧文件关系

| 旧文件 | 状态 |
|--------|------|
| `aquaguard-lumina.css` | 存量页面仍用，逐步迁移 |
| `aquaguard-glass.css` | 存量页面仍用，材质已提炼到 `design-system/` |
| `aquaguard-m3-components.css` 等 | 实验稿，已被 DS 取代 |

**新页面请只用 `design-system/index.css`**

---

## 外部参考

- [Material 3 Figma Kit](https://www.figma.com/community/file/1035203688168086460/material-3-design-kit)
- [Material Theme Builder](https://m3.material.io/theme-builder)
- [通用设计指南](./universal-design-guide.md)
