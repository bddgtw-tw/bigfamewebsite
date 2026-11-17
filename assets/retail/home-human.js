document.documentElement.classList.add('motion-ready');

const revealItems = [...document.querySelectorAll('.reveal')];
if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: .14, rootMargin: '0px 0px -8% 0px' });
  revealItems.forEach((item) => revealObserver.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add('is-visible'));
}

const processRow = document.querySelector('.process-row');
const progressFill = document.querySelector('.progress span');
if (processRow && progressFill) {
  const updateProgress = () => {
    const max = processRow.scrollWidth - processRow.clientWidth;
    const ratio = max > 0 ? processRow.scrollLeft / max : 0;
    progressFill.style.transform = `scaleX(${Math.max(.18, ratio)})`;
  };
  processRow.addEventListener('scroll', updateProgress, { passive: true });
  updateProgress();
}

const choices = [...document.querySelectorAll('.choice')];
const result = document.querySelector('.choice-result');
const contactLink = document.querySelector('.choice-contact');
choices.forEach((choice) => {
  choice.addEventListener('click', () => {
    choices.forEach((item) => item.setAttribute('aria-pressed', 'false'));
    choice.setAttribute('aria-pressed', 'true');
    if (result) result.textContent = choice.dataset.result || '';
    if (contactLink) contactLink.href = choice.dataset.href || contactLink.href;
  });
});
