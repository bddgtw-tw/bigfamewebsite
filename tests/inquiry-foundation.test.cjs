const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const source=fs.readFileSync('js/main.js','utf8');
const fields=['contactForm','inquiry_type','product_category','buyer_role','source_category','source_role','source_product','requested_files','source_page'];
function context(search='') {
 const nodes=Object.fromEntries(fields.map(id=>[id,{value:''}]));
 const sandbox={URL,URLSearchParams,window:{location:{search,origin:'https://www.bigfame.co'}},document:{readyState:'loading',addEventListener(){},getElementById:id=>nodes[id],referrer:''}};
 vm.createContext(sandbox);vm.runInContext(source,sandbox);
 sandbox.trackAnalyticsEvent=()=>{}; sandbox.initInquiryContext();return nodes;
}
test('CAD legacy CTA preserves information request and procurement role',()=>{
 const n=context('?category=engineering_dossier&role=procurement');
 assert.equal(n.requested_files.value,'technical_pack');assert.equal(n.inquiry_type.value,'other');assert.equal(n.buyer_role.value,'buyer_trading_agent');
});
test('explicit requested file overrides fallback',()=>assert.equal(context('?category=engineering_dossier&requested_files=cad_files').requested_files.value,'cad_files'));
test('legacy POS alias preserved',()=>assert.equal(context('?category=pos_display').product_category.value,'pos_displays'));
test('homepage designer CTA preserved',()=>{
 const n=context('?category=bespoke_fixture&role=designer&inquiry_type=custom_dev');assert.equal(n.inquiry_type.value,'custom_dev');assert.equal(n.buyer_role.value,'store_design_engineering');
});
test('direct entry does not preselect an unrelated request',()=>{
 const n=context();assert.equal(n.inquiry_type.value,'');assert.equal(n.requested_files.value,'');
});
test('mobile menu closes on any navigation link and Escape',()=>{
 const handlers={};const menuSet=new Set(),toggleSet=new Set();
 const cls=set=>({contains:x=>set.has(x),toggle:(x,on)=>on?set.add(x):set.delete(x)});
 const link={addEventListener:(e,fn)=>handlers.link=fn};
 const menu={classList:cls(menuSet),querySelectorAll:sel=>{assert.equal(sel,'a[href]');return [link]}};
 const toggle={classList:cls(toggleSet),setAttribute:(k,v)=>handlers[k]=v,addEventListener:(e,fn)=>handlers.click=fn,focus:()=>handlers.focus=true};
 const sandbox={document:{readyState:'loading',addEventListener:(e,fn)=>handlers[e]=fn,querySelector:sel=>sel==='.mobile-toggle'?toggle:menu,body:{classList:cls(new Set())}},window:{addEventListener:(e,fn)=>handlers[e]=fn}};
 vm.createContext(sandbox);vm.runInContext(source,sandbox);sandbox.initMobileMenu();
 handlers.click();assert.equal(handlers['aria-expanded'],'true');handlers.link();assert.equal(handlers['aria-expanded'],'false');
 handlers.click();handlers.keydown({key:'Escape'});assert.equal(handlers['aria-expanded'],'false');assert.equal(handlers.focus,true);
});
for(const lang of ['en','tw','jp'])test(`${lang} contact has accessible menu, honest expectations and fallback`,()=>{
 const html=fs.readFileSync(`${lang}/contact.html`,'utf8');
 assert.match(html,/aria-controls="contact-navigation"/);assert.match(html,/id="contact-navigation"/);
 assert.match(html,/mailto:shopdisplay@bigfame.co/);assert.match(html,/min-height: 0 !important/);
 assert.equal((html.match(/<h1\b/g)||[]).length,1);assert.doesNotMatch(html,/24h|24 小時|24時間|24 hours/);
 for(const m of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) JSON.parse(m[1]);
});
test('English homepage has one heading, real asset paths and parseable metadata',()=>{
 const html=fs.readFileSync('en/index.html','utf8');assert.equal((html.match(/<h1\b/g)||[]).length,1);
 for(const m of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g))JSON.parse(m[1]);
 for(const m of html.matchAll(/src="\.\.\/([^"?]+)(?:\?[^\"]*)?"/g))assert.ok(fs.existsSync(m[1]),m[1]);
 assert.match(html,/requested_files=technical_pack/);assert.doesNotMatch(html,/within 24|24h|Made in Taiwan|85kg|40%/i);
});
