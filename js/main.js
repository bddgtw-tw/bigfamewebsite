/* Big Fame IND. CORP. - Global JavaScript Logic */
var SITE_VERSION = '1.3.21';

document.addEventListener('DOMContentLoaded', () => {
  initAnalytics();
  initThemeSwitcher();
  initHeaderScroll();
  initMobileMenu();
  initScrollAnimations();
  initLanguageTracker();
  highlightActiveLink();
  initPageTransitions();
  initMagneticButtons();
  initOfficeStatus();
  initInquiryTracking();
  initProductInquiryLinks();
  initInquiryContext();
  initTaServiceSchema();
  initVerifiedProductSchema();
  initContactForm();
  initHeroParticles();
  initScrollIndicator();
});

if (document.readyState !== 'loading') {
  initAnalytics();
}

function getMeasurementContext() {
  const segments = window.location.pathname.split('/').filter(Boolean);
  const locale = ['tw', 'en', 'jp'].includes(segments[0]) ? segments[0] : 'root';
  const slug = segments[1] || 'home';
  let pageType = 'content';
  if (slug === 'home') pageType = 'home';
  else if (slug === 'contact') pageType = 'contact';
  else if (['procurement', 'design-support', 'display-hooks', 'apparel-store-fixtures'].includes(slug)) pageType = 'ta_entry';
  else if (slug.startsWith('case-')) pageType = 'case';
  else if (['products', 'applications', 'services', 'about'].includes(slug)) pageType = 'hub';
  else if (['optical-hooks', 'anti-theft-hooks', 'slatwall-pegboard-accessories', 'price-tag-holders', 'pos-displays', 'modular-fixtures', 'custom-metal-parts', 'cosmetic-organizers'].includes(slug)) pageType = 'product';
  return {
    site_locale: locale,
    page_type: pageType,
    content_slug: slug,
    ta_entry: pageType === 'ta_entry' ? slug : 'none'
  };
}

// Add a service entity to the three TA entry pages without changing their
// legacy one-line HTML heads. The JSON-LD is visible in the rendered DOM.
function initTaServiceSchema() {
  if (document.querySelector('script[data-bf-service-schema]')) return;
  const segments = window.location.pathname.split('/').filter(Boolean);
  const locale = ['tw', 'en', 'jp'].includes(segments[0]) ? segments[0] : '';
  const slug = segments[1] || '';
  const entries = {
    'tw/procurement': {
      name: '台灣店面展示設備採購',
      description: '店面展示設備採購與需求整理入口。',
      serviceType: 'Retail display hardware procurement'
    },
    'tw/design-support': {
      name: '零售空間展示系統與設計支援',
      description: '店面設計與展示設備規格協作入口。',
      serviceType: 'Retail display systems and design support'
    },
    'tw/display-hooks': {
      name: '展示掛勾與陳列五金',
      description: '支援洞洞板、槽板與零售展示系統的展示掛勾與陳列五金。',
      serviceType: 'Display hooks and retail display hardware'
    },
    'en/procurement': {
      name: 'Taiwan Retail Display Hardware Procurement',
      description: 'Procurement entry for retail display hardware and fixture requirements.',
      serviceType: 'Retail display hardware procurement'
    },
    'en/design-support': {
      name: 'Retail Display Systems and Design Support',
      description: 'Design collaboration entry for retail display systems and hardware.',
      serviceType: 'Retail display systems and design support'
    },
    'en/display-hooks': {
      name: 'Display Hooks & Retail Display Hardware',
      description: 'Display hooks for pegboard, slatwall and retail fixture projects.',
      serviceType: 'Display hooks and retail display hardware'
    },
    'jp/procurement': {
      name: '台湾の店舗什器・ディスプレイ金具の購買',
      description: '店舗什器とディスプレイ金具の購買相談入口。',
      serviceType: '店舗什器・ディスプレイ金具の購買支援'
    },
    'jp/design-support': {
      name: '店舗什器・ディスプレイシステム設計支援',
      description: '店舗設計とディスプレイシステムの相談入口。',
      serviceType: '店舗什器・ディスプレイシステム設計支援'
    },
    'jp/display-hooks': {
      name: 'ディスプレイフック・店舗什器金物',
      description: '有孔ボード、スラットウォール、店舗什器向けのディスプレイフック。',
      serviceType: 'ディスプレイフック・店舗什器金物'
    }
  };
  const key = `${locale}/${slug}`;
  const entry = entries[key];
  if (!entry) return;
  const existingService = Array.from(document.querySelectorAll('script[type="application/ld+json"]'))
    .some((script) => script.textContent.includes('"@type":"Service"'));
  if (existingService) return;
  const schema = {
    '@context': 'https://schema.org',
    '@type': 'Service',
    '@id': `${window.location.origin}${window.location.pathname}#service`,
    url: `${window.location.origin}${window.location.pathname}`,
    name: entry.name,
    description: entry.description,
    serviceType: entry.serviceType,
    provider: { '@id': `${window.location.origin}/#organization` }
  };
  const script = document.createElement('script');
  script.type = 'application/ld+json';
  script.dataset.bfServiceSchema = '1';
  script.textContent = JSON.stringify(schema);
  document.head.appendChild(script);
}

