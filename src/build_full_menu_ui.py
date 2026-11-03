# -*- coding: utf-8 -*-
import json, sys, os, re

sys.path.append(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline')
from turkish_ascii_converter import to_ascii_turkish

# Load unmapped items
path = r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline\menu_unmapped.json'
with open(path, 'r', encoding='utf-8') as f:
    unmapped = json.load(f)

# Translation dictionary for unmapped items
UNMAPPED_TRANS = {
    "Please press START button to begin": "Baslamak icin lutfen START tusuna basin",
    "PREV PAGE": "ONCEKI SAYFA",
    "QUICK LOAD": "HIZLI YUKLE",
    "QUICK SAVE": "HIZLI KAYIT",
    "REMOVE DAMAGED PROFILE": "HASARLI PROFILI SIL",
    "REMOVE SAVE GAME": "KAYITLI OYUNU SIL",
    "RESTART": "YENIDEN BASLAT",
    "RESTART LOCATION": "BOLGEYI YENIDEN BASLAT",
    "RESTORE DEFAULTS": "VARSAYILANLARA DON",
    "RETRY": "TEKRAR DENE",
    "RETRY LOADING": "YUKLEMEYI TEKRAR DENE",
    "RETRY SAVING": "KAYDETMEYI TEKRAR DENE",
    "SINGLE PLAYER": "TEK OYUNCULU",
    "SKIP FILE": "DOSYAYI ATLA",
    "SPACE": "BOSLUK",
    "SPEECH": "KONUSMA",
    "START GAME": "OYUNU BASLAT",
    "VIEW OBJECTIVES": "HEDEFLERI GORUNTULE",
    "YES, CONTINUE WITHOUT SAVING": "EVET, KAYDETMEDEN DEVAM ET",
    "SETUP A": "AYAR A",
    "SETUP B": "AYAR B",
    "SETUP C": "AYAR C",
    "GOVERNOR'S ISLAND": "GOVERNOR'S ISLAND",
    "SEWERS": "KANALIZASYON",
    "SOVIET DOMINATION": "SOVYET HAKIMIYETI",
    "IN A NEW YORK MINUTE": "BIR NEW YORK DAKIKASINDA",
    "BREAKING FREE!": "KURTULUS!",
    "DESPERATE REVENGE": "CARESİZ INTIKAM",
    "MISSION COMPLETED": "GOREV TAMAMLANDI",
    "ANISOTROPIC": "ANIZOTROPIK",
    "ANTI ALIASING": "KENAR YUMUSATMA",
    "ARE YOU SURE?": "EMIN MISINIZ?",
    "4:3 (STANDARD)": "4:3 (STANDART)",
    "Page": "Sayfa",
    "Pick up %s": "%s Al",
    "FREEDOM FIGHTER": "OZGURLUK SAVASCISI",
    "PRESS ANY KEY": "HERHANGI BIR TUSA BASIN",
    "Registration": "Kayit",
    "Technical Support": "Teknik Destek",
    "Uninstall": "Kaldir",
    "PLAYER": "OYUNCU",
    "PLAYERS": "OYUNCULAR",
    "SELECT MAP": "HARITA SEC",
    "STATS": "ISTATISTIKLER",
    "TIME ON LEVEL": "BOLUMDE GECEN SURE",
    "Save complete.": "Kayit tamamlandi.",
    "No quick save game found.": "Hizli kayit bulunamadi.",
    "Loading profiles.": "Profiller yukleniyor.",
    "Single stick control": "Tek analog kontrol",
    "Single analog stick control": "Tek analog cubuk kontrolu",
    "Single thumbstick control": "Tek basparmak kontrolu",
    "Dual stick control": "Cift analog kontrol",
    "Inventory is full": "Envanter dolu",
    "OBJECT DETAIL": "NESNE DETAYI",
    "LOADING": "YUKLENIYOR",
    "FREEDOM FIGHTER: YOU GOT WHAT IT TAKES?": "OZGURLUK SAVASCISI: CESARETIN VAR MI?",
    "MOUSE SENSITIVITY": "FARE DUYARLILIGI",
    "NAME:": "ISIM:",
    "NAVIGATE": "DOLAS",
    "You have new weapon(s) in arsenal:": "Cephanelikte yeni silah(lar)iniz var:",
    "%i rounds for %s": "%s icin %i mermi",
    "1 Grenade": "1 El Bombasi",
    "%i Grenades": "%i El Bombasi",
    "1 Molotov": "1 Molotof",
    "%i Molotovs": "%i Molotof",
    "LOCATION:": "BOLGE:",
    "General Bulba": "General Bulba",
    "Chris": "Chris",
    "Civilian": "Sivil",
    "Policeman": "Polis",
    "Defector": "Kacak Asker",
    "Freedom Fighter": "Ozgurluk Savascisi",
    "General Tatarin": "General Tatarin",
    "Isabella": "Isabella",
    "Mr. Jones": "Bay Jones",
    "Loudspeaker": "Hoparlor",
    "HOLD POSITION": "MEVZIYI KORU",
    "FOLLOW ME": "BENI TAKIP ET",
    "ATTACK TARGET": "HEDEFE SALDIR",
    "CANCEL ORDER": "EMRI IPTAL ET",
}

# Add automated cheat mappings
cheat_pattern = re.compile(r'^Cheat:\s*(.*)$')
for it in unmapped:
    m = cheat_pattern.match(it)
    if m:
        body = m.group(1)
        body = body.replace('Infinite ammo added', 'Sinirsiz mermi eklendi')
        body = body.replace('Blind -> OFF', 'Korluk -> KAPALI')
        body = body.replace('Blind -> ON', 'Korluk -> ACIK')
        body = body.replace('Maximum charisma added', 'Maksimum karizma eklendi')
        body = body.replace('Fast forward -> OFF', 'Hizli sarma -> KAPALI')
        body = body.replace('Fast forward -> ON', 'Hizli sarma -> ACIK')
        body = body.replace('FlyMo ragdolls -> OFF', 'Ucusan fizikler -> KAPALI')
        body = body.replace('FlyMo ragdolls -> ON', 'Ucusan fizikler -> ACIK')
        body = body.replace('God mode -> OFF', 'Olumsuzluk modu -> KAPALI')
        body = body.replace('God mode -> ON', 'Olumsuzluk modu -> ACIK')
        body = body.replace('Heavy machine gun + misc. given', 'Agir makineli + ekipman verildi')
        body = body.replace('NailGun -> OFF', 'Civi tabancasi -> KAPALI')
        body = body.replace('NailGun -> ON', 'Civi tabancasi -> ACIK')
        body = body.replace('SMG + misc. given', 'Hafif makineli + ekipman verildi')
        body = body.replace('Rocket launcher + misc. given', 'Roketatar + ekipman verildi')
        body = body.replace('Shotgun + misc. given', 'Pompali tufek + ekipman verildi')
        body = body.replace('Slowmotion -> OFF', 'Agir cekim -> KAPALI')
        body = body.replace('Slowmotion -> ON', 'Agir cekim -> ACIK')
        body = body.replace('Sniper + misc. given', 'Keskin nisanci + ekipman verildi')
        body = body.replace('Rifle + misc. given', 'Tufek + ekipman verildi')
        body = body.replace('Jump to spawnpoint', 'Dogma noktasina isinlan')
        UNMAPPED_TRANS[it] = f'Hile: {body}'

# Build the complete map
print(f'Defined manual & cheat translations: {len(UNMAPPED_TRANS)}')
