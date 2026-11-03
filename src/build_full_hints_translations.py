# -*- coding: utf-8 -*-
import json, sys, os, re

sys.path.append(r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline')
from turkish_ascii_converter import to_ascii_turkish
from build_hints_objectives import HINTS_DICT

# Load hints_unmapped.json
path = r'C:\Users\SQT\.gemini\antigravity\brain\9015f081-4636-41e6-97ad-c79d171ab886\scratch\translation_pipeline\hints_unmapped.json'
with open(path, 'r', encoding='utf-8') as f:
    unmapped = json.load(f)

NEW_TRANS = {}

# Specific long dialogues and story briefings
story_dialogues = {
    "This is our base. It's a safe zone. We store equipment here. With complete safety you can choose the weapons you want to take with you into combat.":
        "Burasi bizim ussumuz. Guvenli bir bolgedir. Ekipmanlari burada sakliyoruz. Catismaya goturmek istediginiz silahlari tam bir guvenlik icinde buradan secebilirsiniz.",
    "Lets go over to the table and take a look at the map.":
        "Masaya gecelim ve haritaya bir goz atalim.",
    "Chris - we need to take the Police Station. This will weaken the Soviets grip on the area.":
        "Chris - Polis Merkezini ele gecirmemiz gerek. Bu, Sovyetlerin bolgedeki hakimiyetini zayiflatacaktir.",
    "I have reports that the Soviets have set up a command center in the Post Office. Taking the building will be a great symbolic victory for the resistance.":
        "Sovyetlerin Postanede bir komuta merkezi kurduguna dair raporlar var. Binayi ele gecirmek direnis icin buyuk bir sembolik zafer olacaktir.",
    "Chris - we also have reason to believe that your brother is being held captive at the Post Office.":
        "Chris - ayrica kardesinin Postanede esir tutulduguna inanmak icin sebeplerimiz var.",
    "Once you take their base, it is imperative that you fly the flag from the rooftop. People will see it and start to believe that we can actually win this war! It will prove there are cracks in the Soviet war machine.":
        "Uslerini ele gecirdiginizde, catıya bayragi cekmeniz sart. Insanlar bunu gorecek ve bu savasi gercekten kazanabilecegimize inanmaya baslayacak! Sovyet savas makinesinde catlaklar oldugunu kanitlayacak.",
    "Take control of the precinct building and raise the flag I gave you.":
        "Karakol binasinin kontrolunu ele gecir ve sana verdigim bayragi cek.",
    "Raise the flag once you've taken control of the Post Office.":
        "Postanenin kontrolunu ele gecirdiginde bayragi cek.",
    "The Soviets have a large fuel station that they use for distributing fuel to their vehicles. Destroying it will disrupt their logistics in this sector.":
        "Sovyetlerin araclarina yakit dagitmak icin kullandiklari buyuk bir yakit istasyonu var. Orayi yok etmek bu sektordeki lojistiklerini felce ugratacaktir.",
    "Destroy the fuel tanks at the fuel depot. You will need C4 to accomplish this.":
        "Yakit deposundaki yakit tanklarini yok et. Bunu basarmak icin C4 patlayiciya ihtiyacin olacak.",
    "I'm counting on you Chris. Good luck!":
        "Sana guveniyorum Chris. Iyi sanslar!",
    "Isabella has information about the resistance network. We must rescue her before the Soviets break her spirit.":
        "Isabella direnis agi hakkinda bilgilere sahip. Sovyetler onun direncini kirmadan once onu kurtarmaliyiz.",
    "Chris - the Republican Army has a sniper positioned up on the fuel station. Watch out for him.":
        "Chris - Sovyet Ordusunun yakit istasyonunun tepesinde bir keskin nisancisi var. Ona dikkat et.",
    "It's critical that we destroy that fuel station - it'll help starve their vehicles in this area.":
        "O yakit istasyonunu yok etmemiz cok onemli - bu bolgedeki araclarini yakitsiz birakmaya yardimci olacak.",
    "Listen, Isabella is being held in the Police Station. We need to rescue her!":
        "Dinle, Isabella Polis Merkezinde tutuluyor. Onu kurtarmamiz gerek!",
    "Your brother Troy is being held in the Post Office, I'm sure you'll want to get him out.":
        "Kardesin Troy Postanede tutuluyor, eminim onu oradan cikarmak istersin.",
    "I owe ya one Chris - don't forget about Isabella, I don't think the Reds are treating her very well.":
        "Sana bir can borcluyum Chris - Isabella'yi unutma, Kizillarin ona pek iyi davrandigini sanmiyorum.",
    "Capture the old Fire Station. Soviet reinforcements in this section are coming from that direction.":
        "Eski Itfaiyeyi ele gecir. Bu sektordeki Sovyet takviyeleri o yonden geliyor.",
    "Seize the warehouse buildings. This is where the Soviets store their supplies and munitions.":
        "Depo binalarini ele gecir. Sovyetler erzak ve muhimmatlarini burada depoluyor.",
    "Take control of the old Hotel. The Soviets have established a base of operations there.":
        "Eski Otelin kontrolunu ele gecir. Sovyetler orada bir harekat ussu kurdu.",
    "Chris, for three months the Soviets have been pouring soldiers and equipment into this sector. We need to push them back.":
        "Chris, uc aydir Sovyetler bu sektore asker ve techizat yigiyor. Onlari geri puskurtmeliyiz.",
    "Yeah man, the Reds are everywhere and they brought plenty of toys. Yesterday I saw a gunship helicopter patrolling the docks.":
        "Evet dostum, Kizillar her yerde ve yanlarinda bolca oyuncak getirmisler. Dun rıhtımda devriye gezen bir saldiri helikopteri gordum.",
    "Hang on, let's get real. That bridge is important, but we really need to deal with that gunship. It's tearing our guys apart.":
        "Dur bir dakika, gercekci olalim. O kopru onemli, ama asil su helikopterin icabina bakmamiz gerek. Adimlarimizi biciyor.",
    "The Soviets are holding prisoners somewhere near the Hotel - we need to free them!":
        "Sovyetler Otelin yakinlarinda bir yerde esirler tutuyor - onlari kurtarmamiz lazim!",
    "Oh yeah! We're talkin' one sweet fireworks show when we lay som'a that C4 on those tanks!":
        "Iste bu! O tanklara biraz C4 yerlestirdigimizde muazzam bir havai fisek gosterisi izleyecegiz!",
    "Nice work Chris! I heard ya took out the bridge. Personally, I woulda gone with a bigger boom, but it got the job done.":
        "Guzel is Chris! Kopruyu havaya ucurdugunu duydum. Sahsen ben daha buyuk bir patlama yapardim ama isini gordu.",
    "It's now or never Chris - with the Fire Station under our control, we have a clear shot at their headquarters.":
        "Ya simdi ya hic Chris - Itfaiye kontrolumuzdeyken, karargahlarina dogrudan bir yolumuz var.",
    "Blowing up that Fuel Station really weakened the enemy - we should have an easier time now.":
        "O Yakit Istasyonunu havaya ucurmak dusmani gercekten zayiflatti - artik isimiz daha kolay olmali.",
    "Oh, there you are. Good work handling that Soviet stronghold… very inspired.":
        "Ah, iste buradasin. O Sovyet kalesini halletme konusunda iyi is cikardin... gercekten takdire sayan.",
    "You know - that Soviet compound by the cinema would be a nice addition to our territory.":
        "Bilirsin - sinemanin yanindaki su Sovyet yerleskesi bolgemize guzel bir katki olurdu.",
    "Chris, my man - Ivan's got that main base in the central warehouse - it's up to you to clear it out.":
        "Chris dostum - Ivan'in merkez depoda ana ussu var - orayi temizlemek sana kaldi.",
    "The Reds are sittin' pretty by the Power Station - let's see if they're afraid of the dark.":
        "Kizillar Elektrik Santralinde rahat rahat oturuyor - bakalim karanliktan korkuyorlar miymis.",
    "They're in control of the Power Station - we gotta cut off the juice.":
        "Elektrik Santralinin kontrolu onlarda - elektrigi kesmemiz lazim.",
    "I'm sorry to have to tell you Chris, but your brother is dead. Shortly after that broadcast, they executed him.":
        "Bunu soylemek zorunda kaldigim icin cok uzgunum Chris, ama kardesin oldu. O yayindan kisa bir sure sonra onu idam ettiler.",
    "Man, I can't take this! Tatarin's gonna pay for killin' Troy! He's gonna regret the day he ever stepped foot in America!":
        "Dostum, buna dayanamiyorum! Troy'u oldurdugu icin Tatarin bedelini odeyecek! Amerika'ya ayak bastigi gune lanet edecek!",
    "Bagz! - Chris, I'm sorry. I know it hurts, but we need to keep a cool head.":
        "Bagz! - Chris, cok uzgunum. Caninin yandigini biliyorum ama sakin kalmaliyiz.",
    "Yes, well… you must understand that the only action now that will truly hurt them is to strike at the heart of their command - Tatarin.":
        "Evet, sey... anlamalisin ki artik onlari gercekten yaralayacak tek hamle, komuta kademelerinin kalbine vurmaktir - Tatarin'e.",
    "That's a brilliant plan Jones! Wadda we do? Invite ourselves over for a cocktail at his fortified villa?":
        "Harika bir plan Jones! Ne yapacagiz? Korunakli villasina bir kokteyl icin kendimizi mi davet edecegiz?",
    "We gotta get into that TV station and blow the rest of their security system.":
        "O televizyon kanalina girmeli ve guvenlik sistemlerinin geri kalanini havaya ucurmaliyiz.",
    "Some of their fly-boys are set up behind the Warehouse. Blow their nest!":
        "Su havacilarin bazilari Deponun arkasina yerlesmis. Yuvalarini baslarina yik!",
    "Check this out Chris! We gotta go prime time and shut down the TV Studio. Tell New York the truth!":
        "Buna bak Chris! Canli yayina gecip TV Studyosunu ele gecirmeliyiz. New York'a gercekleri anlat!",
    "Those damn Reds are sittin up inside my old school! I might have skipped a few classes, but nobody desecrates my school!":
        "O lanet Kizillar benim eski okulumun icine coreklenmisler! Bazi dersleri asmis olabilirim ama kimse okulumu kirletemez!",
    "I heard they bagged up some of our boys in the school yard - you should help them out.":
        "Okul bahcesinde bizim cocuklardan bazilarini kistirdiklarini duydum - onlara yardim etmelisin.",
    "Whatever Dog!. . . Yo Chris, we got some C4 out at the base in Yonkers. Way to go!":
        "Aman her neyse!. . . Hey Chris, Yonkers'taki usste biraz C4 bulduk. Helal olsun!",
    "Punk kids! No respect - I got brains, I can handle myself.":
        "Saygisiz veletler! Hic saygi yok - kafam calisiyor, basimin caresine bakabilirim.",
    "This went south in a hurry. We lost everybody out here. We gotta blow that artillery bunker!":
        "Isler cok cabuk sarpa sardi. Buradaki herkesi kaybettik. O topcu siginagini havaya ucurmamiz lazim!",
    "Someone's gotta do something about the shelling, otherwise we'll never get across the ice!":
        "Birisi su bombardimana karsi bir sey yapmali, yoksa buzu asla gecemeyiz!",
    "I hate being on the losing team - lead on, buddy!":
        "Kaybeden tarafta olmaktan nefret ederim - yolu goster ahbap!",
    "It's time to stop the Soviet propaganda.  Check this - we're gonna take the broadcast tower!":
        "Sovyet propagandasini durdurma zamani geldi. Bak simdi - yayin kulesini ele gecirecegiz!",
    "Check this out! I've found out where they've got a Soviet elite training camp.":
        "Sunu dinle! Sovyet elit egitim kampinin nerede oldugunu ogrendim.",
    "Sweet-sweet, I like the new digs little man! Check this out, you even got a sewer map!":
        "Harika, yeni siginagi cok sevdim kucuk adam! Suna bak, kanalizasyon haritan bile var!",
    "Me n' some of my peeps from the block used to sneak down here and hang out.":
        "Ben ve mahalleden birkac arkadas eskiden buraya gizlice iner, takilirdik.",
    "Governor’s Island *looks* like an impenetrable fortress, but they have a weak spot.":
        "Governor's Island gecilmez bir kale gibi *gorunuyor*, ama zayif bir noktalari var.",
    "We took a lickin', Chris - but the fight for freedom ain't over!":
        "Iyi darbe aldik Chris - ama ozgurluk mucadelesi henuz bitmedi!",
    "They kicked our butts once - now let's return the favor!":
        "Bir kez canimizi yaktilar - simdi karsiligini verme zamani!",
}

for k, v in story_dialogues.items():
    NEW_TRANS[k] = v

# Process remaining unmapped items
for it in unmapped:
    if it in NEW_TRANS or it in HINTS_DICT:
        continue
    
    # Generic button/tag replacements
    tr = it
    tr = tr.replace("Press $TapFire$ to fire.", "Ates etmek icin $TapFire$ tusuna basin.")
    tr = tr.replace("To talk to people, approach them and press $TapUse$", "Insanlarla konusmak icin yanlarina yaklasin ve $TapUse$ tusuna basin.")
    tr = tr.replace("To talk to people, approach\\n\nthem and press $TapUse$", "Insanlarla konusmak icin yanlarina\\n\nyaklasin ve $TapUse$ tusuna basin.")
    tr = tr.replace("To throw a Molotov, press $TapFire$", "Molotof atmak icin $TapFire$ tusuna basin.")
    tr = tr.replace("Press $TapFire$ to use the Medic Kit.", "Saglik Cantasini kullanmak icin $TapFire$ tusuna basin.")
    tr = tr.replace("Press $HoldCrouch$ to crouch.", "Egilmek icin $HoldCrouch$ tusuna basin.")
    tr = tr.replace("Go to the flag and press $TapUse$ to hoist the\\n\nStars and Stripes and secure the location.",
                    "Bayraga gidin ve bolgeyi guvenceye alip\\n\nbayragi cekmek icin $TapUse$ tusuna basin.")
    tr = tr.replace("Use $PC_TapMWheelUp$ or $PC_TapMWheelDown$ to select the Medic Kit.",
                    "Saglik Cantasini secmek icin fare tekerlegini yukari veya asagi kaydirin.")
    tr = tr.replace("Use $PC_TapMWheelUp$ or $PC_TapMWheelDown$ to select the Molotov.",
                    "Molotofu secmek icin fare tekerlegini yukari veya asagi kaydirin.")
    tr = tr.replace("Press the $HoldDefend$ to order one squad member to remain at the machine gun.",
                    "Bir tim uyesine makineli tufekte kalmasini emretmek icin $HoldDefend$ tusuna basin.")
    tr = tr.replace("Click and hold left thumbstick to aim,\\n then pull the right trigger to fire weapon",
                    "Nisan almak icin sol basparmak tusunu basili tutun,\\n ardindan ates etmek icin sag tetigi cekin.")
    tr = tr.replace("Pull the left trigger to climb.", "Tirmanmak icin sol tetigi cekin.")
    tr = tr.replace("Click and hold Left Thumbstick to aim at a\\n\nplace on the ground, then press $HoldAttack$ to send off\\n\na squad member.",
                    "Yerdeki bir noktaya nisan almak icin Sol Cubuga basili tutun,\\n\nardindan bir tim uyesini gondermek icin $HoldAttack$ tusuna basin.")
    tr = tr.replace("Use left thumbstick to move and turn.", "Hareket etmek ve donmek icin sol cubugu kullanin.")
    tr = tr.replace("Use left thumbstick to move and\\n\nright thumbstick to look around.", "Hareket etmek icin sol, etrafa bakmak icin\\n\nsag cubugu kullanin.")
    tr = tr.replace("Pull the right trigger to attack.", "Saldirmak icin sag tetigi cekin.")
    tr = tr.replace("Click and hold the right thumbstick\\n\nto bring up the inventory, then select\\n\nthe weapon using the directional pad.",
                    "Envanteri acmak icin sag cubuga basili tutun,\\n\nardindan yon tuslarini kullanarak silahi secin.")
    tr = tr.replace("Click and hold the right thumbstick to bring\\n\nup the inventory, then select the weapon\\n\nusing the directional pad.",
                    "Envanteri acmak icin sag cubuga basili tutun,\\n\nardindan yon tuslarini kullanarak silahi secin.")
    tr = tr.replace("Pull the right trigger to attack.", "Saldirmak icin sag tetigi cekin.")
    tr = tr.replace("Pull the right trigger to fire.", "Ates etmek icin sag tetigi cekin.")
    tr = tr.replace("Pull the right trigger to throw a Molotov.", "Molotof atmak icin sag tetigi cekin.")
    tr = tr.replace("Pull the right trigger to use the Medic Kit.", "Saglik Cantasini kullanmak icin sag tetigi cekin.")
    tr = tr.replace("PRISONERS", "MAHKUMLAR")
    tr = tr.replace("Raise Flag on Post Office.", "Postaneye Bayrak Cek.")
    tr = tr.replace("Destroy Gas Station.", "Benzinligi Yok Et.")
    tr = tr.replace("Free your brother Troy.", "Kardesin Troy'u Kurtar.")
    tr = tr.replace("Raise Flag on Police Station.", "Polis Merkezine Bayrak Cek.")
    tr = tr.replace("NORTHEAST \nBUNKER", "KUZEYDOGU\nSIGINAGI")
    tr = tr.replace("NORTHWEST \nBUNKER", "KUZEYBATI\nSIGINAGI")
    tr = tr.replace("SOUTHWEST \nBUNKER", "GUNEYBATI\nSIGINAGI")
    tr = tr.replace("Raise Flag in front of Harbor.", "Limanin Onune Bayrak Cek.")
    tr = tr.replace("Destroy Tower.", "Kuleyi Yok Et.")
    tr = tr.replace("Raise Flag over Docks.", "Rıhtıma Bayrak Cek.")
    tr = tr.replace("Raise Flag over Warehouse.", "Depoya Bayrak Cek.")
    tr = tr.replace("Raise Flag over Power Plant.", "Elektrik Santraline Bayrak Cek.")
    tr = tr.replace("Raise Flag over TV Station.", "TV Kanalina Bayrak Cek.")
    tr = tr.replace("Raise Flag over Boat Landing.", "Iskeleye Bayrak Cek.")
    tr = tr.replace("Raise Flag over Munitions Depot.", "Muhimmat Deposuna Bayrak Cek.")
    tr = tr.replace("Raise Flag over Artillery.", "Topcu Birligine Bayrak Cek.")
    
    if tr != it:
        NEW_TRANS[it] = tr

print(f'New translations mapped: {len(NEW_TRANS)}')