// Add only the verified product/category identity to product pages. Do not
// invent SKU, price, offer, MOQ or lead-time values from representative data.
function initVerifiedProductSchema() {
  const segments = window.location.pathname.split('/').filter(Boolean);
  const locale = ['tw', 'en', 'jp'].includes(segments[0]) ? segments[0] : '';
  const slug = segments[1] || '';
  const categories = {
    'display-hooks': 'Display hooks and retail display hardware',
    'optical-hooks': 'Eyewear display hooks',
    'anti-theft-hooks': 'Anti-theft display hooks',
    'slatwall-pegboard-accessories': 'Slatwall and pegboard accessories',
    'price-tag-holders': 'Price tag holders and signage accessories',
    'pos-displays': 'POS and countertop retail displays',
    'modular-fixtures': 'Modular retail display fixtures',
    'custom-metal-parts': 'Custom metal retail hardware'
  };
  const verifiedProperties = {
    'display-hooks': [
      { name: 'Documented hook lengths', value: '50 mm, 75 mm, 100 mm, 150 mm, 200 mm' },
      { name: 'Documented wire diameters', value: '5.0 mm, 6.0 mm, 8.0 mm, 10.0 mm' },
      { name: 'DBTHK001-SLW documented lengths', value: '50 mm, 100 mm, 150 mm, 200 mm' },
      { name: 'Documented crossbar sizes', value: '10 × 20 mm, 14 × 24 mm, 20 × 40 mm, 15 × 30 mm' }
    ],
    'optical-hooks': [
      { name: 'EYEHK 2025 pegboard drawing dimensions', value: '160 mm, 175 mm, 150.93 mm, 128 mm and 25.4 mm (drawing labels)' },
      { name: 'EYEHK 2018 drawing material notes', value: 't2.0 iron plate and 4.0 mm iron wire (drawing notes)' },
      { name: 'EYEHK 2018 drawing finish note', value: 'Black powder coating (drawing note)' },
      { name: 'EYEHK 2018 design notes', value: 'End chamfer and approximately 2° upward angle (drawing notes)' }
    ],
    'slatwall-pegboard-accessories': [
      { name: 'GLOOVING documented series image dimension', value: '800 × 450 mm' },
      { name: 'GLOOVING documented dimension variants', value: '10 cm and 15 cm (source image labels)' },
      { name: 'GLOOVING documented material direction', value: 'Aluminium (source image label)' }
    ],
    'modular-fixtures': [
      { name: 'YC-1524L documented dimensions', value: '24 × 30 × 56 in or 48 × 30 × 56 in' },
      { name: 'YC-1524L caster', value: '3 in rubber casters' },
      { name: 'ARC67-A documented dimensions', value: '24.5 × 24.5 × 59 in' },
      { name: 'ARC67-A panels', value: '4 white acrylic panels' },
      { name: 'Documented finish direction', value: 'Powder-coat metal finish' }
    ]
  };
  if (!locale || !categories[slug]) return;
  const existingProductScript = Array.from(document.querySelectorAll('script[type="application/ld+json"]'))
    .find((script) => {
      try {
        const data = JSON.parse(script.textContent);
        return data && (data['@type'] === 'Product' || (Array.isArray(data['@type']) && data['@type'].includes('Product')));
      } catch (error) {
        return false;
      }
    });
  if (existingProductScript && verifiedProperties[slug] && !existingProductScript.dataset.bfVerifiedProperties) {
    try {
      const data = JSON.parse(existingProductScript.textContent);
      data.additionalProperty = verifiedProperties[slug].map((property) => ({
        '@type': 'PropertyValue',
        name: property.name,
        value: property.value
      }));
      existingProductScript.textContent = JSON.stringify(data);
      existingProductScript.dataset.bfVerifiedProperties = '1';
    } catch (error) {
      // Keep the original static schema when it cannot be safely parsed.
    }
  }
  if (existingProductScript || document.querySelector('script[data-bf-product-schema]')) return;
  const heading = document.querySelector('main h1, h1');
  const description = document.querySelector('meta[name="description"]');
  const canonical = document.querySelector('link[rel="canonical"]');
  if (!heading || !description || !canonical) return;
  const name = heading.textContent.replace(/\s+/g, ' ').trim();
  const image = document.querySelector('main img[src]');
  if (!name || !description.content) return;
  const schema = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    '@id': `${canonical.href}#product`,
    url: canonical.href,
    name,
    description: description.content,
    category: categories[slug],
    brand: { '@type': 'Brand', name: 'Big Fame' }
  };
  if (image && image.src) schema.image = [image.src];
  if (verifiedProperties[slug]) {
    schema.additionalProperty = verifiedProperties[slug].map((property) => ({
      '@type': 'PropertyValue',
      name: property.name,
      value: property.value
    }));
  }
  const script = document.createElement('script');
  script.type = 'application/ld+json';
  script.dataset.bfProductSchema = '1';
  script.textContent = JSON.stringify(schema);
  document.head.appendChild(script);
}

