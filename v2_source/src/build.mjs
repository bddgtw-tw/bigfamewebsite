import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..');
const dataPath = path.join(rootDir, 'content', 'site-data.json');
const distDir = path.join(rootDir, 'dist');

const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
const { brand, languages, langLabels, ui, cases } = data;

// Pure, immutable URL helpers (structurally prevents slug/year stacking bugs)
function pageUrl(lang, subpath = '') {
  const clean = subpath.replace(/^\/+|\/+$/g, '');
  return clean ? `/${lang}/${clean}/` : `/${lang}/`;
}

function caseUrl(lang, slug) {
  return `/${lang}/cases/${slug}/`;
}

function esc(str = '') {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function webImg(src) {
  if (!src || !src.endsWith('.png')) return src;
  const webpRel = src.replace(/\.png$/, '.webp');
  const full = path.join(distDir, webpRel.replace(/^\/+/, ''));
  return fs.existsSync(full) ? webpRel : src;
}

function writeHtml(relPath, html) {
  const full = path.join(distDir, relPath);
  fs.mkdirSync(path.dirname(full), { recursive: true });
  fs.writeFileSync(full, html, 'utf8');
}

function fontLinksFor(lang) {
  let href = 'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Inter:wght@400;500;600&display=swap';
  if (lang === 'jp') {
    // Use native Japanese system sans-serif (Hiragino / Yu Gothic) for body; load only Shippori Mincho 500 async for serif headings
    href = 'https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@500&display=swap';
  } else if (lang === 'tw') {
    // Use native TC system sans-serif (PingFang TC / JhengHei) for body; load only Noto Serif TC 500 async for serif headings
    href = 'https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@500&display=swap';
  }
  return `<link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="${href}" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="${href}"></noscript>`;
}

function renderLayout({ lang, title, description, activeNav, subpath, ogImage, bodyHtml }) {
  const t = ui[lang];
  const canonicalPath = pageUrl(lang, subpath);
  const canonicalUrl = `${brand.domain}${canonicalPath}`;
  const ogImgUrl = `${brand.domain}${ogImage || '/assets/images/hero-veltor-island.webp'}`;
  const ogLocale = lang === 'jp' ? 'ja_JP' : lang === 'tw' ? 'zh_TW' : 'en_US';

  const orgJsonLd = JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: brand.legal,
    alternateName: brand.name,
    url: brand.domain,
    foundingDate: brand.founded,
    email: brand.email,
    ...(brand.phone ? { telephone: brand.phone } : {}),
    logo: `${brand.domain}/assets/favicon.svg`,
    description: t.metaDesc,
    location: [
      { '@type': 'Place', name: 'Taipei Headquarters, Taiwan' },
      { '@type': 'Place', name: 'Taiwan Logistics & Warehousing' },
      { '@type': 'Place', name: 'Vietnam Granite & Marble Processing Plant' },
      { '@type': 'Place', name: 'Sunnyward Sdn Bhd, Malaysia' }
    ]
  });

  const hreflangs = languages.map((l) => {
    const href = `${brand.domain}${pageUrl(l, subpath)}`;
    const code = l === 'jp' ? 'ja' : l === 'tw' ? 'zh-Hant' : 'en';
    return `  <link rel="alternate" hreflang="${code}" href="${href}">`;
  }).join('\n');

  const langSwitchLinks = languages.map((l) => {
    const href = pageUrl(l, subpath);
    const active = l === lang ? ' class="active" aria-current="true"' : '';
    return `<a href="${href}"${active}>${esc(langLabels[l])}</a>`;
  }).join('');

  const navItems = [
    { key: 'home', label: t.nav.home, href: pageUrl(lang, '') },
    { key: 'capabilities', label: t.nav.capabilities, href: pageUrl(lang, 'capabilities') },
    { key: 'cases', label: t.nav.cases, href: pageUrl(lang, 'cases') },
    { key: 'inquiry', label: t.nav.inquiry, href: pageUrl(lang, 'inquiry') }
  ];

  const desktopNavHtml = navItems.map((item) => {
    const curr = activeNav === item.key ? ' aria-current="page"' : '';
    return `<li><a href="${item.href}"${curr}>${esc(item.label)}</a></li>`;
  }).join('');

  const mobileNavHtml = navItems.map((item) => {
    return `<li><a href="${item.href}">${esc(item.label)}</a></li>`;
  }).join('');

  return `<!DOCTYPE html>
<html lang="${t.htmlLang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${esc(title)}</title>
  <meta name="description" content="${esc(description)}">
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="canonical" href="${canonicalUrl}">
${hreflangs}
  <link rel="alternate" hreflang="x-default" href="${brand.domain}${pageUrl('en', subpath)}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="${esc(brand.name)}">
  <meta property="og:locale" content="${ogLocale}">
  <meta property="og:title" content="${esc(title)}">
  <meta property="og:description" content="${esc(description)}">
  <meta property="og:url" content="${canonicalUrl}">
  <meta property="og:image" content="${ogImgUrl}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${esc(title)}">
  <meta name="twitter:description" content="${esc(description)}">
  <meta name="twitter:image" content="${ogImgUrl}">
  <script type="application/ld+json">${orgJsonLd}</script>
  ${fontLinksFor(lang)}
  ${subpath === '' ? '<link rel="preload" as="image" href="/assets/images/hero-veltor-island-sm.webp" media="(max-width: 768px)" fetchpriority="high">\n  <link rel="preload" as="image" href="/assets/images/hero-veltor-island.webp" media="(min-width: 769px)" fetchpriority="high">' : ''}
  <link rel="stylesheet" href="/assets/style.css">
  <script async src="https://www.googletagmanager.com/gtag/js?id=${brand.ga4Id}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', '${brand.ga4Id}');
  </script>${brand.posthogKey ? `
  <script>
    !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once register_for_session unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep identify setPersonProperties".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    posthog.init('${brand.posthogKey}', { api_host: '${brand.posthogHost || 'https://us.i.posthog.com'}', person_profiles: 'identified_only' });
  </script>` : ''}
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand-mark" href="${pageUrl(lang, '')}">
        <span>${esc(brand.name)}</span>
        <span class="brand-est">EST. ${esc(brand.founded)}</span>
      </a>
      <nav class="nav-desktop" aria-label="Primary">
        <ul class="nav-links">${desktopNavHtml}</ul>
        <div class="lang-switcher" aria-label="Language">${langSwitchLinks}</div>
        <a class="btn btn-primary btn-sm" href="${pageUrl(lang, 'inquiry')}">${esc(t.nav.cta)}</a>
      </nav>
      <button id="bf-menu-toggle" class="menu-toggle" type="button" aria-label="Toggle menu" aria-expanded="false" aria-controls="bf-mobile-drawer">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">
          <line x1="2" y1="5" x2="18" y2="5"/>
          <line x1="2" y1="10" x2="18" y2="10"/>
          <line x1="2" y1="15" x2="18" y2="15"/>
        </svg>
      </button>
    </div>
    <div id="bf-mobile-drawer" class="mobile-drawer">
      <ul>${mobileNavHtml}</ul>
      <div class="mobile-drawer-controls">
        <div class="lang-switcher" aria-label="Language">${langSwitchLinks}</div>
        <a class="btn btn-primary" href="${pageUrl(lang, 'inquiry')}">${esc(t.nav.cta)}</a>
      </div>
    </div>
  </header>

  <main>
${bodyHtml}
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="brand-mark" style="margin-bottom:12px;">
            <span>${esc(brand.name)}</span>
            <span class="brand-est">EST. ${esc(brand.founded)}</span>
          </div>
          <p class="caption" style="margin:0; max-width:34ch;">${esc(t.footer.tagline)}</p>
        </div>
        <div>
          <h3 class="footer-heading">${esc(t.footer.hubsTitle)}</h3>
          <ul class="footer-list">
            ${t.footer.hubs.map((h) => `<li>${esc(h)}</li>`).join('')}
          </ul>
        </div>
        <div>
          <h3 class="footer-heading">${esc(t.footer.linksTitle)}</h3>
          <ul class="footer-list">
            ${navItems.map((i) => `<li><a href="${i.href}">${esc(i.label)}</a></li>`).join('')}
            <li><a href="${pageUrl(lang, 'privacy-policy')}">${esc(t.footer.privacy)}</a></li>
          </ul>
        </div>
        <div>
          <h3 class="footer-heading">${esc(t.footer.contactTitle)}</h3>
          <ul class="footer-list">
            <li><a href="mailto:${brand.email}" data-contact-method="email">${esc(brand.email)}</a></li>
            ${brand.phone ? `<li><a href="tel:${brand.phone}" data-contact-method="phone">${esc(brand.phone)}</a></li>` : ''}
            <li><a href="${pageUrl(lang, 'inquiry')}" data-contact-method="inquiry_form">${esc(t.nav.cta)}</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>${esc(t.footer.copyright)}</span>
        <a href="${pageUrl(lang, 'privacy-policy')}">${esc(t.footer.privacy)}</a>
      </div>
    </div>
  </footer>

  <script src="/assets/app.js"></script>
</body>
</html>`;
}

