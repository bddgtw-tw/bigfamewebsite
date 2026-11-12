// Run: node --test foundation/tests/inquiry.test.cjs (no external requests)
const test=require('node:test');const assert=require('node:assert/strict');
const {validate}=require('../assets/site.js');const {sendBrief,track}=require('../assets/inquiry-transport.js');
const valid={name:'TEST',email:'test@example.com',company:'Example',product:'custom',market:'Taiwan',brief:'Fixture brief'};
for(const [label,v,expected] of [['valid',valid,[]],['email',{...valid,email:'x'},['email']],['product',{...valid,product:'unknown'},['product']],['length',{...valid,name:'x'.repeat(501)},['name']],['brief length',{...valid,brief:'x'.repeat(4001)},['brief']],['unsafe URL',{...valid,reference:'javascript:alert(1)'},['reference']]])test(label,()=>assert.deepEqual(validate(v),expected));
test('disabled transport makes zero requests',async()=>{let n=0;assert.equal((await sendBrief(valid,{enabled:false},()=>n++)).status,'disabled');assert.equal(n,0)});
test('accepted only with HTTP ok AND provider success',async()=>{assert.equal((await sendBrief(valid,{enabled:true,accessKey:'TEST-NOT-A-REAL-KEY'},async()=>({ok:true,json:async()=>({success:true})}))).status,'accepted');assert.equal((await sendBrief(valid,{enabled:true,accessKey:'TEST-NOT-A-REAL-KEY'},async()=>({ok:false,json:async()=>({success:true})}))).status,'rejected')});
test('network ambiguity is unknown, not safe to resend',async()=>assert.equal((await sendBrief(valid,{enabled:true,accessKey:'TEST-NOT-A-REAL-KEY'},async()=>{throw Error('offline')})).status,'unknown'));
test('analytics inert without production/consent',()=>assert.doesNotThrow(()=>track('brief_checked','custom')));