function initAnalytics() {
  if (window.__bfAnalyticsInitialized) return;
  window.__bfAnalyticsInitialized = true;
  window.dataLayer = window.dataLayer || [];
  if (typeof window.gtag !== 'function') {
    window.gtag = function () { window.dataLayer.push(arguments); };
  }
  if (!document.querySelector('script[src*="googletagmanager.com/gtag/js?id=G-PDW4NPHHW8"]')) {
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=G-PDW4NPHHW8';
    document.head.appendChild(script);
  }
  window.gtag('js', new Date());
  window.gtag('config', 'G-PDW4NPHHW8', {
    page_type: getMeasurementContext().page_type,
    content_slug: getMeasurementContext().content_slug,
    site_locale: getMeasurementContext().site_locale
  });
  trackAnalyticsEvent('bf_page_context');
}

/**
 * Send privacy-safe B2B inquiry events to GA4.
 * Never include form field values or other personally identifiable information.
 */
function trackAnalyticsEvent(eventName, parameters = {}) {
  if (typeof window.gtag !== 'function') return;

  window.gtag('event', eventName, {
    site_language: document.documentElement.lang || 'unknown',
    page_path: window.location.pathname,
    ...getMeasurementContext(),
    ...parameters
  });
}

function initInquiryTracking() {
  document.addEventListener('click', (event) => {
    const link = event.target.closest('a[href]');
    if (!link) return;

    const href = link.getAttribute('href') || '';
    const linkText = (link.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 100);

    if (/(?:^|\/)contact(?:\.html)?(?:[?#]|$)/i.test(href)) {
      let inquiryCategory = 'unspecified';
      try {
        inquiryCategory = new URL(link.href, window.location.href).searchParams.get('category') || 'unspecified';
      } catch (error) {
        // Keep the safe fallback when an older browser cannot parse the URL.
      }

      trackAnalyticsEvent('bf_contact_cta_click', {
        link_text: linkText,
        link_url: link.href,
        inquiry_category: inquiryCategory,
        inquiry_role: new URL(link.href, window.location.href).searchParams.get('role') || 'unspecified',
        inquiry_product: new URL(link.href, window.location.href).searchParams.get('product') || 'unspecified',
        source_page_path: window.location.pathname
      });
      return;
    }

    if (href.startsWith('mailto:') || href.startsWith('tel:')) {
      trackAnalyticsEvent('bf_contact_method_click', {
        contact_method: href.startsWith('mailto:') ? 'email' : 'phone',
        link_text: linkText
      });
    }
  });
}

/**
 * Carry the exact product slug into the inquiry URL so the form can retain
 * product context in addition to the referring page and broad category.
 */
function initProductInquiryLinks() {
  const segments = window.location.pathname.split('/').filter(Boolean);
  const locale = ['tw', 'en', 'jp'].includes(segments[0]) ? segments[0] : '';
  const slug = segments[1] || '';
  const productSlugs = ['display-hooks', 'optical-hooks', 'anti-theft-hooks', 'slatwall-pegboard-accessories', 'price-tag-holders', 'pos-displays', 'modular-fixtures', 'custom-metal-parts', 'cosmetic-organizers'];
  if (!locale || !productSlugs.includes(slug)) return;

  document.querySelectorAll('a[href]').forEach((link) => {
    try {
      const url = new URL(link.href, window.location.href);
      if (url.origin !== window.location.origin || !/(?:^|\/)contact(?:\.html)?$/i.test(url.pathname)) return;
      if (url.searchParams.get('product') === slug) return;
      url.searchParams.set('product', slug);
      link.href = `${url.pathname}${url.search}${url.hash}`;
    } catch (error) {
      // Keep the original link when an older browser cannot parse it.
    }
  });
}

/**
 * Preserve the visitor's role and inquiry context when a CTA opens the form.
 * Query values are controlled category labels only; never copy personal data.
 */
function initInquiryContext() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  const params = new URLSearchParams(window.location.search);
  const category = params.get('category') || '';
  const role = params.get('role') || '';
  const product = params.get('product') || '';
  const requestedFiles = params.get('requested_files') || '';
  let sourcePage = '';
  try {
    if (document.referrer && new URL(document.referrer).origin === window.location.origin) {
      sourcePage = document.referrer;
    }
  } catch (error) {
    // Keep the safe empty fallback for malformed or cross-origin referrers.
  }

  const contextMap = {
    integration: { inquiry_type: 'integration', product_category: 'not_sure' },
    display_hardware: { inquiry_type: 'quote', product_category: 'display_hardware' },
    system_fixtures: { inquiry_type: 'quote', product_category: 'system_fixtures' },
    pos_displays: { inquiry_type: 'quote', product_category: 'pos_displays' },
    pos_display: { inquiry_type: 'quote', product_category: 'pos_displays' },
    modular_fixture: { inquiry_type: 'quote', product_category: 'system_fixtures' },
    signage: { inquiry_type: 'quote', product_category: 'display_hardware' },
    custom_metal_components: { inquiry_type: 'custom_dev', product_category: 'custom_metal_components' }
  };
  const roleMap = {
    brand: 'brand_store_development',
    designer: 'store_design_engineering',
    buyer: 'buyer_trading_agent',
    vm: 'visual_merchandising'
  };
  const mapped = contextMap[category] || {};
  const setValue = (id, value) => {
    const field = document.getElementById(id);
    if (!field || !value) return;
    field.value = value;
    field.defaultValue = value;
  };

  setValue('inquiry_type', mapped.inquiry_type);
  setValue('product_category', mapped.product_category);
  setValue('buyer_role', roleMap[role]);
  setValue('source_category', category || 'unspecified');
  setValue('source_role', role || 'unspecified');
  setValue('source_product', product || 'unspecified');
  setValue('requested_files', requestedFiles);
  setValue('source_page', sourcePage);
}

/**
 * 1. Header scroll effect: Adds background and shrinks header on scroll
 */
function initHeaderScroll() {
  const header = document.querySelector('.header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  // Run on load in case page is already scrolled
  handleScroll();
  window.addEventListener('scroll', handleScroll);
}

/**
 * 2. Mobile Burger Menu toggle
 */
function initMobileMenu() {
  const toggle = document.querySelector('.mobile-toggle');
  const menu = document.querySelector('.nav-menu');

  if (!toggle || !menu) return;

  const setMenuState = (isOpen) => {
    toggle.classList.toggle('active', isOpen);
    menu.classList.toggle('active', isOpen);
    toggle.setAttribute('aria-expanded', String(isOpen));
    document.body.classList.toggle('menu-open', isOpen);
  };

  toggle.addEventListener('click', () => {
    setMenuState(!menu.classList.contains('active'));
  });

  // Close menu when clicking on a link
  const links = document.querySelectorAll('.nav-link');
  links.forEach(link => {
    link.addEventListener('click', () => {
      setMenuState(false);
    });
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menu.classList.contains('active')) {
      setMenuState(false);
      toggle.focus();
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 768) setMenuState(false);
  });
}

/**
 * 3. Scroll Reveal Animations (using Intersection Observer)
 */
function initScrollAnimations() {
  const reveals = document.querySelectorAll('.reveal');
  if (reveals.length === 0) return;

  const revealAboveFold = () => {
    reveals.forEach(el => {
      if (el.getBoundingClientRect().top < window.innerHeight * 1.15) {
        el.classList.add('reveal-active');
      }
    });
  };
  revealAboveFold();

  if (!('IntersectionObserver' in window)) {
    reveals.forEach(el => el.classList.add('reveal-active'));
    return;
  }

  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1 // Triggers when 10% of element is visible
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal-active');
        // Stop observing once animated in
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  reveals.forEach(el => observer.observe(el));
}

/**
 * 4. Language selector tracker (saves user choice to localStorage on click)
 */
function initLanguageTracker() {
  const langSelector = document.querySelector('.lang-selector');
  const langButton = document.querySelector('.lang-btn');
  const langItems = document.querySelectorAll('.lang-dropdown-item');

  if (langSelector && langButton) {
    langButton.addEventListener('click', () => {
      const isOpen = langSelector.classList.toggle('active');
      langButton.setAttribute('aria-expanded', String(isOpen));
    });

    document.addEventListener('click', (event) => {
      if (!langSelector.contains(event.target)) {
        langSelector.classList.remove('active');
        langButton.setAttribute('aria-expanded', 'false');
      }
    });
  }

  langItems.forEach(item => {
    item.addEventListener('click', () => {
      const selectedLang = item.getAttribute('data-lang');
      if (selectedLang) {
        localStorage.setItem('bf_lang', selectedLang);
      }
    });
  });
}

/**
 * 5. Highlights the active nav link based on current page URL
 */
function highlightActiveLink() {
  const normalizePath = (path) => {
    const value = path.replace(/\/index\.html?$/, '/').replace(/\.html?$/, '');
    return value.length > 1 ? value.replace(/\/$/, '') : '/';
  };
  const currentPath = normalizePath(window.location.pathname);
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    
    let linkPath = '';
    try {
      linkPath = normalizePath(new URL(href, window.location.href).pathname);
    } catch (error) {
      return;
    }
    if (linkPath === currentPath) {
      link.classList.add('active');
    }
  });
}

