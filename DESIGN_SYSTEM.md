# BIG FAME IND. CORP. · DESIGN SYSTEM SPECIFICATION (DESIGN_SYSTEM.md)
Version: 3.0.0 (Japanese Modern Architectural Edition)
Target: High-End B2B Store Display Equipment & Custom Engineering

---

## 1. CORE PHILOSOPHY: ARCHITECTURAL PURITY (建築純粹主義)
- 100% PURE WHITE & AIRY LIGHT: Zero dark-mode gloom. All background layers breathe with crisp, natural gallery light.
- 100% SANS-SERIF TYPOGRAPHY: Zero serif / MingTi / Times fonts. Crisp geometric modernism inspired by Neue Haas Grotesk, Inter, and Noto Sans.
- NO ARTIFICIAL TEMPLATES: Strictly ban generic "Hero banner + 3 cards" boilerplate. Employ asymmetric editorial grids, dimensional spectrum scales, and interactive viewport overlays.
- CAD-TO-REALITY DUALITY: Treat wireframe engineering drawings and finished photography as equal design citizens.
- PRODUCT IS COLOR: All chrome/UI elements remain strictly monochrome (black, white, technical steel slate). Only authentic materials (natural brass, cold-rolled steel, FAS oak wood, acrylic) bring color.

---

## 2. COLOR TOKENS (色彩語彙)
```css
:root {
  /* Surface Layers (明亮純粹展廳色) */
  --bf-bg-pure: #ffffff;
  --bf-bg-canvas: #fbfbfa;
  --bf-bg-subtle: #f4f4f2;
  --bf-bg-hover: #ecece8;

  /* Typography & Ink (極限對比層級) */
  --bf-ink-main: #111315;       /* 主標題與深墨字體 */
  --bf-ink-sub: #5a5f66;        /* 說明文案與次級內文 */
  --bf-ink-dim: #8e949e;        /* 技術參數、圖號、次要備註 */
  --bf-ink-invert: #ffffff;     /* 反白文字 */

  /* Structural Lines & Borders (0.5mm 建築細線) */
  --bf-border-light: #e6e6e2;   /* 卡片與隔線細線 */
  --bf-border-dark: #111315;    /* 重點按鈕與焦點框線 */
  --bf-border-dash: #d2d2cc;    /* 規格參數虛線 */

  /* Architectural Accents (精密微量點綴) */
  --bf-accent-steel: #2a3b4c;   /* 工業冷軋鋼色 / CAD 圖紙遙測標籤 */
  --bf-accent-brass: #b89b72;   /* 頂級黃銅五金金色 / 狀態指示器 */
  --bf-accent-cyan: #0070f3;    /* 數位孿生微光亮點 */
}
```

---

## 3. TYPOGRAPHY SYSTEM (無襯線排版法典)
```css
:root {
  --bf-font-sans: 'Inter', 'Noto Sans TC', 'Noto Sans JP', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --bf-font-mono: 'SF Mono', 'JetBrains Mono', Consolas, Menlo, monospace;
}

/* 階層規格 */
h1.bf-hero-title {
  font-family: var(--bf-font-sans);
  font-size: clamp(2.2rem, 3.8vw, 3.8rem);
  font-weight: 400;
  line-height: 1.12;
  letter-spacing: -0.035em;
  color: var(--bf-ink-main);
}

h2.bf-section-title {
  font-family: var(--bf-font-sans);
  font-size: clamp(1.8rem, 2.6vw, 2.6rem);
  font-weight: 400;
  line-height: 1.2;
  letter-spacing: -0.025em;
}

.bf-meta-kicker {
  font-family: var(--bf-font-mono);
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--bf-accent-steel);
}

p.bf-lead {
  font-size: 1.05rem;
  font-weight: 300;
  line-height: 1.8;
  color: var(--bf-ink-sub);
}
```

---

## 4. ASYMMETRICAL SPATIAL GRID (非對稱空間格線)
- Desktop Viewport: 32% (Editorial Left Column) : 68% (Interactive Right Viewport).
- Tablet (<= 1024px): 100% Stacked layout with 32px fluid padding.
- Mobile (<= 768px): 100% Fluid with full-bleed touch targets and dedicated sticky navigation drawer.
- Card Border Radii: Strictly `0px` sharp corners everywhere to reflect industrial metal craftsmanship.

---

## 5. DUAL-TRACK CONVERSION (雙軌商業閉環)
- Track A (Creative / Designer): Rapid sketch/CAD file upload with 24h technical feasibility audit.
- Track B (Procurement / Space Agency): Direct architectural dossier download (CAD library, K/D flat-pack specification).
