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
 const build=()=>['Hello Big Fame,','I would like to discuss a retail display project.','',
 'Role: '+clean(form.elements.role.value),
 'Product type: '+clean(form.elements.category.value),
 'Estimated quantity: '+clean(form.elements.quantity.value),
 'Destination: '+clean(form.elements.destination.value),'',
 'Requirements:',clean(form.elements.requirements.value),'',
 'Please let me know which dimensions, drawings or samples would help you review this request.'].join('\n');
 const button=document.querySelector('#prepare');button.hidden=false;
 button.addEventListener('click',()=>{
  for(const el of [form.elements.quantity,form.elements.destination,form.elements.requirements])el.setCustomValidity(el.value.trim()?'':'Please enter a value, or write “Not decided”.');
  if(!form.reportValidity())return;
  draft.value=build();const uri='mailto:shopdisplay@bigfame.co?subject='+encodeURIComponent('Retail display project brief')+'&body='+encodeURIComponent(draft.value);
  emailLink.href=uri;
  emailLink.hidden=uri.length>1900;
  document.querySelector('#long-note').hidden=uri.length<=1900;
  result.hidden=false;status.textContent='Draft prepared. Nothing has been sent.';
  document.querySelector('#result-title').focus();
 });
 form.addEventListener('input',e=>{if(e.target.setCustomValidity)e.target.setCustomValidity('');result.hidden=true;status.textContent=''});
 form.addEventListener('change',()=>{result.hidden=true;status.textContent=''});
 form.addEventListener('submit',e=>e.preventDefault());
 emailLink.addEventListener('click',()=>{status.textContent='Opening your email app. Review the draft and send it there; this page cannot confirm delivery.'});
 document.querySelector('#copy-brief').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(draft.value);status.textContent='Brief copied. Paste it into an email to shopdisplay@bigfame.co.'}catch{draft.focus();draft.select();status.textContent='Select and copy the brief above using your device’s copy command.'}});
 document.querySelector('#copy-address').hidden=false;
 document.querySelector('#copy-address').addEventListener('click',async()=>{try{await navigator.clipboard.writeText('shopdisplay@bigfame.co');status.textContent='Email address copied.'}catch{status.textContent='Copy this address manually: shopdisplay@bigfame.co'}});
}