function renderCaseCard(lang, c) {
  const cData = c[lang];
  const t = ui[lang];
  return `<article class="case-card" data-case-kind="${c.kind}">
    <a href="${caseUrl(lang, c.slug)}">
      <img class="case-card-img" src="${webImg(c.heroImage)}" alt="${esc(cData.title)}" width="1200" height="800" loading="lazy" decoding="async">
    </a>
    <div class="case-card-body">
      <span class="case-badge">${esc(cData.badge)}</span>
      <h3><a href="${caseUrl(lang, c.slug)}">${esc(cData.title)}</a></h3>
      <p>${esc(cData.summary)}</p>
      <a class="text-link" href="${caseUrl(lang, c.slug)}">${esc(t.casesPage.viewCase)} &rarr;</a>
    </div>
  </article>`;
}

const sitemapUrls = [];

for (const lang of languages) {
  const t = ui[lang];

  // 1. HOME PAGE
  const homeBody = `
    <section class="hero">
      <div class="container hero-grid">
        <div>
          <span class="eyebrow">${esc(t.home.eyebrow)}</span>
          <h1>${esc(t.home.h1)}</h1>
          <p class="lead">${esc(t.home.subtitle)}</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="${pageUrl(lang, 'inquiry')}?mode=budget">${esc(t.home.primaryCta)}</a>
            <a class="btn btn-secondary" href="${pageUrl(lang, 'cases')}">${esc(t.home.secondaryCta)}</a>
          </div>
          <p class="cta-reassurance">${esc(t.home.ctaNote)}</p>
        </div>
        <div class="hero-media">
          <img src="${webImg(t.home.heroImage)}" srcset="/assets/images/hero-veltor-island-sm.webp 800w, /assets/images/hero-veltor-island.webp 1200w" sizes="(max-width: 768px) 92vw, 600px" alt="${esc(t.home.heroAlt)}" width="1200" height="804" fetchpriority="high" decoding="async">
        </div>
      </div>
    </section>

    <section class="stats-strip" aria-label="Track Record">
      <div class="container stats-grid">
        ${t.home.stats.map((s) => `
        <div class="stat-item">
          <div class="stat-value">${esc(s.value)}</div>
          <div class="stat-label">${esc(s.label)}</div>
        </div>`).join('')}
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <div class="section-head-text">
            <span class="eyebrow">${esc(t.home.taEyebrow)}</span>
            <h2>${esc(t.home.taTitle)}</h2>
            <p class="lead" style="margin-bottom:0;">${esc(t.home.taIntro)}</p>
          </div>
          <a class="text-link" href="${pageUrl(lang, 'capabilities')}">${esc(t.home.taLink)} &rarr;</a>
        </div>
        <div class="grid-2">
          ${t.home.taCards.map((card) => `
          <div class="card">
            <div class="ta-card-head">
              <span class="card-num" style="margin-bottom:0;">${esc(card.num)}</span>
              <span class="ta-role">${esc(card.role)}</span>
            </div>
            <h3>${esc(card.title)}</h3>
            <p>${esc(card.desc)}</p>
          </div>`).join('')}
        </div>
      </div>
    </section>

    <section class="section section-surface">
      <div class="container">
        <div class="section-head">
          <div class="section-head-text">
            <span class="eyebrow">${esc(t.home.casesEyebrow)}</span>
            <h2>${esc(t.home.casesTitle)}</h2>
            <p class="lead" style="margin-bottom:0;">${esc(t.home.casesIntro)}</p>
          </div>
          <a class="text-link" href="${pageUrl(lang, 'cases')}">${esc(t.home.casesLink)} &rarr;</a>
        </div>
        <div class="grid-2">
          ${cases.slice(0, 4).map((c) => renderCaseCard(lang, c)).join('')}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <div class="section-head-text">
            <span class="eyebrow">${esc(t.home.craftEyebrow)}</span>
            <h2>${esc(t.home.craftTitle)}</h2>
            <p class="lead" style="margin-bottom:0;">${esc(t.home.craftIntro)}</p>
          </div>
        </div>
        <div class="grid-2">
          ${t.home.craftItems.map((ci) => `
          <article class="case-card">
            <img class="case-card-img" src="${webImg(ci.src)}" alt="${esc(ci.title)}" width="1200" height="800" loading="lazy" decoding="async">
            <div class="case-card-body">
              <h3>${esc(ci.title)}</h3>
              <p>${esc(ci.desc)}</p>
            </div>
          </article>`).join('')}
        </div>
      </div>
    </section>

    <section class="section section-surface">
      <div class="container">
        <div class="section-head">
          <div class="section-head-text">
            <span class="eyebrow">${esc(t.home.processEyebrow)}</span>
            <h2>${esc(t.home.processTitle)}</h2>
          </div>
        </div>
        <div class="grid-4">
          ${t.home.processSteps.map((st) => `
          <div class="card">
            <span class="card-num">${esc(st.num)}</span>
            <h3>${esc(st.title)}</h3>
            <p>${esc(st.desc)}</p>
          </div>`).join('')}
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>${esc(t.home.bottomTitle)}</h2>
        <p>${esc(t.home.bottomDesc)}</p>
        <div class="hero-actions">
          <a class="btn btn-on-dark" href="${pageUrl(lang, 'inquiry')}?mode=budget">${esc(t.home.bottomCta)}</a>
          <a class="btn btn-on-dark-outline" href="${pageUrl(lang, 'inquiry')}?mode=quote">${esc(t.home.bottomSecondaryCta)}</a>
        </div>
      </div>
    </section>
  `;
  writeHtml(`${lang}/index.html`, renderLayout({
    lang,
    title: t.siteTitle,
    description: t.metaDesc,
    activeNav: 'home',
    subpath: '',
    bodyHtml: homeBody
  }));
  sitemapUrls.push(`${brand.domain}${pageUrl(lang, '')}`);

  // 2. CAPABILITIES PAGE
  const capBody = `
    <section class="section">
      <div class="container">
        <span class="eyebrow">${esc(t.capabilities.eyebrow)}</span>
        <h1>${esc(t.capabilities.title)}</h1>
        <p class="lead">${esc(t.capabilities.intro)}</p>
        <div class="grid-3" style="margin-top:40px;">
          ${t.capabilities.pillars.map((p) => `
          <div class="card">
            <span class="card-num">${esc(p.num)}</span>
            <h3>${esc(p.title)}</h3>
            <p>${esc(p.desc)}</p>
            <ul>${p.points.map((pt) => `<li>${esc(pt)}</li>`).join('')}</ul>
          </div>`).join('')}
        </div>
        <div class="spec-note-box">${esc(t.capabilities.note)}</div>
      </div>
    </section>
    <section class="section section-surface">
      <div class="container">
        <div class="section-head">
          <div class="section-head-text">
            <span class="eyebrow">${esc(t.capabilities.systemsEyebrow)}</span>
            <h2>${esc(t.capabilities.systemsTitle)}</h2>
            <p class="lead" style="margin-bottom:0;">${esc(t.capabilities.systemsIntro)}</p>
          </div>
        </div>
        <div class="grid-2">
          ${t.capabilities.systems.map((sys) => `
          <article class="case-card">
            <img class="case-card-img" src="${webImg(sys.src)}" alt="${esc(sys.title)}" width="1200" height="800" loading="lazy" decoding="async">
            <div class="case-card-body">
              <h3>${esc(sys.title)}</h3>
              <p>${esc(sys.desc)}</p>
            </div>
          </article>`).join('')}
        </div>
      </div>
    </section>
    <section class="cta-band">
      <div class="container">
        <h2>${esc(t.home.bottomTitle)}</h2>
        <p>${esc(t.home.bottomDesc)}</p>
        <div class="hero-actions">
          <a class="btn btn-on-dark" href="${pageUrl(lang, 'inquiry')}?mode=budget">${esc(t.home.bottomCta)}</a>
          <a class="btn btn-on-dark-outline" href="${pageUrl(lang, 'inquiry')}?mode=quote">${esc(t.home.bottomSecondaryCta)}</a>
        </div>
      </div>
    </section>
  `;
  writeHtml(`${lang}/capabilities/index.html`, renderLayout({
    lang,
    title: `${t.nav.capabilities} — ${brand.name}`,
    description: t.capabilities.intro,
    activeNav: 'capabilities',
    subpath: 'capabilities',
    bodyHtml: capBody
  }));
  sitemapUrls.push(`${brand.domain}${pageUrl(lang, 'capabilities')}`);

  // 3. CASES INDEX PAGE
  const casesBody = `
    <section class="section">
      <div class="container">
        <span class="eyebrow">${esc(t.casesPage.eyebrow)}</span>
        <h1>${esc(t.casesPage.title)}</h1>
        <p class="lead">${esc(t.casesPage.intro)}</p>
        <div class="filter-bar" role="group" aria-label="Filter projects">
          <button type="button" class="filter-btn active" data-case-filter="all">${esc(t.casesPage.filterAll)}</button>
          <button type="button" class="filter-btn" data-case-filter="real">${esc(t.casesPage.filterReal)}</button>
          <button type="button" class="filter-btn" data-case-filter="concept">${esc(t.casesPage.filterConcept)}</button>
        </div>
        <div class="grid-2">
          ${cases.map((c) => renderCaseCard(lang, c)).join('')}
        </div>
      </div>
    </section>
  `;
  writeHtml(`${lang}/cases/index.html`, renderLayout({
    lang,
    title: `${t.nav.cases} — ${brand.name}`,
    description: t.casesPage.intro,
    activeNav: 'cases',
    subpath: 'cases',
    bodyHtml: casesBody
  }));
  sitemapUrls.push(`${brand.domain}${pageUrl(lang, 'cases')}`);

  // 4. INDIVIDUAL CASE DETAIL PAGES
  cases.forEach((c, idx) => {
    const cData = c[lang];
    const next = cases[(idx + 1) % cases.length];
    const detailBody = `
      <section class="section">
        <div class="container">
          <a class="text-link" href="${pageUrl(lang, 'cases')}" style="margin-bottom:20px;">&larr; ${esc(t.caseDetail.backToCases)}</a>
          <span class="eyebrow">${esc(cData.badge)}</span>
          <h1>${esc(cData.title)}</h1>

          <div class="meta-grid">
            <div>
              <div class="meta-label">${esc(t.caseDetail.metaType)}</div>
              <div class="meta-val">${esc(cData.spaceType)}</div>
            </div>
            <div>
              <div class="meta-label">${esc(t.caseDetail.metaCategory)}</div>
              <div class="meta-val">${esc(cData.badge)}</div>
            </div>
            <div>
              <div class="meta-label">${esc(t.caseDetail.metaScope)}</div>
              <div class="meta-val">${esc(cData.scope)}</div>
            </div>
            <div>
              <div class="meta-label">${esc(t.caseDetail.metaMaterials)}</div>
              <div class="meta-val">${esc(cData.materials)}</div>
            </div>
          </div>

          ${c.gallery.map((g, gIdx) => `
          <figure class="figure-block">
            <img src="${webImg(g.src)}" alt="${esc(g.caption[lang])}" width="1200" height="800"${gIdx === 0 ? ' fetchpriority="high"' : ' loading="lazy"'} decoding="async">
            <figcaption>${esc(g.caption[lang])}</figcaption>
          </figure>`).join('')}

          <div class="narrative-grid">
            <div>
              <h2>${esc(t.caseDetail.briefTitle)}</h2>
              <p style="color:var(--ink-secondary);">${esc(cData.brief)}</p>
            </div>
            <div>
              <h2>${esc(t.caseDetail.execTitle)}</h2>
              <ul class="exec-list">
                ${cData.execution.map((ex) => `<li>${esc(ex)}</li>`).join('')}
              </ul>
            </div>
          </div>

          <div class="spec-note-box">
            <strong>${esc(t.caseDetail.specTitle)}${lang === 'en' ? ': ' : '：'}</strong>${esc(t.caseDetail.specNote)}
          </div>

          <div style="margin-top:44px; display:flex; flex-wrap:wrap; justify-content:space-between; gap:16px; padding-top:28px; border-top:1px solid var(--border-hairline);">
            <a class="btn btn-primary" href="${pageUrl(lang, 'inquiry')}">${esc(t.caseDetail.inquireCase)}</a>
            <a class="btn btn-secondary" href="${caseUrl(lang, next.slug)}">${esc(t.caseDetail.nextCase)}: ${esc(next[lang].title)} &rarr;</a>
          </div>
        </div>
      </section>
    `;

    writeHtml(`${lang}/cases/${c.slug}/index.html`, renderLayout({
      lang,
      title: `${cData.title} — ${brand.name}`,
      description: cData.summary,
      activeNav: 'cases',
      subpath: `cases/${c.slug}`,
      ogImage: webImg(c.heroImage),
      bodyHtml: detailBody
    }));
    sitemapUrls.push(`${brand.domain}${caseUrl(lang, c.slug)}`);
  });

  // 5. INQUIRY PAGE (Clean Intent-Driven Progressive UI: Choose 1 of 4 intents -> Only relevant panel/fields appear)
  const inqBody = `
    <section class="section">
      <div class="container inquiry-shell">
        <span class="eyebrow">${esc(t.inquiry.eyebrow)}</span>
        <h1>${esc(t.inquiry.title)}</h1>
        <p class="lead">${esc(t.inquiry.intro)}</p>

        <div class="choice-bar" role="tablist" aria-label="${esc(t.inquiry.fields.modeLegend)}">
          ${t.inquiry.choices.map((ch, idx) => `
          <button type="button" class="choice-tab${idx === 0 ? ' active' : ''}" role="tab" aria-selected="${idx === 0 ? 'true' : 'false'}" data-inquiry-choice="${esc(ch.id)}">
            <span class="choice-tab-title">${esc(ch.label)}</span>
            <span class="choice-tab-sub">${esc(ch.short)}</span>
          </button>`).join('')}
        </div>

        <div id="bf-form-panel" class="form-card">
          <p id="bf-mode-hint" class="mode-banner"
             data-hint-budget="${esc(t.inquiry.modeHints.budget)}"
             data-hint-quote="${esc(t.inquiry.modeHints.quote)}"
             data-hint-callback="${esc(t.inquiry.modeHints.callback)}">${esc(t.inquiry.modeHints.budget)}</p>

          <form id="bf-inquiry-form" name="bf-engineering-inquiry" method="POST" data-netlify="true" netlify-honeypot="bot-field" enctype="multipart/form-data" novalidate>
            <input type="hidden" name="form-name" value="bf-engineering-inquiry">
            <input type="hidden" name="page_lang" value="${esc(lang)}">
            <input type="hidden" id="bf-mode-input" name="inquiry_mode" value="budget">
            <p class="sr-only" hidden><label>Do not fill: <input name="bot-field"></label></p>

            <div class="form-group">
              <label for="bf-email">${esc(t.inquiry.fields.email)}</label>
              <input id="bf-email" name="email" type="email" required autocomplete="email" placeholder="${esc(t.inquiry.fields.emailPh)}">
            </div>

            <div class="form-group" data-show-for="callback" hidden>
              <label for="bf-contact-alt">${esc(t.inquiry.fields.contactAlt)}</label>
              <input id="bf-contact-alt" name="contact_alt" type="text" placeholder="${esc(t.inquiry.fields.contactAltPh)}">
            </div>

            <div class="form-group" data-show-for="budget quote">
              <label for="bf-requirements">${esc(t.inquiry.fields.requirements)}</label>
              <textarea id="bf-requirements" name="requirements" required placeholder="${esc(t.inquiry.fields.requirementsPh)}"></textarea>
            </div>

            <div class="form-group" data-show-for="callback" hidden>
              <label for="bf-callback-note">${esc(t.inquiry.fields.callbackNote)}</label>
              <textarea id="bf-callback-note" name="callback_note" style="min-height:92px;" placeholder="${esc(t.inquiry.fields.callbackNotePh)}"></textarea>
            </div>

            <div class="form-row-2" data-show-for="budget quote">
              <div class="form-group">
                <label for="bf-ref-link">${esc(t.inquiry.fields.referenceLink)}</label>
                <input id="bf-ref-link" name="reference_link" type="text" placeholder="${esc(t.inquiry.fields.referenceLinkPh)}">
              </div>
              <div class="form-group">
                <label for="bf-ref-file">${esc(t.inquiry.fields.referenceFile)}</label>
                <input id="bf-ref-file" name="reference_file" type="file" multiple accept=".jpg,.jpeg,.png,.webp,.pdf,.dwg,.dxf,.step,.stp,.zip">
              </div>
            </div>

            <div data-show-for="quote" hidden>
              <div class="form-group">
                <label for="bf-batch-qty">${esc(t.inquiry.fields.batchQty)}</label>
                <input id="bf-batch-qty" name="batch_qty" type="text" placeholder="${esc(t.inquiry.fields.batchQtyPh)}">
              </div>
              <div class="form-row-2">
                <div class="form-group">
                  <label for="bf-quote-date">${esc(t.inquiry.fields.quoteDate)}</label>
                  <input id="bf-quote-date" name="quote_date" type="date">
                </div>
                <div class="form-group">
                  <label for="bf-delivery-date">${esc(t.inquiry.fields.deliveryDate)}</label>
                  <input id="bf-delivery-date" name="delivery_date" type="date">
                </div>
              </div>
            </div>

            <label class="focus-option nda-option" for="bf-nda-first" data-show-for="budget quote">
              <input id="bf-nda-first" name="nda_first" type="checkbox" value="yes">
              <span>${esc(t.inquiry.fields.ndaFirst)}</span>
            </label>

            <details class="more-details">
              <summary>${esc(t.inquiry.fields.moreToggle)}</summary>
              <div class="form-row-2" style="margin-top:14px;">
                <div class="form-group" style="margin-bottom:0;">
                  <label for="bf-company">${esc(t.inquiry.fields.company)}</label>
                  <input id="bf-company" name="company" type="text" autocomplete="organization" placeholder="${esc(t.inquiry.fields.companyPh)}">
                </div>
                <div class="form-group" style="margin-bottom:0;">
                  <label for="bf-name">${esc(t.inquiry.fields.name)}</label>
                  <input id="bf-name" name="name" type="text" autocomplete="name" placeholder="${esc(t.inquiry.fields.namePh)}">
                </div>
              </div>
            </details>

            <label class="checkbox-row" for="bf-consent">
              <input id="bf-consent" name="privacy_consent" type="checkbox" required>
              <span>${esc(t.inquiry.fields.consentPrefix)}<a href="${pageUrl(lang, 'privacy-policy')}">${esc(t.inquiry.fields.consentLink)}</a>${esc(t.inquiry.fields.consentSuffix)}</span>
            </label>

            <button class="btn btn-primary" type="submit">${esc(t.inquiry.fields.submit)}</button>
          </form>

          <div id="bf-form-status" class="form-status" role="status" aria-live="polite">
            <strong>${esc(t.inquiry.successTitle)}</strong>
            <p style="margin:8px 0 12px;">${esc(t.inquiry.successDesc)}</p>
            <div class="receipt-box">
              <div class="receipt-title">${esc(t.inquiry.receiptTitle)}</div>
              <dl id="bf-receipt-list" class="receipt-list"></dl>
            </div>
          </div>
        </div>

        <div id="bf-email-panel" class="form-card direct-email-card" hidden>
          <span class="eyebrow" style="margin-bottom:8px;">${esc(t.inquiry.directEmailCard.eyebrow)}</span>
          <h2 style="margin-bottom:12px;">${esc(t.inquiry.directEmailCard.title)}</h2>
          <p class="lead" style="margin-bottom:24px;">${esc(t.inquiry.directEmailCard.desc)}</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="mailto:${brand.email}?subject=${encodeURIComponent(t.inquiry.directEmailCard.mailtoSubject)}&amp;body=${encodeURIComponent(t.inquiry.directEmailCard.mailtoBody)}" data-contact-method="email_mailto">${esc(t.inquiry.directEmailCard.mailtoBtn)}</a>
            <button class="btn btn-secondary" type="button" data-copy-email="${esc(brand.email)}" data-copied-label="${esc(t.inquiry.directEmailCard.copiedText)}" data-contact-method="email_copy">${esc(t.inquiry.directEmailCard.copyBtn)}</button>
          </div>
          <p class="caption" style="margin-top:20px;">${esc(t.inquiry.directDesc)}</p>
        </div>

        <div class="inquiry-footnote">
          <span>${esc(t.inquiry.directDesc)}</span>
          <a href="mailto:${brand.email}" data-contact-method="email">${esc(brand.email)}</a>
        </div>
      </div>
    </section>
  `;
  writeHtml(`${lang}/inquiry/index.html`, renderLayout({
    lang,
    title: `${t.nav.inquiry} — ${brand.name}`,
    description: t.inquiry.intro,
    activeNav: 'inquiry',
    subpath: 'inquiry',
    bodyHtml: inqBody
  }));
  sitemapUrls.push(`${brand.domain}${pageUrl(lang, 'inquiry')}`);

  // 6. PRIVACY POLICY PAGE
  const privBody = `
    <section class="section">
      <div class="container" style="max-width:820px;">
        <span class="eyebrow">${esc(t.privacy.eyebrow)}</span>
        <h1>${esc(t.privacy.title)}</h1>
        <p class="caption" style="margin-bottom:36px;">${esc(t.privacy.updated)}</p>
        ${t.privacy.sections.map((s) => `
        <div style="margin-bottom:28px;">
          <h3>${esc(s.h)}</h3>
          <p style="color:var(--ink-secondary); margin:0;">${esc(s.p)}</p>
        </div>`).join('')}
      </div>
    </section>
  `;
  writeHtml(`${lang}/privacy-policy/index.html`, renderLayout({
    lang,
    title: `${t.privacy.title} — ${brand.name}`,
    description: t.privacy.sections[0].p,
    activeNav: '',
    subpath: 'privacy-policy',
    bodyHtml: privBody
  }));
  sitemapUrls.push(`${brand.domain}${pageUrl(lang, 'privacy-policy')}`);
}

