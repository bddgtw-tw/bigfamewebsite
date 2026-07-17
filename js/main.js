/* Big Fame IND. CORP. - Global JavaScript Logic */
const SITE_VERSION = '1.3.9';

document.addEventListener('DOMContentLoaded', () => {
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
  initContactForm();
  initHeroParticles();
  initScrollIndicator();
});

/**
 * Send privacy-safe B2B inquiry events to GA4.
 * Never include form field values or other personally identifiable information.
 */
function trackAnalyticsEvent(eventName, parameters = {}) {
  if (typeof window.gtag !== 'function') return;

  window.gtag('event', eventName, {
    site_language: document.documentElement.lang || 'unknown',
    page_path: window.location.pathname,
    ...parameters
  });
}

function initInquiryTracking() {
  document.addEventListener('click', (event) => {
    const link = event.target.closest('a[href]');
    if (!link) return;

    const href = link.getAttribute('href') || '';
    const linkText = (link.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 100);

    if (/contact\.html(?:[?#]|$)/i.test(href)) {
      let inquiryCategory = 'unspecified';
      try {
        inquiryCategory = new URL(link.href, window.location.href).searchParams.get('category') || 'unspecified';
      } catch (error) {
        // Keep the safe fallback when an older browser cannot parse the URL.
      }

      trackAnalyticsEvent('bf_contact_cta_click', {
        link_text: linkText,
        link_url: link.href,
        inquiry_category: inquiryCategory
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
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    
    // Check if path ends with href or if it's the home page
    const cleanHref = href.replace('../', '');
    if (currentPath.includes(cleanHref) && cleanHref !== '') {
      link.classList.add('active');
    } else if ((currentPath.endsWith('/') || currentPath.endsWith('index.html')) && (cleanHref === 'index.html' || cleanHref === '')) {
      // Handle home page variations
      const linkLang = link.closest('.lang-dropdown-item') ? null : link;
      if (linkLang) {
        // Only active if it's direct navigation
        link.classList.add('active');
      }
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

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Set loading state
    btn.disabled = true;
    btn.innerHTML = `<span class="spinner"></span> Sending...`;

    const formData = new FormData(form);
    
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
          product_category: String(formData.get('product_category') || 'unspecified')
        });
        showFormStatus(true, getLangSuccessMsg(document.documentElement.lang));
        form.reset();
      } else {
        showFormStatus(false, data.message || 'Error sending message.');
      }
    } catch (err) {
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
    document.body.appendChild(modal);
  }
  
  modal.innerText = message;
  modal.className = isSuccess ? 'form-status-modal show' : 'form-status-modal show error';
  
  // Hide after 4 seconds
  setTimeout(() => {
    modal.classList.remove('show');
  }, 4000);
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
