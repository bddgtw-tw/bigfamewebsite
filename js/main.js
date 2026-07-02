/* Big Fame IND. CORP. - Global JavaScript Logic */

document.addEventListener('DOMContentLoaded', () => {
  initHeaderScroll();
  initMobileMenu();
  initScrollAnimations();
  initLanguageTracker();
  highlightActiveLink();
  initPageTransitions();
  initMagneticButtons();
  initOfficeStatus();
});

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

  toggle.addEventListener('click', () => {
    toggle.classList.toggle('active');
    menu.classList.toggle('active');
  });

  // Close menu when clicking on a link
  const links = document.querySelectorAll('.nav-link');
  links.forEach(link => {
    link.addEventListener('click', () => {
      toggle.classList.remove('active');
      menu.classList.remove('active');
    });
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
  const langItems = document.querySelectorAll('.lang-dropdown-item');
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
      const href = link.getAttribute('href');
      if (href && href !== '') {
        e.preventDefault();
        document.body.classList.remove('page-loaded');
        setTimeout(() => {
          window.location.href = href;
        }, 350);
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
      
      // Multi-language text maps
      let badgeText = '';
      let statusClass = '';
      let localLabel = '';
      
      if (lang === 'ja') {
        badgeText = isOpen ? '● 営業中' : '○ 営業時間外';
        localLabel = '現地時間';
      } else if (lang === 'en') {
        badgeText = isOpen ? '● Open' : '○ Closed';
        localLabel = 'Local Time';
      } else { // tw
        badgeText = isOpen ? '● 營業中' : '○ 休息中';
        localLabel = '當地時間';
      }
      
      statusClass = isOpen ? 'status-open' : 'status-closed';
      
      container.innerHTML = `
        <span class="status-badge ${statusClass}">${badgeText}</span> 
        <span>(${localLabel}: ${timeStr})</span>
      `;
    });
  };
  
  // Initial run and interval update every 15s
  updateTimes();
  setInterval(updateTimes, 15000);
}