// Root index.html (serves EN home directly for clean preview & zero redirect hop)
fs.copyFileSync(path.join(distDir, 'en', 'index.html'), path.join(distDir, 'index.html'));
// Root /privacy-policy/index.html (eliminates P1 /privacy-policy 404)
fs.mkdirSync(path.join(distDir, 'privacy-policy'), { recursive: true });
fs.copyFileSync(path.join(distDir, 'en', 'privacy-policy', 'index.html'), path.join(distDir, 'privacy-policy', 'index.html'));

// Clean Branded 404.html
writeHtml('404.html', renderLayout({
  lang: 'en',
  title: `Page Not Found — ${brand.name}`,
  description: 'The requested page could not be found on bigfame.co.',
  activeNav: '',
  subpath: '',
  bodyHtml: `
    <section class="section">
      <div class="container" style="max-width:720px; padding-block:48px;">
        <span class="eyebrow">404 · PAGE NOT FOUND</span>
        <h1>This page has moved or no longer exists.</h1>
        <p class="lead">Explore our updated commercial fixture &amp; hospitality FF&amp;E portfolio, or contact our Taipei engineering desk directly at <a href="mailto:${brand.email}" style="text-decoration:underline;">${brand.email}</a>.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="/en/">English Home</a>
          <a class="btn btn-secondary" href="/jp/">日本語ホーム</a>
          <a class="btn btn-secondary" href="/tw/">繁體中文首頁</a>
        </div>
      </div>
    </section>`
}));

