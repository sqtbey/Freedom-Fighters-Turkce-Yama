# -*- coding: utf-8 -*-
import json, sys
sys.path.append(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline')
from turkish_ascii_converter import to_ascii_turkish

# Translation dictionary for Chapters 1 & 2
CH1_CH2_RAW = {
    # C01A
    "What \x96 you\x92re not supposed to be here?":
        "Ne... burada olmaman gerekiyordu!",
    "What – you’re not supposed to be here?":
        "Ne... burada olmaman gerekiyordu!",
    "What \x96 you\x92re not supposed to be here?":
        "Ne... burada olmaman gerekiyordu!",
    "You\x92re in violation of new code, citizen!":
        "Yeni kanunlari ihlal ediyorsun, vatandas!",
    "You’re in violation of new code, citizen!":
        "Yeni kanunlari ihlal ediyorsun, vatandas!",
    "It is fortunate that you found me - quickly, this way.":
        "Beni bulmaniz buyuk sans - cabuk, bu taraftan.",
    "Come my friend - we cannot stay here long.":
        "Gelin dostum - burada uzun sure kalamayiz.",
    "Hurry! We mustn't linger here.":
        "Acele edin! Burada oyalanmamaliyiz.",
    "Up here - I know a way out of this, stay close!":
        "Buradan yukari - bir cikis yolu biliyorum, yakinimda kalin!",
    "Come out here!":
        "Buraya gelin!",
    "Perfect, he won't trouble us anymore.":
        "Harika, artik bize sorun cikaramaz.",
    "Take his weapon!":
        "Silahini alin!",
    "Take his weapon, if you want to survive!":
        "Hayatta kalmak istiyorsaniz silahini alin!",
    "More soldiers! Shoot them!":
        "Daha fazla asker! Vurun onlari!",
    "We are doing fine - come, let us move on..!!":
        "Iyi gidiyoruz - gelin, devam edelim..!!",
    "See those soldiers down there! We are not as well supplied as the enemy, so we'll have to improvise. Aim at the fuel barrels rather than the soldiers.":
        "Asagidaki su askerleri goruyor musunuz! Dusman kadar iyi techizatli degiliz, bu yuzden dogaclama yapmaliyiz. Askerlerden ziyade yakit varillerine nisan alin.",
    "Do it now! Shoot the barrels!":
        "Simdi yapin! Varillere ates edin!",
    "You're wounded - take that Medical Kit behind the Ambulance.":
        "Yaralisiniz - Ambulansin arkasindaki Saglik Cantasini alin.",
    "Good - you are ready for battle again.":
        "Guzel - artik tekrar savasa hazirsiniz.",
    "Use the health pack - you can't afford to let your wounds slow you down.":
        "Saglik paketini kullanin - yaralarinizin sizi yavaslatmasina izin veremezsiniz.",
    "We're not out of the woods yet - it's us or them!":
        "Henuz tehlikeyi atlatmadik - ya biz ya onlar!",
    "Hellloooo\x96":
        "Kimse var miii...",
    "Hellloooo…":
        "Kimse var miii...",
    "Hellloooo...":
        "Kimse var miii...",
    "Find some cover!":
        "Bir siper bulun!",
    "Grab a Molotov and come with me now.":
        "Bir Molotof kap ve hemen benimle gel.",
    "What's our status?":
        "Durumumuz nedir?",
    "Okay, come with me guys. I've got supplies that'll get us out of this mess.":
        "Tamam, benimle gelin beyler. Bizi bu beladan cikaracak malzemelerim var.",
    "Throw those babies!":
        "Firlat su bebekleri!",
    "Oh yeah baby! Steee-rike, and he's out!":
        "Iste bu be! Tam isabet, nakavt!",
    "Hurry up!":
        "Acele edin!",
    "Arrrrrrgghh!":
        "Aaaaaargghh!",
    "He's wounded! You have a health kit, save this man's life!":
        "Yaralandi! Saglik cantaniz var, bu adamin hayatini kurtarin!",
    "That was close! I guess I owe ya one, pal.":
        "Ucuz atlattik! Galiba sana bir can borcum var, dostum.",
    "He's bleeding to death! He needs your help!":
        "Kanamadan oluyor! Yardiminiza ihtiyaci var!",
    "No time to waste - they'll be back if we don't hurry!":
        "Vakit kaybetmeyelim - acele etmezsek geri donerler!",
    "I think they have your brother in that helicopter, but don't worry we'll find him!":
        "Sanirim kardesinizi o helikoptere bindirdiler, ama merak etmeyin onu bulacagiz!",
    "Grab a Molotov - lets show the Reds!":
        "Bir Molotof kap - Kizillara gunlerini gosterelim!",
    "We must leave now!":
        "Hemen gitmeliyiz!",
    "Please hurry! We must move on now!":
        "Lutfen acele edin! Hemen ilerlemeliyiz!",
    "What is the problem? We must act now!":
        "Sorun nedir? Hemen harekete gecmeliyiz!",
    "The soldiers are sure to find us here - we must find another hiding place!":
        "Askerler bizi burada kesin bulur - baska bir siginak bulmaliyiz!",
    "We have no time for this - follow me! I know a safe place where we can rest.":
        "Bunun icin vaktimiz yok - beni takip edin! Dinlenebilecegimiz guvenli bir yer biliyorum.",
    "Get a move on! We cannot waste time!":
        "Harekete gecin! Zaman kaybedemeyiz!",
    "You have no business here \x96 identify yourself, citizen!":
        "Burada isiniz yok - kimliginizi aciklayin, vatandas!",
    "You have no business here – identify yourself, citizen!":
        "Burada isiniz yok - kimliginizi aciklayin, vatandas!",
    "Open this manhole with your wrench \x96 we can escape to safety below in the sewers!":
        "Bu rogar kapagini ingiliz anahtarinizla acin - asagidaki kanalizasyona kacip kurtulabiliriz!",
    "Open this manhole with your wrench – we can escape to safety below in the sewers!":
        "Bu rogar kapagini ingiliz anahtarinizla acin - asagidaki kanalizasyona kacip kurtulabiliriz!",
    "Okay! In the future, remember this is your only way to safety. Now - let's get down and out\xa0of here":
        "Tamam! Ileride unutmayin, kurtulus icin tek yolunuz bu. Simdi - asagi inip buradan cikalim.",
    "Okay! In the future, remember this is your only way to safety. Now - let's get down and out of here":
        "Tamam! Ileride unutmayin, kurtulus icin tek yolunuz bu. Simdi - asagi inip buradan cikalim.",
    "Get your hands off me, you stinking commie! No Chris! Save yourself!":
        "Cekin ellerinizi uzerimden, sizi pis komunistler! Hayir Chris! Kendini kurtar!",
    "Follow me and stay close! They're shelling without restraint.":
        "Beni takip edin ve yakinimda kalin! Hic acimadan bombaliyorlar.",

    # C02A
    "Hey bro', it's damn good to see ya', knew you'd come looking for me!":
        "Hey kardesim, seni gormek harika, beni aramaya gelecegini biliyordum!",
    "On the roof, bro\x92! Don\x92t forget the flag!":
        "Catida, kardesim! Bayragi unutma!",
    "On the roof, bro’! Don’t forget the flag!":
        "Catida, kardesim! Bayragi unutma!",
    "Yo man! I gotta talk to you.":
        "Hey dostum! Seninle konusmam lazim.",
    "You wanna blow up that gas station? Your gonna need some explosives. You can find some in the other neighborhood.":
        "O benzinligi havaya ucurmak mi istiyorsun? Patlayiciya ihtiyacin olacak. Diger mahallede biraz bulabilirsin.",
    "Check that! You found some C4. All ya gotta do now is blow the gas station.":
        "Su ise bak! C4 bulmussun. Simdi tek yapman gereken benzinligi havaya ucurmak.",
    "No way pal - no one gets by until Isabella is free.":
        "Olmaz dostum - Isabella serbest kalana kadar kimse gecemez.",
    "Isabella you're back!":
        "Isabella dondun!",
    "Yes, and I owe it all to this man.":
        "Evet, ve bunu tamamen bu adama borcluyum.",
    "You must be Chris - come on in!":
        "Sen Chris olmalisin - iceri gel!",
    "This is only a temporary base - we're using it as a staging place for this mission. Let's plan our next move - like it or not, you have a new profession now...  Freedom Fighter.":
        "Burası sadece gecici bir us - bu gorev icin toplanma alani olarak kullaniyoruz. Bir sonraki hamlemizi planlayalim - istesen de istemesen de artik yeni bir meslegin var... Ozgurluk Savascisi.",
    "Hey man!":
        "Hey dostum!",
    "Come on in - Mi casa, es su casa":
        "Iceri gel - Benim evim, senin evin.",
    "Here we have an overview of the enemy compound, you can see them unloading equipment... They're using this post office as a temporary command center, and planning further advances into the city from here. It would really set them back if we recaptured this area. You won't be alone. Ever since you proved yourself by rescuing me, people are starting to believe in you.":
        "Burada dusman yerleskesinin bir gorunumu var, techizat indirdiklerini gorebilirsiniz... Bu postaneyi gecici bir komuta merkezi olarak kullaniyorlar ve sehirdeki ilerleyislerini buradan planliyorlar. Bu bolgeyi geri alirsak onlari buyuk olcude sekteye ugratiriz. Yalniz olmayacaksin. Beni kurtararak kendini kanitladigindan beri insanlar sana inanmaya basladi.",
    "I'll let you lead two of my best men into action.":
        "En iyi iki adamimi operasyona senin liderliginde gonderecegim.",
    "As long as they're recruited, these guys will follow you wherever you go, just like bodyguards.":
        "Birligine alindigi surece bu adamlar koruma gibi nereye gidersen seni takip edecekler.",
    "You can also send them off to take out sentries.":
        "Nobetcileri etkisiz hale getirmek icin onlari ileri de gonderebilirsin.",
    "Just point in the direction you want them to go and give the attack order.":
        "Sadece gitmelerini istedigin yonu goster ve saldiri emrini ver.",
    "Come on - try sending them to that doorway over there.":
        "Hadi - onlari suradaki kapi araligina gondermeyi dene.",
    "Good!":
        "Guzel!",
    "Don't worry, you can always call them back to you.":
        "Merak etme, onlari istedigin zaman yanina geri cagirabilirsin.",
    "Call them back!":
        "Onlari geri cagir!",
    "There you go!":
        "Iste boyle!",
    "Remember - they're good fighters, but they can't think for themselves. It's up to you to keep them alive.":
        "Unutma - iyi savascilardir ama kendi baslarina dusunemezler. Onlari hayatta tutmak sana bagli.",
    "If a squad member is wounded, approach him and use a health pack.":
        "Bir tim uyesi yaralanirsa yanina git ve saglik paketi kullan.",
    "Don't be careless, you don't wanna waste medical supplies.":
        "Dikkatsiz olma, tibbi malzemeleri bosa harcamak istemezsin.",
    "You can also order your men to defend a position.":
        "Adamlarina bir mevziyi savunmalarini da emredebilirsin.",
    "Tell one of them to hold a defensive position by that barrel.":
        "Birine su varilin yaninda savunma mevzisi almasini soyle.",
    "Order him to take cover!":
        "Ona siper almasini emret!",
    "Excellent - they'll hold the position until you call them back.":
        "Mukemmel - sen onlari geri cagirana kadar o mevziyi tutacaklar.",
    "Now let's review our main objectives.":
        "Simdi ana hedeflerimizi gozden gecirelim.",
    "First, we'll need to gain access to the Post Office - it's heavily guarded so keep your eyes open.":
        "Ilk olarak Postaneye girmemiz gerekiyor - cok siki korunuyor, o yuzden gozlerini dort ac.",
    "Next, search the building and locate Troy.":
        "Ardindan binayi arayin ve Troy'u bulun.",
    "Finally, hoist our flag from the roof of the Post Office - that'll signal our victory, and show the city that we can beat these guys!":
        "Son olarak bayragimizi Postanenin catisina cekin - bu zaferimizi duyuracak ve sehre bu adamlari yenebilecegimizi gosterecek!",
    "We have a lot of work to do, let's get moving!":
        "Yapacak cok isimiz var, harekete gecelim!",
    "We're running low on supplies, there's no way we can support this mission!":
        "Malzemelerimiz azaliyor, bu gorevi bu sekilde desteklememize imkan yok!",
    "I'll need some C4 to breach that security door.":
        "O guvenlik kapisini kirmak icin biraz C4'e ihtiyacim olacak.",
    "I'll have to find another way in...":
        "Iceri girmek icin baska bir yol bulmaliyim...",
    "What the... Troy!":
        "Ne... Troy!",
    "You really think you're gonna win this, don't you brother?":
        "Bunu gercekten kazanabilecegini saniyorsun, degil mi kardesim?",
    "Hey! Stop it!":
        "Hey! Durun!",
    "This won't bring him back Chris...":
        "Bu onu geri getirmeyecek Chris...",
    "What about Troy?":
        "Peki ya Troy?",
    "Troy...":
        "Troy...",
    "We have to stop this madness...":
        "Bu cilginligi durdurmaliyiz...",
    "Get down!":
        "Yere yatin!",
    "Now go and fight! Good luck.":
        "Simdi git ve savas! Iyi sanslar.",
    "Remember you are the leader. You can issue your men commands. Order them to attack that small patrol up ahead.":
        "Lider oldugunu unutma. Adamlarina emir verebilirsin. Ilerideki o kucuk devriyeye saldirmalarini emret.",
    "Good, your men will fight every enemy in the direction you are pointing them.":
        "Guzel, adamlarin yonlendirdigin taraftaki her dusmanla savasacaktir.",
    "If you want your men to fall back, simply call them.":
        "Adamlarinin geri cekilmesini istiyorsan onlari cagirman yeterli.",
    "Great! You are a true leader, sometimes it's important to know when to fall back.":
        "Harika! Gercek bir lidersin, bazen ne zaman geri cekilecegini bilmek onemlidir.",
    "This is an important vantage point that gives you an overview of the battlefield, useful for strategic maneuvers. From here you can command your troops and cover them at the same time.":
        "Burası savas alanina hakim onemli bir gozlem noktasi, stratejik manevralar icin cok faydali. Buradan birliklerine komuta edebilir ve ayni anda onlari koruyabilirsin.",
    "Get on top of the container.":
        "Konteynerin uzerine cik.",
    "Pinpointing the exact location of your Freedom Fighters can be very useful for advanced strategy.":
        "Ozgurluk Savascilarinin tam konumunu belirlemek gelismis strateji icin cok faydali olabilir.",
    "Let's go! Take me to the safe house!":
        "Hadi gidelim! Beni guvenli eve gotur!",
    "Remember to check the map once in a while.":
        "Arada bir haritayi kontrol etmeyi unutma.",
    "On the map you can see the mission objectives. It's easy to get lost, so use the map to find your targets. They might make life easier for you.":
        "Haritada gorev hedeflerini gorebilirsin. Kaybolmak cok kolaydir, o yuzden hedeflerini bulmak icin haritayi kullan. Isini kolaylastirabilir.",
    "You guys ready for a fight? It's waiting right downstairs!":
        "Savasa hazir misiniz millet? Tam alt katta bizi bekliyor!",
    "Stock up on the equipment we got here!":
        "Buradaki ekipmanlardan stok yapin!",
    "Hey!":
        "Hey!",
    "What's the good word?":
        "Ne haber?",
    "Hey there!":
        "Selam!",
    "Nice work!":
        "Iyi is!",
    "You're a regular Hero mister!":
        "Tam bir Kahramansiniz bayim!",
    "We really needed to get started on this.":
        "Buna gercekten baslamamiz gerekiyordu.",
    "Chris are you ready? Come on follow me!":
        "Chris hazir misin? Hadi takip et beni!",
    "Remember that you can always join the fight to help out your men!":
        "Adamlarina yardim etmek icin her zaman savasa katilabilecegini unutma!",
    "Follow me Chris, I'll take you to the safe house.":
        "Beni takip et Chris, seni guvenli eve goturecegim.",
    "Come on Chris, we have no time to waste.":
        "Hadi Chris, kaybedecek vaktimiz yok.",
    "Come on, keep up with me.":
        "Hadi, bana yetis.",
    "Come on Chris, follow me.":
        "Hadi Chris, takip et beni.",
    "Follow me Chris, come on.":
        "Beni takip et Chris, hadi.",
    "Come on, stay close to me.":
        "Hadi, yakinimda kal.",
    "We gotta run, come on.":
        "Kosmamiz lazim, hadi.",
    "This way Chris.":
        "Bu taraftan Chris.",
    "Stay close to me.":
        "Yakinimda kal.",
    "Heeelp!":
        "Yardim ediiin!",
    "Chriiis, where are you?!!":
        "Chriiis, neredesiiin?!!",
    "I'm over heere!":
        "Buradayiiim!",
    "The snipers have the street covered! Nothing gets by them\x96 alive.":
        "Keskin nisancilar caddeyi tutmus! Yanlarindan hicbir sey... canli gecemez.",
    "The snipers have the street covered! Nothing gets by them\u2026 alive.":
        "Keskin nisancilar caddeyi tutmus! Yanlarindan hicbir sey... canli gecemez.",
    "The snipers have the street covered! Nothing gets by them alive.":
        "Keskin nisancilar caddeyi tutmus! Yanlarindan hicbir sey... canli gecemez.",

    # C02B
    "Thanks - I'm Isabella, nice to meet you. Let's clean up this place. It's time to fly our own colors again!":
        "Tesekkurler - Ben Isabella, tanistigimiza memnun oldum. Burayi temizleyelim. Kendi bayragimizi yeniden dalgalandirmanin zamani geldi!",
    "Remember - run it up the flagpole on the roof.":
        "Unutma - catidaki bayrak diregine cek.",
    "The snipers have the street covered! Nothing gets by them\x96 alive.":
        "Keskin nisancilar caddeyi kontrol altinda tutuyor! Yanlarindan hicbir sey... canli gecemez.",
    "The snipers have the street covered! Nothing gets by them– alive.":
        "Keskin nisancilar caddeyi kontrol altinda tutuyor! Yanlarindan hicbir sey... canli gecemez.",
    "The snipers have the street covered! Nothing gets by them... alive.":
        "Keskin nisancilar caddeyi kontrol altinda tutuyor! Yanlarindan hicbir sey... canli gecemez.",
    "Please help, we're pinned down here.":
        "Lutfen yardim edin, burada kisilip kaldik.",
    "Hey listen buddy - grab some explosives and get back to the sewers. Go to the Gas Station - that's where you'll need to blow the Fuel Tank. Just go through the sewer you came from.":
        "Hey dinle ahbap - patlayici alip kanalizasyona don. Benzinlige git - orada Yakit Tankini havaya ucurman gerekecek. Sadece geldigin kanalizasyondan gec.",
    "Enter the police station through the parking garage but stay low, or the soldiers will spot you.":
        "Polis karakoluna otoparktan gir ama alcaktan ilerle, yoksa askerler seni fark eder.",
    "Thanks friend. Nice to get rid of the snipers. Listen - if you are going to infiltrate the police station, I'd recommend that you use the subway tunnel.":
        "Sag ol dostum. Keskin nisancilardan kurtulmak harika oldu. Dinle - eger polis karakoluna sizacaksan metro tunelini kullanmani tavsiye ederim.",
    "Wait a minute! We're not going anywhere before our own colors are flying from the flagpole.":
        "Bir dakika bekle! Bayragimiz direkte dalgalanmadan hicbir yere gitmiyoruz.",
    "Take the C4 and get to the Gas Station by accessing the sewers.":
        "C4'u al ve kanalizasyonu kullanarak Benzinlige ulas.",
    "Over here!":
        "Buradayim!",
    "Help me!":
        "Yardim edin!",
    "Please come and rescue me!":
        "Lutfen gelip beni kurtarin!",
    "Thanks. Don't forget the flag.":
        "Tesekkurler. Bayragi unutma.",
    "Good work! This way.":
        "Iyi is! Bu taraftan.",
    "Thank you, follow me.":
        "Tesekkur ederim, beni takip et.",

    # C02RB
    "The Post Office is a Soviet stronghold. It's used as a supply depot to support troops advancing into the city. Your brother is being held somewhere inside. Raise your flag on the roof to signal our victory. To get near the Police Station, you'll have to destroy the sniper's nest on the Gas Station.":
        "Postane bir Sovyet kalesidir. Sehirde ilerleyen birlikleri desteklemek icin ikmal deposu olarak kullaniliyor. Kardesiniz iceride bir yerde tutuluyor. Zaferimizi ilan etmek icin bayraginizi catiya cekin. Polis Karakoluna yaklasmak icin Benzinlikteki keskin nisanci mevzisini yok etmeniz gerekecek.",
    "Secure the Police Station and liberate our leader Isabella. Raise your flag to signal her release. The Police Officers will assist you, but they need your help taking out the snipers on the nearby Gas Station.":
        "Polis Karakolunu guvenceye alin ve liderimiz Isabella'yi kurtarin. Serbest kalisini duyurmak icin bayraginizi cekin. Polis Memurlari size yardim edecek, ancak yakinlardaki Benzinlikteki keskin nisancilari etkisiz hale getirmek icin yardiminiza ihtiyaclari var.",
    "This is our base. It's a safe zone. We store equipment here. With complete control of the sewer system, the tunnels enable us to bypass many of the Soviet roadblocks. All of our maps will indicate the location of the sewer access points.":
        "Burası bizim ussumuz. Guvenli bir bolgedir. Ekipmanlari burada sakliyoruz. Kanalizasyon sisteminin tam kontrolu elimizdeyken, tuneller bircok Sovyet barikatini atlatmamizi sagliyor. Tum haritalarimiz kanalizasyon giris noktalarinin yerini gosterecektir.",
    "Lets go over to the table and take a look at the map.":
        "Masaya gecip haritaya bir goz atalim.",
    "Chris - we need to take the Police Station. This will weaken the Soviets grip on the area.":
        "Chris - Polis Karakolunu almaliyiz. Bu Sovyetlerin bolgedeki hakimiyetini zayiflatacaktir.",
    "I have reports that the Soviets have set up a command center in the Post Office. We must raise our flag on the roof. It will really demoralize their troops and give hope to the people..":
        "Sovyetlerin Postanede bir komuta merkezi kurduguna dair raporlar var. Bayragimizi catiya cekmeliyiz. Bu gercekten onlarin birliklerinin moralini bozacak ve halka umut verecektir..",
    "Chris - we also have reason to believe that your brother is being held captive at the Post Office.":
        "Chris - kardesinizin Postanede esir tutulduguna inanmak icin de nedenlerimiz var.",
    "Once you take their base, it is imperative that you fly the flag from the rooftop. People will see it and start to believe that we can actually win this war! It will prove there are cracks in the Soviet war machine.":
        "Ussu ele gecirdiginizde catida bayragi dalgalandirmaniz sarttir. Insanlar bunu gorecek ve bu savasi gercekten kazanabilecegimize inanmaya baslayacak! Sovyet savas makinesinde catlaklar oldugunu kanitlayacaktir.",
    "Hm - er denne her ikke overfl\xf8dig, hvis Isabella giver selvsamme clue her??? - Morten I.":
        "",
    "Samme besked fra forfatter som vedr. Jones_Flag2A - overfl\xf8dig, ikke? - Morten I.":
        "",
    "Chris - the Republican Army has a sniper positioned up on the fuel station. He's making it impossible for us to move through the area.":
        "Chris - Kizil Ordu benzinlige bir keskin nisanci yerlestirdi. Bolgede hareket etmemizi imkansiz kiliyor.",
    "It's critical that we destroy that fuel station - it'll help starve the Soviet vehicles and take away a roost for that sniper.":
        "O benzinligi yok etmemiz cok onemli - Sovyet araclarinin yakitsiz kalmasina yardimci olacak ve o keskin nisancinin mevzisini ortadan kaldiracaktir.",
    "Listen, Isabella is being held in the Police Station. We need to rescue her. She can stand up to interrogation, but the resistance is weakened without her leadership.":
        "Dinle, Isabella Polis Karakolunda tutuluyor. Onu kurtarmamiz gerek. Sorgulamaya dayanabilir, ancak onun liderligi olmadan direnis zayiflar.",
    "Your brother Troy is being held in the Post Office, I'm sure you'll want to get him out. We can use a man like him fighting in our ranks.":
        "Kardesin Troy Postanede tutuluyor, onu kurtarmak isteyeceginden eminim. Saflarimizda onun gibi savasan bir adama ihtiyacimiz var.",
    "Hvorfor giver Troy den samme clue som Jones - er det for replay value...?-Morten":
        "",
    "Good work up there - people are lining up to help fight. Seeing our flag again really got people mobilized.":
        "Orada iyi is cikardin - insanlar savasmaya yardim etmek icin siraya giriyor. Bayragimizi tekrar gormek insanlari gercekten harekete gecirdi.",
    "Nice job freeing your brother, but you still have some unfinished business - what about our flag? People have to see it or we'll lose credibility.":
        "Kardesini kurtarman harika bir is, ama hala bitmemis bir isin var - ya bayragimiz? Insanlarin onu gormesi gerek yoksa inandiriciligimizi kaybederiz.",
    "I know the boys in that part of town - news travels fast here. They know you freed me and should be willing to follow you - just ask them.":
        "Sehrin o kismindaki cocuklari taniyorum - haberler burada cabuk yayilir. Beni kurtardigini biliyorlar ve senin pesinden gelmeye gonullu olmalilar - sadece onlara sor.",
    "Perfect! That arms cache you found in the Police Station has really improved our odds against the Republican Army.":
        "Harika! Polis Karakolunda buldugun silah deposu, Kizil Ordu'ya karsi sansimizi gercekten artirdi.",
    "Excellent work demolishing the fuel station. We're able to move around at our leisure now that the snipers are gone.":
        "Benzinligi havaya ucurarak mukemmel bir is cikardin. Keskin nisancilar gittigine gore artik rahatca hareket edebiliyoruz.",
    "You rescued Isabella! Bravo!":
        "Isabella'yi kurtardin! Tebrikler!",
    "Good work Chris! The Reds have evacuated this part of the city. We found plenty of medical supplies, so grab a kit - I want you coming back alive bro'..":
        "Iyi is cikardin Chris! Kizillar sehrin bu bolumunu tahliye etti. Bolca tibbi malzeme bulduk, bu yuzden bir canta kap - senin canli donmeni istiyorum kardesim..",
    "Like I said, I owe ya one Chris! The Reds ain't much for hospitality.":
        "Dedigim gibi sana bir can borcum var Chris! Kizillarin misafirperverlik anlayisi pek iyi degil.",
    "GAS STATION": "BENZINLIK",
    "Raise Flag on Post Office.": "Postaneye Bayrak Cek.",
    "Destroy Gas Station.": "Benzinligi Yok Et.",
    "Free your brother Troy.": "Kardesin Troy'u Kurtar.",
    "Raise Flag on Police Station.": "Polis Karakoluna Bayrak Cek.",
    "Free Isabella in the Police Station.": "Polis Karakolundaki Isabella'yi Kurtar.",
    "Free prisoners in the Police Station.": "Polis Karakolundaki Mahkumlari Kurtar.",
    "Gas Station destroyed - Snipers eliminated!": "Benzinlik yok edildi - Keskin nisancilar etkisiz hale getirildi!",
    "Troy freed!": "Troy kurtarildi!",
    "Isabella freed!": "Isabella kurtarildi!",
    "I owe ya one Chris - don't forget about Isabella, I don't think the Reds are playing nice.":
        "Sana bir can borcum var Chris - Isabella'yi unutma, Kizillarin pek nazik davrandigini sanmiyorum.",
    "Raise the flag once you've taken control of the Post Office.":
        "Postanenin kontrolunu ele gecirdikten sonra bayragi cekin.",
    "Take control of the precinct building and raise the flag I gave you.":
        "Karakol binasinin kontrolunu ele gecirin ve size verdigim bayragi cekin."
}

CH1_CH2_TRANSLATIONS = {
    orig: to_ascii_turkish(trans)
    for orig, trans in CH1_CH2_RAW.items()
}

if __name__ == '__main__':
    total = 0
    missing = []
    for grp in ['C01A', 'C02A', 'C02B', 'C02RB']:
        path = rf'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_work\group_{grp}.json'
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        total += len(data)
        for k, v in data.items():
            if v not in CH1_CH2_TRANSLATIONS:
                missing.append((grp, k, v))
    print(f"Coverage: {total - len(missing)} / {total}")
    if missing:
        print("Missing:")
        for grp, k, v in missing:
            print(f"  [{grp}] {k}: {repr(v)}")
