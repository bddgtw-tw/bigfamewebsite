# Changelog

All notable changes to the Big Fame IND. CORP. website project will be documented in this file.

The project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.5] - 2026-07-11

### Changed
- Rewrote all four Case Study cards on `applications.html` (TW only for now) from supplier-perspective language to **buyer pain-point language** based on `TARGET_PERSONA.md`.
- Each case now maps to a specific store archetype: Type A (lifestyle/variety retail), Type B (sporting goods), Type C (eyewear), Type D (drugstore/beauty).
- Added gold **「適合店型」label** above each case title for instant visitor self-identification, without ever explicitly naming client brands.
- Rewrote Case 04 entirely around the **drugstore/beauty persona (Type D)**: gondola, lit vanity display counters, price rails, acrylic tester stands, end cap fixtures—all from one supplier.
- NDA notice shortened to be direct and inviting ("如果你正好遇到同樣的問題，歡迎直接聯絡我們").
- Incremented `SITE_VERSION` constant to `'1.3.5'` in `js/main.js`.

## [1.3.4] - 2026-07-10

### Changed
- Enriched the Applications page (`applications.html` across all languages) with B2B technical tag chips (e.g. `SPCC Cold-Rolled Steel`, `Automated Welding`, `96H NSS Salt Spray Test`) for each Case Study.
- This adds detailed engineering credibility and content depth while maintaining the clean, flat 2-column image layout.
- Incremented `SITE_VERSION` constant to `'1.3.4'` in `js/main.js`.

## [1.3.3] - 2026-07-10

### Changed
- Restored the 6-step project timeline layout on the Services page (`services.html` across all languages) as requested, while redesigning it to be highly premium, minimalist, and straight-edged.
- Removed circles from timeline step numbers, converting them to strictly square outline boxes in line with the brand rules.
- Inserted a 3-column "B2B Service Promises" grid at the top of the timeline section to add depth and enrich the layout with key value points.
- Incremented `SITE_VERSION` constant to `'1.3.3'` in `js/main.js`.

## [1.3.2] - 2026-07-10

### Changed
- Replaced the boring text timeline on the Services subpage (`services.html` across all languages) with a rich, curated **Alternate Gallery Layout** matching nendo's portfolio grid.
- Associated the 4 major phases of Big Fame's turn-key B2B service integration with real, high-quality local factory and QC footage (`factory_cnc.jpg`, `factory_welding.jpg`, `factory_finishing.jpg`, `factory_loading.jpg`).
- Incremented `SITE_VERSION` constant to `'1.3.2'` in `js/main.js`.

## [1.3.1] - 2026-07-10

### Fixed
- Added a `margin-top: var(--header-height)` offset to `.breadcrumbs` to resolve fixed header overlay issues on subpages, preventing the breadcrumbs bar from overlapping with the logo and nav links.
- Incremented `SITE_VERSION` constant to `'1.3.1'` in `js/main.js`.

## [1.3.0] - 2026-07-10

### Changed
- Reverted all heading font families back to **Shippori Mincho** (明朝體) with a weight of `400` and restricted letter-spacing to `0.02em` for Chinese characters to restore authentic Japanese craftsmanship brand feel.
- Modified `--bg-secondary` to a light warm-gray (`#f8f7f4` for light theme; `#151413` for dark theme) to add subtle contrast layer between sections.
- Compacted spacings: reduced `.section` padding from `100px` to `80px`, and `.gallery-item` margin-bottom from `120px` to `60px`.
- Decreased body `line-height` from `1.8` to `1.6` for tighter, more structured content flow.
- Incremented `SITE_VERSION` constant to `'1.3.0'` in `js/main.js`.

## [1.2.4] - 2026-07-10

### Changed
- Configured HTML5 `<video>` background source elements in `tw/index.html`, `en/index.html`, and `jp/index.html` to prioritize a local self-hosted video file (`../videos/hero_bg.mp4`) before falling back to remote Mixkit CDN URLs.
- Created `videos/` folder inside the project to allow dropping in custom brand videos directly.
- Incremented `SITE_VERSION` constant to `'1.2.4'` in `js/main.js`.

## [1.2.3] - 2026-07-10

### Changed
- Replaced traditional/retro Japanese serif font (Shippori Mincho) with contemporary sans-serif font family (`Outfit` and `Noto Sans JP`) for all headings to establish a sharper, more "modern/tech-forward" luxury brand presentation.
- Set heading font-weight to `300` and letter-spacing to `0.06em` to maintain refined luxury elegance.
- Incremented `SITE_VERSION` constant to `'1.2.3'` in `js/main.js`.