// P0 Complete _redirects (100% coverage of all 113 live bigfame.co URLs + 20162016 slug stacking + /privacy-policy)
const langRedirects = languages.map((l) => `
# --- ${l.toUpperCase()} Legacy URL Convergence (301) ---
/${l}/case-eyewear-2016* /${l}/cases/eyewear-boutique-fixtures/ 301
/${l}/optical-hooks* /${l}/cases/eyewear-boutique-fixtures/ 301
/${l}/case-apparel-2016* /${l}/cases/apparel-footwear-flagship/ 301
/${l}/apparel-store-fixtures* /${l}/cases/apparel-footwear-flagship/ 301
/${l}/case-japanese-wine-bar* /${l}/cases/japanese-wine-bar-millwork/ 301
/${l}/case-boutique-hotel-furniture* /${l}/cases/hotel-guestroom-vanity-ffe/ 301
/${l}/case-veltor-motorcycle-store* /${l}/cases/veltor-retail-concept/ 301
/${l}/case-ivy-modular-system* /${l}/capabilities/ 301
/${l}/modular-fixtures* /${l}/capabilities/ 301
/${l}/slatwall-pegboard-accessories* /${l}/capabilities/ 301
/${l}/custom-metal-parts* /${l}/capabilities/ 301
/${l}/anti-theft-hooks* /${l}/capabilities/ 301
/${l}/display-hooks* /${l}/capabilities/ 301
/${l}/cosmetic-organizers* /${l}/capabilities/ 301
/${l}/jewelry-display-accessories* /${l}/capabilities/ 301
/${l}/pos-displays* /${l}/capabilities/ 301
/${l}/price-tag-holders* /${l}/capabilities/ 301
/${l}/products* /${l}/capabilities/ 301
/${l}/services* /${l}/capabilities/ 301
/${l}/applications* /${l}/capabilities/ 301
/${l}/design-support* /${l}/capabilities/ 301
/${l}/procurement* /${l}/capabilities/ 301
/${l}/technical-resources* /${l}/capabilities/ 301
/${l}/guide-* /${l}/capabilities/ 301
/${l}/case-* /${l}/cases/ 301
/${l}/contact* /${l}/inquiry/ 301
/${l}/project-start* /${l}/inquiry/ 301
/${l}/about* /${l}/ 301`).join('\n');

