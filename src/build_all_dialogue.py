# -*- coding: utf-8 -*-
import json, re, sys, os

sys.path.append(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline')
from turkish_ascii_converter import to_ascii_turkish

# Load both files
with open(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline\remaining_hints.json', 'r', encoding='utf-8') as f:
    hints_rem = json.load(f)

with open(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_work\combat_voices.json', 'r', encoding='utf-8') as f:
    combat_all = json.load(f)

all_dialogue = list(dict.fromkeys(hints_rem + combat_all))
print(f'Total combined dialogue lines: {len(all_dialogue)}')