/**
 * 6. Page transition animations
 */
function initPageTransitions() {
  document.body.classList.add('page-loaded');
  
  const transitionLinks = document.querySelectorAll('a:not([target="_blank"]):not([href^="#"]):not([href^="mailto:"]):not([href^="tel:"]):not(.lang-dropdown-item)');
  transitionLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      // Allow modifier keys (Ctrl, Shift, Alt, Cmd) and non-left clicks (like middle click to open in new tab)
      if (e.button !== 0 || e.ctrlKey || e.shiftKey || e.altKey || e.metaKey) {
        return;
      }
      const href = link.getAttribute('href');
      if (href && href !== '') {
        e.preventDefault();
        document.body.classList.remove('page-loaded');
        setTimeout(() => {
          window.location.href = href;
        }, 150);
      }
    });
  });
}

/**
 * 7. Magnetic cursor/hover effects on buttons
 */
function initMagneticButtons() {
  const buttons = document.querySelectorAll('.btn-primary, .btn-secondary');
  buttons.forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left - (rect.width / 2);
      const y = e.clientY - rect.top - (rect.height / 2);
      btn.style.transform = `translate(${x * 0.25}px, ${y * 0.25}px)`;
    });
    
    btn.addEventListener('mouseleave', () => {
      btn.style.transform = 'translate(0px, 0px)';
    });
  });
}

