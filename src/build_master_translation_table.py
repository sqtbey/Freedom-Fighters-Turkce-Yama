# -*- coding: utf-8 -*-
"""
Master Translation Table Builder for Freedom Fighters Turkish Patch.
Combines all modular translation dictionaries into a single verified master mapping.
"""
import json, sys, os
sys.path.append(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline')

from translations_moviecuts import MOVIECUTS_TRANSLATIONS
from translations_menu_ui import MENU_TRANSLATIONS
from trans_hints import HINTS_TRANSLATIONS
from trans_levels_ch1_ch2 import CH1_CH2_TRANSLATIONS
from trans_levels_ch3_ch5 import CH3_CH5_TRANSLATIONS
from trans_levels_ch6_ch8 import CH6_CH8_TRANSLATIONS
from trans_combat_voices_part1 import COMBAT_PART1_TRANSLATIONS
from trans_combat_civ import CIV_TRANSLATIONS
from trans_combat_ffs import FFS_TRANSLATIONS

def build_master_table():
    master = {}
    dictionaries = [
        ("Moviecuts & Cinematics", MOVIECUTS_TRANSLATIONS),
        ("Menu & UI", MENU_TRANSLATIONS),
        ("Hints & Controls", HINTS_TRANSLATIONS),
        ("Chapters 1 & 2 Dialogues", CH1_CH2_TRANSLATIONS),
        ("Chapters 3, 4, 5 Dialogues", CH3_CH5_TRANSLATIONS),
        ("Chapters 6, 7, 8 Dialogues", CH6_CH8_TRANSLATIONS),
        ("Combat Voices Part 1 (Hero/Soviet/Prisoner/Defector)", COMBAT_PART1_TRANSLATIONS),
        ("Civilian Voice Lines", CIV_TRANSLATIONS),
        ("Freedom Fighters Voice Lines", FFS_TRANSLATIONS),
    ]

    for name, d in dictionaries:
        master.update(d)
        print(f"Loaded {name}: {len(d)} translations")

    output_path = r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline\master_translation_dict.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(master, f, indent=2, ensure_ascii=False)

    print(f"\nMaster translation table saved to {output_path}")
    print(f"Total unique translated entries: {len(master)}")
    return master

if __name__ == '__main__':
    build_master_table()
