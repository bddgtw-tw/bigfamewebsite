const {test}=require('node:test');
const {execFileSync}=require('node:child_process');
test('read-only release checker rejects unsafe inputs and distinguishes preview SEO',()=>{
execFileSync('python3',['-c',`
from scripts.validate_release import inspect,run
page='<h1>Title</h1><link rel="canonical" href="https://www.bigfame.co/en/">'
assert not inspect(page,{},'production')['failures']
assert inspect(page,{},'preview')['failures']
assert not inspect(page,{'x-robots-tag':'noindex'},'preview')['failures']
assert inspect(page,{'x-robots-tag':'noindex'},'production')['failures']
assert inspect('<h1>A</h1><h1>B</h1>',{},'production')['failures']
assert not inspect(page+'<meta name="robots" content="noindex">',{},'preview')['failures']
for u in ['http://example.com','https://a:b@example.com','https://example.com?email=test']:
 try: run(u,'preview',[]); raise AssertionError('accepted unsafe URL')
 except ValueError: pass
for path in ['//evil.example/','https://evil.example/','/?email=test']:
 try: run('https://example.com','preview',[path]); raise AssertionError('accepted unsafe path')
 except ValueError: pass
`],{stdio:'pipe'});
});