/**
 * 8. Real-time office status and local time display
 */
function initOfficeStatus() {
  const statusContainers = document.querySelectorAll('.office-status');
  if (statusContainers.length === 0) return;
  
  const updateTimes = () => {
    statusContainers.forEach(container => {
      const offset = parseInt(container.getAttribute('data-offset') || '8');
      const lang = document.documentElement.lang || 'ja';
      
      // Calculate local time for timezone
      const utc = Date.now() + (new Date().getTimezoneOffset() * 60000);
      const localTime = new Date(utc + (3600000 * offset));
      
      const hours = localTime.getHours();
      const day = localTime.getDay(); // 0 = Sun, 6 = Sat
      
      // Simple business hours check: Monday-Friday, 9:00 - 18:00
      const isOpen = (day >= 1 && day <= 5) && (hours >= 9 && hours < 18);
      
      const timeStr = localTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
      
      // Multi-language text maps (without dots, dots styled via CSS status-dot)
      let badgeText = '';
      let statusClass = '';
      let localLabel = '';
      
      if (lang === 'ja') {
        badgeText = isOpen ? '営業中' : '営業時間外';
        localLabel = '現地時間';
      } else if (lang === 'en') {
        badgeText = isOpen ? 'Open' : 'Closed';
        localLabel = 'Local Time';
      } else { // tw
        badgeText = isOpen ? '營業中' : '休息中';
        localLabel = '當地時間';
      }
      
      statusClass = isOpen ? 'status-open' : 'status-closed';
      
      container.innerHTML = `
        <span class="status-badge ${statusClass}">
          <span class="status-dot"></span>
          <span class="status-text">${badgeText}</span>
        </span> 
        <span>(${localLabel}: ${timeStr})</span>
      `;
    });
  };
  
  // Initial run and interval update every 15s
  updateTimes();
  setInterval(updateTimes, 15000);
}


