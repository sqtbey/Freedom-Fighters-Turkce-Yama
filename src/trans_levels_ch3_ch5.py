# -*- coding: utf-8 -*-
import json, sys
sys.path.append(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline')
from turkish_ascii_converter import to_ascii_turkish

# Translation dictionary for Chapters 3, 4, 5
CH3_CH5_RAW = {
    # C03A
    "Yo man, blowing up that bridge will stop the Reds from steppin' out into the other neighborhoods. But remember, you'll need some serious TNT if you are gonna do it right.":
        "Hey ahbap, o kopruyu havaya ucurmak Kizillarin diger mahallelere gecmesini engeller. Ama unutma, bunu dogru durust yapmak icin saglam bir TNT'ye ihtiyacin olacak.",
    "Phew! Thank you young man! Looks like you mean business - keep your eyes peeled - I saw lot's of Red soldiers down by the water guarding some landing pad.":
        "Oh be! Tesekkurler genc adam! Ciddi gorunuyorsun - gozlerini dort ac - su kenarinda inis pistini koruyan bir suru Kizil asker gordum.",

    # C03B
    "Seems like the best way to down those choppers is to take out their landing pad. You can get there through one of those old buildings over there.":
        "O helikopterleri dusurmenin en iyi yolu inis pistlerini yok etmek gibi gorunuyor. Oraya suradaki eski binalardan birinin icinden ulasabilirsin.",
    "Thanks for helping out an old timer like me! If I were younger I'd tag along with you. You Resistance boys might wanna know that the Reds have been moving plenty of trucks across that bridge. The one near the tracks.":
        "Benim gibi yasli birine yardim ettigin icin sag ol! Daha genc olsaydim pesine takilirdim. Siz Direnis cocuklari, Kizillarin su kopruden bir suru kamyon gecirdigini bilmek isteyebilirsiniz. Raylarin yakinindakinden.",

    # C03C
    "Hey yo boss - there's some serious dynamite in the Diner - you look like you could use some.":
        "Hey patron - Lokantada saglam dinamit var - birazina ihtiyacin var gibi duruyor.",
    "Thanks Doc! I owe ya one - There are a lot of Rooskies around. Better steer clear of that helipad near the Harbor.":
        "Sag ol Doktor! Sana borclandim - Etrafta cok Rus var. Limanin yakinindaki o helikopter pistinden uzak dursan iyi edersin.",

    # C03RB
    "Capture the old Fire Station. Soviet reinforcements in this section are coordinated from here. Then destroy the remaning bridge. It makes an important supply route for the Soviets - take it out and the influx of troops to surrounding areas will greatly diminish.":
        "Eski Itfaiye Merkezini ele gecirin. Bu bolgedeki Sovyet takviyeleri buradan koordine ediliyor. Ardindan kalan kopruyu havaya ucurun. Sovyetler icin onemli bir ikmal yolu - onu yok ederseniz cevre bolgelere asker akisi buyuk olcude azalacaktir.",
    "Seize the warehouse buildings. This is where the Soviets store their small arms and artillery that they unload from the ships \x96 taking these buildings will greatly reduce enemy firepower. Blow up the helicopter fueling station here as well. This will ground the Soviet chopper fleet.":
        "Depo binalarini ele gecirin. Sovyetlerin gemilerden indirdikleri hafif silahlari ve muhimmati depoladiklari yer burasidir - bu binalari almak dusmanin ates gucunu buyuk olcude azaltacaktir. Buradaki helikopter yakit istasyonunu da havaya ucurun. Bu durum Sovyet helikopter filosunu yere cakacaktir.",
    "Seize the warehouse buildings. This is where the Soviets store their small arms and artillery that they unload from the ships \u2013 taking these buildings will greatly reduce enemy firepower. Blow up the helicopter fueling station here as well. This will ground the Soviet chopper fleet.":
        "Depo binalarini ele gecirin. Sovyetlerin gemilerden indirdikleri hafif silahlari ve muhimmati depoladiklari yer burasidir - bu binalari almak dusmanin ates gucunu buyuk olcude azaltacaktir. Buradaki helikopter yakit istasyonunu da havaya ucurun. Bu durum Sovyet helikopter filosunu yere cakacaktir.",
    "Seize the warehouse buildings. This is where the Soviets store the small arms and artillery that they unloaded from the ships \x96 taking these buildings will greatly reduce enemy firepower. Blow up the helicopter fuelling station here as well. This will ground the Soviet chopper fleet.":
        "Depo binalarini ele gecirin. Sovyetlerin gemilerden indirdikleri hafif silahlari ve muhimmati depoladiklari yer burasidir - bu binalari almak dusmanin ates gucunu buyuk olcude azaltacaktir. Buradaki helikopter yakit istasyonunu da havaya ucurun. Bu durum Sovyet helikopter filosunu yere cakacaktir.",
    "Seize the warehouse buildings. This is where the Soviets store the small arms and artillery that they unloaded from the ships \u2013 taking these buildings will greatly reduce enemy firepower. Blow up the helicopter fuelling station here as well. This will ground the Soviet chopper fleet.":
        "Depo binalarini ele gecirin. Sovyetlerin gemilerden indirdikleri hafif silahlari ve muhimmati depoladiklari yer burasidir - bu binalari almak dusmanin ates gucunu buyuk olcude azaltacaktir. Buradaki helikopter yakit istasyonunu da havaya ucurun. Bu durum Sovyet helikopter filosunu yere cakacaktir.",
    "Take control of the old Hotel. The Soviets have established a base of operations inside. We have seen Soviet soldiers storing ammunition in an abandoned diner. You can stock up on explosives here. There is a POW camp in the area - release the prisoners and lead them to the sewers.":
        "Eski Otelin kontrolunu ele gecirin. Sovyetler iceride bir operasyon ussu kurdular. Sovyet askerlerinin terk edilmis bir lokantada muhimmat depoladigini gorduk. Buradan patlayici tedarik edebilirsiniz. Bolgede bir esir kampi var - mahkumlari serbest birakin ve onlari kanalizasyona yonlendirin.",
    "Chris, for three months the Soviets have been pouring soldiers and equipment into the city. We have to plan every move very carefully. The people need to see that there is hope\x96 If we stumble now, that'll be lost.":
        "Chris, uc aydir Sovyetler sehre asker ve techizat yigiyor. Her adimi cok dikkatli planlamaliyiz. Insanlarin umut oldugunu gormesi gerek... Simdi tokezlersek bu umut kaybolur.",
    "Chris, for three months the Soviets have been pouring soldiers and equipment into the city. We have to plan every move very carefully. The people need to see that there is hope… If we stumble now, that'll be lost.":
        "Chris, uc aydir Sovyetler sehre asker ve techizat yigiyor. Her adimi cok dikkatli planlamaliyiz. Insanlarin umut oldugunu gormesi gerek... Simdi tokezlersek bu umut kaybolur.",
    "Yeah man, the Reds are everywhere and they brought plenty of toys. Yesterday our boys tried to blow a bridge on their supply route. Only today, Red trucks are rolling back-and-forth like nothing happened. I tell ya, if I demo'ed that bridge, there'd be nothing left to put back together. Instead, they got more soldiers than ever sittin' on it. Gimme some TNT and I'll blow that baby - or die trying.":
        "Aynen dostum, Kizillar her yerde ve bir suru oyuncak getirdiler. Dun bizim cocuklar ikmal yollarindaki bir kopruyu havaya ucurmaya calisti. Ama bugun Kizil kamyonlar hicbir sey olmamis gibi vira vira geciyor. Sana diyeyim, o kopruyu ben havaya ucursaydim birlestirecek parca kalmazdi. Onun yerine simdi ustunde her zamankinden cok asker var. Bana biraz TNT verin o bebegi havaya ucurayim - ya da denerken oleyim.",
    "Hang on, let's get real. That bridge is important, but we really need to capture the command center too. The Soviets deploy their troops from the old Fire Station. We need to take control back.":
        "Dur bakalim, gercekci olalim. O kopru onemli ama komuta merkezini de mutlaka ele gecirmeliyiz. Sovyetler birliklerini eski Itfaiye Merkezinden sevk ediyor. Kontrolu geri almaliyiz.",
    "Hey, don't expect to crash their party and say \"hasta la vista\" to everyone in a red beret. They got snipers and choppers up there\x96 this ain't no Kiddie Park.":
        "Hey, partilerini basip kizil bereli herkese \"hasta la vista\" demeyi bekleme. Yukarida keskin nisancilari ve helikopterleri var... burasi cocuk parki degil.",
    "Hey, don't expect to crash their party and say \"hasta la vista\" to everyone in a red beret. They got snipers and choppers up there… this ain't no Kiddie Park.":
        "Hey, partilerini basip kizil bereli herkese \"hasta la vista\" demeyi bekleme. Yukarida keskin nisancilari ve helikopterleri var... burasi cocuk parki degil.",
    "Chris, before you go, Troy wants a word with you. Be careful up there, remember retreat to the sewers if things get too hot. I'll be waiting for you.":
        "Chris, gitmeden once Troy seninle konusmak istiyor. Yukarida dikkatli ol, ortalik cok kizarirsa kanalizasyona cekilmeyi unutma. Seni bekliyor olacagim.",
    "Hey Chris, I've been thinking\x96 there's gotta be other Freedom Fighters outside Manhattan. I'm gonna find 'em and gonna tell 'em what we've got going here. Who knows, maybe we can scratch together some sorta national resistance movement.":
        "Hey Chris, dusunuyordum da... Manhattan disinda da baska Ozgurluk Savascilari olmali. Onlari bulacagim ve burada basardiklarimizi anlatacagim. Kim bilir, belki de bir tur ulusal direnis hareketi baslatabiliriz.",
    "Hey Chris, I've been thinking… there's gotta be other Freedom Fighters outside Manhattan. I'm gonna find 'em and gonna tell 'em what we've got going here. Who knows, maybe we can scratch together some sorta national resistance movement.":
        "Hey Chris, dusunuyordum da... Manhattan disinda da baska Ozgurluk Savascilari olmali. Onlari bulacagim ve burada basardiklarimizi anlatacagim. Kim bilir, belki de bir tur ulusal direnis hareketi baslatabiliriz.",
    "Listen up, man - you're gonna need some serious firecrackers to take out the bridges. Now there's some C4 stashed in the Diner, ya know - but get plenty, ya never know when you'll need it.":
        "Dinle dostum - kopruleri yok etmek icin saglam patlayicilara ihtiyacin olacak. Lokantada saklanmis biraz C4 var biliyorsun - ama bolca al, ne zaman gerekecegi hic belli olmaz.",
    "Dude, I'm tellin' ya, kid, those choppers are a pain in the you-know-what... WHAAAT?!! They've got some major hardware in those babies. We just gotta figure out where they resupply and blow the place - it's up to you man!":
        "Dostum, sana diyorum, su helikopterler bas belasi... NEE?!! O bebeklerde agir muhimmat var. Nereden yakit aldiklarini bulup orayi havaya ucurmaliyiz - sana bagli ahbap!",
    "Chris - We have to find a way to ground those helicopters. They're really hurting us out there. We did get some small arms from the Police Station, but they're not enough against bridges and helicopters. The Soviets have to have something that will do the job - something with power that we can turn against them!":
        "Chris - O helikopterleri yere indirmenin bir yolunu bulmaliyiz. Disarida bize buyuk zarar veriyorlar. Polis Karakolundan bazi hafif silahlar aldik ama koprulere ve helikopterlere karsi yetersizler. Sovyetlerin elinde bu isi gorecek bir seyler olmali - onlara karsi kullanabilecegimiz guclu bir sey!",
    "Although the bridge is a key target, the Fire Station is a rally point for Soviet reinforcements. Raise our flag on the roof.":
        "Kopru kilit bir hedef olsa da Itfaiye Merkezi Sovyet takviyeleri icin bir toplanma noktasidir. Bayragimizi catiya cekin.",
    "The Soviets are holding prisoners somewhere near the Hotel - we need to free our brothers.":
        "Sovyetler Otelin yakinlarinda bir yerde esir tutuyor - kardeslerimizi kurtarmamiz gerek.",
    "Oh yeah! We're talkin' one sweet fireworks show when we lay som'a that C4 on a bridge.":
        "Iste bu! O C4'lerden birini kopruye yerlestirdigimizde muhtesem bir havai fisek gosterisi olacak.",
    "Nice work Chris! I heard ya took out the bridge. Personally, I woulda gone for more of a bang, but hey that's just my style.":
        "Iyi is Chris! Kopruyu havaya ucurdugunu duydum. Sahsen ben daha buyuk bir patlama yapardim ama hey, benim tarzim bu.",
    "It's now or never Chris - with the Fire Station under our control, we have a small edge. . . for the moment. People are seeing the Stars-and-Stripes and are joining our cause. They even led us to cache of Soviet SMG's. Take one for your next mission.":
        "Ya simdi ya hic Chris - Itfaiye Merkezi kontrolumuz altindayken kucuk bir ustunlugumuz var... simdilik. Insanlar bayragimizi goruyor ve davamiza katiliyor. Hatta bizi bir Sovyet makineli tufek zulasina goturduler. Bir sonraki gorevin icin bir tane al.",
    "Blowing up that Fuel Station really weakened the enemy - we should have an easier time in this area.":
        "O Yakit Istasyonunu havaya ucurmak dusmani gercekten zayiflatti - bu bolgede isimiz daha kolay olmali.",
    "Great job! We control the Hotel now! Even better, we found the huge munitions depot inside!":
        "Harika is! Artik Oteli biz kontrol ediyoruz! Daha da iyisi, iceride devasa bir muhimmat deposu bulduk!",
    "Grounding those helicopters strengthened our grip on the area!":
        "O helikopterleri yere indirmek bolgedeki hakimiyetimizi guclendirdi!",
    "Risking yourself and releasing the prisoners has really paid off - you've earned their respect and many have joined our ranks.":
        "Kendini tehlikeye atip mahkumlari kurtarman gercekten ise yaradi - onlarin saygisini kazandin ve bircogu saflarimiza katildi.",
    "BRIDGE": "KOPRU",
    "WAREHOUSE BUILDINGS": "DEPO BINASI",
    "Destroy bridge.": "Kopruyu yok et.",
    "Raise flag on Fire Station.": "Itfaiye Merkezine bayrak cek.",
    "Raise flag on Fuel Station.": "Yakit Istasyonuna bayrak cek.",
    "Locate C4.": "C4 Patlayiciyi bul.",
    "Raise Flag on Hotel.": "Otele Bayrak Cek.",
    "Bridge destroyed!": "Kopru yok edildi!",
    "C4 found!": "C4 bulundu!",

    # C04C, C04D
    "Got any C4? I'd use it on that bridge over there.":
        "Hic C4'un var mi? Suradaki koprude kullanirdim.",
    "Stay out of sight sonny or them Rooskies will spot you for sure.":
        "Gozden uzak dur evlat, yoksa su Ruslar seni kesin fark eder.",
    "The Soviet soldiers took my son! He did nothing! They're holding a whole group of people down at the Harbor - this is horrible! Please help - I want my son back.":
        "Sovyet askerleri oglumu goturdu! Hicbir sey yapmamisti! Limanda butun bir insan grubunu tutuyorlar - bu cok korkunc! Lutfen yardim edin - oglumu geri istiyorum.",
    "Ain't no way you're gonna blow that Power Plant. Taking out the power lines in the back'll do the trick.":
        "O Elektrik Santralini havaya ucurmana imkan yok. Arkadaki elektrik hatlarini yok etmek isini gorur.",

    # C04RB
    "Flag raised - Area secured!": "Bayrak cekildi - Bolge guvenceye alindi!",
    "Destroy Helipad.": "Helikopter Pistini Yok Et.",
    "Free Prisoners.": "Mahkumlari Kurtar.",
    "Secure the Movie Theater. Soviets are using it to temporarily house prisoners before sending them to Alaskan labor camps. You'll want to eliminate the chopper service pad, it will bring down the number of units protecting the Power Station.":
        "Sinemayi guvenceye alin. Sovyetler burayi mahkumlari Alaska calisma kamplarina gondermeden once gecici olarak tutmak icin kullaniyor. Helikopter servis pistini ortadan kaldirmak isteyeceksiniz, bu durum Elektrik Santralini koruyan birlik sayisini azaltacaktir.",
    "Secure the Movie Theater. Soviets are using it to temporarily house prisoners before sending them to Alaskan labour camps. You'll want to eliminate the chopper service pad, it will bring down the number of units protecting the Power Station.":
        "Sinemayi guvenceye alin. Sovyetler burayi mahkumlari Alaska calisma kamplarina gondermeden once gecici olarak tutmak icin kullaniyor. Helikopter servis pistini ortadan kaldirmak isteyeceksiniz, bu durum Elektrik Santralini koruyan birlik sayisini azaltacaktir.",
    "Bring down the bridges - we need to choke off the reinforcements and equipment being transported from the warehouses out to the surrounding areas. Some elite Soviet forces have their HQ located here, so it's heavily guarded. Hoist our flag over it. It'll be a tremendous boost to our fighters\x92 morale.":
        "Kopruleri yikin - depolardan cevre bolgelere tasinan takviye kuvvetleri ve techizati engellememiz gerekiyor. Bazi seckin Sovyet birliklerinin karargahi burada, bu yuzden cok siki korunuyor. Uzerine bayragimizi cekin. Savascilarimizin moraline buyuk bir guc katacaktir.",
    "Bring down the bridges - we need to choke off the reinforcements and equipment being transported from the warehouses out to the surrounding areas. Some elite Soviet forces have their HQ located here, so it's heavily guarded. Hoist our flag over it. It'll be a tremendous boost to our fighters’ morale.":
        "Kopruleri yikin - depolardan cevre bolgelere tasinan takviye kuvvetleri ve techizati engellememiz gerekiyor. Bazi seckin Sovyet birliklerinin karargahi burada, bu yuzden cok siki korunuyor. Uzerine bayragimizi cekin. Savascilarimizin moraline buyuk bir guc katacaktir.",
    "Take out the Power Station on the Manhattan side of the water. Power lines run parallel with the bridge and into the adjoining areas, supplying power to most of downtown. Destroying the power lines will kill the floodlights in the docking area, making it easier to infiltrate.":
        "Suyun Manhattan tarafindaki Elektrik Santralini devre disi birakin. Elektrik hatlari kopruye paralel uzanarak komsu bolgelere gider ve sehir merkezinin buyuk kismina elektrik saglar. Elektrik hatlarini yok etmek liman bolgesindeki projektorleri sonurecek ve sizmayi kolaylastiracaktir.",
    "Sometimes I wonder how Mr. Jones gets all his information.":
        "Bazen Bay Jones'un tum bu bilgileri nasil aldigini merak ediyorum.",
    "Beats me - he sure is connected though. We'd be nowhere without him.":
        "Hic fikrim yok - ama saglam baglantilari var. O olmasa bir hic olurduk.",
    "Hmm, what did he do before the war?":
        "Hmm, savastan once ne yapiyordu acaba?",
    "Probably worked on Wall Street or something - I think Chris and him go way back\x96":
        "Muhtemelen Wall Street'te falan calisiyordu - sanirim Chris ile eskiye dayanan bir tanisikliklari var...",
    "Probably worked on Wall Street or something - I think Chris and him go way back…":
        "Muhtemelen Wall Street'te falan calisiyordu - sanirim Chris ile eskiye dayanan bir tanisikliklari var...",
    "Oh, there you are. Good work handling that Soviet stronghold\x96 very inspired. We've really stirred them up this time; they've added plenty of reinforcements. We'll need to start operating at night, so stick to the shadows and avoid their floodlights. There are three areas to deal with here: The Soviets are unloading BTR\x92s at the docks. That\x92ll be our first target. Next is the Power Plant \x96 some of our fighters tried to take it last night, but were caught. We think they are being held somewhere close by. Last is the Movie Theater - it's a bit of a mystery to us, but a lot of troops are moving in and out of the area so we need to take action. This will be a tough assignment Chris - we know you can handle it.":
        "Ah, iste buradasin. O Sovyet kalesini halletmen cok iyi oldu... cok ilham vericiydi. Bu sefer onlari gercekten kizdirdik; bolca takviye getirdiler. Artik geceleri operasyon yapmamiz gerekecek, bu yuzden golgelerde kal ve projektorlerinden kacin. Burada ilgilenilmesi gereken uc bolge var: Sovyetler limana zirhli araclar indiriyor. Ilk hedefimiz bu olacak. Siradaki Elektrik Santrali - dun gece savascilarimizdan bazilari orayi almaya calisti ama yakalandilar. Yakinlarda bir yerde tutulduklarini dusunuyoruz. Sonuncusu ise Sinema - bizim icin biraz gizemli ama bolgeye cok sayida asker girip cikiyor, bu yuzden harekete gecmeliyiz. Bu zor bir gorev olacak Chris - ustesinden gelebilecegini biliyoruz.",
    "Oh, there you are. Good work handling that Soviet stronghold… very inspired. We've really stirred them up this time; they've added plenty of reinforcements. We'll need to start operating at night, so stick to the shadows and avoid their floodlights. There are three areas to deal with here: The Soviets are unloading BTR’s at the docks. That’ll be our first target. Next is the Power Plant – some of our fighters tried to take it last night, but were caught. We think they are being held somewhere close by. Last is the Movie Theater - it's a bit of a mystery to us, but a lot of troops are moving in and out of the area so we need to take action. This will be a tough assignment Chris - we know you can handle it.":
        "Ah, iste buradasin. O Sovyet kalesini halletmen cok iyi oldu... cok ilham vericiydi. Bu sefer onlari gercekten kizdirdik; bolca takviye getirdiler. Artik geceleri operasyon yapmamiz gerekecek, bu yuzden golgelerde kal ve projektorlerinden kacin. Burada ilgilenilmesi gereken uc bolge var: Sovyetler limana zirhli araclar indiriyor. Ilk hedefimiz bu olacak. Siradaki Elektrik Santrali - dun gece savascilarimizdan bazilari orayi almaya calisti ama yakalandilar. Yakinlarda bir yerde tutulduklarini dusunuyoruz. Sonuncusu ise Sinema - bizim icin biraz gizemli ama bolgeye cok sayida asker girip cikiyor, bu yuzden harekete gecmeliyiz. Bu zor bir gorev olacak Chris - ustesinden gelebilecegini biliyoruz.",
    "You know - that Soviet compound by the cinema would be a nice addition to our fine line of downtown real estate. . . know what I mean?":
        "Bilirsin ya - sinemanin yanindaki o Sovyet yerleskesi, sehir merkezindeki guzel emlak koleksiyonumuza hos bir ekleme olurdu... ne demek istedigimi anladin mi?",
    "Chris, my man - Ivan's got that main base in the central warehouse - it's up for grabs, if you hurry - snooze and you lose!":
        "Chris, aslanim - Ivan'in ana ussu merkez depoda - acele edersen kapabilirsin, uyursan kaybedersin!",
    "The Reds are sittin' pretty by the Power Station - let's see if they're afraid of the dark!":
        "Kizillar Elektrik Santralinde keyif catıyor - bakalim karanliktan korkuyorlar mi!",
    "They're in control of the Power Station - we gotta cut off the juice.":
        "Elektrik Santralinin kontrolu onlarda - elektrigi kesmemiz gerek.",
    "It's going to be hard to maneuver  with all of the helicopters buzzing around - we believe that the helipad is near the parking garage. Your best bet might be to sneak in. Attacking the Sovets head on would be risky.":
        "Etrafta vizir vizir helikopterler varken manevra yapmak zor olacak - helikopter pistinin otoparkin yakininda olduguna inaniyoruz. En iyi sansin gizlice sizmak olabilir. Sovyetlere dogrudan saldirmak riskli olacaktir.",
    "I think the best course of action would be to take out both bridges. That would isolate the troops here and prevent reinforcement.":
        "Bence en iyi hareket tarzi her iki kopruyu de havaya ucurmak olacaktir. Bu durum buradaki birlikleri izole eder ve takviye almalarini engeller.",
    "Blowing up those helipads would really take the sting out of their arsenal - you can do it Chris!":
        "O helikopter pistlerini havaya ucurmak cephaneliklerindeki zehri gercekten sokup alir - bunu yapabilirsin Chris!",
    "If you really want to be a hero you should try and liberate the prisoners being held near the Harbor.":
        "Eger gercekten bir kahraman olmak istiyorsan Limanin yakininda tutulan mahkumlari kurtarmayi denemelisin.",
    "Good! With the bridges down, the Soviets will have to divert their troops elsewhere.":
        "Guzel! Kopruler yikildiginda Sovyetler birliklerini baska yerlere yonlendirmek zorunda kalacak.",
    "Sounds like the Theater was a hard fight - you came through Chris. Good work!":
        "Sinema zorlu bir mucadele olmus gibi gorunuyor - ustesinden geldin Chris. Iyi is!",
    "Excellent! Controlling the Warehouse puts us in a good position.":
        "Mukemmel! Depoyu kontrol etmek bizi cok iyi bir konuma getirdi.",
    "Now that we control the power supply here, we are really in charge!":
        "Artik buradaki elektrik kaynagini kontrol ettigimize gore ipler gercekten bizim elimizde!",
    "Great! The grid is out. They're in the dark now.":
        "Harika! Sebeke coktu. Artik karanliktalar.",
    "WEST BRIDGE": "BATI KOPRUSU",
    "EAST BRIDGE": "DOGU KOPRUSU",
    "WAREHOUSE": "DEPO",
    "POWER STATION": "ELEKTRIK SANTRALI",
    "TRANSFORMER TOWER": "TRAFO KULESI",
    "Raise Flag on Movie Theater.": "Sinemaya Bayrak Cek.",
    "Destroy West Bridge.": "Bati Koprusunu Yok Et.",
    "Destroy East Bridge.": "Dogu Koprusunu Yok Et.",
    "Raise Flag on Warehouse.": "Depoya Bayrak Cek.",
    "Raise Flag on Power Station.": "Elektrik Santraline Bayrak Cek.",
    "Destroy Transformer Tower.": "Trafo Kulesini Yok Et.",
    "West Bridge destroyed!": "Bati Koprusu yok edildi!",
    "East Bridge destroyed!": "Dogu Koprusu yok edildi!",
    "Transformer Tower destroyed!": "Trafo Kulesi yok edildi!",

    # C05A
    "We are under attack - all personnel to battle stations - our brave leader has been killed. Secure all areas - the enemy has infiltrated our camp - find the intruders - those who kill the Rebels will be declared heroes of the Soviet Union - this is not a drill - avenge the death of our beloved General.":
        "Saldiri altindayiz - tum personel savas mevzilerine - cesur liderimiz olduruldu. Tum bolgeleri guvenceye alin - dusman kampimiza sizdi - davetsiz misafirleri bulun - Asileri oldurenler Sovyetler Birligi kahramani ilan edilecektir - bu bir tatbikat degildir - sevgili Generalimizin intikamini alin.",

    # C05RB
    "You must assassinate Tatarin. Without his leadership the Soviet Armed Forces will crumble. This is no easy task and demands stealth if you are to succeed. Bide your time and find a good sniping position - it is the key to your success.":
        "Tatarin'e suikast duzenlemelisiniz. Onun liderligi olmadan Sovyet Silahli Kuvvetleri cokecektir. Bu kolay bir is degildir ve basarili olmak icin gizlilik gerektirir. Zamaninizi kollayin ve iyi bir keskin nisanci mevzisi bulun - basarinizin anahtari budur.",
    "Excellent work! Your handling of the Command Center was very effective at quelling further advances by the Soviets. Well done indeed!":
        "Mukemmel is! Komuta Merkezini halletmeniz Sovyetlerin daha fazla ilerlemesini bastirmada cok etkili oldu. Gercekten tebrikler!",
    "Yeah, well it's not all good news Jones - tell him, tell him what happened. We're seriously hurtin' here\x96":
        "Evet, sey... tum haberler iyi degil Jones - ona soyle, ne oldugunu soyle. Burada canimiz gercekten cok yaniyor...",
    "Yeah, well it's not all good news Jones - tell him, tell him what happened. We're seriously hurtin' here…":
        "Evet, sey... tum haberler iyi degil Jones - ona soyle, ne oldugunu soyle. Burada canimiz gercekten cok yaniyor...",
    "I'm sorry to have to tell you Chris, but your brother is dead. Shortly after he appeared on television he was taken to Governor's Island. We understand that he was executed personally by General Tatarin. It is said that he died like a man, without a flinch or tear. I know it is painful, but you can be proud of him.":
        "Bunu sana soylemek zorunda kaldigim icin uzgunum Chris, ama kardesin oldu. Televizyonda gorundukten kisa sure sonra Governor's Island'a goturuldu. General Tatarin tarafindan bizzat idam edildigini ogrendik. Bir erkek gibi, gozunu bile kirpmadan ve gozyasi dokmeden oldugu soyleniyor. Aci verici oldugunu biliyorum ama onunla gurur duyabilirsin.",
    "Man, I can't take this! Tatarin's gonna pay for killin' Troy! He's gonna regret he ever stepped foot in New York! I say we hit 'em with everything we've got and\x96":
        "Dostum buna dayanamiyorum! Tatarin Troy'u oldurdugu icin bedelini odeyecek! New York'a ayak bastigina pisman olacak! Bence elimizdeki her seyle onlara vuralim ve...",
    "Man, I can't take this! Tatarin's gonna pay for killin' Troy! He's gonna regret he ever stepped foot in New York! I say we hit 'em with everything we've got and…":
        "Dostum buna dayanamiyorum! Tatarin Troy'u oldurdugu icin bedelini odeyecek! New York'a ayak bastigina pisman olacak! Bence elimizdeki her seyle onlara vuralim ve...",
    "Bagz! - Chris, I'm sorry. I know it hurts, but we need to keep a cool head. We don\x92t want to do anything irrational. Yet, I have a strange feeling about this.":
        "Bagz! - Chris, cok uzgunum. Caninin yandigini biliyorum ama sakin kalmaliyiz. Mantiksizca bir sey yapmak istemeyiz. Yine de bu konuda icimde garip bir his var.",
    "Bagz! - Chris, I'm sorry. I know it hurts, but we need to keep a cool head. We don’t want to do anything irrational. Yet, I have a strange feeling about this.":
        "Bagz! - Chris, cok uzgunum. Caninin yandigini biliyorum ama sakin kalmaliyiz. Mantiksizca bir sey yapmak istemeyiz. Yine de bu konuda icimde garip bir his var.",
    "Yes, well\x96 you must understand that the only action now that will truly hurt the Soviet agenda is to assassinate Tatarin. Eliminating him will spread chaos in the Soviet ranks and give way to a united American resistance.":
        "Evet, sey... anlamalisiniz ki artik Sovyet planlarina gercekten darbe vuracak tek eylem Tatarin'e suikast duzenlemektir. Onu ortadan kaldirmak Sovyet saflarina kaos yayacak ve birlesik bir Amerikan direnisi yaratacaktir.",
    "Yes, well… you must understand that the only action now that will truly hurt the Soviet agenda is to assassinate Tatarin. Eliminating him will spread chaos in the Soviet ranks and give way to a united American resistance.":
        "Evet, sey... anlamalisiniz ki artik Sovyet planlarina gercekten darbe vuracak tek eylem Tatarin'e suikast duzenlemektir. Onu ortadan kaldirmak Sovyet saflarina kaos yayacak ve birlesik bir Amerikan direnisi yaratacaktir.",
    "That's a brilliant plan Jones! Wadda we do? Invite ourselves over for a cocktail, then slip some cyanide in his vodka? We're gonna need some serious firepower to take him down, that guy's got his eye on every rat and cockroach on the island.":
        "Harika bir plan Jones! Ne yapacagiz? Kendimizi kokteyle davet ettirip votkasina siyanur mu atacagiz? Onu indirmek icin ciddi bir ates gucune ihtiyacimiz olacak, o adam adadaki her siçani ve hamamboceğini izliyor.",
    "Jones might be right. If we did manage to remove Tatarin, it could be the turning point for our cause. Let's double-check our intelligence, there has to be a way to get to him.":
        "Jones hakli olabilir. Eger Tatarin'i ortadan kaldirmayi basarirsak davamiz icin bir donum noktasi olabilir. Istihbaratimizi tekrar kontrol edelim, ona ulasmanin bir yolu olmali.",
    "After yesterday's hit on their installations they'll be expecting company. This will need to be a surgical strike. We can't risk sending in a squad. . . I'm afraid this is a solo operation.":
        "Tesislerine dunku saldirimizdan sonra misafir bekleyeceklerdir. Bunun cerrahi bir operasyon olmasi gerekecek. Bir tim gonderme riskini goze alamayiz... Korkarim ki bu tek kisilik bir operasyon.",
    ". . . or a two man operation. I know this is personal Chris, and that's cool kid, but if you need me, I'm with you all the way Buddy. Bring on Tatarin and his boys, I've got plenty of bullets for 'em.":
        "... ya da iki kisilik bir operasyon. Bunun kisisel oldugunu biliyorum Chris, ve bu cok dogal evlat, ama bana ihtiyacin olursa sonuna kadar seninleyim dostum. Tatarin ve adamlarini karsima cikarin, onlar icin bolca mermim var.",
    "I quite agree with Isabella, this mission calls for stealth, not ham-handed bravado. There's a sniper rifle in the weapons gallery. Chris, I'll arrange for a rowboat to the island.":
        "Isabella'ya kesinlikle katiliyorum, bu gorev kaba kuvvete degil gizlilige dayaniyor. Silah galerisinde bir keskin nisanci tufegi var. Chris, adaya gitmen icin bir kayik ayarlayacagim.",
    "It's all up to you Chris! We heard that Tatarin is usually in his office working late. That might be your best shot.":
        "Her sey sana bagli Chris! Tatarin'in genellikle ofisinde gec saatlere kadar calistigini duyduk. En iyi firsatin bu olabilir.",
    "I believe that the only shot you'll have on Tatarin is from the harbor towers. Be alert, they'll be plenty of soldiers.":
        "Tatarin'e tek atis sansinin liman kulelerinden olacagina inaniyorum. Dikkatli ol, etrafta cok sayida asker olacaktir.",
    "Chris - only you can sneak into their base. Taking out Tatarin is risky, but it's the only chance we've got to turn the tide in our favor.":
        "Chris - onlarin ussune sadece sen sizabilirsin. Tatarin'i ortadan kaldirmak riskli ama gidisati lehimize cevirmek icin tek sansimiz bu.",
    "TATARIN": "TATARIN",
    "Kill Tatarin.": "Tatarin'i Oldur.",
    "Tatarin killed!": "Tatarin olduruldu!"
}

CH3_CH5_TRANSLATIONS = {
    orig: to_ascii_turkish(trans)
    for orig, trans in CH3_CH5_RAW.items()
}

if __name__ == '__main__':
    total = 0
    missing = []
    groups = ['C03A', 'C03B', 'C03C', 'C03RB', 'C04C', 'C04D', 'C04RB', 'C05A', 'C05RB']
    for grp in groups:
        path = rf'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_work\group_{grp}.json'
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        total += len(data)
        for k, v in data.items():
            if v not in CH3_CH5_TRANSLATIONS:
                missing.append((grp, k, v))
    print(f"Coverage: {total - len(missing)} / {total}")
    if missing:
        print("Missing:")
        for grp, k, v in missing:
            print(f"  [{grp}] {k}: {repr(v)}")