const redirects = `# Big Fame P0 Redirect Convergence (301) — Verified against 113 Live bigfame.co URLs
/privacy-policy /en/privacy-policy/ 301
/privacy-policy/ /en/privacy-policy/ 301
${langRedirects}

# Legacy PHP, blog & root routes
/list.php /en/cases/ 301
/overview /en/capabilities/ 301
/overview/ /en/capabilities/ 301
/contact /en/inquiry/ 301
/contact/ /en/inquiry/ 301
/contact-us /en/inquiry/ 301
/contact-us/ /en/inquiry/ 301
/blog /en/cases/ 301
/blog/ /en/cases/ 301
/blog/retail-fixture-blog /en/capabilities/ 301
/blog/retail-fixture-blog/ /en/capabilities/ 301
/blog/author/benny /en/ 410
/blog/author/benny/ /en/ 410
`;
fs.writeFileSync(path.join(distDir, '_redirects'), redirects, 'utf8');

// Auto-generated sitemap.xml from Single Source of Truth (zero duplicate years)
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${sitemapUrls.map((u) => `  <url><loc>${u}</loc></url>`).join('\n')}
</urlset>
`;
fs.writeFileSync(path.join(distDir, 'sitemap.xml'), sitemap, 'utf8');

console.log(`Built ${sitemapUrls.length} localized pages + root index + /privacy-policy + _redirects + sitemap.xml`);