/**
 * 9. AJAX Form submission for Web3Forms (with Loading and success popups)
 */
function initContactForm() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  const btn = form.querySelector('button[type="submit"]');
  const btnOriginalText = btn.innerText;
  let formStarted = false;

  form.addEventListener('focusin', (event) => {
    if (formStarted || !event.target.matches('input, select, textarea')) return;
    formStarted = true;
    trackAnalyticsEvent('form_start', {
      inquiry_category: String(form.querySelector('[name="source_category"]')?.value || 'unspecified'),
      inquiry_role: String(form.querySelector('[name="source_role"]')?.value || 'unspecified'),
      inquiry_product: String(form.querySelector('[name="source_product"]')?.value || 'unspecified'),
      requested_files: String(form.querySelector('[name="requested_files"]')?.value || 'unspecified'),
      source_page_path: String(form.querySelector('[name="source_page"]')?.value || 'unspecified')
    });
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Set loading state
    btn.disabled = true;
    btn.innerHTML = `<span class="spinner"></span> Sending...`;

    const formData = new FormData(form);

    trackAnalyticsEvent('bf_form_submit_attempt', {
      inquiry_type: String(formData.get('inquiry_type') || 'unspecified'),
      product_category: String(formData.get('product_category') || 'unspecified'),
      requested_files: String(formData.get('requested_files') || 'unspecified'),
      inquiry_category: String(formData.get('source_category') || 'unspecified'),
      inquiry_role: String(formData.get('source_role') || 'unspecified'),
      inquiry_product: String(formData.get('source_product') || 'unspecified')
    });
    
    // Fallback Mock for testing
    const accessKey = formData.get('access_key');
    if (accessKey === 'YOUR_ACCESS_KEY_HERE') {
      setTimeout(() => {
        showFormStatus(true, getLangSuccessMsg(document.documentElement.lang));
        form.reset();
        btn.disabled = false;
        btn.innerText = btnOriginalText;
      }, 1000);
      return;
    }

    try {
      const response = await fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        body: formData
      });
      const data = await response.json();
      if (data.success) {
        trackAnalyticsEvent('generate_lead', {
          currency: 'USD',
          value: 0,
          inquiry_type: String(formData.get('inquiry_type') || 'unspecified'),
          product_category: String(formData.get('product_category') || 'unspecified'),
          requested_files: String(formData.get('requested_files') || 'unspecified'),
          inquiry_category: String(formData.get('source_category') || 'unspecified'),
          inquiry_role: String(formData.get('source_role') || 'unspecified'),
          inquiry_product: String(formData.get('source_product') || 'unspecified'),
          source_page_path: String(formData.get('source_page') || 'unspecified')
        });
        showFormStatus(true, getLangSuccessMsg(document.documentElement.lang));
        form.reset();
      } else {
        trackAnalyticsEvent('bf_form_submit_error', {
          error_type: 'web3forms_rejected',
          inquiry_type: String(formData.get('inquiry_type') || 'unspecified'),
          product_category: String(formData.get('product_category') || 'unspecified'),
          requested_files: String(formData.get('requested_files') || 'unspecified')
        });
        showFormStatus(false, data.message || 'Error sending message.');
      }
    } catch (err) {
      trackAnalyticsEvent('bf_form_submit_error', {
          error_type: 'network_or_parse_error',
          inquiry_type: String(formData.get('inquiry_type') || 'unspecified'),
          product_category: String(formData.get('product_category') || 'unspecified'),
          requested_files: String(formData.get('requested_files') || 'unspecified')
      });
      showFormStatus(false, 'Failed to connect to server. Please try again.');
    } finally {
      btn.disabled = false;
      btn.innerText = btnOriginalText;
    }
  });
}

