'use strict';
const frame = document.querySelector('#preview');
const picker = document.querySelector('#page');
const status = document.querySelector('#status');
const openPage = document.querySelector('#open-page');
const widths = [320, 390, 1280];
const pages = new Map([
  ['/atelier/', 'Homepage'],
  ['/atelier/projects/', 'Project routes'],
  ['/atelier/brief/', 'Brief builder']
]);
let width = 320;
function announce() {
  const label = pages.get(picker.value);
  status.textContent = label + ' · ' + width + ' × 844 CSS pixels';
  frame.title = label + ' preview at ' + width + ' pixels wide';
}
document.querySelectorAll('[data-width]').forEach(button => {
  button.addEventListener('click', () => {
    const next = Number(button.dataset.width);
    if (!widths.includes(next)) return;
    width = next;
    frame.style.width = width + 'px';
    frame.width = String(width);
    document.querySelectorAll('[data-width]').forEach(control => {
      control.setAttribute('aria-pressed', String(Number(control.dataset.width) === width));
    });
    announce();
  });
});
picker.addEventListener('change', () => {
  if (!pages.has(picker.value)) return;
  frame.src = picker.value;
  openPage.href = picker.value;
  announce();
});
