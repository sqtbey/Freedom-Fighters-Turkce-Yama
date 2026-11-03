# -*- coding: utf-8 -*-
import json, sys
sys.path.append(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline')
from turkish_ascii_converter import to_ascii_turkish

# Translation dictionary for Chapters 6, 7, 8
CH6_CH8_RAW = {
    # C06A
    "Ha-ha-ha - Remember me Chris! Yes - I know your name. Perhaps this is more familiar \"Hello Christopher!\" You see, I've resumed my original profession. You never questioned where all that juicy information was coming from. That's what I love about the Americans - one finger up the nose and the other on the remote control. You were all so busy entertaining yourselves to death while our great nation was busy - busy liberating Europe from the same fate. Our horizon grew while yours has faded out!":
        "Ha-ha-ha - Beni hatirladin mi Chris! Evet - adini biliyorum. Belki su daha tanidiktir: \"Merhaba Christopher!\" Goruyorsun ya, asil meslegime geri dondum. O balli bilgilerin nereden geldigini hic sorgulamadin. Amerikalilarin en sevdigim yani bu iste - bir parmagi burnunda, digeri uzaktan kumandada. Buyuk ulkemiz Avrupa'yi ayni kaderden kurtarmakla mesgulken, siz olumune eglenmekle mesguldunuz. Bizim ufkumuz genislerken sizinki silinip gitti!",
    "Chris - stop this foolishness! We know you are here - it is only a matter of time before we find you. Show yourself and we will be gentle with you.":
        "Chris - bu sacmaliga son ver! Burada oldugunu biliyoruz - seni bulmamiz an meselesi. Kendini goster, sana karsi nazik olacagiz.",
    "Where are your precious Freedom Fighters Christopher? You're all alone - surrender now and we'll leave you your dignity.":
        "O cok kiymetli Ozgurluk Savascilarin nerede Christopher? Yapayalnizsin - simdi teslim ol, sana haysiyetini birakalim.",
    "Do not make me angry Christopher! I have tried to reason with you - do not try my patience further!":
        "Beni kizdirma Christopher! Seninle mantikli konusmaya calistim - sabrimi daha fazla zorlama!",
    "I don't wish any further bloodshed in this matter. We have won Chris - you must see that - your cause has ended.":
        "Bu meselede daha fazla kan dokulsun istemiyorum. Biz kazandik Chris - bunu gormelisin - davan sona erdi.",
    "I will spare the lives of your friends if you surrender now! Simply lay down your weapon and show yourself. Surely you don't wish any harm to come to them?":
        "Simdi teslim olursan arkadaslarinin hayatini bagislarim! Sadece silahini birak ve kendini goster. Onlarin zarar gormesini istemezsin herhalde?",
    "This foolish bravery will cost you your life Chris!":
        "Bu aptalca cesaret hayatina mal olacak Chris!",
    "I know there is doubt in your heart Chris - lay down your weapon and we will resolve this in a civilized manner.":
        "Kalbinde suphe oldugunu biliyorum Chris - silahini birak, bunu medeni bir sekilde cozelim.",
    "I do not have time for this foolishness Christopher! I have more important matters to attend to. Let us end this quickly!":
        "Bu sacmalikla kaybedecek vaktim yok Christopher! Ilgilenmem gereken daha onemli meseleler var. Bunu hemen bitirelim!",
    "Enough! My patience is at an end! You will live to regret your actions!":
        "Yeter! Sabrim tukendi! Yaptiklarina pisman olacaksin!",
    "You have no options left Chris! There is only one way out for you now! I will see to that personally!":
        "Hicbir secenegin kalmadi Chris! Artik senin icin tek bir cikis yolu var! Bununla bizzat ilgilenecegim!",
    "I will punish you for your impudence! Your struggle ends here!":
        "Bu kustahligini cezalandiracagim! Mucadelen burada bitiyor!",
    "Quick over here! Before they find us! When I climb up, you run down that pipe!. . . Hnng!. . . Heads up!. . . Now go!":
        "Cabuk bu tarafa! Bizi bulmadan once! Ben yukari tirmaninca sen su borudan asagi kos!... Hnng!... Dikkat et!... Simdi git!",
    "Don't worry Dog! I'm cool! I've been hanging out down here since they killed my parents. I'm on your side!":
        "Endiselenme ahbap! Ben iyiyim! Ailemi oldurduklerinden beri buralarda takiliyorum. Senin tarafındayim!",
    "You're packing some serious hardware! Don't let it slow you down - we gotta roll fast - let's go!":
        "Uzerinde saglam techizat var! Seni yavaslatmasina izin verme - hizli hareket etmeliyiz - hadi gidelim!",
    "Chris! Man, I'm sure glad to see you! They got Isabella - I didn't have a chance, there were too many of 'em. I always thought that Jones was bogus! I was just about to jump them when you stormed in. I got my M16 locked and loaded - I'll be back to settle that score with Jones. . . So what do we do now Chris?":
        "Chris! Dostum, seni gordugume cok sevindim! Isabella'yi aldilar - hic sansim yoktu, cok kalabaliktilar. O Jones'un sahtekar oldugunu hep dusunmustum zaten! Tam sen iceri daldiginda ben de onlara saldirmak uzereydim. M16'm kurulu ve dolu - Jones ile o hesabi kapatmak icin geri donecegim... Peki simdi ne yapiyoruz Chris?",
    "Just keep up with me - I got a hideout over this way - the Reds ain't never gonna find us up here!":
        "Sadece beni takip et - bu tarafta bir siginagim var - Kizillar bizi burada asla bulamaz!",
    "Uh, Helloooo? I'm trapped in here - anybody there?":
        "Sey, kimse var mi? Burada kapana kisildim - orada kimse var mi?",
    "Righteous! Here, take this C4, you're gonna need it.":
        "Harika! Al, su C4'u al, ihtiyacin olacak.",

    # C07RB
    "PRISONERS": "MAHKUMLAR",
    "Prisoners freed!": "Mahkumlar kurtarildi!",
    "HELIPAD": "HELIKOPTER PISTI",
    "Power Generator destroyed!": "Guc Jeneratoru yok edildi!",
    "It's time to stop the Soviet propaganda.  Check this - we're gonna take over the SAFN studios. Once we control the airwaves, we can get the truth out to the people. Oh yeah, I hear they got a lot of wounded civilians around, so pack plenty of health packs.":
        "Sovyet propagandasini durdurma zamani geldi. Bak simdi - SAFN studyolarini ele gecirecegiz. Yayinlari kontrol ettigimizde gercekleri halka ulastirabiliriz. Ha bu arada, etrafta cok sayida yarali sivil oldugunu duydum, bu yuzden yanina bolca saglik paketi al.",
    "Check this out! I've found out where they've got a Soviet elite training facility - it's in the High School. Take it back and cancel their classes dog, for real. From what I hear, they keep political prisoners there for interrogation too. I say we bust 'em out. Do all that and we'll be livin' gangsta.":
        "Sunu dinle! Sovyetlerin seckin egitim tesisinin nerede oldugunu buldum - Lisede. Orayi geri al ve derslerini iptal et dostum, harbiden. Duyduguma gore sorgulama icin siyasi mahkumlari da orada tutuyorlarmis. Bence gidip onlari cikaralim. Bunlarin hepsini yaparsak tam anlamiyla krallar gibi yasariz.",
    "Sweet-sweet, I like the new digs little man! Check this out, you even got a computer. Hey Chris - I think the mold here looks better than our old place.":
        "Tatli tatli, yeni mekanı sevdim kucuk adam! Su ise bak, bilgisayarin bile var. Hey Chris - bence buradaki kufler eski yerimizdekilerden daha iyi gorunuyor.",
    "Me n' some of my peeps from the block used to sneak down here and hang out. I don't think they're coming back though. The Reds were gunnin' for them pretty hard.":
        "Ben ve mahalleden birkac arkadas buraya gizlice girip takilirdik. Ama geri doneceklerini sanmiyorum. Kizillar peslerine cok fena takilmisti.",
    "You guys hungry? I scavenged some pizza from the shop the Reds toasted on 2nd and East 10th. Help yo'self.":
        "Aciktiniz mi beyler? Kizillarin 2. Cadde ve Dogu 10. Sokakta yaktigi dukkandan biraz pizza asirdim. Cekinmeyin.",
    "Naw man, maybe later. I'm not eating until we find Isabella. I wanna lay the hurt on the Reds for busting up our base.":
        "Yok dostum, belki sonra. Isabella'yi bulana kadar bir sey yemeyecegim. Ussumuzu bastiklari icin Kizillara dunyayi dar etmek istiyorum.",
    "Yo, check this out. . . After shakin' down this old Red computer and surfin' around in some of their files -  I found floorplans for the SAFN Studio building. I say we break in there start wreckin' their stuff. You know what i'm sayin'? Shut that propaganda chick up!":
        "Hey, sunu dinleyin... Bu eski Kizil bilgisayari kurcalayip dosyalarinda biraz dolastiktan sonra SAFN Studyosu binasinin kat planlarini buldum. Bence oraya dalip mallarini parcalamaya baslayalim. Ne dedigimi anliyor musunuz? O propagandaci kizin sesini kesin!",
    "Great plan Einstein! We're a little low on guys and guns right now! Get a load of him Chris - Junior thinks he's running the show now.":
        "Harika plan Einstein! Su anda adam ve silah bakimindan biraz zayifiz! Sunu goruyor musun Chris - Kucuk bey artik ipleri eline aldigini saniyor.",
    "Hey yo, check this out kid - listen up! Look, they're all kicked back right? They think they fixed us so good - so now's the time to hit 'em. Check this out - they got a blind spot in their surveillance. Let's catch 'em while they're blinkin' dog.":
        "Hey, dinle ahbap! Bak, su an ayaklarini uzatmis rahatlar, degil mi? Bizi tamamen bitirdiklerini saniyorlar - iste tam simdi onlari vurma zamani. Bak suraya - gozetlemelerinde bir kor nokta var. Onlari gozlerini kirptiklari anda yakalayalim dostum.",
    "Now - now you are talkin' - when you put it that way, we might have a chance. What do you think Chris?":
        "Iste simdi mantikli konustun - boyle soyleyince bir sansimiz olabilir gibi. Sen ne dusunuyorsun Chris?",
    "I'm coming with you! I don't wanna miss out on a chance to be on national TV!":
        "Ben de seninle geliyorum! Ulusal televizyona cikma firsatini kacirmak istemem!",
    "Right behind you Chris! I'll just check my gear before we head out.":
        "Hemen arkandayim Chris! Yola cikmadan once ekipmanimi kontrol edecegim.",
    "We gotta get into that TV station and blow the rest of their security system. When that's done the rest of us can bust in.":
        "O televizyon istasyonuna girip guvenlik sistemlerinin geri kalanini havaya ucurmaliyiz. Bu yapildiginda geri kalanlarimiz iceri dalabilir.",
    "Some of their fly-boys are set up behind the Warehouse. Blow their nest!":
        "Pilotlarindan bazilari Deponun arkasina konuslanmis. Yuvalarini baslarina yik!",
    "Check this out Chris! We gotta go prime time and shut down the TV Studio. Top it off with one of your flags - our ratings will be off the hook.":
        "Su ise bak Chris! Ana yayina girip Televizyon Studyosunu kapatmaliyiz. Uzerine de bir bayrak cek - reytinglerimiz tavan yapacak.",
    "Those damn Reds are sittin up inside my old school! I might have skipped a few classes, but they messed with my friends and they're gonna pay for that! Take 'em out Chris!":
        "O lanet Kizillar benim eski okulumun icine coreklenmisler! Birkac dersi asmis olabilirim ama arkadaslarima bulastilar ve bunun bedelini odeyecekler! Indir onlari Chris!",
    "I heard they bagged up some of our boys in the school yard - you should help 'em out.":
        "Okul bahcesinde bizim cocuklardan bazilarini yakaladiklarini duydum - onlara yardim etmelisin.",
    "Bad news Chris - they've got tanks watching the TV Station - better roll with an RPG.":
        "Kotu haber Chris - Televizyon Istasyonunu gozetleyen tanklari var - yanina bir roketatar alsan iyi edersin.",
    "Whoa - that was quite a speech Chris! Half the City is behind you now. Things should be a breeze from here on\x96":
        "Vay canina - ne konusmaydi ama Chris! Artik sehrin yarisi arkanda. Bundan sonrasi cocuk oyuncagi olmali...",
    "Whoa - that was quite a speech Chris! Half the City is behind you now. Things should be a breeze from here on…":
        "Vay canina - ne konusmaydi ama Chris! Artik sehrin yarisi arkanda. Bundan sonrasi cocuk oyuncagi olmali...",
    "I wasn't ever very patriotic, but seeing that flag flying up there really puts a lump in my throat. I'm tellin' ya Chris we're one step away - I can feel it! When this is all over, we're gonna do some serious partying!":
        "Hicbir zaman cok vatansever biri olmamistim, ama o bayragin yukarida dalgalandigini gormek bogazimi dugumluyor. Sana soyleyeyim Chris, zafere bir adim kaldi - hissedebiliyorum! Her sey bittiginde fena parti yapacagiz!",
    "Phew - I see you cancelled some of their flights today! It'll be a lot easier getting inside that TV Station now.":
        "Oh be - bugun ucuslarindan bazilarini iptal ettigini goruyorum! Artik o Televizyon Istasyonuna girmek cok daha kolay olacak.",
    "Booyah! 'took out that tank like a pro - there's nothing they can throw at us that we can't handle! Bring it on losers!":
        "Iste bu! O tanki bir profesyonel gibi indirdin - ustumuze salabilecekleri hicbir sey yok ki basa cikamayalim! Gelin bakalim ezikler!",
    "Yo Dog - listen up! Ivan's got a blind eye on the doors. Roll up through the alley and bust up in the place.":
        "Hey dostum - iyi dinle! Ivan kapilari goremiyor. Ara sokaktan ilerle ve mekana dal.",
    "BATTLE TANK": "SAVAS TANKI",
    "Raise Flag on TV Station roof.": "Televizyon Istasyonu Catısına Bayrak Cek.",
    "Destroy the Tank.": "Tanki Yok Et.",
    "Raise Flag on High School roof.": "Lise Catısına Bayrak Cek.",
    "Destroy the Helipad.": "Helikopter Pistini Yok Et.",
    "Free the Prisoners near the High School.": "Lise Yakinindaki Mahkumlari Kurtar.",
    "Tank destroyed!": "Tank imha edildi!",

    # C08A
    "Sure could use some C4. We can blow this vent to give us a way in. There may be some explosives in the depot nearby. It's worth a look.":
        "Biraz C4 cok ise yarardi. Iceri bir yol acmak icin bu havalandirmayi havaya ucurabiliriz. Yakinlardaki depoda biraz patlayici olabilir. Bakmaya deger.",
    "Hey \x96 lighten up. Look on the bright side \x96 at least I\x92m not hurt.":
        "Hey - sakin ol. Iyi tarafindan bak - en azindan ben yaralanmadim.",
    "Hey – lighten up. Look on the bright side – at least I’m not hurt.":
        "Hey - sakin ol. Iyi tarafindan bak - en azindan ben yaralanmadim.",
    "Who put that bozo in charge of the explosives? He lost it! The whole operation is Fubar! We may as well pack it up and go home.":
        "Patlayicilarin basina o salağı kim gecirdi? Hepsini kaybetti! Butun operasyon mahvoldu! Toplanip eve donsek daha iyi.",
    "We gotta be resourceful, this mission is too important. It's a long shot, but check out the wrecked helicopter - maybe there's something we can use.":
        "Becerikli olmaliyiz, bu gorev cok onemli. Dusuk bir ihtimal ama su enkaza donmus helikoptere bir bak - belki kullanabilecegimiz bir seyler vardir.",

    # C08E
    "Hello American friend - be careful. Grenade launchers are shooting this area. It is dangerous to go this way.":
        "Merhaba Amerikali dostum - dikkatli ol. Bombaatarlar bu bolgeye ates aciyor. Bu yoldan gitmek tehlikeli.",
    "We were so close! Where'd you go? When you left all hell broke loose! We regrouped here. The Reds have had time to reinforce their positions. We've gotta press the attack - there's no going back!":
        "Cok yaklasmistik! Nereye gittin? Sen ayrildiginda kiyamet koptu! Burada yeniden toplandik. Kizillarin mevzilerini guclendirmek icin zamani oldu. Saldiriyi surdurmeliyiz - geri donus yok!",
    "Chris! Help me!":
        "Chris! Yardim et!",
    "Over here, Chris!":
        "Buradayim Chris!",
    "Save me!":
        "Kurtar beni!",
    "Thanks Chris. Don't forget that you have to hoist all the flags.":
        "Tesekkurler Chris. Tum bayraklari cekmen gerektigini unutma.",
    "Thanks! You have to remember to hoist all four flags to take control of the zone.":
        "Tesekkurler! Bolgenin kontrolunu ele gecirmek icin dort bayragin hepsini cekmen gerektigini unutma.",
    "Well done Chris! Now go and raise those four flags in the name of freedom!":
        "Tebrikler Chris! Simdi git ve ozgurluk adina o dort bayragi dalgalandir!",

    # C08RB
    "C4": "C4",
    "Helipad destroyed!": "Helikopter pisti yok edildi!",
    "Flag raised - Area secure!": "Bayrak cekildi - Bolge guvende!",
    "Governor\x92s Island *looks* like an impenetrable fortress, but they have a weak spot - the ventilation system. You gotta blow a hole in that giant vent so our boys can roll up inside. That's the only way for them to get onto the island.":
        "Governor's Island gecilmez bir kale gibi *gorunuyor*, ama zayif bir noktalari var - havalandirma sistemi. O devasa havalandirmada bir delik acmalisin ki cocuklarimiz iceri girebilsin. Adaya ulasabilmelerinin tek yolu bu.",
    "Governor’s Island *looks* like an impenetrable fortress, but they have a weak spot - the ventilation system. You gotta blow a hole in that giant vent so our boys can roll up inside. That's the only way for them to get onto the island.":
        "Governor's Island gecilmez bir kale gibi *gorunuyor*, ama zayif bir noktalari var - havalandirma sistemi. O devasa havalandirmada bir delik acmalisin ki cocuklarimiz iceri girebilsin. Adaya ulasabilmelerinin tek yolu bu.",
    "Sweet! Here's a chance to get our hands on some major ammo. Find the Ammunition Depot so we can supply our boys for the final attack on the island. We need that ammo - we can't go in shootin' blanks.":
        "Harika! Iste agir muhimmat ele gecirmek icin bir sans. Muhimmat Deposunu bul ki adaya son saldiri icin cocuklarimiza cephane saglayabilelim. O muhimmata ihtiyacimiz var - iceri kurusiki ile giremeyiz.",
    "Aiiight! The boys in red have mortar cannons sittin' all around here.  We are stopped dead until you can take those babies out. Once they're snuffed, our boys are rollin' again.":
        "Pekala! Kizil cocuklarin buralarda konuslanmis havan toplari var. Sen o bebekleri ortadan kaldirana kadar tamamen kilitlendik. Onlar susturuldugunda cocuklarimiz tekrar harekete gececek.",
    "The Reds are deploying troops from here. Now, we gotta stop their flyboys from buzzing around. Blow the helipad and we're lookin' at clear skies.":
        "Kizillar birliklerini buradan sevk ediyor. Simdi, o ucan cocuklarin tepemizde vizildamasini durdurmaliyiz. Helikopter pistini patlat ve tertemiz bir gokyuzune bakalim.",
    "Well, they got Isabella locked away in Fort Jay. Free her first! This is the last Soviet stronghold. Raise all four of our flags and it's game over for the Reds! Let's send those boys packin' back to the Motherland! YEAH!":
        "Evet, Isabella'yi Fort Jay'e hapsettiler. Once onu kurtar! Burasi son Sovyet kalesi. Dort bayragimizi da dalgalandir ve Kizillar icin oyun bitsin! O cocuklari Anavatanlarina geri postalayalim! EVET!",
    "This is it fellas. Governor\x92s Island. The baddest boys in red are holed up in here, waiting for backup. We ain't alone neither! I got guys hollaring at me from all around the States, tellin' me that everyone is plannin' a major blow up on the Reds all at once. We gotta show up too! But, they're dug in tight up in here, man. I'm talkin' \x96 heavy guns, minefields, artillery. . . but the real deal is here: Fort Jay. Now this. . . this is where they control the subs \x96 and those nukes they\x92re carrying.":
        "Iste geldik beyler. Governor's Island. Kizillarin en azili adamlari takviye bekleyerek buraya kapandi. Ama biz de yalniz degiliz! Butun Amerika'dan bana seslenen arkadaslar var, herkesin ayni anda Kizillara karsi buyuk bir taarruz planladigini soyluyorlar. Biz de kendimizi gostermeliyiz! Ama buraya cok siki mevzilenmisler dostum. Agir silahlardan, mayin tarlalarindan, topculardan bahsediyorum... Ama asil mevzu burada: Fort Jay. Iste burasi... denizaltilari ve tasidiklari o nukleer fuzeleri buradan kontrol ediyorlar.",
    "This is it fellas. Governor’s Island. The baddest boys in red are holed up in here, waiting for backup. We ain't alone neither! I got guys hollaring at me from all around the States, tellin' me that everyone is plannin' a major blow up on the Reds all at once. We gotta show up too! But, they're dug in tight up in here, man. I'm talkin' – heavy guns, minefields, artillery. . . but the real deal is here: Fort Jay. Now this. . . this is where they control the subs – and those nukes they’re carrying.":
        "Iste geldik beyler. Governor's Island. Kizillarin en azili adamlari takviye bekleyerek buraya kapandi. Ama biz de yalniz degiliz! Butun Amerika'dan bana seslenen arkadaslar var, herkesin ayni anda Kizillara karsi buyuk bir taarruz planladigini soyluyorlar. Biz de kendimizi gostermeliyiz! Ama buraya cok siki mevzilenmisler dostum. Agir silahlardan, mayin tarlalarindan, topculardan bahsediyorum... Ama asil mevzu burada: Fort Jay. Iste burasi... denizaltilari ve tasidiklari o nukleer fuzeleri buradan kontrol ediyorlar.",
    "Aw man - we've already been there once! We gotta sail out there again? They've got Isabella! If we move on 'em now, they'll just waste her. We don't want that. Heck, we control most of New York, can't we wait 'till they leave? Know what I'm saying? Like, let 'em go home, just leave the back door open and let them slip out quietly.":
        "Hadi ama dostum - oraya zaten bir kez gittik! Oraya tekrar mi acilacagiz? Isabella ellerinde! Simdi uzerlerine gidersek onu hemen oldururler. Bunu istemeyiz. Tanri askina, New York'un buyuk kismini kontrol ediyoruz, gidene kadar bekleyemez miyiz? Ne dedigimi anliyor musun? Yani birakalim evlerine donsunler, arka kapiyi acik birakalim ve sessizce sizip gitsinler.",
    "Dog - you're trippin'!?! Look they're here for good -  Didja hear what I'm saying, they're bringing major back-up\x96 They ain't asking for a ride home, they wanna smoke us for sure. I'm sayin' they're fixin' to wreck us, kid. They're gonna bust out with their big guns. Did your Mama drop you on your head or something? Maybe you shouldn\x92t shoot off your mouth until your brain is fully loaded.":
        "Dostum kafayi mi yedin sen!?! Bak adamlar temelli buradalar - Ne dedigimi duydun mu, devasa takviyeler getiriyorlar... Eve donmek icin otostop cekmiyorlar, bizi yok etmek istiyorlar. Seni temin ederim bizi ezmeye hazirlaniyorlar evlat. Buyuk silahlariyla gelecekler. Annen seni kucukken kafanin ustune falan mi dusurdu? Belki de beynin tam dolmadan cenen calismamalidir.",
    "Dog - you're trippin'!?! Look they're here for good -  Didja hear what I'm saying, they're bringing major back-up… They ain't asking for a ride home, they wanna smoke us for sure. I'm sayin' they're fixin' to wreck us, kid. They're gonna bust out with their big guns. Did your Mama drop you on your head or something? Maybe you shouldn’t shoot off your mouth until your brain is fully loaded.":
        "Dostum kafayi mi yedin sen!?! Bak adamlar temelli buradalar - Ne dedigimi duydun mu, devasa takviyeler getiriyorlar... Eve donmek icin otostop cekmiyorlar, bizi yok etmek istiyorlar. Seni temin ederim bizi ezmeye hazirlaniyorlar evlat. Buyuk silahlariyla gelecekler. Annen seni kucukken kafanin ustune falan mi dusurdu? Belki de beynin tam dolmadan cenen calismamalidir.",
    "Alright! Alright! I get it! But I'm tellin' ya this is crazy, kid. I'm only doing this for Isabella. Chris! Chris! Chris, I'm with ya. I gotta get in a few shots before the Reds bail outta here. Hey Junior, you'll need to step aside on this one, it's gonna be a man's job.":
        "Tamam! Tamam! Anladim! Ama sana soyleyeyim bu delilik cocuk. Bunu sadece Isabella icin yapiyorum. Chris! Chris! Chris, seninleyim. Kizillar buradan kacmadan once birkac kursun sikmam gerek. Hey ufaklik, bu sefer kenara cekilmen gerekecek, bu erkek isi olacak.",
    "Whatever Dog!. . . Yo Chris, we got some C4 out at the base in Yonkers. Way I see it, we got one shot at this. Don't flinch! We gotta step in the ring for a shot at the title.":
        "Ne dersen de dostum!... Hey Chris, Yonkers'taki usste biraz C4'umuz var. Gordugum kadariyla tek bir sansimiz var. Gozunu kirpma! Sampiyonluk icin ringe cikmamiz gerek.",
    "Punk kids! No respect - I got brains, I can handle myself.":
        "Saygisiz veletler! Saygi yok - bende akil var, basimin caresine bakabilirim.",
    "This went south in a hurry. We lost everybody out here. We gotta blow that vent so we can get back in.":
        "Isler cok cabuk tersine dondu. Burada herkesi kaybettik. Iceri geri girebilmek icin o havalandirmayi havaya ucurmamiz gerek.",
    "Someone's gotta do something about the shelling, otherwise we'll never get past this point.":
        "Biri bu bombardiman konusunda bir sey yapmali, yoksa bu noktayi asla gecemeyiz.",
    "I hate being on the losing team - lead on, buddy!":
        "Kaybeden tarafta olmaktan nefret ediyorum - yolu goster dostum!",
    "Chris - we're with you all the way. Let's send those Reds packing!":
        "Chris - sonuna kadar seninleyiz. Su Kizillari ait olduklari yere yollayalim!",
    "For now, we should be safe in this old bunker.":
        "Simdilik bu eski siginakta guvende olmaliyiz.",
    "We lost communication outside the island, but through these tunnels we have access all around Manhattan.":
        "Ada disiyla iletisimi kaybettik, ancak bu tuneller sayesinde Manhattan'in her yerine erisimimiz var.",
    "Try and see if you can find any C4 in that Soviet depot on the eastside of the island. We saw loads of it there as we rushed through the place. We NEED to blow up that vent.":
        "Adanin dogu tarafindaki o Sovyet deposunda C4 bulabilecek misin bir bak. Oradan hizla gecerken bir suru gorduk. O havalandirmayi KESINLIKLE patlatmamiz gerek.",
    "Damn! These choppers are laying it on thick! What are we gonna do?":
        "Lanet olsun! Bu helikopterler cok agir indiriyor! Ne yapacagiz?",
    "What are we gonna do - WHAT ARE WE GONNA DO!!!":
        "Ne yapacagiz - NE YAPACAGIZ!!!",
    "C'mon Chris - tell us what to do!":
        "Hadi Chris - ne yapacagimizi soyle!",
    "We're going down the drain, if you don't fix this!":
        "Bunu duzeltmezsen mahvolacagiz!",
    "Town's full of Rooskies - let's flush 'em back into the sea!":
        "Sehir Rus kayniyor - onlari denize dokelim!",
    "You've taken us this far, Chris - it's crunch time!":
        "Bizi buraya kadar getirdin Chris - artik karar ani!",
    "Let's go, Chris - we know you can do it.":
        "Hadi Chris - bunu yapabilecegini biliyoruz.",
    "We took a lickin', Chris - but the fight for freedom ain't over!":
        "Darbe aldik Chris - ama ozgurluk mucadelesi bitmedi!",
    "They kicked our butts once - now let's return the favor!":
        "Bize bir kez haddimizi bildirdiler - simdi sira bizde!",
    "HARBOR ENTRANCE": "LIMAN GIRISI",
    "TOWER": "KULE",
    "VENTILATION SHAFT": "HAVALANDIRMA SAFTI",
    "SUPPLY HANGAR": "IKMAL HANGARI",
    "MORTAR\nPOSITION": "HAVAN\nMEVZISI",
    "ATTACK CHOPPER HELIPAD": "SALDIRI HELIKOPTERI PISTI",
    "GENERATOR BUILDING": "JENERATOR BINASI",
    "FUEL STATION": "YAKIT ISTASYONU",
    "TROOP TRANSPORT HELIPAD": "ASKER TASIMA HELIKOPTERI PISTI",
    "SOUTHEAST \nBUNKER": "GUNEYDOGU \nSIGINAGI",
    "NORTHEAST \nBUNKER": "KUZEYDOGU \nSIGINAGI",
    "NORTHWEST \nBUNKER": "KUZEYBATI \nSIGINAGI",
    "SOUTHWEST \nBUNKER": "GUNEYBATI \nSIGINAGI",
    "Raise Flag in front of Harbor.": "Limanin Onune Bayrak Cek.",
    "Destroy Tower.": "Kuleyi Yok Et.",
    "Destroy ventilation shaft grating.": "Havalandirma safti izgarasini yok et.",
    "Locate C4 charges.": "C4 patlayicilari bul.",
    "Raise Flag at Hangar.": "Hangara Bayrak Cek.",
    "Find C4 storage.": "C4 deposunu bul.",
    "Destroy Mortar Position.": "Havan Mevzisini Yok Et.",
    "Raise Flag at Sewer.": "Kanalizasyona Bayrak Cek.",
    "Destroy Attack Chopper Helipad.": "Saldiri Helikopteri Pistini Yok Et.",
    "Raise Flag near Generator Building.": "Jenerator Binasi Yakinina Bayrak Cek.",
    "Destroy Fuel Station.": "Yakit Istasyonunu Yok Et.",
    "Destroy Troop Transport Helipad.": "Asker Tasima Helikopteri Pistini Yok Et.",
    "Raise Flag over Southeast Bunker.": "Guneydogu Siginagina Bayrak Cek.",
    "Raise Flag over Northeast Bunker.": "Kuzeydogu Siginagina Bayrak Cek.",
    "Raise Flag over Northwest Bunker.": "Kuzeybati Siginagina Bayrak Cek.",
    "Raise Flag over Southwest Bunker.": "Guneybati Siginagina Bayrak Cek.",
    "Free Isabella.": "Isabella'yi Kurtar.",
    "Tower destroyed!": "Kule yok edildi!",
    "Ventilation shaft is open!": "Havalandirma safti acildi!",
    "C4 located!": "C4 bulundu!",
    "Mortar positon destroyed!": "Havan mevzisi yok edildi!",
    "Fuel Station destroyed!": "Yakit Istasyonu yok edildi!",
    "All flags raised - Area secure!": "Tum bayraklar cekildi - Bolge guvende!"
}

CH6_CH8_TRANSLATIONS = {
    orig: to_ascii_turkish(trans)
    for orig, trans in CH6_CH8_RAW.items()
}

if __name__ == '__main__':
    total = 0
    missing = []
    groups = ['C06A', 'C07RB', 'C08A', 'C08E', 'C08RB']
    for grp in groups:
        path = rf'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_work\group_{grp}.json'
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        total += len(data)
        for k, v in data.items():
            if v not in CH6_CH8_TRANSLATIONS:
                missing.append((grp, k, v))
    print(f"Coverage: {total - len(missing)} / {total}")
    if missing:
        print("Missing:")
        for grp, k, v in missing:
            print(f"  [{grp}] {k}: {repr(v)}")
