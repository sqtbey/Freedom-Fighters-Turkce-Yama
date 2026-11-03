# -*- coding: utf-8 -*-
from turkish_ascii_converter import to_ascii_turkish

# Translation dictionary for moviecuts and story cinematics
MOVIECUTS_TRANSLATIONS_RAW = {
    "1945\nSoviet Air Force drops the A-bomb on Berlin,\nending WW2 in Europe.":
        "1945\nSovyet Hava Kuvvetleri Berlin'e atom bombasi atti,\nAvrupa'da 2. Dunya Savasi sona erdi.",

    "1953\nBritain reluctantly joins the Communist Block, \nthe last European country to do so.":
        "1953\nIngiltere istemeyerek de olsa Komunist Bloka katildi,\nbunu yapan son Avrupa ulkesi oldu.",

    "1961\nDespite U.S. protests, mid-range nuclear missiles \nare placed in Cuba.":
        "1961\nABD'nin protestolarina ragmen, Kuba'ya\norta menzilli nukleer fuzeler yerlestirildi.",

    "1976\nThe Soviet Union sends thousands of military 'advisors'\nto Guatemala and Honduras.":
        "1976\nSovyetler Birligi, Guatemala ve Honduras'a\nbinlerce askeri 'danisman' gonderdi.",

    "1996\nMexican Communist Party celebrates\ndisputed victory in presidential election.":
        "1996\nMeksika Komunist Partisi baskanlik secimindeki\nsaibeli zaferini kutluyor.",

    "2001\nFoiled assassination attempt on the U.S. president \n- an unnamed foreign power is implicated.":
        "2001\nABD baskanina duzenlenen suikast girisimi engellendi\n- adi aciklanmayan yabanci bir guc suclaniyor.",

    "Yesterday\nReports of low-flying drones from all over the U.S.A.\nGovernment dismisses the sightings as weather balloons.":
        "Dun\nABD genelinden alcaktan ucan insansiz hava araci raporlari geldi.\nHukumet ihbarlari hava durumu balonu diyerek gecistirdi.",

    "They were wrong. . .":
        "Yanilmislardi. . .",

    "Present Day New York Harbour 6:00 hrs":
        "Gunumuz New York Limani 06:00",

    "Electronic Arts Presents":
        "Electronic Arts Sunar",

    "A Game By IO Interactive":
        "Bir IO Interactive Oyunu",

    "Music Composed By Jesper Kyd":
        "Muzikler: Jesper Kyd",

    ". . .anyway, when I couldn’t pinpoint the exact location of my humble “summer cottage” in the Hamptons, she dropped me right there. Cold!! Damn I looked like an idiot, still holding the drinks I'd been paying for all night! Well, who cares, you know, her loss – hey, pop the clutch and lets get on with it - what’s top of the work sheet today, bro´. . .?":
        ". . .neyse, Hamptons'taki mutevazi 'yazligimin' tam yerini gosteremeyince beni oracikta birakiverdi. Buz gibi hem de!! Lanet olsun, butun gece parasini odedigim icecekler elimde bir aptal gibi kalakaldim! Neyse, kimin umurunda, kendi kaybi - hey, debriyaja bas da yola koyulalim, bugun is listesinin basinda ne var kardesim. . .?",

    "Mmm, let’s see. . . Isabella Angelina, a condo in Midtown Manhattan – drain plug and leaky garbage disposal. . .":
        "Mmm, bakalim. . . Isabella Angelina, Midtown Manhattan'da bir daire - tikali gider ve su sizdiran cop ogutucu. . .",

    "Do we have to get the crappiest route EVERY Monday morning? I wish for once we'd get a fancy condo on the east side with a beau…whoa, Isabella Angewhatever -  she's that hot spokesbabe for the “Warning Against Reds” movement? Saw her on TV yesterday!":
        "HER pazartesi sabahi en berbat rotayi almak zorunda miyiz? Keske bir kere de dogu yakasinda guzel bir daire gelseydi... oo, Isabella her neyse - su 'Kizillara Karsi Uyari' hareketinin o cekici sozcusu mu? Dun televizyonda gordum onu!",

    "No idea - besides, I don't follow all that conspiracy crap like you do.":
        "Hicbir fikrim yok - hem ben senin gibi oyle komplo zirvalarini takip etmem.",

    "Whaddaya mean, \"conspiracy crap\"? Doesn’t the Soviet invasion of South America bother you? You need a reality check, bro'. Know what? Next thing you know you'll be waking up under a Russian flag, and you won't think it's \"conspiracy crap\" then!!":
        "Ne demek \"komplo zirvasi\"? Guney Amerika'nin Sovyetler tarafindan isgal edilmesi seni hic rahatsiz etmiyor mu? Gerceklerle yuzlesmen lazim birader. Biliyor musun? Bir bakmissin yarin bir Rus bayraginin altinda uyaniyorsun, o zaman bunun \"komplo zirvasi\" oldugunu dusunmezsin!!",

    "Riiight. . .":
        "Tabi tabi. . .",

    "You're so in denial! Try listening to those \"Warning Against Reds\" guys. Speaking of which, how 'bout this first stop? I’d really like to check out the plumbing on that Isabella chick. . .":
        "Inkar edip duruyorsun! Su \"Kizillara Karsi Uyari\" elemanlarini bir dinle. Lafi acilmisken, su ilk duraga ne dersin? Su Isabella denen kizin tesisatini kontrol etmeyi cok isterdim dogrusu. . .",

    "Hello? Plumbers on Patrol. Anybody home. . .?":
        "Alo? Tesisatcilar geldi. Evde kimse var mi. . .?",

    "Phew, no wonder – Sister Sludge sure needs a drain surgeon here…":
        "Pff, hic sasirmamali - bu pislik yuvasi kesinlikle bir gider uzmanina ihtiyac duyuyor...",

    "There’s one here-freeze! Don’t move! Remain calm, citizen!":
        "Burada biri var, kipirdama! Kimildama! Sakin ol vatandas!",

    "Whoa – stay cool, man. . . I’m just the plumber. . .":
        "Sakin ol dostum. . . Ben sadece tesisatciyim. . .",

    "Where is your girlfriend, citizen?":
        "Kiz arkadasin nerede vatandas?",

    "Girlfriend. . .? Hey, she’s not. . .":
        "Kiz arkadasim mi. . .? Hey, o benim...",

    "I will ask again: Where is Isabella Angelina? Mmm. . .?":
        "Tekrar soruyorum: Isabella Angelina nerede? Mmm. . .?",

    "What her?! Look, I think. . .  I mean, she's, look, she's not. . .":
        "O mu?! Bakin, sanirim. . . Yani, o benim bir seyim degil...",

    "Well. . . Isabella cannot be far from here, bomb the place to pieces.":
        "Pekala. . . Isabella buradan cok uzakta olamaz, burayi yerle bir edin.",

    "I wanna see a lawyer, buddy!":
        "Avukatimi gormek istiyorum ahbap!",

    "COMRADE NEWSANCHOR":
        "YOLDAS HABER SUNUCUSU",

    "ADRESSES THE NATION":
        "ULUSA SESLENIYOR",

    "Citizens of New York and comrades from The Soviet Armed Forces – welcome to our first news broadcast after today’s events. My name is Tatiana Kempinski, and I will be your regular news anchor from now on. We hope in time to obtain the  cooperation of most of your familiar TV personalities, once they return from a re-education program at our training facilities in Alaska. Meanwhile, I will make sure you get all necessary information about our efforts to restore peace and stability in your troubled country.":
        "New York vatandaslari ve Sovyet Silahli Kuvvetleri'nin degerli yoldaslari - bugunku olaylarin ardindan yayinlanan ilk haber bultenimize hos geldiniz. Benim adim Tatiana Kempinski ve bundan boyle duzenli haber sunucunuz olacagim. Alaska'daki egitim tesislerimizde yeniden egitim programindan donduklerinde, tanidiginiz cogu televizyoncunun da aramiza katilmasini bekliyoruz. Bu surecte, sikintili ulkenizde baris ve istikrari yeniden tesis etme cabalarimiz hakkinda gerekli tum bilgileri size ulastiracagim.",

    "Our Soviet leaders have been concerned for years by the plight of the poor American people, suffering under a corrupt regime. Today, we have finally succeeded in liberating the suppressed masses of Americans from further hardship, and we will soon restore law and order in a new rule of government. And we expect and believe that every citizen will swear allegiance to this new order. Cooperate, and you will reap all the benefits of the Soviet system – all measures of resistance will be futile and dealt with swiftly.":
        "Sovyet liderlerimiz, yozlasmis bir rejim altinda ezilen zavalli Amerikan halkinin durumundan yillardir endise duymaktaydi. Bugun nihayet ezilen Amerikan halkini daha fazla sikintidan kurtarmayi basardik ve yakinda yeni hukumet duzeniyle kanun ve nizam yeniden tesis edecegiz. Her vatandasin bu yeni duzene baglilik yemini edecegine inaniyoruz. Isbirligi yapin, boylece Sovyet sisteminin tum nimetlerinden faydalanin - her turlu direnis beyhude olacak ve derhal bastirilacaktir.",

    "Our great leader, comrade General Tatarin, will be addressing the nation later. So – on behalf of the dedicated staff here at the studio, and the glorious Soviet Armed Forces: Welcome, New York – to a better future!":
        "Buyuk liderimiz, yoldas General Tatarin, birazdan ulusa seslenecek. Bu nedenle - buradaki studyo calisanlari ve sanli Sovyet Silahli Kuvvetleri adina: New York, daha guzel bir gelecege hos geldin!",

    "TATIANA KEMPINSKI":
        "TATIANA KEMPINSKI",

    "GENERAL TATARIN":
        "GENERAL TATARIN",

    "STAY TUNED TO THIS CHANNEL FOR IMPORTANT INFORMATION. ALL OTHER BROADCASTS HAVE BEEN CANCELLED UNTIL FURTHER NOTICE. CITIZENS ARE REQUIRED TO TUNE IN DAILY FOR IMPORTANT UPDATES. OTHER COMMUNICATIONS HAVE BEEN SUSPENDED IN MOST AREAS AND WILL ONLY BE RESTORED FOR PROPERLY REGISTERED CITIZENS. SEE THE COMMISAR IN YOUR LOCAL AREA FOR REGISTRATION DETAILS. CURFEW IS IN EFFECT - CITIZENS FOUND ON THE CITY STREETS AFTER DUSK MAY BE SHOT ON SIGHT. PROPERLY REGISTERED CITIZENS WILL RECEIVE FOOD COUPONS THAT MAY BE REDEEMED AT YOUR LOCAL GOVERNMENT RATIONING STATION. EARLIER THIS MORNING OUR BRAVE REPUBLICAN SOLDIERS WERE GREETED BY JUBILANT NEW YORKERS - SEE THE SPECIAL REPORT AT 8:00 PM \"SOVIETS IN TIMES SQUARE, A NEW WORLD ORDER\". VIEWING IS COMPULSORY. TORRENTIAL RAINS AND THUNDERSTORMS ARE EXPECTED IN THE MIDWEST AND ARE UNRELATED TO THE DEPLOYMENT OF A FEW MINOR TACTICAL NUCLEAR DEVICES BY OUR TROOPS AGAINST REBELS IN THE ROCKY MOUNTAINS.":
        "ONEMLI BILGILER ICIN BU KANALI TAKIP EDIN. IKINCI BIR BILDIRIME KADAR DIGER TUM YAYINLAR IPTAL EDILMISTIR. VATANDASLARIN GUNLUK OLARAK GELISMELERI TAKIP ETMESI ZORUNLUDUR. DIGER ILETISIM AGLARI COGU BOLGEDE ASKIYA ALINMIS OLUP, YALNIZCA KAYITLI VATANDASLAR ICIN ACILACAKTIR. KAYIT DETAYLARI ICIN BOLGENIZDEKI KOMISERE BASVURUN. SOKAGA CIKMA YASAGI YURURLUKTEDIR - HAVA KARARDIKTAN SONRA SOKAKTA BULUNAN VATANDASLAR GORULDUGU YERDE VURULABILIR. KAYITLI VATANDASLAR YIYECEK KUPONU ALACAKTIR. BU SABAH ASKERLERIMIZ COSKUYLA KARSILANDI. SAAT 20:00'DEKI 'TIMES SQUARE'DE SOVYETLER, YENI DUNYA DUZENI' OZEL YAYININI IZLEMEK ZORUNLUDUR. ORTA BATIDAKI SIDDETLI YAGISLARIN ASKERLERIMIZIN ROCKY DAGLARINDA ISYANCILARA KARSI KULLANDIGI KUCUK TAKTIK NUKLEER PATLAMALARLA ILGISI YOKTUR.",

    "This is Tatiana Kempinski at SAFN studios in New York – in today’s headlines: A downtown precinct was attacked by rebels earlier today. The attackers freed several rebel detainees. There are reports of many casualties.":
        "New York SAFN studyolarindan Tatiana Kempinski bildiriyor - bugunun basliklarinda: Sehir merkezindeki bir polis karakolu bugun erken saatlerde isyancilar tarafindan saldiriya ugradi. Saldirganlar bircok isyanci tutukluyu serbest birakti. Cok sayida can kaybi oldugu bildiriliyor.",

    "Several witnesses confirm that the raid was carried out by a small group of armed rebels, headed by an individual who authorities believe to be the new leader of the resistance.":
        "Bircok gorku tanigi, baskinin direnisin yeni lideri olduguna inanilan bir sahis onderligindeki kucuk bir silahli isyanci grubu tarafindan gerceklestirildigini dogruladi.",

    "Isabella Angelina, seen in these pictures, is an important member of the underground resistance movement, and the operation looked like a carefully planned and executed rescue attempt. The group was led by a shadowy figure as yet unidentified, but believed to be a male Caucasian in his early thirties. Earlier today I interviewed our leader General Tatarin on the situation.":
        "Fotograflarda gorulen Isabella Angelina, yeralti direnis hareketinin onemli bir uyesidir ve operasyon planli bir kurtarma girisimidir. Gruba otuzlu yaslarinda beyaz bir erkek olduguna inanilan gizemli bir sahis liderlik etmistir. Bugun erken saatlerde liderimiz General Tatarin ile roportaj yaptim.",

    "This sort of action against the Soviet Liberation Army will not be tolerated, and such attacks only increase tension here. However, I assure you that this was an isolated event, and we have restored peace and stability.":
        "Sovyet Kurtulus Ordusu'na karsi yapilan bu tur eylemlere musamaha gosterilmeyecektir ve bu tur saldirilar gerilimi artirir. Ancak sizi temin ederim ki bu munferit bir olaydi, baris ve istikrari yeniden tesis ettik.",

    "That was General Tatarin earlier today. On the phone now from Governor’s Island is comrade Colonel Bulba, Head of KGB.":
        "General Tatarin boyle konustu. Simdi Governor's Island'dan telefon hattimizda KGB Baskani yoldas Albay Bulba var.",

    "Comrade Kempinski: These people are not rebels from proletariat. This “freedom phantom” is vigilante – a terrorist! But they are few, and will be executed when caught – after a trial, of course.":
        "Yoldas Kempinski: Bu kisiler halk tabakasindan isyancilar degildir. Bu \"ozgurluk hayaleti\" kanunsuz bir hayduttur - bir teroristtir! Fakat sayilari azdir ve yakalandiklarinda idam edileceklerdir - elbette yargilanmanin ardindan.",

    "And on this reassuring note, let’s look at the forecast – what’s in store for us on weather front tomorrow, comrade Ilyana…?":
        "Ve bu guven verici aciklamanin ardindan hava durumuna bakalim - yarin bizi neler bekliyor, yoldas Ilyana...?",

    "COMRADE GENERAL VASILIJ TATARIN":
        "YOLDAS GENERAL VASILIJ TATARIN",

    "COMRADE COLONEL BULBA":
        "YOLDAS ALBAY BULBA",

    "NEWSFLASH - REBEL ATTACK!":
        "SON DAKIKA - ISYANCI SALDIRISI!",

    "REMINDER - FOOD COUPONS MAY BE REDEEMED AT YOUR LOCAL GOVERNMENT RATIONING STATION. CITIZENS POSSESSING AN AMERICAN FLAG WILL BE ARRESTED. DISPLAYING AN AMERICAN FLAG IS PUNISHABLE BY DEATH. RADIOACTIVE FALLOUT IN MONTANA HAS CLAIMED THE LIVES OF AN ESTIMATED 10,000 REBEL SOLDIERS. ALL WINTER CLOTHING FOR REGISTERED CITIZENS WILL BE BROWN - BUY NOW AND AVOID STANDING IN LINE. USE OF ANY COMBINATION OF RED, WHITE AND BLUE COLORS IS ILLEGAL. THE ICE-SKATING COMPETITION IN CENTRAL PARK HAS BEEN ARRANGED BY THE LOCAL UNIT OF THE SOVIET LIBERATION ARMY - WONDERFUL PRIZES BE AWARDED! THE DOLLAR WILL BE DISCONTINUED AS OF FEBRUARY 1ST. YOU CAN CHANGE UP TO $1,000 IN ANY BANK - RATIO IS $10 FOR ONE SOVIET ROUBLE. FAMOUS ELITE GYMNAST OLGA MALNUTRITINOVA IS PREGNANT AGAIN - SHE PROUDLY PROCLAIMED \"RUSSIAN DOCTORS HAVE ALWAYS PERFORMED MIRACLES!\"":
        "HATIRLATMA - GIDA KUPONLARI YEREL HUKUMET ERZAK MERKEZINDE KULLANILABILIR. AMERIKAN BAYRAGI BULUNDURANLAR TUTUKLANACAKTIR. AMERIKAN BAYRAGI ASMAK OLUMLE CEZALANDIRILIR. MONTANA'DAKI RADYOAKTIF SERPINTI 10.000 ISYANCININ CANINI ALDI. TUM KISLIK KIYAFETLER KAHVERENGI OLACAKTIR. KIRMIZI, BEYAZ VE MAVI RENK KOMBINASYONLARI YASA DISIDIR. CENTRAL PARK'TAKI BUZ PATENI YARISMASINDA HARIKA ODULLER VERILECEKTIR. DOLAR 1 SUBAT'TA KALDIRILACAKTIR. HER BANKADA 1.000 DOLARA KADAR BOZDURABILIRSINIZ - ORAN 1 SOVYET RUBLESI ICIN 10 DOLARDIR.",

    "\"Rebels are #1 enemy of the people\"":
        "\"Isyancilar halkin 1 numarali dusmanidir\"",

    "Good evening - this is Tatiana Kempinski at SAFN studios in New York. Autumn is definitely here – there’s a chill in the air, but the citizens of New York are coping, thanks to the many Soviet engineers working overtime to repair the many power stations that were damaged during the recent rash of rebel attacks. “Freedom Phantom”, the mythical figure that has eluded our troops and orchestrated so many surprise attacks on central installations, is thought to be responsible. Earlier today comrade General Tatarin had this comment.":
        "Iyi aksamlar - New York SAFN studyolarindan Tatiana Kempinski bildiriyor. Sonbahar geldi - hava soguk, ancak son isyanci saldirilarinda hasar goren elektrik santrallerini onarmak icin fazla mesai yapan Sovyet muhendisleri sayesinde New York vatandaslari durumu idare ediyor. Askerlerimizden kacan efsanevi figur \"Ozgurluk Hayaleti\"nin sorumlu oldugu dusunuluyor. Bugun erken saatlerde General Tatarin su aciklamada bulundu.",

    "All that this “Freedom Phantom character” and his rabid followers are really achieving is punishing the citizens of New York with these attacks – They really must stop for the sake of the people; we simply cannot get the food and the power situation under control until we can guarantee the safety of the hard working men and women of this administration.":
        "Bu 'Ozgurluk Hayaleti sahsiyeti' ve takipcilerinin basarabildigi tek sey vatandaslari cezalandirmaktir. Halkin iyiligi icin bunlar durmalidir; calisanlarimizin guvenligini saglayana kadar gida ve elektrik durumunu kontrol altina alamayiz.",

    "Comrade Tatarin - Colonel Bulba, says that the situation will only get under control once “The Phantom” is found and eliminated, and if this doesn’t happen soon, severe measures will be taken against any collaborators and all others helping them. What are your comments on that?":
        "Yoldas Tatarin - Albay Bulba, durumun yalnizca 'Hayalet' ortadan kaldirildiginda kontrol altina alinabilecegini ve agir tedbirler alinacagini soyluyor. Bu konudaki yorumunuz nedir?",

    ". . . hmmm…we hope to resolve this in. . . civilized way without further collateral damage. . . we are here to restore stability, not disrupt it. . . no further questions, please - spasiba.":
        ". . . hmmm... bunu daha fazla ikincil hasar olmadan... medeni bir yolla cozmeyi umuyoruz. . . biz buraya istikrari yeniden saglamaya geldik. . . baska soru olmasin lutfen - spasiba.",

    "We will be back after  a short break – stay with us!":
        "Kisa bir aradan sonra tekrar buradayiz - bizden ayrilmayin!",

    "It is obvious that our heroic Soviet Army has once again. . .":
        "Kahraman Sovyet Ordumuzun bir kez daha kanitladigi uzere. . .",

    "TIRED OF YOUR PETS? TURN THEM OVER TO PETS4FREE AT LINCOLN TUNNEL, AND WE WILL TAKE GOOD CARE OF THEM FOR YOU. ILLEGAL DEMONSTRATIONS HAVE PLAGUED MAJOR U.S. CITIES - OUR EFFECTIVE FORCES HAVE CAUGHT MANY PARTICIPANTS, WHO WILL BE INTERROGATED AND SUBSEQUENTLY SENT TO REFORM CAMPS IN ALASKA. PROBLEMS WITH FEEDING YOUR FAMILY? ALL REGISTERED WORKERS CAN EACH WEEK COLLECT 1 KILO OF UNSPECIFIED MINCED MEAT AT FOODS4FREE AT LINCOLN TUNNEL. THE RAMPANT CHOLERA EPIDEMIC CAN BE STOPPED - ALL CITIZENS ARE ADVISED AGAINST DISPOSING OF HUMAN WASTE AND BODIES IN PUBLIC AREAS. AS OF NEXT MONTH, ALL NEWBORN BABIES WILL BE ISSUED A SOCIAL SECURITY NUMBER TATTOOED IN THEIR NECKS. REMEMBER - ONLY REGISTERED WORKERS ARE ELIGIBLE FOR HOSPITAL TREATMENT. NEW ACTIVITIES ADDED TO THE LIST OF OFFENCES SUBJECT TO INDETERMINATE INCARCERATION UNDER NEW ORDER: GRAFFITI, STREET BASKETBALL AND SKATEBOARDING. REPEAT POSSESSION OF OLD AMERICAN FLAGS NOW PUNISHABLE BY DEATH - THREE FLAGS YOU'RE OUT. REGISTERED WORKERS CAN EACH WEEK COLLECT 10 POUNDS OF COMBUSTIBLE MATERIAL AND SHREDDED PAPERS AT NEAREST LIBRARY FOR PRIVATE HEATING PURPOSES. RUSSIAN SCIENTISTS MAKING":
        "EVCIL HAYVANLARINIZDAN SIKILDINIZ MI? LINCOLN TUNELINDEKI PETS4FREE'YE TESLIM EDIN, BIZ ONLARA IYI BAKARIZ. YASA DISI GOSTERILER ONEMLI ABD SEHIRLERINI SARDI - ETKILI KUVVETLERIMIZ COK SAYIDA EYLEMCIYI YAKALADI, SORGUYA CEKILIP ALASKA'DAKI ISLAH KAMPLARINA GONDERILECEKLER. AILELERINIZI DOYURMAKTA ZORLANIYOR MUSUNUZ? TUM KAYITLI ISCILER HER HAFTA LINCOLN TUNELINDEKI FOODS4FREE'DEN 1 KILO KIYMA ALABILIR. KOLERA SALGINI DURDURULABILIR - VATANDASLARIN ATIKLARI VE CESETLERI KAMUSAL ALANLARA ATILMAMALIDIR. GELECEK AYDAN ITIBAREN YENI DOGAN BEBEKLERIN BOYNUNA SOSYAL GUVENLIK NUMARASI DOVME YAPILACAKTIR. UNUTMAYIN - YALNIZCA KAYITLI ISCILER HASTANE HIZMETINDEN YARARLANABILIR. YENI DUZEN ALTINDA SURESIZ HAPIS CEZASI GEREKTIREN YENI SUCLAR: GRAFITI, SOKAK BASKETBOLU VE KAYKAY. ESKI AMERIKAN BAYRAGI BULUNDURMANIN CEZASI ARTIK OLUMDUR. KAYITLI ISCILER HER HAFTA EN YAKIN KUTUPHANEDEN ISINMA AMACLI 10 POUND YANICI MADDE VE KAGIT ALABILIR.",

    "POWER RESTORED":
        "ELEKTRIK GERI GELDI",

    "RIOTING REPORTED IN ATLANTA, LOS ANGELES AND CHICAGO - MINOR CASUALTIES - OUR TROOPS ARE IN CONTROL. DOCUMENTS FOUND BY RUSSIAN RESEARCHERS PROVE THAT LAST THREE AMERICAN PRESIDENTS WERE CORRUPT, INVOLVED IN ASSASSINATION ATTEMPTS ON FOREIGN LEADERS AND CHEATED ON THEIR WIVES. IT'S FALL IN NEW YORK - LOG ON TO OUR WEBSITE FOR BEAUTIFUL PICTURES OF HAPPY CITIZENS ENJOYING LIFE. ALSO FIND TASTY RECIPES - 7 WAYS TO TURN ENTRAILS INTO A FEAST. ONLY 9 SOVIET YAGUKOV AIRPLANES HAVE CRASHED THIS WEEK, BRINGING BACK OPTIMISM IN THE TOURIST INDUSTRY. ANGRY SHAREHOLDERS DEMONSTRATING IN WASHINGTON AGAINST THE NATIONALIZATION OF BIMM, DORF, COCO-LOCO AND MANY MORE. MOST WERE ARRESTED AND SENT TO CAMPS.":
        "ATLANTA, LOS ANGELES VE CHICAGO'DA ISYANLAR BILDIRILDI - KUCUK KAYIPLAR - ASKERLERIMIZ KONTROLU SAGLADI. RUS ARASTIRMACILARIN BULDUGU BELGELER, SON UC AMERIKAN BASKANININ YOZLASMIS OLDUGUNU GOSTERIYOR. NEW YORK'TA SONBAHAR - MUTLU VATANDASLARIN RESIMLERI ICIN SITEMIZE GIRIN. BU HAFTA YALNIZCA 9 SOVYET UCAGI DUSTU. DEVLESTIRILMEYE KARSI GOSTERI YAPAN HISSEDARLAR TUTUKLANDI VE KAMPLARA GONDERILDI.",

    "Key figure captured":
        "Kilit isim yakalandi",

    "Repentant brother of \"Freedom Phantom\"":
        "\"Ozgurluk Hayaleti\"nin pisman olan kardesi",

    "We have breaking news in the war against the rebels. Earlier tonight a rebel stronghold was successfully captured by our troops. The head of the group is  one of the most prominent leaders and symbols of the underground resistance;  none other than the brother of the alleged “Freedom Phantom”. The “Phantom” has been unmasked; his real name is Christopher Stone, a 32 year old plumber.":
        "Isyancilara karsi savasta son dakika haberi: Bu gece bir isyanci kalesi ele gecirildi. Grubun basi sozde \"Ozgurluk Hayaleti\"nin kardesidir. \"Hayalet\"in maskesi dusuruldu; gercek adi 32 yasindaki tesisatci Christopher Stone'dur.",

    "After a brief interrogation by our intelligence officers, the brother - Troy Stone - confessed to his participation in many crimes carried out by the rebel group. Now repentant, Troy Stone has agreed to send a plea to his brother to stop further terrorist activities. We take you live to a press conference at City Hall. . .":
        "Kisa bir sorgunun ardindan Troy Stone, bircok suca katildigini itiraf etti. Pisman olan Troy Stone, kardesine teror eylemlerini durdurmasi icin cagri yapmayi kabul etti. Sizi Belediye Binasi'ndaki canli basin toplantisina goturuyoruz. . .",

    "Citizens of New York: A dark chapter in your history is drawing to a close. Here now, is the brother of the “Freedom Phantom”, with a special plea to his brother to desist from further fighting.":
        "New York vatandaslari: Tarihinizdeki karanlik bir bolum sona eriyor. Simdi karsinizda, kardesine savasmaktan vazgecmesi icin ozel bir cagri yapmak uzere \"Ozgurluk Hayaleti\"nin kardesi var.",

    ". . .ahem…mmm. . . M-my brother and I were just bored, and sort of drifted into crime at a young age due to a lack of direction, ideals and playing video games all night - violent ones. The society we grew up in kind of abandoned us, but it’s never too late to straighten out. So um, Chris – for my sake, and the sake of the New System - I beg you to stop your terrorist activities. Surrender to the authorities, and they will treat you fairly – the Soviet government gives you their word of honor - just please do as they ask!":
        ". . .ooo...mmm. . . K-kardesim ve ben sadece sikilmistik, genc yasta suca suruklendik. Chris - benim hatrim icin ve Yeni Duzen'in hatri icin - terorist eylemlerini durdurman icin sana yalvariyorum. Yetkililere teslim ol, sana adil davranacaklar - Sovyet hukumeti seref sozu veriyor - lutfen sadece istediklerini yap!",

    "Everything I said was LIES! They forced me, Chris! Don’t believe their stinking propaganda! KEEP FIGHTING!!! SET US ALL FREE!!! Uuuurgh. . . Arrrg. . . GET YOUR HANDS. . .":
        "Soyledigim her sey YALANDI! Beni zorladilar Chris! Onlarin pis propagandasina inanma! SAVASMAYA DEVAM ET!!! HEPIMIZI KURTAR!!! Uuuurgh. . . Arrrg. . . CEKIN ELLERINIZI. . .",

    "Ahem! And. . . now to the weather for tomorrow - I hear it's getting colder, Comrade Ilyana?":
        "Oho! Ve. . . simdi yarinki hava durumu - duyduguma gore hava giderek soguyor, Yoldas Ilyana?",

    "REBEL GROUP INFILTRATED":
        "ISYANCI GRUBA SIZILDI",

    "TROY STONE":
        "TROY STONE",

    "REBELS PLEDGE FOR PEACE":
        "ISYANCILAR BARIS SOZU VERDI",

    "TOMORROW IS COSMONAUT'S DAY - TO CELEBRATE, CURFEW IS LIFTED UNTIL 10 PM. ENCOURAGE YOUR KIDS TO JOIN THE KOMSOMOL - THE COMMUNIST YOUTH MOVEMENT OFFERS A VARIETY OF EXCITING ACTIVITIES - NO MORE CHURCH, BUT LOTS OF SPORTS! NEW FINDINGS PROVE THAT RUSSIAN TRIBES CROSSING THE BERING STRAIT SEVERAL THOUSAND YEARS AGO ORIGINALLY INHABITED AMERICA - AN IMPERIALISTIC INVASION IN 1492 EXTERMINATED OUR FOREFATHERS HERE. PLANS TO CULTIVATE THE MIDWEST PLAINS - NEW AND IMPROVED GRAINS WILL YIELD CROPS 5 TIMES BIGGER THAN USUAL AND IN LESS TIME. REPORTS ON BIRTH DEFECTS IN AREAS ALREADY USING THESE GRAINS LARGELY EXAGGERATED, SAY OUR EXPERTS. DUE TO DEPLETION OF SOUTH AMERICAN RAIN FOREST, TOILET PAPER WILL BE ON RATION AS OF TOMORROW FOR ALL CITIZENS - EXCEPT THE RUSSIAN AUTHORITIES AND MILITARY FORCES. SCIENTISTS ARE WORKING ON AN ALTERNATIVE MADE OUT OF SEAWEED. A GIANT TSUNAMI WILL HIT NORTHERN JAPAN IN 7 HOURS DUE TO THE RAPIDLY CHANGING WORLD CLIMATE - SEVERAL JAPANESE SHIPS HAVE SOUGHT REFUGE IN RUSSIAN PORTS, BUT KINDLY BEEN REFUSED. OUR NAVY IN VLADIVOSTOCK NEED THE PORTS FOR THEIR UPCOMING FALL MANOEUVRES. FAMOUS DRAKEWORKS CARTOONS IS LUCKY ENOUGH TO BE CHOSEN FOR THE HONOUR OF MAKING \"THE LIFE AND TIMES OF JOSEPH STALIN - OUR BELOVED FATHER AND NATIONAL HERO\".":
        "YARIN KOZMONOT GUNU - KUTLAMAK ICIN SOKAGA CIKMA YASAGI SAAT 22:00'YE KADAR KALDIRILDI. COCUKLARINIZI KOMSOMOL'A KATILMAYA TESVIK EDIN. YENI BULGULAR, BINLERCE YIL ONCE BERING BOGAZI'NI GECEN RUS KABILELERININ AMERIKA'NIN ILK YERLESIMCILERI OLDUGUNU KANITLIYOR. YARINDAN ITIBAREN TUVALET KAGIDI KOTAYA BAGLANACAKTIR. DEV BIR TSUNAMI 7 SAAT ICINDE KUZEY JAPONYA'YI VURACAK. MESHUR DRAKEWORKS CIZGI FILMLERI 'JOSEF STALIN'IN HAYATI VE DONEMI'NI YAPMA ONURUNA ERISTI.",

    "Citizens - stand by for celebration details.":
        "Vatandaslar - kutlama detaylari icin beklemede kalin.",

    "Long live our new leader Bulba!":
        "Yeni liderimiz Bulba cok yasa!",

    "This is Tatiana Kempinski at SAFN studios in New York: The Soviet Armed Forces have tonight declared a total victory over the underground rebellion. After numerous barbaric attacks by the rebels on Soviet bases in each borough of New York, the situation is finally under control. We continue to receive reports of minor incidents around the city, but it is clear that the rebels have been defeeated. Tragically, our beloved Commander-in-Chief General Tatarin has paid the ultimate price in his relentless fight against the “Freedom Phantom” and his henchmen. He was assassinated earlier tonight in a dastardly rebel ambush. We go now live to Governor’s Island, where the funeral ceremony is about to commence.":
        "New York SAFN studyolarindan Tatiana Kempinski bildiriyor: Sovyet Silahli Kuvvetleri bu gece yeralti isyanina karsi kesin zafer ilan etti. Durum nihayet kontrol altinda. Ne yazik ki sevgili Baskomutanimiz General Tatarin kallesce bir isyanci pususunda suikaste ugradi. Simdi cenaze toreninin baslamak uzere oldugu Governor's Island'a canli baglaniyoruz.",

    "Comrades! This is indeed a day of infamy. We are gathered here today to bid farewell to our great leader. We came to restore law and order, to secure peace and stability in this region and save the American citizens from brutality and exploitation – and this is the brave General's reward. He shall not have died in vain – as 2nd in command, I respectfully take his place, and I vow today to track down the cowardly scum who committed this outrage. . . I swear revenge today, on the so-called “Freedom Phantom” Christopher Stone and puny 'army' of remaining rebels for the brutal killing of our beloved leader Tatarin. Stone, your days are numbered – you and your followers will be flushed out and destroyed like sewer rats! Long live the Soviet Union! Long live the Revolution! Long live Soviet Government of The United States!":
        "Yoldaslar! Bugun gercekten kara bir gundur. Buyuk liderimize veda etmek icin toplandik. Bu bolgeye kanun ve nizam getirmek icin geldik ve cesur Generalimizin mukafati bu oldu. Onun olumu bosa gitmeyecek - 2. komutan olarak yerini aliyorum ve bu alcaligi yapanlari bulacagima ant iciyorum. . . Christopher Stone'dan ve cılız isyanci ordusundan intikam alacagima yemin ederim. Stone, gunlerin sayili - kanalizasyon fareleri gibi yok edileceksiniz! Yasasin Sovyetler Birligi! Yasasin Devrim! Yasasin Amerika Birlesik Devletleri Sovyet Hukumeti!",

    "S.A.F. DECLARES TOTAL VICTORY!":
        "SAF KESIN ZAFER ILAN ETTI!",

    "OUR BELOVED LEADER TATARIN ASSASSINATED":
        "SEVGILI LIDERIMIZ TATARIN SUIKASTE UGRADI",

    "New Yorkers, fellow Americans. . . I am Chris Stone, the so-called \"Freedom Phantom\". I stand before you today a free man and I vow to die a free man. Like you my world was shattered eight long months ago. I watched as my family and friends were tortured, captured and killed. I have nothing left of my former life. . . except the hope for a better future. . . a better future for our children - the American dream. I for one still believe in that dream. We've read this in our schoolbooks as children, now is the time for us to embrace those ideals and stand up against the weight of Tyranny. We have a duty to ourselves to throw off our oppressors. When I look around this city I do not see smoldering ruins. . . no, instead I see a sleeping army, ready to awaken.  The world is watching us now. . . how we respond will prove our claim. I stand before you and the world today to reaffirm the pledge our forefathers made to each other, and for each of us - to protect our lives, our fortunes and our self-worth. So I ask you now to take up arms against the evil invaders and yell in their faces that THEY WILL NEVER TAKE OUR FREEDOM!!":
        "New Yorklular, vatandaslarim. . . Ben Chris Stone, nam-i diger \"Ozgurluk Hayaleti\". Bugun karsinizda ozgur bir adam olarak duruyorum ve ozgur bir adam olarak olecegime yemin ediyorum. Tipki sizin gibi benim de dunyam sekiz uzun ay once yikildi. Ailemin ve dostlarimin iskence gordugunu, esir alindigini ve olduruldugunu izledim. Eski hayatimdan geriye hicbir sey kalmadi. . . daha iyi bir gelecek umudu disinda. . . cocuklarimiz icin daha iyi bir gelecek - Amerikan ruyasi. Ben hala o ruyaya inaniyorum. Cocukken bunu okul kitaplarimizda okuduk, simdi bu ideallere sarilmanin ve Zulmun agirligina karsi dik durmanin zamanidir. Bizi ezenleri sirtimizdan atmak kendimize olan borcumuzdur. Bu sehre baktigimda dumanlar tuten enkazlar gormuyorum. . . hayir, aksine uyanmaya hazir uyuyan bir ordu goruyorum. Dunya simdi bizi izliyor. . . verecegimiz karsilik davamizi kanitlayacak. Bugun atalarimizin birbirine ve her birimize verdigi sozu tazelemek icin buradayim - hayatlarimizi, varligimizi ve onurumuzu korumak icin. Simdi sizden bu zalim isgalcilere karsi silaha sarilmanizi ve yuzlerine haykirmanizi istiyorum: BIZIM OZGURLUGUMUZU ASLA ALAMAYACAKSINIZ!!",

    "Damn it! They're breaking up the ice - HEAD FOR THE SHORE AS FAST AS YOU CAN!":
        "Lanet olsun! Buzlari kiriyorlar - OLABILDIGINCE HIZLI KIYIYA DOGRU KOSUN!",

    "Hey, Chris – I’ve been looking all over for you - what’s wrong? Why don’t you celebrate with me and the rest of the crowd?":
        "Hey, Chris - her yerde seni ariyordum, ne oldu? Neden benimle ve digerleriyle birlikte kutlamiyorsun?",

    "There's nothing for me to celebrate - they'll be back - with bigger guns and more soldiers.":
        "Benim icin kutlanacak bir sey yok - geri gelecekler - daha buyuk silahlarla ve daha cok askerle.",

    "I know how you feel, but you stood up for what you believed in, you fought for freedom. And you won, Chris - we all won.":
        "Ne hissettigini biliyorum, ama inandigin sey icin ayaga kalktin, ozgurluk icin savastin. Ve kazandin Chris - hepimiz kazandik.",

    "Today, this morning - kids here will wake up to the burning ruins of New York. And it’s my fault!":
        "Bugun, bu sabah - buradaki cocuklar New York'un alevler icindeki yikintilarina uyanacak. Ve bu benim sucum!",

    "No, it isn’t! This is our land – you helped us remember what’s so great about it. It may be hard to define, but when you haven’t got it anymore, you know exactly what it is. It’s about loss – and I don’t wanna lose you.":
        "Hayir, degil! Burasi bizim topragimiz - buranin neden bu kadar guzel oldugunu hatirlamamizi sagladin. Belki tanimlamasi zordur, ama artik sahip olmadiginda onun ne oldugunu tam olarak anlarsin. Bu kaybetmekle ilgili - ve ben seni kaybetmek istemiyorum.",

    ". . . you. . . you'd better go.":
        ". . . sen. . . gitsen iyi olur.",

    "You're saying that like. . . you might change your mind.":
        "Bunu sanki. . . fikrini degistirebilirmissin gibi soyluyorsun.",

    "That's why it's better that you go.":
        "Iste bu yuzden gitmen daha iyi.",

    "Hey, guys – you’re gonna miss the party – oh, did I interrupt something? Hey, hey – don't get all mushy on me now! Don't go writing love letters in the sand while I babysit the Kid.":
        "Hey millet - partiyi kaciracaksiniz - ah, bir sey mi boldum? Hey, hey - simdi duygusallasmayin hemen! Ben Kid'e dadiyik yaparken siz kuma ask mektuplari yazmaya kalkmayin sakin.",

    "No. . . wait, I was just saying. . . aw, man – am I gonna stand here at the end, looking like an idiot?":
        "Hayir. . . dur, sadece diyordum ki. . . of ya - en sonunda burada bir aptal gibi dikilip duracak miyim?",

    "Look, I mean I'm just like everyone else - I have dreams too. I want the same things! Sometimes I can't say it right - it's, uh. . . all about loving your fellow man right? Even if it takes losing your whole world to find them.":
        "Bakin, yani ben de herkes gibiyim - benim de hayallerim var. Ayni seyleri istiyorum! Bazen dogru ifade edemiyorum - bu, sey. . . insanlari sevmekle ilgili degil mi? Onlari bulmak butun dunyani kaybetmek anlamina gelse bile."
}

MOVIECUTS_TRANSLATIONS = {
    orig: to_ascii_turkish(trans)
    for orig, trans in MOVIECUTS_TRANSLATIONS_RAW.items()
}
