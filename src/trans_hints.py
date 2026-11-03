# -*- coding: utf-8 -*-
import json, sys
sys.path.append(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline')
from turkish_ascii_converter import to_ascii_turkish

# 78 hints translations
HINTS_MAP = {
    # Aiming
    "Press and hold $HoldPrecisionAim$ to aim,\\n then press $TapFire$ to fire weapon":
        "Nisan almak icin $HoldPrecisionAim$ tusunu basili tutun,\\n ardindan ates etmek icin $TapFire$ tusuna basin",
    "Press and hold $HoldPrecisionAim$ to aim\\n then press $TapFire$ to fire.":
        "Nisan almak icin $HoldPrecisionAim$ tusunu basili tutun\\n ardindan ates etmek icin $TapFire$ tusuna basin.",
    "Press and hold $HoldPrecisionAim$ to aim,\\n then press $TapFire$ to fire weapon.":
        "Nisan almak icin $HoldPrecisionAim$ tusunu basili tutun,\\n ardindan ates etmek icin $TapFire$ tusuna basin.",
    "Click and hold left thumbstick to aim,\\n then pull the right trigger to fire weapon.":
        "Nisan almak icin sol analoga basili tutun,\\n ardindan ates etmek icin sag tetigi cekin.",
    "To activate precision aiming: Hold down $HoldPrecisionAim$\\n":
        "Hassas nisan almayi etkinlestirmek icin: $HoldPrecisionAim$ tusunu basili tutun\\n",
    "To activate precision aiming: Hold down $HoldPrecisionAim$.\\n":
        "Hassas nisan almayi etkinlestirmek icin: $HoldPrecisionAim$ tusunu basili tutun.\\n",

    # C02A C4 / Isabella
    "You need C4 to destroy the fuel tanks.\\n\nReturn to the sewer and search another\\n\nlocation for some C4.":
        "Yakit tanklarini yok etmek icin C4'e ihtiyaciniz var.\\n\nKanalizasyona donun ve C4 bulmak icin\\n\nbaska bir bolge arayin.",
    "You need to rescue Isabella in the police station.\\n\nReturn to the sewer, press $TapUse$ and select another\\n\nlocation.":
        "Polis karakolundaki Isabella'yi kurtarmaniz gerekiyor.\\n\nKanalizasyona donun, $TapUse$ tusuna basin ve baska bir\\n\nbolge secin.",
    "To place C4 explosives, walk to the base\\n\nof the large fuel tanks, and press $TapUse$":
        "C4 patlayicilari yerlestirmek icin buyuk yakit tanklarinin\\n\ntabanina yaklasin ve $TapUse$ tusuna basin",
    "To place C4 explosives, walk to the base\\n\nof the large fuel tanks, and press $TapUse$.":
        "C4 patlayicilari yerlestirmek icin buyuk yakit tanklarinin\\n\ntabanina yaklasin ve $TapUse$ tusuna basin.",
    "To place C4 explosives, walk to the base\\n\nof the large fuel tanks and press $TapUse$":
        "C4 patlayicilari yerlestirmek icin buyuk yakit tanklarinin\\n\ntabanina yaklasin ve $TapUse$ tusuna basin",
    "To place C4 explosives, walk to the base\\n\nof the large fuel tanks and press $TapUse$.":
        "C4 patlayicilari yerlestirmek icin buyuk yakit tanklarinin\\n\ntabanina yaklasin ve $TapUse$ tusuna basin.",

    # C03 C4
    "You need C4 to demolish the bridge.\\n\nReturn to the sewer and search another\\n\nlocation for some C4.":
        "Kopruyu havaya ucurmak icin C4'e ihtiyaciniz var.\\n\nKanalizasyona donun ve C4 bulmak icin\\n\nbaska bir bolge arayin.",
    "You need C4 to destroy the Helipad.\\n\nReturn to the sewer and search another\\n\nlocation for some C4.":
        "Helikopter pistini yok etmek icin C4'e ihtiyaciniz var.\\n\nKanalizasyona donun ve C4 bulmak icin\\n\nbaska bir bolge arayin.",

    # Charisma & Squad control
    "The two circles above show that you\\n\nare at Charisma Level 2. This means\\n \nthat two Freedom Fighters will join you.":
        "Yukaridaki iki daire Karizma Seviyenizin 2 oldugunu gosterir.\\n\nBu, size iki Ozgurluk Savascisi'nin\\n \nkatilabilecegi anlamina gelir.",
    "Press and hold $HoldPrecisionAim$ to aim at a\\n place on the ground, then press $HoldAttack$ to send off\\n a squad member.":
        "Yerdeki bir noktaya nisan almak icin $HoldPrecisionAim$ tusunu basili tutun,\\n ardindan bir tim uyesini gondermek icin $HoldAttack$ tusuna basin.",
    "Press and hold $HoldPrecisionAim$ to aim at a\\n \nplace on the ground, then press $HoldAttack$ to send off\\n\na squad member.":
        "Yerdeki bir noktaya nisan almak icin $HoldPrecisionAim$ tusunu basili tutun,\\n \nardindan bir tim uyesini gondermek icin $HoldAttack$ tusuna basin.",
    "Press and hold $HoldPrecisionAim$ to aim at a place\\n on the ground, then press $HoldAttack$ to send off\\n a squad member.":
        "Yerdeki bir noktaya nisan almak icin $HoldPrecisionAim$ tusunu basili tutun,\\n ardindan bir tim uyesini gondermek icin $HoldAttack$ tusuna basin.",
    "Click and hold Left Thumbstick to aim at a\\n\nplace on the ground, then press $HoldAttack$ to send off\\n\na squad member.":
        "Yerdeki bir noktaya nisan almak icin Sol Analoga basili tutun,\\n\nardindan bir tim uyesini gondermek icin $HoldAttack$ tusuna basin.",
    "Press $HoldFormFormation$ to order a squad member \\n\nto return to you. \\n\nHold it, and the entire squad will return.":
        "Bir tim uyesinin size donmesini emretmek icin $HoldFormFormation$ tusuna basin.\\n\nBasili tutarsaniz tum tim geri doner.",
    "Press $HoldFormFormation$ to order a squad member\\n \nto return to you.\\n \nHold it, and the entire squad will return.":
        "Bir tim uyesinin size donmesini emretmek icin $HoldFormFormation$ tusuna basin.\\n \nBasili tutarsaniz tum tim geri doner.",
    "Press $HoldFormFormation$ to order a squad member\\n\nto return to you.\\n\nHold it, and the entire squad will return.":
        "Bir tim uyesinin size donmesini emretmek icin $HoldFormFormation$ tusuna basin.\\n\nBasili tutarsaniz tum tim geri doner.",
    "Press and hold $HoldFormFormation$ to order \\n\nall squad members to return to you.":
        "Tum tim uyelerinin size donmesini emretmek icin\\n\n$HoldFormFormation$ tusunu basili tutun.",
    "Press and hold $HoldAttack$ to order all your\\n\nFreedom Fighters to attack an enemy.":
        "Tum Ozgurluk Savascilariniza bir dusmana saldirmalarini emretmek icin\\n\n$HoldAttack$ tusunu basili tutun.",
    "Press the $HoldDefend$ to order one squad member to remain at the machinegun.":
        "Bir tim uyesine makineli tufekte kalmasini emretmek icin $HoldDefend$ tusuna basin.",
    "Press the $HoldDefend$ to order one squad member to remain at the machine gun.":
        "Bir tim uyesine makineli tufekte kalmasini emretmek icin $HoldDefend$ tusuna basin.",
    "Walk up to each of the Freedom Fighters,\\n \nand press $TapUse$ to recruit them.":
        "Ozgurluk Savascilarinin her birinin yanina gidin,\\n \nve onlari birliginize almak icin $TapUse$ tusuna basin.",
    "Walk up to each of the Freedom Fighters\\n \nand press $TapUse$ to recruit them.":
        "Ozgurluk Savascilarinin her birinin yanina gidin\\n \nve onlari birliginize almak icin $TapUse$ tusuna basin.",

    # Movement & Controls
    "Press $TapJump$ to climb.": "Tirmanmak icin $TapJump$ tusuna basin.",
    "Pull the left trigger to climb.": "Tirmanmak icin sol tetigi cekin.",
    "Press $HoldCrouch$ to toggle crouch.": "Egilmeyi acip kapatmak icin $HoldCrouch$ tusuna basin.",
    "Press $HoldCrouch$ to crouch.": "Egilmek icin $HoldCrouch$ tusuna basin.",
    "Use Control Stick to move and turn.": "Hareket etmek ve donmek icin kontrol cubugunu kullanin.",
    "Use Control Stick to move and\\n C Stick to look around.": "Hareket etmek icin kontrol cubugunu,\\n etrafa bakmak icin C cubugunu kullanin.",
    "Use left analog stick to move and turn.": "Hareket etmek ve donmek icin sol analog cubugu kullanin.",
    "Use left analog stick to move and\\n\nright analog stick to look around.": "Hareket etmek icin sol analog,\\n\netrafa bakmak icin sag analog cubugu kullanin.",
    "Use left thumbstick to move and turn.": "Hareket etmek ve donmek icin sol cubugu kullanin.",
    "Use left thumbstick to move and\\n\nright thumbstick to look around.": "Hareket etmek icin sol,\\n\netrafa bakmak icin sag cubugu kullanin.",
    "Use $HoldMoveForward1$, $HoldMoveLeft1$, $HoldMoveBackward1$ and $HoldMoveRight1$ to move.":
        "Hareket etmek icin $HoldMoveForward1$, $HoldMoveLeft1$, $HoldMoveBackward1$ ve $HoldMoveRight1$ tuslarini kullanin.",

    # Weapon selection & Attacks
    "To change weapons: Hold down $HoldInventoryWheelMode$ \\n and move the control stick to select weapon.":
        "Silah degistirmek icin: $HoldInventoryWheelMode$ tusunu basili tutun\\n ve silah secmek icin kontrol cubugunu hareket ettirin.",
    "To change weapons: Hold down $HoldInventoryWheelMode$ \\n and move left stick to select weapon\\n":
        "Silah degistirmek icin: $HoldInventoryWheelMode$ tusunu basili tutun\\n ve silah secmek icin sol cubugu hareket ettirin\\n",
    "To change weapons: Hold down $HoldInventoryWheelMode$ \\n and move left stick to select weapon.\\n":
        "Silah degistirmek icin: $HoldInventoryWheelMode$ tusunu basili tutun\\n ve silah secmek icin sol cubugu hareket ettirin.\\n",
    "To change weapons: Press and hold down $HoldInventoryWheelMode$ \\n and move left analog stick to select weapon.\\n":
        "Silah degistirmek icin: $HoldInventoryWheelMode$ tusunu basili tutun\\n ve silah secmek icin sol analog cubugu hareket ettirin.\\n",
    "Press and hold $HoldInventoryWheelMode$ to bring up the inventory,\\n\nthen select the Medic Kit with the control stick.":
        "Envanteri acmak icin $HoldInventoryWheelMode$ tusunu basili tutun,\\n\nardindan kontrol cubugu ile Saglik Cantasini secin.",
    "Press and hold $HoldInventoryWheelMode$ to bring up the inventory,\\n\nthen select the Molotov with the control stick.":
        "Envanteri acmak icin $HoldInventoryWheelMode$ tusunu basili tutun,\\n\nardindan kontrol cubugu ile Molotofu secin.",
    "Press and hold $HoldInventoryWheelMode$ to bring up the inventory,\\n\nthen select the Medic Kit with the left analog stick.":
        "Envanteri acmak icin $HoldInventoryWheelMode$ tusunu basili tutun,\\n\nardindan sol analog cubuk ile Saglik Cantasini secin.",
    "Press and hold $HoldInventoryWheelMode$ to bring up the inventory,\\n\nthen select the Molotov with the left analog stick.":
        "Envanteri acmak icin $HoldInventoryWheelMode$ tusunu basili tutun,\\n\nardindan sol analog cubuk ile Molotofu secin.",
    "Click and hold the right thumbstick\\n\nto bring up the inventory, then select\\n\nthe Medic Kit with the left thumbstick.":
        "Envanteri acmak icin sag cubuga basili tutun,\\n\nardindan sol cubuk ile\\n\nSaglik Cantasini secin.",
    "Click and hold the right thumbstick\\n\nto bring up the inventory, then select\\n\nthe Molotov with the left thumbstick.":
        "Envanteri acmak icin sag cubuga basili tutun,\\n\nardindan sol cubuk ile\\n\nMolotofu secin.",
    "Use $PC_TapMWheelUp$ or $PC_TapMWheelDown$ to select the Medic Kit.":
        "Saglik Cantasini secmek icin $PC_TapMWheelUp$ veya $PC_TapMWheelDown$ kullanin.",
    "Use $PC_TapMWheelUp$ or $PC_TapMWheelDown$ to select the Molotov.":
        "Molotofu secmek icin $PC_TapMWheelUp$ veya $PC_TapMWheelDown$ kullanin.",
    "Press $TapFire$ to attack.": "Saldirmak icin $TapFire$ tusuna basin.",
    "Press $TapFire$ to fire.": "Ates etmek icin $TapFire$ tusuna basin.",
    "Press $TapCloseCombat$ to attack.": "Yakin dovus saldirisi icin $TapCloseCombat$ tusuna basin.",
    "Pull the right trigger to attack.": "Saldirmak icin sag tetigi cekin.",
    "Pull the right trigger to fire.": "Ates etmek icin sag tetigi cekin.",
    "To throw a Molotov, press $TapFire$": "Molotof atmak icin $TapFire$ tusuna basin",
    "Press $TapFire$ to use the Medic Kit.": "Saglik Cantasini kullanmak icin $TapFire$ tusuna basin.",
    "Pull the right trigger to use the Medic Kit.": "Saglik Cantasini kullanmak icin sag tetigi cekin.",

    # Level interaction / Items / Flag / Sewers
    "To enter a location, go to\\n\nthe map and press $TapUse$": "Bir bolgeye girmek icin haritaya gidin\\n\nve $TapUse$ tusuna basin",
    "Search for some C4.": "C4 patlayici arayin.",
    "Search for some C4": "C4 patlayici arayin",
    "Search for a Medic Kit.": "Saglik Cantasi arayin.",
    "Search for a Medical Kit.": "Saglik Cantasi arayin.",
    "Go to flag and press $TapUse$ to hoist the\\n\nStars and Stripes and secure the location.":
        "Bayraga gidin ve bayragi cekip\\n\nbolgeyi guvenceye almak icin $TapUse$ tusuna basin.",
    "Go to the flag and press $TapUse$ to hoist the\\n\nStars and Stripes and secure the location.":
        "Bayraga gidin ve bayragi cekip\\n\nbolgeyi guvenceye almak icin $TapUse$ tusuna basin.",
    "Approach a wounded person\\n\nand press $TapUse$ to heal him.": "Yarali birinin yanina gidin\\n\nve onu iyilestirmek icin $TapUse$ tusuna basin.",
    "Approach a wounded person and\\n\npress $TapUse$ to heal him.": "Yarali birinin yanina gidin ve\\n\nonu iyilestirmek icin $TapUse$ tusuna basin.",
    "Press $TapActivateMap$ to access your map.": "Haritaniza erismek icin $TapActivateMap$ tusuna basin.",
    "Approach the manhole cover\\n\nand press $TapUse$ to open it.": "Rogar kapagina yaklasin\\n\nve acmak icin $TapUse$ tusuna basin.",
    "Move over the C4 to pick it up.": "Almak icin C4'un uzerine gelin.",
    "Move over a Medic Kit to pick it up.": "Almak icin Saglik Cantasinin uzerine gelin.",
    "Move over a Molotov to pick it up.": "Almak icin Molotofun uzerine gelin.",
    "Move over a weapon to pick it up.": "Almak icin bir silahin uzerine gelin.",
    "Find a manhole, press $TapUse$\\n\nand select another location.": "Bir rogar kapagi bulun, $TapUse$ tusuna basin\\n\nve baska bir bolge secin.",
    "To talk to people, approach them and press $TapUse$": "Insanlarla konusmak icin yanlarina gidin ve $TapUse$ tusuna basin",
    "To talk to people, approach\\n\nthem and press $TapUse$": "Insanlarla konusmak icin yanlarina\\n\ngidin ve $TapUse$ tusuna basin",

    # Developer test string
    "The quick brown\\n $TapUse$ fox jumps over the lazy dog.\\n $TapUse$ to kill the dog shoot him in the head and watch him die slowly.":
        "Hizli kahverengi\\n $TapUse$ tilki tembel kopegin uzerinden atlar."
}

HINTS_TRANSLATIONS = {
    orig: to_ascii_turkish(trans)
    for orig, trans in HINTS_MAP.items()
}

if __name__ == '__main__':
    with open(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_work\group_Hints.json', 'r', encoding='utf-8') as f:
        hints = json.load(f)
    missing = []
    for k, v in hints.items():
        if v not in HINTS_TRANSLATIONS:
            missing.append((k, v))
    print(f"group_Hints coverage: {len(hints) - len(missing)} / {len(hints)}")
    if missing:
        print("Missing:")
        for k, v in missing:
            print(f"  {k}: {repr(v)}")
