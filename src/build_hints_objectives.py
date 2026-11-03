# -*- coding: utf-8 -*-
import json, re, sys, os

sys.path.append(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline')
from turkish_ascii_converter import to_ascii_turkish

# Load hints_objectives.json
path = r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_work\hints_objectives.json'
with open(path, 'r', encoding='utf-8') as f:
    items = json.load(f)

HINTS_DICT = {}

# Patterns for hints
for it in items:
    # Developer note in Danish
    if 'Samme besked fra forfatter' in it or 'overflødig' in it or 'overfldig' in it:
        HINTS_DICT[it] = ""
        continue

    # Hints with tags
    if 'Press and hold $HoldPrecisionAim$ to aim' in it:
        HINTS_DICT[it] = "Nisan almak icin $HoldPrecisionAim$ tusunu basili tutun,\\n ardindan ates etmek icin $TapFire$ tusuna basin"
        continue
    if 'To activate precision aiming: Hold down $HoldPrecisionAim$' in it:
        HINTS_DICT[it] = "Hassas nisan almayi etkinlestirmek icin: $HoldPrecisionAim$ tusunu basili tutun\\n"
        continue
    if 'Press and hold $HoldPrecisionAim$ to aim at a' in it:
        HINTS_DICT[it] = "Yerdeki bir noktaya nisan almak icin $HoldPrecisionAim$ tusunu basili tutun,\\n ardindan bir tim uyesini gondermek icin $HoldAttack$ tusuna basin."
        continue
    if 'You need C4 to destroy the fuel tanks.' in it:
        HINTS_DICT[it] = "Yakit tanklarini yok etmek icin C4'e ihtiyaciniz var.\\n\nKanalizasyona donun ve C4 bulmak icin\\n\nbaska bir bolge arayin."
        continue
    if 'You need to rescue Isabella in the police station.' in it:
        HINTS_DICT[it] = "Polis merkezindeki Isabella'yi kurtarmaniz gerekiyor.\\n\nKanalizasyona donun, $TapUse$ tusuna basin ve baska bir\\n\nbolge secin."
        continue
    if 'To place C4 explosives, walk to the base' in it:
        HINTS_DICT[it] = "C4 patlayicilari yerlestirmek icin buyuk yakit tanklarinin\\n\ntabanina yaklasin ve $TapUse$ tusuna basin."
        continue
    if 'You need C4 to demolish the bridge.' in it:
        HINTS_DICT[it] = "Kopruyu havaya ucurmak icin C4'e ihtiyaciniz var.\\n\nKanalizasyona donun ve C4 bulmak icin\\n\nbaska bir bolge arayin."
        continue
    if 'You need C4 to destroy the Helipad.' in it:
        HINTS_DICT[it] = "Helikopter pistini yok etmek icin C4'e ihtiyaciniz var.\\n\nKanalizasyona donun ve C4 bulmak icin\\n\nbaska bir bolge arayin."
        continue
    if 'The two circles above show that you' in it:
        HINTS_DICT[it] = "Yukaridaki iki daire Karizma Seviyenizin 2 oldugunu gosterir.\\n\nBu, size iki Ozgurluk Savascisi'nin\\n\nkatilabilecegi anlamina gelir."
        continue
    if 'Press $TapJump$ to climb.' in it:
        HINTS_DICT[it] = "Tirmanmak icin $TapJump$ tusuna basin."
        continue
    if 'Press and hold $HoldFormFormation$ to order \\n\nall squad members to return to you.' in it:
        HINTS_DICT[it] = "Tum tim uyelerinin size donmesini emretmek icin\\n\n$HoldFormFormation$ tusunu basili tutun."
        continue
    if 'Press $HoldFormFormation$ to order a squad member' in it:
        HINTS_DICT[it] = "Bir tim uyesinin size donmesini emretmek icin\\n\n$HoldFormFormation$ tusuna basin.\\n\nBasili tutarsaniz tum tim geri doner."
        continue
    if 'Press $HoldCrouch$ to toggle crouch.' in it:
        HINTS_DICT[it] = "Egilmeyi acip kapatmak icin $HoldCrouch$ tusuna basin."
        continue
    if 'To change weapons: Hold down $HoldInventoryWheelMode$' in it:
        HINTS_DICT[it] = "Silah degistirmek icin: $HoldInventoryWheelMode$ tusunu basili tutun\\n ve silah secmek icin kontrol cubugunu hareket ettirin."
        continue
    if 'Press and hold $HoldAttack$ to order all your' in it:
        HINTS_DICT[it] = "Tum Ozgurluk Savascilariniza bir dusmana saldirmalarini emretmek icin\\n\n$HoldAttack$ tusunu basili tutun."
        continue
    if 'Press the $HoldDefend$ to order one squad member to remain at the machinegun.' in it:
        HINTS_DICT[it] = "Bir tim uyesine makineli tufekte kalmasini emretmek icin $HoldDefend$ tusuna basin."
        continue
    if 'Walk up to each of the Freedom Fighters' in it:
        HINTS_DICT[it] = "Ozgurluk Savascilarinin her birinin yanina gidin\\n\nve onlari birliginize almak icin $TapUse$ tusuna basin."
        continue
    if 'To enter a location, go to' in it:
        HINTS_DICT[it] = "Bir bolgeye girmek icin haritaya gidin\\n\nve $TapUse$ tusuna basin."
        continue
    if 'Search for some C4.' in it or 'Search for some C4' in it:
        HINTS_DICT[it] = "C4 patlayici arayin."
        continue
    if 'Search for a Medic Kit.' in it or 'Search for a Medical Kit.' in it:
        HINTS_DICT[it] = "Saglik Cantasi arayin."
        continue
    if 'Go to flag and press $TapUse$ to hoist the' in it:
        HINTS_DICT[it] = "Bayraga gidin ve bolgeyi guvenceye alip\\n\nbayragi cekmek icin $TapUse$ tusuna basin."
        continue
    if "The Soviets will only open the gates" in it:
        HINTS_DICT[it] = "Sovyetler kale kapilarini sadece son care olarak acacaktir.\\n\nBu noktanin otesine erisim saglamadan once\\n\nGovernor's Island'daki diger tum bayraklari almalisiniz."
        continue
    if 'Approach a wounded person' in it:
        HINTS_DICT[it] = "Yarali birinin yanina gidin\\n\nve onu iyilestirmek icin $TapUse$ tusuna basin."
        continue
    if 'Press $TapActivateMap$ to access your map.' in it:
        HINTS_DICT[it] = "Haritaniza erismek icin $TapActivateMap$ tusuna basin."
        continue
    if 'Use Control Stick to move and turn.' in it or 'Use left analog stick to move and turn.' in it:
        HINTS_DICT[it] = "Hareket etmek ve donmek icin kontrol cubugunu kullanin."
        continue
    if 'Use Control Stick to move and\\n C Stick to look around.' in it or 'Use left analog stick to move and\\n\nright analog stick to look around.' in it:
        HINTS_DICT[it] = "Hareket etmek icin sol, etrafa bakmak icin\\n\nsag analog cubugu kullanin."
        continue
    if 'Approach the manhole cover' in it:
        HINTS_DICT[it] = "Rogar kapagina yaklasin\\n\nve acmak icin $TapUse$ tusuna basin."
        continue
    if 'Move over the C4 to pick it up.' in it:
        HINTS_DICT[it] = "Almak icin C4'un uzerine gelin."
        continue
    if 'Move over a Medic Kit to pick it up.' in it or 'Move over a Medical Kit to pick it up.' in it:
        HINTS_DICT[it] = "Almak icin Saglik Cantasinin uzerine gelin."
        continue
    if 'Move over a Molotov to pick it up.' in it:
        HINTS_DICT[it] = "Almak icin Molotofun uzerine gelin."
        continue
    if 'Move over a weapon to pick it up.' in it:
        HINTS_DICT[it] = "Almak icin bir silahin uzerine gelin."
        continue
    if 'Press $TapFire$ to attack.' in it:
        HINTS_DICT[it] = "Saldirmak icin $TapFire$ tusuna basin."
        continue
    if 'Press $TapCloseCombat$ to attack.' in it:
        HINTS_DICT[it] = "Yakin dovus saldirisi icin $TapCloseCombat$ tusuna basin."
        continue
    if 'Find a manhole, press $TapUse$\\n\nand select another location.' in it:
        HINTS_DICT[it] = "Bir rogar kapagi bulun, $TapUse$ tusuna basin\\n\nve baska bir bolge secin."
        continue
    if 'Press and hold $HoldInventoryWheelMode$ to bring up the inventory' in it:
        HINTS_DICT[it] = "Envanteri acmak icin $HoldInventoryWheelMode$ tusunu basili tutun,\\n\nardindan silah secmek icin kontrol cubugunu hareket ettirin."
        continue

# Short objectives & mission messages
short_map = {
    "Destroy Helipad.": "Helikopter Pistini Yok Et.",
    "Destroy the Helipad.": "Helikopter Pistini Yok Et.",
    "Destroy Helipad": "Helikopter Pistini Yok Et",
    "Helipad destroyed!": "Helikopter pisti yok edildi!",
    "Locate C4.": "C4 Patlayiciyi Bul.",
    "Locate C4": "C4 Patlayiciyi Bul",
    "C4 located!": "C4 bulundu!",
    "Raise Flag on Hotel.": "Otele Bayrak Cek.",
    "Raise Flag on Hotel roof.": "Otel Catısına Bayrak Cek.",
    "Free Prisoners.": "Mahkumlari Kurtar.",
    "Free the Prisoners.": "Mahkumlari Kurtar.",
    "Bridge destroyed!": "Kopru havaya ucuruldu!",
    "Destroy Bridge.": "Kopruyu Yok Et.",
    "Destroy the Bridge.": "Kopruyu Yok Et.",
    "Destroy West Bridge.": "Bati Koprusunu Yok Et.",
    "Destroy East Bridge.": "Dogu Koprusunu Yok Et.",
    "Kill Tatarin.": "Tatarin'i Oldur.",
    "Kill General Tatarin.": "General Tatarin'i Oldur.",
    "Tatarin killed!": "Tatarin olduruldu!",
    "General Tatarin killed!": "General Tatarin olduruldu!",
    "Raise Flag on Movie Theater.": "Sinemaya Bayrak Cek.",
    "Raise Flag on High School roof.": "Lise Catısına Bayrak Cek.",
    "Free the Prisoners near the High School.": "Lise Yakinindaki Mahkumlari Kurtar.",
    "Flag raised - Area secure!": "Bayrak cekildi - Bolge guvende!",
    "Flag raised!": "Bayrak cekildi!",
    "Tank destroyed!": "Tank imha edildi!",
    "Free Isabella.": "Isabella'yi Kurtar.",
    "Rescue Isabella.": "Isabella'yi Kurtar.",
    "Tower destroyed!": "Kule yok edildi!",
    "Ventilation shaft is open!": "Havalandirma safti acildi!",
    "Ventilation shaft open!": "Havalandirma safti acildi!",
    "EAST BRIDGE": "DOGU KOPRUSU",
    "WEST BRIDGE": "BATI KOPRUSU",
    "WAREHOUSE": "DEPO",
    "POWER STATION": "ELEKTRIK SANTRALI",
    "TRANSFORMER TOWER": "TRAFO KULESI",
    "HARBOR ENTRANCE": "LIMAN GIRISI",
    "TOWER": "KULE",
    "VENTILATION SHAFT": "HAVALANDIRMA SAFTI",
    "SUPPLY HANGAR": "IKMAL HANGARI",
    "NORTHWEST BUNKER": "KUZEYBATI SIGINAGI",
    "SOUTHWEST BUNKER": "GUNEYBATI SIGINAGI",
    "Raise Flag over Northwest Bunker.": "Kuzeybati Siginagina Bayrak Cek.",
    "Raise Flag over Southwest Bunker.": "Guneybati Siginagina Bayrak Cek.",
    "Raise Flag on Fort Jay.": "Jay Kalesine Bayrak Cek.",
    "Fort Jay captured!": "Jay Kalesi ele gecirildi!",
    "SEWERS": "KANALIZASYON",
}

for k, v in short_map.items():
    HINTS_DICT[k] = v

print(f'Populated direct matches: {len(HINTS_DICT)} / {len(items)}')
