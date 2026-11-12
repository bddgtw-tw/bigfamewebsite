# A production / B preview validation

This branch adds read-only verification, not a release or A/B test. Built on PR15's actual remote commit 0b7a7bd, isolated from the earlier local working branch and independent foundation-v1 prototype. Production and DNS are unchanged. Do not merge to main just to enable scheduled checks: existing main workflows can deploy websites.

## Run

`npm test`

`python3 scripts/validate_release.py --base https://www.bigfame.co --mode production --output production-check.json`

`python3 scripts/validate_release.py --base https://cb67d3bd.bigfamewebsite.pages.dev --mode preview --output preview-check.json`

Only GETs six public language home/contact pages, no form submission, storage/cookies or analytics events. Records URL/status/content hash, indexability, canonical and form action. HTTP success is NOT delivery, browser QA, accessibility, ranking or conversion certification. Reports always have release_approved=false. Network failures mean check blocked, not proof of outage.

CI runs tests and the read-only production check on relevant PR changes; manual workflow is included. No recurring job is activated by this branch. Any separate scheduler must explicitly be verified before promising daily monitoring. Review artifacts even when the check fails.

## Evidence and hard gates

PR15 is still draft/open. Cloudflare bot confirms its preview deployment, not the production domain's project or release. Six PR15 preview pages also returned 200 with noindex. Their forms still point to the real Web3Forms endpoint: do not submit from preview without an approved test and destination. Six production pages were readable (200, one H1, canonical, no noindex) in the initial check. Their raw HTML hashes did not match corresponding files at either known main ec40b9d or PR15 0b7a7bd; transformations or another source may explain this. Do NOT infer a deployed commit from headers or URL alone. Check authenticated Cloudflare Pages custom domains, production branch, deployment ID and commit. Production owner/session access is currently unavailable.

Fill release-gates.json only with observed evidence. Until production source and known-good production rollback target are verified, no promotion, route changes, live traffic experiment or rollback drill against live site. Cloudflare preview deployment is not a valid production rollback target.

Next manual gates: desktop and narrow viewport all languages; menu/keyboard/validation/errors/retry; approved synthetic inquiry to owned destination and actual mailbox receipt with source fields; analytics accepted/qualified events deduplicated and no personal/free-text/drawing URLs; source rights/commercial claims; canonical/hreflang/redirect inventory; then explicit human release review. Never send test customer data or modify security/permissions to unblock.

## Future experiment contract (disabled)

First establish baseline and instrument the full inquiry path. Main measure: deduplicated qualified inquiries per eligible visitor; define qualification before looking at variants, excluding vendor pitches/spam/internal tests. CTA clicks and form starts are diagnostics. Track errors, delivery, mobile/performance and privacy as guardrails. Stable anonymous assignment across return visits; bot rules identical across variants; document cross-device limits. No personal data in analytics.

90/10 is a small-risk canary, not a promise of a weekly winner. Set a hypothesis, frozen version, eligibility, minimal useful effect, sample/duration and maturation window in advance; check sample-ratio mismatch. Daily checks diagnose safety/data issues, weekly reviews can conclude insufficient evidence. No auto-promotion based on small counts or repeated p-value peeking. Keep a human-approved release and rollback record. Private/noindex preview and public experiment canonical rules are separate.
