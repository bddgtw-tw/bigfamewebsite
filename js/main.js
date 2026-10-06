/* Shared navigation and truthful inquiry handling. No theme/effect injection. */
document.addEventListener('DOMContentLoaded',()=>{
 const button=document.querySelector('.menu-toggle'),nav=document.querySelector('.nav-menu');
 const setOpen=open=>{if(!button||!nav)return;button.setAttribute('aria-expanded',String(open));nav.classList.toggle('is-open',open);};
 button?.addEventListener('click',()=>setOpen(button.getAttribute('aria-expanded')!=='true'));
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&button?.getAttribute('aria-expanded')==='true'){setOpen(false);button.focus();}});
 nav?.addEventListener('click',e=>{if(e.target.closest('a'))setOpen(false);});
 window.addEventListener('resize',()=>{if(window.innerWidth>1280)setOpen(false);});
 const form=document.getElementById('contactForm');if(!form)return;
 const locale=document.body.dataset.locale;
 const messages={jp:{sending:'送信中…',ok:'送信を受け付けました。',error:'送信できませんでした。入力内容を保持しています。メールでもご相談いただけます。'},en:{sending:'Sending…',ok:'Your inquiry has been accepted.',error:'We could not send your inquiry. Your entries are preserved. You can also contact us by email.'},tw:{sending:'送出中…',ok:'已收到你的諮詢。',error:'暫時無法送出，填寫內容仍保留；也可改用 Email 聯絡。'}}[locale];
 const params=new URLSearchParams(location.search);
 for(const [name,key] of [['source_category','category'],['source_role','role'],['source_product','product']]){const input=form.elements.namedItem(name);if(input)input.value=params.get(key)||'';}
 const source=form.elements.namedItem('source_page');if(source)source.value=location.pathname;
 const submit=form.querySelector('button[type="submit"]'),status=document.getElementById('form-status'),original=submit.textContent;
 form.addEventListener('submit',async event=>{
  event.preventDefault();if(submit.disabled||!form.reportValidity())return;
  submit.disabled=true;submit.textContent=messages.sending;status.textContent='';status.className='';
  try{
   const data=new FormData(form);if(!data.get('access_key')||data.get('access_key')==='YOUR_ACCESS_KEY_HERE')throw new Error('Unconfigured form');
   const response=await fetch(form.action,{method:'POST',body:data});const result=await response.json();
   if(!response.ok||result.success!==true)throw new Error('Submission rejected');
   status.textContent=messages.ok;status.className='form-success';form.reset();
  }catch(error){status.textContent=messages.error;status.className='form-error';}
  finally{submit.disabled=false;submit.textContent=original;}
 });
});
