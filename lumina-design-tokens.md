---
name: Lumina Safety System
colors:
  surface: '#fbf8ff'
  surface-dim: '#dbd9e0'
  surface-bright: '#fbf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f2fa'
  surface-container: '#efedf4'
  surface-container-high: '#e9e7ef'
  surface-container-highest: '#e3e1e9'
  on-surface: '#1b1b21'
  on-surface-variant: '#454651'
  inverse-surface: '#2f3036'
  inverse-on-surface: '#f2f0f7'
  outline: '#757682'
  outline-variant: '#c5c5d3'
  surface-tint: '#4659a9'
  primary: '#001760'
  on-primary: '#ffffff'
  primary-container: '#182e7d'
  on-primary-container: '#879aee'
  inverse-primary: '#b8c4ff'
  secondary: '#8d4f00'
  on-secondary: '#ffffff'
  secondary-container: '#fea54c'
  on-secondary-container: '#6f3d00'
  tertiary: '#3d1300'
  on-tertiary: '#ffffff'
  tertiary-container: '#602200'
  on-tertiary-container: '#e3875c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b8c4ff'
  on-primary-fixed: '#001454'
  on-primary-fixed-variant: '#2c408f'
  secondary-fixed: '#ffdcc0'
  secondary-fixed-dim: '#ffb876'
  on-secondary-fixed: '#2d1600'
  on-secondary-fixed-variant: '#6b3b00'
  tertiary-fixed: '#ffdbcd'
  tertiary-fixed-dim: '#ffb595'
  on-tertiary-fixed: '#350f00'
  on-tertiary-fixed-variant: '#76320e'
  background: '#fbf8ff'
  on-background: '#1b1b21'
  surface-variant: '#e3e1e9'
typography:
  headline-lg:
    fontFamily: Hanken Grotesque
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Hanken Grotesque
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Hanken Grotesque
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesque
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: Hanken Grotesque
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 20px
  label-sm:
    fontFamily: Hanken Grotesque
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is built for mission-critical clarity and unwavering reliability. It follows a **Corporate / Modern** aesthetic, prioritizing legibility and functional hierarchy above all else. The brand personality is authoritative yet accessible, designed to evoke a sense of security and precision in safety-critical environments.

The visual language utilizes high-contrast color blocking and precise geometric alignment to ensure that critical information is never missed. By combining the deep, trustworthy tones of "Starry Purple" with the urgent, high-visibility "Tango Orange," the UI creates a psychological landscape of "Control" and "Awareness."

## Colors

The palette is anchored by **Starry Purple (#182E7D)**, used for primary navigation, headers, and stable UI elements to communicate strength and depth. **Tango Orange (#F79F47)** serves as the high-visibility accent for calls-to-action, warnings, and safety-critical status indicators. 

The system utilizes **Pure White (#FFFFFF)** for all base surfaces to maximize contrast and maintain a clean, clinical workspace. Neutral tones are derived from a cool-grey scale to complement the primary purple, ensuring that structural elements like borders and disabled states do not compete with critical information.

## Typography

The design system exclusively uses **Hanken Grotesque**, a contemporary sans-serif known for its exceptional legibility and geometric clarity. 

- **Headlines:** Use Bold weights to create a clear information hierarchy.
- **Safety Labels:** Critical data points use the `label-bold` style with uppercase casing to ensure they stand out in high-stress situations.
- **Body Text:** Maintained at a minimum of 16px to ensure accessibility across various viewing distances.
- **Mobile Scaling:** For mobile devices, `headline-lg` should scale down to 24px to prevent excessive wrapping while maintaining its semantic importance.

## Layout & Spacing

This design system employs a **Fluid Grid** model based on an 8px square baseline. 

- **Desktop:** 12-column grid with 24px gutters and 32px side margins.
- **Tablet:** 8-column grid with 16px gutters and 24px side margins.
- **Mobile:** 4-column grid with 12px gutters and 16px side margins.

Horizontal and vertical rhythm is maintained by using multiples of 8px for all padding and margin tokens. This ensures a predictable, structured layout that reduces cognitive load when scanning complex data dashboards.

## Elevation & Depth

Visual hierarchy is established through **Tonal Layers** and **Low-contrast Outlines** rather than aggressive shadows. 

1. **Base:** Pure White (#FFFFFF) for the main background.
2. **Surface:** Light grey (F8FAFC) for secondary containers and sidebars.
3. **Overlays:** Modals and tooltips use a very soft, diffused shadow (0px 4px 20px rgba(24, 46, 125, 0.08)) to lift them above the content without introducing visual clutter.
4. **Borders:** 1px solid strokes in a light-medium grey are used to define boundaries between data clusters, ensuring clear separation without the weight of heavy shadows.

## Shapes

Following the "Round Eight" principle, the design system utilizes a **Rounded (8px)** corner radius for all standard UI components. This balance of geometric precision and softened edges provides a professional look that feels modern and approachable.

- **Standard Elements:** 0.5rem (8px) radius.
- **Large Containers/Cards:** 1rem (16px) radius.
- **Badges/Chips:** Full pill (999px) for distinct visual separation from data fields.

## Components

- **Buttons:** 
    - **Primary:** Starry Purple background with White text.
    - **Secondary/Safety:** Tango Orange background with Navy/Black text for maximum contrast.
    - **Outline:** 2px stroke of Starry Purple with matching text.
- **Input Fields:** Use an 8px radius with a 1px Grey border. On focus, the border transitions to Starry Purple with a 2px thickness.
- **Chips:** Used for filtering and status. "Active" status chips should use Tango Orange to draw the eye immediately.
- **Cards:** White background, 1px border (Grey-200), and an 8px (rounded-lg) corner radius. Cards should have consistent internal padding of 24px (md spacing).
- **Status Indicators:** Use Tango Orange for "Alert" or "Warning" states. Critical errors must pair color with a heavy icon to ensure accessibility for colorblind users.
- **Lists:** High-density rows with 1px bottom dividers and 12px vertical padding to maintain data density without sacrificing readability.