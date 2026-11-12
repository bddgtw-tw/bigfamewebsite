# B release migration and content review (2026-11-12)

## Preserve existing search entry points
Source: main sitemap.xml and _redirects inspected. Existing language roots are /en/, /tw/, /jp/; B uses /en/ and /zh/ under /foundation/. Do not redirect /tw/ to an absent /zh/ route or remove Japanese pages. Current preview stays noindex. Do not deploy its directory as a replacement root.

Keep all existing about, products, services, applications, procurement, design-support, technical-resources, product-category, case and guide URLs available until a semantically equivalent page is reviewed. B currently covers only home, eyewear hook family, one historical engineering record and inquiry. Never redirect all old pages to the homepage.

Candidate mapping after review, NOT an active redirect configuration:
- /en/contact and /tw/contact: preserve URL; integrate approved inquiry experience in-place.
- /en/optical-hooks and /tw/optical-hooks: compare old product details against B product page before any replacement.
- /en/case-headphone-display-set and /tw/case-headphone-display-set: compare source records; no automatic replacement.
- All /jp/ URLs: retain existing content until reviewed Japanese B content exists.
- Existing /overview, /contact-us, /contact, /our-works, /know-how, /blog, /portfolio and download aliases: preserve current _redirects destinations.

Release checks: retain important query parameters for attribution (never personal data); validate 200/301 status and no redirect loops; add canonical URLs and reciprocal hreflang using FINAL chosen URLs; x-default homepage; regenerate sitemap only for released indexable pages, meaningful lastmod; retain legacy URLs that have no replacement; remove preview noindex only on approved production content. Compare GSC clicks/indexing and actual inquiries before/after. No ranking promise.

## Content and rights
B copy does not promise 24h response, fixed MOQ, guaranteed lead time, certification or universal Made in Taiwan origin. It identifies Taiwan-based coordination and project-specific terms. Historical record is explicitly not proof of completed delivery. The reference image exists in the repository, but original rights and exact drawing-to-image variant are not independently verified; source note stays visible. Do not add customer logos, names or testimonial claims without evidence and publication permission. Public preview is not confidential storage; noindex is not access control.

## Accessibility and CTA
Skip link, visible keyboard focus, labelled required inputs, live status, first-error focus, 48px input/button height, narrow navigation and reduced-motion rule inspected in source. Email address remains available without form JS. Physical-device, screen-reader and full WCAG assessment not certified. Mailto is an explicit user action, not a delivery receipt. Only a verified incoming message can certify successful delivery.

## Mail service gate
Two connected Gmail accounts searched for Web3Forms account messages. shopdisplay@bigfame.co has welcome email dated 2026-07-02; bddg.tw@gmail.com has no matching account message in this search. Welcome email proves registration, not current notification routing. Need authenticated read access to https://app.web3forms.com/forms/ for shopdisplay account: inspect target form's recipient(s), extra notifications and integrations without exporting keys. No access key, password or token is included here. Until then B online transport stays disabled; email fallback remains.