function showFormStatus(isSuccess, message) {
  // Create modal element if not exists
  let modal = document.getElementById('formStatusModal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'formStatusModal';
    modal.className = 'form-status-modal';
    modal.setAttribute('role', 'status');
    modal.setAttribute('aria-live', 'assertive');
    modal.setAttribute('aria-atomic', 'true');
    modal.setAttribute('tabindex', '-1');
    document.body.appendChild(modal);
  }
  
  modal.innerText = message;
  modal.className = isSuccess ? 'form-status-modal show' : 'form-status-modal show error';
  modal.focus({ preventScroll: true });
  
  // Keep the result visible long enough to be read on desktop and mobile.
  setTimeout(() => {
    modal.classList.remove('show');
  }, 8000);
}

function getLangSuccessMsg(lang) {
  if (lang === 'ja') {
    return 'お問い合わせありがとうございます。担当者よりご連絡いたします。';
  } else if (lang === 'en') {
    return 'Inquiry submitted successfully! We will get back to you shortly.';
  } else { // tw
    return '詢問送出成功！我們的專案經理會儘快與您聯絡。';
  }
}

/**
 * 10. Theme Switcher (Dark/Light Mode) Dynamic Injection & Controller
 */
function initThemeSwitcher() {
  const savedTheme = localStorage.getItem('theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const isDark = savedTheme === 'dark' || (!savedTheme && systemPrefersDark);
  
  if (isDark) {
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    document.documentElement.removeAttribute('data-theme');
  }
  
  const langSelector = document.querySelector('.lang-selector');
  if (!langSelector) return;
  
  const toggleBtn = document.createElement('button');
  toggleBtn.className = 'theme-toggle';
  toggleBtn.id = 'themeToggle';
  toggleBtn.setAttribute('aria-label', 'Toggle Theme');
  
  const sunSvg = `
    <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: ${isDark ? 'block' : 'none'};">
      <circle cx="12" cy="12" r="5"></circle>
      <line x1="12" y1="1" x2="12" y2="3"></line>
      <line x1="12" y1="21" x2="12" y2="23"></line>
      <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
      <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
      <line x1="1" y1="12" x2="3" y2="12"></line>
      <line x1="21" y1="12" x2="23" y2="12"></line>
      <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
      <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
    </svg>
  `;
  const moonSvg = `
    <svg class="moon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: ${isDark ? 'none' : 'block'};">
      <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
    </svg>
  `;
  
  toggleBtn.innerHTML = sunSvg + moonSvg;
  langSelector.parentNode.insertBefore(toggleBtn, langSelector.nextSibling);
  
  toggleBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const sunIcon = toggleBtn.querySelector('.sun-icon');
    const moonIcon = toggleBtn.querySelector('.moon-icon');
    
    if (currentTheme === 'dark') {
      document.documentElement.removeAttribute('data-theme');
      localStorage.setItem('theme', 'light');
      sunIcon.style.display = 'none';
      moonIcon.style.display = 'block';
    } else {
      document.documentElement.setAttribute('data-theme', 'dark');
      localStorage.setItem('theme', 'dark');
      sunIcon.style.display = 'block';
      moonIcon.style.display = 'none';
    }
  });
}

