"""Remove legacy inline GA initialization where main.js owns analytics."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r'\s*<!-- Google tag \(gtag\.js\) -->\s*<script async src="https://www\.googletagmanager\.com/gtag/js\?id=G-PDW4NPHHW8"></script>\s*<script>\s*window\.dataLayer = window\.dataLayer \|\| \[\];\s*function gtag\(\)\{dataLayer\.push\(arguments\);\}\s*gtag\(\'js\', new Date\(\)\);\s*gtag\(\'config\', \'G-PDW4NPHHW8\'\);\s*</script>', re.MULTILINE)

for path in ROOT.glob('**/*.html'):
    text = path.read_text(encoding='utf-8', errors='ignore')
    if 'main.js' not in text:
        continue
    updated, count = PATTERN.subn('', text, count=1)
    if count:
        path.write_text(updated, encoding='utf-8')
