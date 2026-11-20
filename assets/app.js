/* Big Fame Prototype v2 — GA4 (bf_contact_method_click + generate_lead), Intent-Driven Progressive Inquiry & Mobile Nav */
(function () {
  'use strict';

  var GA4_ID = 'G-PDW4NPHHW8';
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };

  function trackEvent(eventName, params) {
    var payload = Object.assign({
      page_path: window.location.pathname,
      page_lang: document.documentElement.lang || 'en'
    }, params || {});

    try {
      window.gtag('event', eventName, payload);
    } catch (e) {}
    window.__bfAnalyticsLog = window.__bfAnalyticsLog || [];
    window.__bfAnalyticsLog.push({ event: eventName, params: payload, ts: Date.now() });
  }

  // 1. Mobile Navigation Toggle (390px / 768px safe)
  var toggleBtn = document.getElementById('bf-menu-toggle');
  var drawer = document.getElementById('bf-mobile-drawer');
  if (toggleBtn && drawer) {
    toggleBtn.addEventListener('click', function () {
      var expanded = toggleBtn.getAttribute('aria-expanded') === 'true';
      toggleBtn.setAttribute('aria-expanded', String(!expanded));
      drawer.classList.toggle('open', !expanded);
    });
  }

  // 2. Preserve existing GA4 P0 Gatekeeper event: bf_contact_method_click + Copy Email helper
  document.addEventListener('click', function (ev) {
    var copyBtn = ev.target.closest('[data-copy-email]');
    if (copyBtn) {
      var addr = copyBtn.getAttribute('data-copy-email') || '';
      var copiedLabel = copyBtn.getAttribute('data-copied-label') || 'Copied!';
      var origLabel = copyBtn.getAttribute('data-orig-label') || copyBtn.textContent;
      copyBtn.setAttribute('data-orig-label', origLabel);
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(addr).catch(function () {});
      }
      copyBtn.textContent = copiedLabel;
      setTimeout(function () { copyBtn.textContent = origLabel; }, 2200);
    }

    var el = ev.target.closest('[data-contact-method]');
    if (!el) return;
    trackEvent('bf_contact_method_click', {
      contact_method: el.getAttribute('data-contact-method'),
      link_url: el.getAttribute('href') || el.getAttribute('data-copy-email') || ''
    });
  });

  // 3. Portfolio Filter (Real Completed vs Concept Studies)
  var filterButtons = document.querySelectorAll('[data-case-filter]');
  var caseCards = document.querySelectorAll('[data-case-kind]');
  if (filterButtons.length && caseCards.length) {
    filterButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var target = btn.getAttribute('data-case-filter');
        filterButtons.forEach(function (b) { b.classList.toggle('active', b === btn); });
        caseCards.forEach(function (card) {
          var kind = card.getAttribute('data-case-kind');
          card.style.display = (target === 'all' || kind === target) ? '' : 'none';
        });
      });
    });
  }

  // 4. Intent-Driven Progressive Inquiry (Only shows relevant fields for the chosen intent)
  var form = document.getElementById('bf-inquiry-form');
  var formPanel = document.getElementById('bf-form-panel');
  var emailPanel = document.getElementById('bf-email-panel');
  var statusBox = document.getElementById('bf-form-status');
  var receiptList = document.getElementById('bf-receipt-list');
  var modeInput = document.getElementById('bf-mode-input');
  var modeHint = document.getElementById('bf-mode-hint');
  var choiceTabs = document.querySelectorAll('[data-inquiry-choice]');

  if (form && choiceTabs.length) {
    var reqField = form.querySelector('[name="requirements"]');
    var showBlocks = form.querySelectorAll('[data-show-for]');
    var activeMode = 'budget';

    function setInquiryChoice(mode) {
      if (['budget', 'quote', 'callback', 'email'].indexOf(mode) === -1) mode = 'budget';
      activeMode = mode;

      choiceTabs.forEach(function (tab) {
        var isMatch = tab.getAttribute('data-inquiry-choice') === mode;
        tab.classList.toggle('active', isMatch);
        tab.setAttribute('aria-selected', String(isMatch));
      });

      if (mode === 'email') {
        if (formPanel) formPanel.hidden = true;
        if (emailPanel) emailPanel.hidden = false;
        return;
      }

      if (formPanel) formPanel.hidden = false;
      if (emailPanel) emailPanel.hidden = true;
      if (modeInput) modeInput.value = mode;
      if (modeHint) {
        var hintAttr = modeHint.getAttribute('data-hint-' + mode);
        if (hintAttr) modeHint.textContent = hintAttr;
      }

      showBlocks.forEach(function (blk) {
        var allowed = (blk.getAttribute('data-show-for') || '').split(/\s+/);
        blk.hidden = allowed.indexOf(mode) === -1;
      });

      if (reqField) {
        reqField.required = (mode !== 'callback');
      }
      if (statusBox) {
        statusBox.classList.remove('visible');
      }
    }

    // Honor ?mode=budget|quote|callback|email
    try {
      var qMode = new URLSearchParams(window.location.search).get('mode');
      if (qMode) setInquiryChoice(qMode);
      else setInquiryChoice('budget');
    } catch (e) {
      setInquiryChoice('budget');
    }

    choiceTabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        setInquiryChoice(tab.getAttribute('data-inquiry-choice'));
      });
    });

    if (statusBox) {
      form.addEventListener('submit', function (ev) {
        ev.preventDefault();
        if (!form.checkValidity()) {
          form.reportValidity();
          return;
        }

        var activeTab = document.querySelector('[data-inquiry-choice="' + activeMode + '"] .choice-tab-title');
        var modeLabel = activeTab ? activeTab.textContent.trim() : activeMode;

        var email = (form.querySelector('[name="email"]') || {}).value.trim();
        var contactAlt = (form.querySelector('[name="contact_alt"]') || {}).value.trim();
        var requirements = activeMode === 'callback'
          ? ((form.querySelector('[name="callback_note"]') || {}).value || '').trim()
          : ((form.querySelector('[name="requirements"]') || {}).value || '').trim();
        var ndaFirst = activeMode !== 'callback' && !!(form.querySelector('[name="nda_first"]') || {}).checked;
        var refLink = activeMode !== 'callback' ? ((form.querySelector('[name="reference_link"]') || {}).value || '').trim() : '';
        var fileInput = form.querySelector('[name="reference_file"]');
        var fileNames = (activeMode !== 'callback' && fileInput && fileInput.files && fileInput.files.length)
          ? Array.prototype.map.call(fileInput.files, function (f) { return f.name; }).join(', ')
          : '';
        var batchQty = activeMode === 'quote' ? ((form.querySelector('[name="batch_qty"]') || {}).value || '').trim() : '';
        var quoteDate = activeMode === 'quote' ? ((form.querySelector('[name="quote_date"]') || {}).value || '').trim() : '';
        var deliveryDate = activeMode === 'quote' ? ((form.querySelector('[name="delivery_date"]') || {}).value || '').trim() : '';
        var company = (form.querySelector('[name="company"]') || {}).value.trim();
        var contactName = (form.querySelector('[name="name"]') || {}).value.trim();

        var record = {
          inquiry_mode: activeMode,
          inquiry_mode_label: modeLabel,
          email: email,
          contact_alt: contactAlt || '-',
          requirements: requirements || '-',
          nda_first: ndaFirst,
          reference_link: refLink || '-',
          reference_files: fileNames || '-',
          batch_qty: batchQty || '-',
          quote_date: quoteDate || '-',
          delivery_date: deliveryDate || '-',
          company: company || '-',
          name: contactName || '-',
          page_lang: document.documentElement.lang || 'en',
          submitted_at: new Date().toISOString()
        };

        window.__bfLastSubmission = record;

        var isLocal = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1');
        if (!isLocal) {
          try {
            var fd = new FormData(form);
            fd.set('inquiry_mode', activeMode);
            fd.set('requirements', requirements);
            fd.set('nda_first', ndaFirst ? 'yes' : 'no');
            fetch('/', { method: 'POST', body: fd }).catch(function () {});
          } catch (e) {}
        }

        trackEvent('generate_lead', {
          event_category: 'engineering_inquiry',
          inquiry_mode: activeMode,
          nda_first: ndaFirst ? 'yes' : 'no',
          has_reference: (refLink || fileNames) ? 'yes' : 'no',
          has_dates: (quoteDate || deliveryDate) ? 'yes' : 'no',
          currency: 'USD',
          value: 1
        });

        if (receiptList) {
          receiptList.innerHTML = '';
          var rows = [
            ['Entry / 入口', modeLabel],
            ['Email', email]
          ];
          if (contactAlt) rows.push(['Alt Contact', contactAlt]);
          if (requirements) rows.push(['Note / Requirements', requirements]);
          if (activeMode !== 'callback') {
            rows.push(['NDA First', ndaFirst ? 'Yes' : 'No']);
            rows.push(['Ref Link / File', (refLink || fileNames) ? [refLink, fileNames].filter(Boolean).join(' | ') : '-']);
          }
          if (activeMode === 'quote') {
            rows.push(['Batch Qty', batchQty || '-']);
            rows.push(['Quote Date', quoteDate || '-']);
            rows.push(['Delivery Date', deliveryDate || '-']);
          }
          if (company) rows.push(['Company', company]);
          if (contactName) rows.push(['Contact', contactName]);

          rows.forEach(function (pair) {
            var dt = document.createElement('dt');
            dt.textContent = pair[0];
            var dd = document.createElement('dd');
            dd.textContent = pair[1];
            receiptList.appendChild(dt);
            receiptList.appendChild(dd);
          });
        }

        statusBox.classList.add('visible');
        statusBox.setAttribute('tabindex', '-1');
        statusBox.focus();
        form.reset();
        setInquiryChoice(activeMode);
        statusBox.classList.add('visible');
      });
    }
  }

  window.__bfGA4Id = GA4_ID;
})();
