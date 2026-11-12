/* Preview-safe inquiry transport. No credentials or personal data in analytics. */
(function(root){
'use strict';
async function sendBrief(values, config, fetcher){
 if(!config || config.enabled !== true || !config.accessKey) return {status:'disabled'};
 const data=new FormData(); data.set('access_key',config.accessKey);
 data.set('subject','Big Fame project inquiry'); data.set('from_name','Big Fame Website');
 for(const field of ['name','email','company','product','market','quantity','brief','reference']) data.set(field,String(values[field]||'').slice(0,field==='brief'?4000:500));
 const controller=new AbortController();const timeout=setTimeout(()=>controller.abort(),20000);
 try {
  const response=await fetcher('https://api.web3forms.com/submit',{method:'POST',body:data,signal:controller.signal});
  const result=await response.json();
  return response.ok&&result.success===true?{status:'accepted'}:{status:'rejected'};
 } catch { return {status:'unknown'}; }
 finally {clearTimeout(timeout);}
}
function track(event,detail){
 const allowed=['brief_checked','contact_email_click','inquiry_attempt','inquiry_accepted','inquiry_unknown'];
 if(!allowed.includes(event))return;
 if(typeof location==='undefined'||!['www.bigfame.co','bigfame.co'].includes(location.hostname))return;
 // Consent is session-only. Enabling analytics must never include name/email/free text.
 if(root.bfAnalyticsConsent!==true||typeof root.gtag!=='function')return;
 root.gtag('event',event,{site_version:'foundation_b',page_path:location.pathname,product:['eyewear','custom'].includes(detail)?detail:'unspecified'});
}
if(typeof module!=='undefined')module.exports={sendBrief,track};
else root.BFInquiry={sendBrief,track};
})(typeof window==='undefined'?{}:window);
