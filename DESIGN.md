# BIG FAME IND. CORP. · OFFICIAL DESIGN.md
version: 3.1.0-architectural
name: BigFame-Japanese-Modern-Retail-Architecture
description: A museum-grade, Japanese architectural minimalism design system extracted and calibrated for high-end retail fixture manufacturing and bespoke B2B spatial engineering. Clean gallery-white surfaces (#ffffff / #fbfbfa) alternate with technical steel-blue accents and subtle brushed brass, driven by negative letter-spacing sans-serif typography, asymmetric editorial grids, zero generic card boilerplate, and dual CAD-to-reality viewports.

---

## 1. DESIGN PHILOSOPHY & INVARIANTS (核心不可動搖法則)
1. 100% PURE GALLERY LIGHT (零暗黑沉悶)：
   - 拒絕 Dark Mode。全站採用如同美術館般的自然光影白（Canvas: #ffffff）與極淺建築灰（#fbfbfa / #f4f4f2）。
   - 介面本身保持零彩度（黑、白、深墨、細線），讓真實材質（拉絲黃銅、冷拔鋼、白橡木、壓克力）成為畫面唯一色彩。
2. 100% SANS-SERIF MODERNISM (現代無襯線排版)：
   - 嚴禁明體、新細明體與 Serif 字體。
   - 主標題採用負字距 (Tight Tracking: -0.035em)、大行高與無襯線幾何體（Inter / Noto Sans），展現精密工程的冷冽洗練。
3. ANTI-TEMPLATE ARCHITECTURE (去模板化空間格線)：
   - 嚴禁「大圖 + 下方齊刷刷擺三張卡片」的 AI 罐頭模板。
   - 採用左 32%（縱向編輯與尺度刻度）: 右 68%（CAD-to-Reality 漸變透視畫布）非對稱格局。
4. CAD-TO-REALITY DUALITY (線稿與實景互為表裡)：
   - 線框圖 (Wireframe) 與門市實景 (Finished Scene) 並重，強化「看得見的微距收口 (0.5mm Osamari)」與「結構力學承重能力」。
5. DUAL-TRACK CONVERSION (雙軌商業閉環)：
   - 軌道 A：帶草圖/照片快速諮詢（面向設計師與品牌創辦人）。
   - 軌道 B：索取 CAD 圖集與工程白皮書（面向空間事務所與商社採購主管）。

---

## 2. COLOR TOKENS (精確色彩變數)
```yaml
colors:
  # 背景層級 (Museum Light Surfaces)
  canvas: "#ffffff"
  canvas-subtle: "#fbfbfa"
  canvas-parchment: "#f4f4f2"
  canvas-hover: "#ecece8"
  
  # 墨色與排版 (Ink Hierarchy)
  ink-main: "#111315"           # 主標題、純墨
  ink-sub: "#5a5f66"            # 內文、副標題 (60% 墨度)
  ink-dim: "#8e949e"            # 圖號、CAD標註、頁尾版權
  ink-invert: "#ffffff"         # 反白字體
  
  # 工藝邊框與結構線 (0.5mm Hairlines)
  hairline: "#e6e6e2"           # 標準分割線、卡片細邊框
  hairline-dark: "#111315"      # 聚焦邊框、主按鈕邊框
  hairline-dash: "#d2d2cc"      # 規格表點狀虛線
  
  # 精密工程點綴 (Architectural Accents)
  accent-steel: "#2a3b4c"       # 冷軋鋼色 / 遙測標籤
  accent-brass: "#b89b72"       # 霧金黃銅色 / 狀態與焦點指示
  accent-cad-cyan: "#0070f3"    # CAD 瞄準與捕捉點
```

---

## 3. TYPOGRAPHY SYSTEM (字體與字距標準)
```yaml
typography:
  display-hero:
    fontFamily: "Inter, 'Noto Sans TC', 'Noto Sans JP', system-ui, sans-serif"
    fontSize: "clamp(2rem, 3.2vw, 3.4rem)"
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: "-0.035em"
  
  display-section:
    fontFamily: "Inter, 'Noto Sans TC', 'Noto Sans JP', system-ui, sans-serif"
    fontSize: "clamp(1.6rem, 2.4vw, 2.2rem)"
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: "-0.02em"
    
  kicker-mono:
    fontFamily: "'SF Mono', Consolas, 'Courier New', monospace"
    fontSize: "0.72rem"
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: "0.2em"
    textTransform: "uppercase"
    color: "{colors.accent-steel}"
    
  lead-editorial:
    fontFamily: "Inter, 'Noto Sans TC', 'Noto Sans JP', system-ui, sans-serif"
    fontSize: "0.95rem"
    fontWeight: 300
    lineHeight: 1.8
    color: "{colors.ink-sub}"
    
  spec-table-row:
    fontFamily: "'SF Mono', Consolas, monospace"
    fontSize: "0.82rem"
    lineHeight: 1.9
```

---

## 4. COMPONENT MATRIX (組件設計字典)
```yaml
components:
  # 主導覽列 (Frosted Architectural Bar)
  nav-bar:
    background: "rgba(255, 255, 255, 0.95)"
    backdropFilter: "blur(16px)"
    borderBottom: "1px solid {colors.hairline}"
    height: "72px"
    padding: "0 48px"
    
  # 主要 CTA 按鈕 (Sharp Boxy Action)
  button-primary:
    background: "{colors.ink-main}"
    textColor: "{colors.ink-invert}"
    border: "1px solid {colors.ink-main}"
    borderRadius: "0px"
    padding: "16px 32px"
    fontSize: "0.88rem"
    fontWeight: 600
    hover:
      background: "transparent"
      textColor: "{colors.ink-main}"

  # 次要線框按鈕 (Architectural Line)
  button-line:
    background: "transparent"
    textColor: "{colors.ink-main}"
    border: "1px solid {colors.hairline}"
    borderRadius: "0px"
    padding: "12px 24px"
    hover:
      borderColor: "{colors.ink-main}"
      background: "{colors.canvas-subtle}"

  # 空間光譜按鈕 (Dimension Spectrum Buttons)
  spectrum-tick:
    background: "{colors.canvas-subtle}"
    border: "1px solid {colors.hairline}"
    borderRadius: "0px"
    padding: "12px 10px"
    active:
      background: "{colors.ink-main}"
      textColor: "{colors.ink-invert}"
      borderColor: "{colors.ink-main}"
```

---

## 5. RWD & VIEWPORT BREAKPOINTS (響應式斷點)
- Desktop (> 1024px): 32% (Left Editorial) : 68% (Right Canvas) Asymmetric Grid.
- Tablet (769px ~ 1024px): 100% Stacked layout, 32px fluid padding, Canvas min-height: 380px.
- Mobile (<= 768px): 100% Fluid with hamburger navigation drawer, full-width touch CTA targets, 20px edge padding.