/**
 * 11. Dynamic Particle Background (Canvas overlay in Hero Section)
 */
function initHeroParticles() {
  const hero = document.querySelector('.hero');
  if (!hero) return;
  
  // Only enable particles on desktop (768px+)
  if (window.innerWidth < 768) return;
  
  const canvas = document.createElement('canvas');
  canvas.className = 'hero-canvas';
  hero.appendChild(canvas);
  
  const ctx = canvas.getContext('2d');
  let particles = [];
  let width = canvas.width = hero.offsetWidth;
  let height = canvas.height = hero.offsetHeight;
  
  const handleResize = () => {
    width = canvas.width = hero.offsetWidth;
    height = canvas.height = hero.offsetHeight;
  };
  window.addEventListener('resize', handleResize);
  
  class Particle {
    constructor() {
      this.reset();
    }
    
    reset() {
      this.x = Math.random() * width;
      this.y = Math.random() * height + height;
      this.size = Math.random() * 2 + 1;
      this.speedY = -(Math.random() * 0.4 + 0.1);
      this.speedX = (Math.random() * 0.2 - 0.1);
      this.opacity = Math.random() * 0.5 + 0.1;
    }
    
    update() {
      this.y += this.speedY;
      this.x += this.speedX;
      
      if (this.y < 0 || this.x < 0 || this.x > width) {
        this.reset();
        this.y = height + Math.random() * 20;
      }
    }
    
    draw() {
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      const color = isDark ? `rgba(197, 168, 128, ${this.opacity})` : `rgba(43, 58, 74, ${this.opacity * 0.7})`;
      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fill();
    }
  }
  
  const particleCount = 20;
  for (let i = 0; i < particleCount; i++) {
    const p = new Particle();
    p.y = Math.random() * height;
    particles.push(p);
  }
  
  function animate() {
    ctx.clearRect(0, 0, width, height);
    particles.forEach(p => {
      p.update();
      p.draw();
    });
    requestAnimationFrame(animate);
  }
  
  animate();
}

/**
 * 12. Dynamic Scroll Down Mouse Indicator
 */
function initScrollIndicator() {
  const hero = document.querySelector('.hero');
  if (!hero) return;
  
  const indicator = document.createElement('div');
  indicator.className = 'scroll-indicator';
  
  const isTW = document.documentElement.lang === 'zh-Hant-TW' || window.location.pathname.includes('/tw/');
  const isJP = document.documentElement.lang === 'ja' || window.location.pathname.includes('/jp/');
  let scrollText = 'Scroll Down';
  if (isTW) scrollText = '向下滾動';
  else if (isJP) scrollText = 'スクロール';
  
  indicator.innerHTML = `
    <div class="scroll-indicator-mouse">
      <div class="scroll-indicator-wheel"></div>
    </div>
    <span class="scroll-indicator-text">${scrollText}</span>
  `;
  
  hero.appendChild(indicator);
  
  indicator.addEventListener('click', () => {
    const nextSection = hero.nextElementSibling;
    if (nextSection) {
      nextSection.scrollIntoView({ behavior: 'smooth' });
    }
  });
}

// Keep the form result and mobile scroll cue readable in every supported language.
function getLangSuccessMsg(lang) {
  if (lang === 'ja') return 'お問い合わせを受け付けました。内容を確認してご連絡します。';
  if (lang === 'en') return 'Inquiry submitted successfully! We will get back to you shortly.';
  return '需求已送出，我們會確認內容後與您聯絡。';
}

function initScrollIndicator() {
  const hero = document.querySelector('.hero');
  if (!hero || hero.querySelector('.scroll-indicator')) return;
  const indicator = document.createElement('div');
  indicator.className = 'scroll-indicator';
  const lang = document.documentElement.lang;
  const label = lang === 'ja' ? 'スクロール' : (lang === 'en' ? 'Scroll down' : '往下查看');
  indicator.innerHTML = '<div class="scroll-indicator-mouse"><div class="scroll-indicator-wheel"></div></div><span class="scroll-indicator-text">' + label + '</span>';
  hero.appendChild(indicator);
  indicator.addEventListener('click', () => {
    const nextSection = hero.nextElementSibling;
    if (nextSection) nextSection.scrollIntoView({ behavior: 'smooth' });
  });
}
