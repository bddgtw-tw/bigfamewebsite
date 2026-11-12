#!/usr/bin/env python3
"""Read-only HTTP release checks. Never submits forms or changes routing."""
import argparse, hashlib, json, urllib.request, urllib.error
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

class Document(HTMLParser):
    def __init__(self):
        super().__init__(); self.canonicals=[]; self.noindex=False; self.forms=[]; self.h1=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='h1': self.h1+=1
        if tag=='link' and 'canonical' in a.get('rel','').lower().split(): self.canonicals.append(a.get('href',''))
        if tag=='meta' and a.get('name','').lower() in ('robots','googlebot') and 'noindex' in a.get('content','').lower(): self.noindex=True
        if tag=='form': self.forms.append(a.get('action',''))

def inspect(body, headers, mode):
    d=Document(); d.feed(body)
    noindex=d.noindex or 'noindex' in headers.get('x-robots-tag','').lower()
    failures=[]
    if mode=='preview' and not noindex: failures.append('Preview lacks noindex')
    if mode=='production' and noindex: failures.append('Production is noindex')
    if d.h1!=1: failures.append('Expected exactly one H1')
    if mode=='production' and len(d.canonicals)!=1: failures.append('Expected one production canonical')
    return {'noindex':noindex,'canonical':d.canonicals,'h1_count':d.h1,'form_actions':d.forms,'failures':failures}

def run(base, mode, paths):
    origin=urlparse(base)
    if origin.scheme!='https' or not origin.hostname or origin.username or origin.password or origin.query or origin.fragment:
        raise ValueError('Supply an HTTPS base URL without credentials, query or fragment')
    results=[]
    for path in paths:
        if not path.startswith('/') or path.startswith('//') or '?' in path or '#' in path: raise ValueError('Paths must be same-origin paths without query or fragment')
        url=urljoin(base,path); row={'url':url}
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'BigFame-ReadOnly-ReleaseCheck/1.0','Cache-Control':'no-cache'})
            with urllib.request.urlopen(req,timeout=25) as r:
                data=r.read(2_000_001); headers={k.lower():v for k,v in r.headers.items()}
                if len(data)>2_000_000: raise ValueError('HTML exceeds safety limit')
                if 'text/html' not in headers.get('content-type',''): raise ValueError('Expected HTML')
                row.update(status=r.status,final_url=r.url,sha256=hashlib.sha256(data).hexdigest())
                row.update(inspect(data.decode('utf-8',errors='replace'),headers,mode))
                if urlparse(r.url).hostname != origin.hostname: row['failures'].append('Redirect changed host; review mapping')
        except Exception as e: row.update(failures=[f'{type(e).__name__}: {e}'])
        results.append(row)
    return {'checked_at_utc':datetime.now(timezone.utc).isoformat(),'mode':mode,'base':base,'read_only':True,'release_approved':False,'results':results}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--base',required=True); p.add_argument('--mode',choices=['production','preview'],required=True); p.add_argument('--output',required=True); p.add_argument('--paths',nargs='+',default=['/en/','/en/contact','/tw/','/tw/contact','/jp/','/jp/contact']); a=p.parse_args()
    report=run(a.base,a.mode,a.paths); Path(a.output).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n'); print(json.dumps(report,ensure_ascii=False,indent=2)); return int(any(r['failures'] for r in report['results']))
if __name__=='__main__': raise SystemExit(main())
