'use strict';
document.body.classList.add('enhanced');
const menu=document.querySelector('.menu'), nav=document.querySelector('#navigation');
menu.hidden=false;
menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open)});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.focus()}});
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false')}));
const form=document.querySelector('#brief');
if(form){
 const roles=['Brand team','Retail designer','Procurement','Other'];
 const categories=['Display hooks & hardware','Custom retail fixtures','POS & countertop displays','Custom metal parts','Not sure yet'];
 const params=new URLSearchParams(location.search);
 if(roles.includes(params.get('role')))form.elements.role.value=params.get('role');
 if(categories.includes(params.get('category')))form.elements.category.value=params.get('category');
 const result=document.querySelector('#result'),draft=document.querySelector('#draft'),emailLink=document.querySelector('#open-email'),status=document.querySelector('#status');
 const clean=v=>String(v).trim().replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/g,'');
 const build=()=>['Hello Big Fame,','I would like to discuss the following project.','',
 'PROJECT REQUIREMENTS SUMMARY',
 '1. Project context',
 'Role: '+clean(form.elements.role.value),
 'Product type: '+clean(form.elements.category.value),'',
 '2. Quantity and destination',
 'Estimated quantity: '+clean(form.elements.quantity.value),
 'Destination: '+clean(form.elements.destination.value),'',
 '3. Timing and available information',
 'Target timing (requested, not confirmed): '+(clean(form.elements.timing.value)||'Not specified'),
 'Existing drawings / references: '+(clean(form.elements.drawings.value)||'Not specified'),'',
 '4. Requirements and open questions',clean(form.elements.requirements.value),'',
 'Please advise which dimensions, drawings or samples are needed next and what scope we should review before quotation.',
 'No files are attached by this brief builder.'].join('\n');
 const invalidate=()=>{
  const prepared=!result.hidden;
  result.hidden=true;
  draft.value='';
  emailLink.removeAttribute('href');
  status.textContent=prepared?'Details changed. Prepare a new brief before opening an email draft. Nothing has been sent.':'';
 };
 const fields=[...form.querySelectorAll('[data-error]')];
 const nativeUserInvalid=CSS.supports('selector(:user-invalid)');
 const attempted=new WeakSet();
 const syncError=(el,force=false)=>{
  if(!el.dataset.error)return;
  const shown=!el.validity.valid&&(force||attempted.has(el)||(nativeUserInvalid&&el.matches(':user-invalid')));
  el.setAttribute('aria-invalid',String(shown));
  document.getElementById(el.dataset.error).hidden=!shown;
  const ids=(el.getAttribute('aria-describedby')||'').split(/\s+/).filter(id=>id&&id!==el.dataset.error);
  if(shown)ids.push(el.dataset.error);
  if(ids.length)el.setAttribute('aria-describedby',ids.join(' '));else el.removeAttribute('aria-describedby');
 };
 form.addEventListener('invalid',e=>{attempted.add(e.target);syncError(e.target,true)},true);
 form.addEventListener('focusout',e=>syncError(e.target));
 const button=document.querySelector('#prepare');button.hidden=false;
 button.addEventListener('click',()=>{
  for(const el of [form.elements.quantity,form.elements.destination,form.elements.requirements])el.setCustomValidity(el.value.trim()?'':'Please enter a value, or write “Not decided”.');
  fields.forEach(el=>{attempted.add(el);syncError(el,true)});
  if(!form.reportValidity()){status.textContent='Please correct the fields marked Error. Nothing has been sent.';return;}
  draft.value=build();const uri='mailto:shopdisplay@bigfame.co?subject='+encodeURIComponent('Retail display project brief')+'&body='+encodeURIComponent(draft.value);
  emailLink.href=uri;
  emailLink.hidden=uri.length>1900;
  document.querySelector('#long-note').hidden=uri.length<=1900;
  result.hidden=false;status.textContent='Draft prepared. Nothing has been sent.';
  document.querySelector('#result-title').focus();
 });
 form.addEventListener('input',e=>{if(e.target.setCustomValidity)e.target.setCustomValidity('');syncError(e.target);invalidate()});
 form.addEventListener('change',e=>{syncError(e.target);invalidate()});
 form.addEventListener('submit',e=>e.preventDefault());
 emailLink.addEventListener('click',()=>{status.textContent='Opening your email app. Review the draft and send it there; this page cannot confirm delivery.'});
 document.querySelector('#copy-brief').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(draft.value);status.textContent='Brief copied. Paste it into an email to shopdisplay@bigfame.co.'}catch{draft.focus();draft.select();status.textContent='Select and copy the brief above using your device’s copy command.'}});
 document.querySelector('#copy-address').hidden=false;
 document.querySelector('#copy-address').addEventListener('click',async()=>{try{await navigator.clipboard.writeText('shopdisplay@bigfame.co');status.textContent='Email address copied.'}catch{status.textContent='Copy this address manually: shopdisplay@bigfame.co'}});
}
