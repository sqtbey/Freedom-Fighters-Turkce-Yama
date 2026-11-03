# -*- coding: utf-8 -*-
import json, os, sys
sys.path.append(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline')
from turkish_ascii_converter import to_ascii_turkish

# Load menu_ui.json
path = r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_work\menu_ui.json'
with open(path, 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f'Total menu items to translate: {len(items)}')
