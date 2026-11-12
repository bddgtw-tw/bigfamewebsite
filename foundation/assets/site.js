(function(){
'use strict';
function validate(values){
 const errors=[];
 for(const key of ['name','email','company','product','market','brief'])if(!String(values[key]||'').trim())errors.push(key);
 if(values.email&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(values.email))errors.push('email');
 if(values.reference){try{const url=new URL(values.reference);if(!['http:','https:'].includes(url.protocol))errors.push('reference');}catch{errors.push('reference');}}
 return [...new Set(errors)];
}
if(typeof module!=='undefined')module.exports={validate};
if(typeof document==='undefined')return;
const form=document.getElementById('brief-form');if(!form)return;
const chosen=new URLSearchParams(location.search).get('product');if(['eyewear','custom'].includes(chosen))form.elements.product.value=chosen;
const status=document.getElementById('status'),result=document.getElementById('result');let summary='';
form.addEventListener('input',()=>{result.hidden=true;summary='';status.textContent='';});
form.addEventListener('submit',e=>{
 e.preventDefault(); const values=Object.fromEntries(new FormData(form));for(const k in values)values[k]=values[k].trim();
 const errors=validate(values);for(const field of form.querySelectorAll('input,select,textarea'))field.setAttribute('aria-invalid',String(errors.includes(field.name)));
 if(errors.length){result.hidden=true;status.textContent=form.dataset.error;form.elements[errors[0]].focus();return;}
 summary='BIG FAME — PROJECT BRIEF / 詢價摘要\nDEMO: NOT SENT / 示範：尚未送出\n\n'+Object.entries(values).map(([k,v])=>k+': '+v).join('\n');
 document.getElementById('summary').textContent=summary;
 const mail=document.getElementById('email-brief');if(mail){mail.href='mailto:shopdisplay@bigfame.co?subject='+encodeURIComponent('Big Fame project inquiry')+'&body='+encodeURIComponent(summary.replace('DEMO: NOT SENT / 示範：尚未送出','Prepared by the visitor; sent only through their email app.'));mail.hidden=false;}result.hidden=false;status.textContent=form.dataset.success;status.focus();
});
document.getElementById('download').addEventListener('click',()=>{if(!summary)return;const url=URL.createObjectURL(new Blob([summary],{type:'text/plain;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download='big-fame-project-brief.txt';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);});
// Enable only after all local-only handlers are installed. Fail closed without JS.
form.querySelector('button[type="submit"]').disabled=false;
})();
