# AquaGuard 设计任务 · Agent 行为规则

## 动手前必须确认（Agent 主动输出对齐单）

1. **载体**：网页 / 平板 / 手机 / 地图叠层？（默认：AquaGuard HTML 四端）
2. **参考**：`design-system/` 或用户指定
3. **验收标准**：3 条以内

## 材质决策

- 静态背景 → `ag-panel` / `ag-card`
- 地图/照片叠层 → `ag-glass`（低白度磨砂）
- 卫星图 HUD → `ag-hud-dark`

## Glimmer 迁移（非眼镜）

- 极简信息、ambient 2s 缓入、纵深三档、克制用色
- 禁止在网页上照搬眼镜黑底

## 交稿前自检

- [ ] 背景色能透出？
- [ ] 去掉 blur 后是否仍像白卡片？
- [ ] 有 far/mid/near 纵深？
- [ ] 状态有图标？
- [ ] 只用 `design-system/index.css`？

## 禁止

- 一次交付 10 个组件（先做一个确认）
- 硬编码 hex 而不用 `--ag-*` token
- 用户批评后只改 opacity 不重做材质
