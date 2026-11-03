import sys, re, json
sys.path.append(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline')
from translations_moviecuts import MOVIECUTS_TRANSLATIONS

def normalize_text(s):
    # Replace any replacement character or curly quotes or dashes
    s = s.replace('\ufffd', "'")
    s = s.replace('’', "'").replace('‘', "'").replace('`', "'")
    s = s.replace('“', '"').replace('”', '"')
    s = s.replace('–', '-').replace('—', '-')
    s = re.sub(r'[\s\n\r]+', ' ', s).strip()
    return s

norm_map = {normalize_text(k): v for k, v in MOVIECUTS_TRANSLATIONS.items()}

path = r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_work\moviecuts_story.json'
with open(path, 'r', encoding='utf-8') as f:
    items = json.load(f)

missing = []
for it in items:
    if normalize_text(it) not in norm_map:
        missing.append(it)

print(f'Total items: {len(items)}')
print(f'Matched with norm: {len(items) - len(missing)}')
print(f'Missing: {len(missing)}')
for m in missing:
    print('Still missing:', repr(m[:80]))
