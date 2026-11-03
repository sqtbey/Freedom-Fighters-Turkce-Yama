# -*- coding: utf-8 -*-
import json, sys
sys.path.append(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline')
from turkish_ascii_converter import to_ascii_turkish

# Translation dictionary for Civilians (Civ_ComeWithMe, Civ_Helped, Civ_Negative, Civ_SpecHints, Civ_Vehicle, Civ_Wounded)
CIV_RAW = {
    # === Civ_ComeWithMe ===
    "Are you a Freedom Fighter? You should see this before the Reds do.":
        "Ozgurluk Savascisi misin? Kizillar gormeden once bunu gormelisin.",
    "Come over here - I've gotta show you somethin'.":
        "Buraya gel - sana bir sey gostermem lazim.",
    "Excuse me Mister! I gotta show you something.":
        "Affedersiniz Bayim! Size bir sey gostermem lazim.",
    "Fast - over here! Follow me!":
        "Cabuk - bu tarafa! Takip et beni!",
    "Hey Mister, follow me.":
        "Hey Bayim, takip edin beni.",
    "Hey follow me quick - before the Reds spot us.":
        "Hey hemen takip et beni - Kizillar bizi fark etmeden once.",
    "Hey you! Follow me - there's something you need to see!":
        "Hey sen! Takip et beni - gormen gereken bir sey var!",
    "Hey you! Follow me, there is something you need to see.":
        "Hey sen! Beni takip et, gormen gereken bir sey var.",
    "Hey you, come on... this way.":
        "Hey sen, hadi... bu taraftan.",
    "Hey! Are you a Freedom Fighter? Over here. There is something you have to see.":
        "Hey! Sen Ozgurluk Savascisi misin? Bu tarafa. Gormen gereken bir sey var.",
    "Hey, are you a Freedom Fighter? Over here, there's something you hafta see.":
        "Hey, sen Ozgurluk Savascisi misin? Bu tarafa, kesinlikle gormen gereken bir sey var.",
    "Hey, this way\x96 quick.":
        "Hey, bu taraftan... cabuk.",
    "Hey, this way– quick.":
        "Hey, bu taraftan... cabuk.",
    "Hey, this way… quick.":
        "Hey, bu taraftan... cabuk.",
    "Hey, this way... quick.":
        "Hey, bu taraftan... cabuk.",
    "I have something to show - but only if you can be trusted.":
        "Gosterecek bir seyim var - ama sadece sana guvenebileceksem.",
    "I have something to show. But only if you can be trusted.":
        "Gosterecek bir seyim var. Ama sadece sana guvenebileceksem.",
    "I think you should see this. It might be important. Follow me.":
        "Bunu gormelisin bence. Onemli olabilir. Takip et beni.",
    "I want to show you something that will help your cause - follow me.":
        "Davaniza yardimci olacak bir sey gostermek istiyorum - takip edin beni.",
    "I've got somethin' to show ya. Follow me and you'll see what I'm talkin' about.":
        "Sana gosterecek bir seyim var. Takip et beni, ne demek istedigimi goreceksin.",
    "Keep you head down and follow me!":
        "Basini eg ve beni takip et!",
    "Over here, quick!":
        "Bu tarafa, cabuk!",
    "Over this way! Before the soldiers see us.":
        "Bu taraftan! Askerler bizi gormeden once.",
    "Over this way, you gotta see this. It'll help your cause.":
        "Bu taraftan, bunu gormelisin. Davaniza yardimci olacaktir.",
    "Phantom! Over here, follow me.":
        "Hayalet! Bu tarafa, beni takip et.",
    "Psst! Over here, come with me.":
        "Pst! Bu tarafa, benimle gel.",
    "Quick follow me before the Reds spot us!":
        "Cabuk takip et beni, Kizillar fark etmeden once!",
    "Quick! Hey come over this way, but stay quiet.":
        "Cabuk! Hey bu tarafa gel, ama sessiz ol.",
    "Um, hey. I got somethin' you should see.":
        "Sey, hey. Gormen gereken bir sey var.",
    "You the Phantom? Follow me, I'll show ya something.":
        "Hayalet sen misin? Takip et beni, sana bir sey gosterecegim.",

    # === Civ_Helped ===
    "Ahh! That's nice!": "Ahh! Bu cok iyi geldi!",
    "Are you doctor? Thank you!": "Doktor musunuz? Tesekkurler!",
    "Huh! I'm feeling better already!": "Huh! Simdiden daha iyi hissediyorum!",
    "I feel better already.": "Simdiden daha iyi hissediyorum.",
    "I think I can make it from here.": "Sanirim buradan sonrasini halledebilirim.",
    "I think I'll pull through now!": "Sanirim artik kurtulacagim!",
    "I'm feeling better already!": "Simdiden daha iyi hissediyorum!",
    "I.. I think I can get up now!": "B.. bence artik ayaga kalkabilirim!",
    "I\x96 I think I can get up now!": "B... bence artik ayaga kalkabilirim!",
    "I– I think I can get up now!": "B... bence artik ayaga kalkabilirim!",
    "I… I think I can get up now!": "B... bence artik ayaga kalkabilirim!",
    "My hero!": "Kahramanim benim!",
    "Oh thank you! I thought I was gonna die out here.":
        "Oh tesekkur ederim! Burada olecegimi sanmistim.",
    "Thank you Sir!": "Tesekkurler Bayim!",
    "Thank you so much.": "Cok tesekkur ederim.",
    "Thank you!": "Tesekkur ederim!",
    "Thank you, I didn't think I was gonna make it.":
        "Tesekkurler, kurtulabilecegimi sanmiyordum.",
    "Thanks Doc!": "Sag ol Doktor!",
    "Thanks Doc! I'll spread the word about you.":
        "Sag ol Doktor! Sana olan minnetimi herkese anlatacagim.",
    "Thanks Mister!": "Tesekkurler Bayim!",
    "Thanks Mister! I feel strong enough to stand up.":
        "Tesekkurler Bayim! Ayaga kalkacak kadar guclu hissediyorum.",
    "Thanks a lot!": "Cok tesekkurler!",
    "Thanks!": "Tesekkurler!",
    "Thanks! I think I can make it on my own now.":
        "Sag ol! Sanirim artik tek basima gidebilirim.",
    "That feels a lot better!": "Bu cok daha iyi hissettirdi!",
    "That's a nice field dressing. Thanks Doc!":
        "Harika bir ilk yardim pansumani. Sag ol Doktor!",
    "There are a few good ones left. Thank you!":
        "Hala birkac iyi insan kalmis. Tesekkur ederim!",
    "You came along just in time. I appreciate your help.":
        "Tam zamaninda yetistin. Yardimin icin cok tesekkurler.",
    "You sure know your way around a Medi-Kit. Thanks!":
        "Ilk yardim cantasini kullanmayi gercekten biliyorsun. Sag ol!",
    "You're the Man.": "Harikasin dostum.",

    # === Civ_Negative ===
    "Can't you find someone else? I don't wanna die.":
        "Baska birini bulamaz misin? Olmek istemiyorum.",
    "Count me out!": "Beni saymayin!",
    "Count me out, they're too many of Rooskies.":
        "Beni karistirmayin, Ruslar cok kalabalik.",
    "Do I look like I have a death wish? Try someone else.":
        "Olmek istiyor gibi bir halim mi var? Baska birini deneyin.",
    "Find someone else to fight in your army.":
        "Ordunuzda savasacak baska birini bulun.",
    "Find someone else!": "Baska birini bulun!",
    "Hey, not me!": "Hey, ben olmaz!",
    "I can't fight, but keep asking around. I'm sure you'll find someone.":
        "Ben savasamam, ama etrafa sormaya devam edin. Kesin birini bulursunuz.",
    "I can't get involved!": "Karısamam!",
    "I can't get involved.": "Karısamam.",
    "I don't think so!": "Hic sanmiyorum!",
    "I don't wanna get involved with any Freedom Fighters.":
        "Hicbir Ozgurluk Savascisi'na bulasmak istemiyorum.",
    "I'm not a fighter! Find someone else!":
        "Ben savasci degilim! Baska birini bulun!",
    "I'm not prepared to die!": "Olum icin hazir degilim!",
    "I'm not prepared to die.": "Olum icin hazir degilim.",
    "No Thanks!": "Hayir Tesekkurler!",
    "No thanks!": "Hayir tesekkurler!",
    "No thanks! I'll just slow you down anyway.":
        "Hayir tesekkurler! Zaten sadece sizi yavaslatirim.",
    "No thanks! I'm allergic to bullets.":
        "Hayir tesekkurler! Mermilere alerjim var.",
    "No thanks! You can keep your war to yourself.":
        "Hayir tesekkurler! Savasiniz size kalsin.",
    "No thanks! You con keep your war to yourself.":
        "Hayir tesekkurler! Savasiniz size kalsin.",
    "No way I'm following you!": "Pesinizden gelmeme imkan yok!",
    "No way man!": "Olmaz dostum!",
    "No way!": "Olmaz!",
    "No way! I don't want them to even see me talkin' to ya.":
        "Olmaz! Seninle konustugumu bile gormelerini istemiyorum.",
    "No way! I've got no beef with the Rooskies!":
        "Olmaz! Ruslarla bir alip veremedigim yok!",
    "No way, I'm keeping my nose clean!":
        "Olmaz, ben beladan uzak duruyorum!",
    "No way, not me!": "Olmaz, ben olmaz!",
    "No, the Soviets are ruthless, I can't get involved.":
        "Hayir, Sovyetler cok acimasiz, karısamam.",
    "No... no way, the Soviets are ruthless, I can't get involved.":
        "Hayir... imkani yok, Sovyetler cok acimasiz, karısamam.",
    "Not me!": "Ben degil!",
    "Not me! I'll mind my own business.":
        "Ben degil! Kendi isime bakarim.",
    "There's no way I'm following you.":
        "Seni takip etmeme imkan yok.",
    "Try someone else.": "Baska birini deneyin.",
    "Unh-unh! Not me!": "Cık cık! Ben olmaz!",
    "You better find someone else.": "Baska birini bulsaniz iyi olur.",
    "You kiddin'?! No Way!": "Saka mi yapiyorsun?! Imkani yok!",
    "You kiddin'? No way.": "Saka mi yapiyorsun? Imkani yok.",

    # === Civ_SpecHints ===
    "Didja see that?": "Gordun mu sunu?",
    "Hey look!": "Hey bak!",
    "I don't know if you're interested, but they've been moving a lot of troops through here.":
        "Ilgilenir misiniz bilmem ama buradan cok sayida asker geciriyorlar.",
    "I think I saw something in that building over there.":
        "Suradaki binada bir sey gordum sanirim.",
    "I think that bridge is important to the Sovets.":
        "Sanirim o kopru Sovyetler icin onemli.",
    "I think there are prisoners in that building.":
        "Sanirim o binada mahkumlar var.",
    "I've seen a bunch of Soviets down there.":
        "Asagida bir suru Sovyet askeri gordum.",
    "I've seen a lot of troops in that area.":
        "O bolgede cok fazla asker gordum.",
    "I've seen prisoners being led into that building.":
        "O binaya mahkumlarin goturuldugunu gordum.",
    "It's not a prison, but they have some prisoners inside. Watch out or you'll end up there too.":
        "Hapishane degil ama iceride bazi mahkumlar var. Dikkat et yoksa sen de kendini orada bulursun.",
    "Last time I saw, there were a bunch of soldiers in that building. They've been real quiet.":
        "Son gordugumde o binada bir suru asker vardi. Cok sessiz duruyorlar.",
    "Look at this": "Buna bak",
    "Look over there": "Suraya bak",
    "Look!": "Bak!",
    "Looks like the Soviets think this bridge is important.":
        "Sovyetler bu koprunun onemli oldugunu dusunuyor gibi.",
    "Man - they sure have had lots of soldiers marching through here. Wonder where they're headed?":
        "Dostum - buradan kesinlikle cok sayida asker gecti. Nereye gidiyorlar acaba?",
    "Not too far ahead is a helipad.":
        "Cok ileride degil, bir helikopter pisti var.",
    "Not too far ahead is a hellipad.":
        "Cok ileride degil, bir helikopter pisti var.",
    "Over there - look!": "Surada - bak!",
    "Take a look in this area.": "Bu bolgeye bir goz atin.",
    "Take a look over there.": "Suraya bir goz atin.",
    "That building might have something your after.":
        "O binada aradiginiz bir sey olabilir.",
    "That way leads to the Port.": "O yol Limana cikar.",
    "The Port Area is that way.": "Liman Bolgesi su tarafta.",
    "The Soviet helicopters land somewhere over that way.":
        "Sovyet helikopterleri su tarafta bir yere iniyor.",
    "The Soviets are crawling all over the place.":
        "Sovyetler her yerde kayniyor.",
    "The Soviets really want to protect this bridge - must be important.":
        "Sovyetler bu kopruyu korumayi cok istiyor - onemli olmali.",
    "The Soviets sure have sent in a big army - I'd love to send them home with their tails between their legs.":
        "Sovyetler kesinlikle buyuk bir ordu gonderdi - kuyruklarini kistirip evlerine donduklerini gormeyi cok isterdim.",
    "The docks are over there.": "Liman surada.",
    "The helipad is over there.": "Helikopter pisti surada.",
    "The port is down that way.": "Liman su asagidadir.",
    "The soldiers in that place are angrier than a hornets nest. Something musta strirred them up.":
        "Oradaki askerler esek arisi kovanindan daha ofkeli. Bir sey onlari kiskirtmis olmali.",
    "There are a lot of Soviet troops down there.":
        "Asagida cok sayida Sovyet birligi var.",
    "There are a lot of soldiers over there.":
        "Surada cok fazla asker var.",
    "There has been a lotta Soviet movement through here.":
        "Buradan cok sayida Sovyet hareketliligi oldu.",
    "There might be something in that building.":
        "O binada bir sey olabilir.",
    "There were a bunch of soldiers down that way.":
        "Su tarafta bir grup asker vardi.",
    "There's a building over there that the Soviets have been interested in.":
        "Surada Sovyetlerin ilgilendigi bir bina var.",
    "There's been a lot Soviet movement through here.":
        "Burada cok fazla Sovyet hareketliligi oldu.",
    "They have tons of equipment crossing that bridge.":
        "O kopruden tonlarca techizat geciriyorlar.",
    "They were leading prisoners into that building.":
        "O binaya mahkumlari goturuyorlardi.",
    "They've been moving troops through here. Must be up to something.":
        "Buradan asker sevk ediyorlar. Bir seyler pesinde olmalilar.",
    "Try searching over there.": "Surayi aramayi deneyin.",
    "Wait a minute - what is that?": "Bir dakika - o da ne?",
    "Wait a minute! What's that?": "Bir dakika! O da ne?",
    "What is that?": "O nedir?",
    "What the...?": "Ne oluyor...?",
    "What's that over there?": "Suradaki de ne?",
    "What\x92s that over there?": "Suradaki de ne?",
    "What’s that over there?": "Suradaki de ne?",
    "Whoa! Check that out!": "Vay canina! Su ise bak!",
    "You better check out that building over there.":
        "Suradaki binaya bir baksaniz iyi olur.",
    "You might find something in that building over there.":
        "Suradaki binada bir seyler bulabilirsiniz.",
    "You might want to check out that building over there.":
        "Suradaki binaya bir goz atmak isteyebilirsiniz.",
    "You might want to look over there.":
        "Suraya bakmak isteyebilirsiniz.",
    "You should check out that building.":
        "O binaya bir bakmalisiniz.",
    "You'll find a helipad over there.":
        "Surada bir helikopter pisti bulacaksiniz.",

    # === Civ_Vehicle ===
    "Better get out of the way!": "Yoldan cekilseniz iyi olur!",
    "Crazy driver!": "Deli sofor!",
    "Get out of the road!": "Yoldan cekilin!",
    "Get out of the street!": "Caddeden cekilin!",
    "Get out of the way!": "Yoldan cekil!",
    "Heads up!": "Dikkat edin!",
    "Hey - Look out!": "Hey - Dikkat et!",
    "Look out!": "Dikkat et!",
    "Run!": "Kacin!",
    "Shh! Drives worse than a New York taxi!":
        "Pst! New York taksisinden daha beter suruyor!",
    "Tch! Drives worse than a New York taxi!":
        "Tch! New York taksisinden daha beter suruyor!",
    "That driver is crazy!": "Bu sofor deli!",
    "That driver's crazy!": "Bu sofor cilgin!",
    "That guy drives worse than a New York cabbie!":
        "Bu herif New York taksicisinden daha beter suruyor!",
    "That guy must be in a hurry!": "Bu adamin acelesi olmali!",
    "That guy must be in a hurry.": "Bu adamin acelesi olmali.",
    "That guy's worse than a cabbie!": "Bu herif taksiciden beter!",
    "Watch out!": "Dikkat!",

    # === Civ_Wounded ===
    "(groan)": "(inleme)",
    "<Groan> I'm bleedin' bad.": "<Inleme> Cok fena kaniyorum.",
    "Ack! Help! I'm dying!": "Ah! Yardim edin! Oluyorum!",
    "Ahh! Pain!": "Ahh! Cok aciyor!",
    "Ahhh!": "Ahhh!",
    "Are you here to help me?": "Bana yardim etmeye mi geldiniz?",
    "Can you help me?": "Bana yardim edebilir misiniz?",
    "Damn Reds shot me!": "Lanet Kizillar beni vurdu!",
    "Find me a doctor - please!": "Bana bir doktor bulun - lutfen!",
    "Find me a doctor!": "Bana bir doktor bulun!",
    "Find me a doctor.": "Bana bir doktor bulun.",
    "Find me a doctor... please.": "Bana bir doktor bulun... lutfen.",
    "Help me!": "Yardim et!",
    "Help me.": "Yardim et bana.",
    "Help!": "Yardim edin!",
    "Hey Mister! You gotta help me, I'm shot!":
        "Hey Bayim! Bana yardim etmelisiniz, vuruldum!",
    "Hey, I'm shot - help me out here!":
        "Hey, vuruldum - yardim edin bana!",
    "I can't go on!": "Daha fazla devam edemiyorum!",
    "I have to get to a doctor!": "Bir doktora ulasmam lazim!",
    "I need medical attention!": "Tibbi mudahaleye ihtiyacim var!",
    "I'm getting cold!": "Usuyorum!",
    "I'm shot! Oh damn, help me!": "Vuruldum! Kahretsin, yardim edin!",
    "I'm shot! Oh dear, help me!": "Vuruldum! Aman Tanrim, yardim edin!",
    "I'm shot! Ya gotta help me!": "Vuruldum! Bana yardim etmelisin!",
    "Ohhh!": "Ohhh!",
    "Ohhh! I'm shot!": "Ohhh! Vuruldum!",
    "Quick find me a doctor!": "Cabuk bana bir doktor bulun!",
    "Quick! Find me a doctor!": "Cabuk! Bana bir doktor bulun!",
    "They shot me!": "Beni vurdular!",
    "Unhh!": "Unhh!",
    "Y... you gotta help me... I've been shot.":
        "B... bana yardim etmelisin... vuruldum.",
    "You gotta help me, I've been shot!":
        "Bana yardim etmelisin, vuruldum!",
    "You there, I need help! I need medical attention!":
        "Hey sen, yardima ihtiyacim var! Tibbi yardima ihtiyacim var!",
    "[groaging in pain]": "[aci icinde inleme]",
    "[groaning in pain]": "[aci icinde inleme]",
    "it hurts!": "aciyor!",
    "ow, the pain!": "ah, cok aciyor!"
}

CIV_TRANSLATIONS = {
    orig: to_ascii_turkish(trans)
    for orig, trans in CIV_RAW.items()
}

if __name__ == '__main__':
    path = r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_work\alllevels_Civ.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    unique_grp = set(data.values())
    total = len(unique_grp)
    missing = [v for v in unique_grp if v not in CIV_TRANSLATIONS]
    print(f"Coverage: {total - len(missing)} / {total}")
    if missing:
        print("Missing:")
        for v in missing:
            print(f"  {repr(v)}")
