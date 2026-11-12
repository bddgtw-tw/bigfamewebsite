# Big Fame new website foundation v1

Independent bilingual vertical prototype. No existing repository, PR15 or production site was modified. Open `index.html` directly after extracting the ZIP; no installation needed. `en/` and `zh/` contain approach, product, engineering record and inquiry pages. Source text and shared layout live in build.py; run `python build.py` after edits. CSS/JS under assets. The dist directory is a preview copy, not production deployment.

## Design and scope
First screen identifies Big Fame, retail brand/design/sourcing audiences, display development and a concrete brief CTA. Deep-green/warm-neutral editorial layout uses an existing EYEHK product asset. One source-backed product family and one anonymized historical engineering record: no fake customer logos, testimonials, delivery outcomes, guaranteed lead times or Made in Taiwan claim.

Static HTML chosen over Astro for the first bounded slice: no install, no runtime dependency, understandable and maintainable, all copy crawlable without JS. Astro remains a candidate once content volume/editorial workflow and deployment ownership are settled, not an assumed requirement.

## Evidence
Product grounded in PRODUCT_EVIDENCE_READBACK_EYEHK_2026-08-04.md from existing bigfamewebsite repo: 2025 pegboard and 2018 screw/slatwall drawings. Anonymous record grounded in CASE_EVIDENCE_READBACK_HEADPHONE_DISPLAY_2026-08-04.md. Those are existing readback records, not freshly inspected original Drive PDFs. The existing product image is a reference, not verified mapping to either drawing or a completed client installation. Source notes visible in both languages. Publication rights still need final review before public release.

## Inquiry behavior
Required-field and email/URL checks, inline live feedback, first invalid field focus, safe text-only summary and client-side TXT download. No backend, fetch, tracking, cookies, persisted browser storage, real email or third-party submission. Values are cleared on navigation; changing a field invalidates the previous preview. This is NOT a production lead-capture system.

## Verified on 2026-11-12
- Node JS syntax check passed.
- Node tests: 6/6 (valid input, missing required, malformed email, unsafe URL, HTTPS, whitespace).
- Eight language pages: internal references/assets, one H1, field labels passed.
- Managed browser: English homepage rendered and visually inspected at desktop width; inquiry empty submit showed error and focused name; filled fictitious buyer values produced NOT SENT summary; EN to Chinese corresponding-page switch worked.
- Local preview served via supported sites-preview, then stopped. Its localhost address is NOT a user-accessible hosted URL.

## Not yet verified / release gates
- Actual mobile device and 10-second comprehension study, full keyboard/screen-reader audit, WCAG, performance field metrics and real-browser download completion not certified.
- Search metadata, language links and crawlable content are present, but intentionally noindex. Production canonical URLs, sitemap, indexability and redirects must be prepared for chosen host. No ranking/exposure claims.
- Real inquiry transport needs authenticated owned backend, spam/rate controls, privacy/retention statement, verified destination and consented end-to-end delivery test. Add analytics only after defining/approving measurement and consent handling.
- Original document/source rights and current commercial product availability need final review. Anonymous engineering record is NOT evidence of completed shipment.
- Production deployment, redirect preservation and rollout/reversion plan remain separate. No deployment or external message was sent.

## Follow-up non-production QA (2026-11-12)
- Expanded repeatable `node --test test.cjs` suite to 16 tests, all passing: eight localized pages' links/metadata/headings, dist-source consistency, no outgoing submission/storage APIs, disabled-by-default submit and mobile navigation.
- Fixed narrow-screen navigation: all four links now wrap into two rows with 44px minimum target height, instead of hiding the inquiry link in a horizontal scroll strip.
- Disabled the submit button in generated HTML; the local-only JavaScript enables it only after event handlers are installed. This prevents ordinary implicit form submission while the demo script is unavailable.
- Browser-tested the English inquiry in a 390px-wide iframe (375px content viewport after scrollbar): no horizontal document overflow; empty input shows error/focus; synthetic valid input produces explicit NOT SENT summary; changing company hides the stale summary; language link reaches the corresponding empty Chinese inquiry page. This is narrow-layout testing, not physical-device certification.
- Attempted real browser TXT download: the automation download wait timed out and reset; file completion remains unverified. No customer inquiry was sent.
- Cloudflare dashboard remains sign-in gated at this check; another authorized task is coordinating sign-in. No DNS, release, access-control or routing changes were made.
- Still no backend, verified new-site mailbox delivery, production analytics, production/rollback mapping or traffic experiment. PR15/16 apply to the older site and cannot certify this new prototype.


## 2026-11-12 integration draft
Packaged under /foundation/ on isolated branch. Existing website remains unchanged. Added a visible email inquiry fallback on every substantive page, available without JavaScript. Local brief generator remains explicitly NOT SENT. Real submission remains blocked until independent end-to-end receipt verification; never infer mailto click equals lead receipt. Preview remains noindex. Original image rights and content review gates remain. Production rollback reference: main ec40b9d1ae114c5779fdb4765529dbde52bb66a8, Cloudflare deployment df16c993-c6ad-4342-b238-5d9d17a11d3e. Do not deploy over production.