## [1.2.2] - 2026-07-10

### Changed
- Removed all `linear-gradient` overlays across the website (including hero banners and project showcase cards) to eliminate tacky gradient effects and transition to pure flat, solid-color styling.
- Repositioned portfolio/project texts to display cleanly below images rather than inside overlay hover boxes.
- Incremented `SITE_VERSION` constant to `'1.2.2'` in `js/main.js`.

## [1.2.1] - 2026-07-10

### Added
- Integrated premium Japanese serif typography **Shippori Mincho** (`--font-title`) for all headers and titles to give a sense of high-end craftsmanship.
- Created B2B client sectors wall block below the trust metrics bar to display segment social proof (e.g. `/ 日本最大連鎖眼鏡品牌 / 歐美頂尖運動通路 /` etc.) in a highly clean and refined manner.
- Set stylesheet cache buster versions in all index files (`tw/index.html`, `en/index.html`, `jp/index.html`) and subpages to force client browser updates.

### Changed
- Incremented `SITE_VERSION` constant to `'1.2.1'` in `js/main.js`.

## [1.2.0] - 2026-07-10

### Added
- Redesigned site aesthetic to a Japanese Minimalist Clean style (inspired by nendo, sinato, and Schemata).
- Replaced font-family integration with Google Fonts 'Outfit' and 'Noto Sans JP' with lightweight weights (200, 300, 400).
- Simplified color variables in `css/style.css` to pure minimalist tones (pure white `#ffffff` backgrounds, neutral thin borders, charcoal black accents).
- Removed all cards border-radius, shadows, gradients, and translation lifting hover animations for `.product-card`, `.app-card`, and `.location-card`.
- Re-styled the Home trust metrics bar with vertical divider lines and thin weight 300 typography.
- Adjusted all form input labels to weight 400 for a lighter visual footprint.

### Changed
- Incremented `SITE_VERSION` constant to `'1.2.0'` in `js/main.js`.

## [1.1.1] - 2026-07-10

### Added
- Integrated high-quality, loopable, muted HTML5 background video (showing premium retail store boutique shopfront) in the Hero section of the homepage for all three languages (`tw/index.html`, `en/index.html`, `jp/index.html`).
- Set local premium industrial image `hero_display_fixture.jpg` as the fallback poster and background image for browsers or situations where background video cannot be autoplayed or loaded.
- Created CSS style rules `.hero-video` with `object-fit: cover` and `z-index` layering inside `css/style.css`.

### Changed
- Incremented `SITE_VERSION` constant to `'1.1.1'` in `js/main.js`.

## [1.1.0] - 2026-07-10

### Added
- Created trust metrics badges section showing industry status ("38+ Years", "3 Global Bases", "100% Japan QA Standard") across all language homepages (`tw/index.html`, `en/index.html`, `jp/index.html`).
- Added page breadcrumbs to subpages for structured, accessible navigation.
- Added direct phone call CTA buttons (`+886-2-2311-8601`) to all page headers.
- Integrated LinkedIn social company link with SVG icon into all page footers.
- Generated and saved 9 realistic industrial and product images in the local `images/` directory to replace Unsplash placeholders:
  - `hero_display_fixture.jpg` (Hero/Fixtures)
  - `factory_cnc.jpg` (About/CNC Factory)
  - `factory_welding.jpg` (Welding)
  - `factory_finishing.jpg` (Finishing Line)
  - `factory_loading.jpg` (Consolidation/Loading)
  - `product_fixtures.jpg` (Fixtures Category)
  - `product_hooks.jpg` (Hooks & Accessories Category)
  - `product_pos.jpg` (POS & POP Displays Category)
  - `product_parts.jpg` (Custom Components Category)
- Added Minimum Order Quantity (MOQ) and production lead time info cards on the Capabilities pages across all languages.
- Restructured Applications pages with 4 B2B case studies mapping back to realistic OEM/ODM requirements and local image assets.
- Appended a glassmorphic success/error toast notification for Web3Forms feedback.
- Added direct email fallback hints below Web3Forms contacts for failed submissions.

### Changed
- Incremented `SITE_VERSION` constant to `'1.1.0'` in `js/main.js`.
- Corrected schema organization URL and logo domain reference to `https://www.bigfame.co` inside all homepages.
- Patched click event listener in `js/main.js` page transitions to allow Ctrl/Cmd/Shift/middle-click navigation to bypass transition logic.
- Standardized page banner padding-top to `60px` when breadcrumbs are present to balance vertical spacing.
