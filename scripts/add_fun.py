import json
S={ # silly sentences: (cz, en, emoji scene)
1:[("Dobrý den, čaj. Na shledanou, čaj.","Hello, tea. Goodbye, tea.","🍵👋"),("Ahoj, čaj!","Hi, tea!","🙋🍵")],
2:[("Promiňte, čaj, mluvíte anglicky?","Excuse me, tea, do you speak English?","🍵🇬🇧"),("Ano. Ne. Trochu.","Yes. No. A little.","🤷")],
3:[("Jedno pivo pro kočku, prosím.","One beer for the cat, please.","🐈🍺"),("Medvěd si dá kafe.","The bear will have a coffee.","🐻☕")],
4:[("Sedm koček pije pivo.","Seven cats are drinking beer.","🐈🐈🐈🍺"),("Tři medvědi a jedno kafe.","Three bears and one coffee.","🐻🐻🐻☕")],
5:[("Kolik stojí medvěd? Sto korun.","How much is the bear? A hundred crowns.","🐻💰"),("Taška, účtenka, medvěd. To je všechno.","Bag, receipt, bear. That's all.","🛍️🐻")],
6:[("Kočka jí sýr a pije mléko.","The cat eats cheese and drinks milk.","🐈🧀🥛"),("Máte rohlík pro medvěda?","Do you have a roll for the bear?","🥖🐻")],
7:[("Jmenuji se Rohlík. Jsem z Turecka.","My name is Roll. I'm from Turkey.","🥖🇹🇷"),("Medvěd se učí česky.","The bear is learning Czech.","🐻📚")],
8:[("Kočka má tři děti a jeden rohlík.","The cat has three children and one roll.","🐈👶🥖"),("Táta pije čaj, děti pijí kafe.","Dad drinks tea, the kids drink coffee.","👨🍵👧☕")],
9:[("Dvacet medvědů v tramvaji.","Twenty bears on a tram.","🐻🚋"),("Rohlík stojí sto korun?!","A roll costs a hundred crowns?!","🥖😱")],
10:[("Kde je medvěd? Tam, na záchodě!","Where's the bear? There, in the toilet!","🐻🚽"),("Kočka jde rovně, pak vlevo.","The cat goes straight, then left.","🐈⬆️⬅️")],
11:[("Medvěd nemá jízdenku.","The bear doesn't have a ticket.","🐻🎫"),("Příští zastávka: Rohlík.","Next stop: Roll.","🚋🥖")],
12:[("Kolik je hodin? Čas na pivo.","What time is it? Beer time.","⏰🍺"),("Kočka pije kafe každé ráno.","The cat drinks coffee every morning.","🐈☕🌅")],
13:[("Medvěda bolí hlava. Moc piva.","The bear has a headache. Too much beer.","🐻🤕🍺"),("Kočka má horečku a recept.","The cat has a fever and a prescription.","🐈🌡️📄")],
14:[("Jak se máš, rohlíku?","How are you, roll?","🥖🙂"),("Dobře, děkuji. A vy, pane medvěde?","Fine, thanks. And you, Mr Bear?","🙂🐻")],
15:[("Dám si svíčkovou a sedm knedlíků.","I'll have the svíčková and seven dumplings.","🥩🥟"),("Medvěd platí zvlášť.","The bear pays separately.","🐻🧾")],
16:[("Nejsem medvěd. Jsem rohlík.","I'm not a bear. I'm a roll.","🙅🐻🥖"),("Kočka nemá čas. Má schůzku.","The cat has no time. She has a meeting.","🐈📅")],
17:[("V našem výtahu bydlí medvěd.","A bear lives in our lift.","🛗🐻"),("Klíč je ve sklepě. A medvěd taky.","The key is in the cellar. And the bear too.","🔑🐻")],
18:[("Prší pivo!","It's raining beer!","🌧️🍺"),("Medvěd má deštník, kočka nemá.","The bear has an umbrella, the cat doesn't.","🐻☂️🐈")],
19:[("Chtěl bych sto rohlíků.","I'd like a hundred rolls.","🥖💯"),("Můžu platit rohlíkem?","Can I pay with a roll?","🥖💳")],
20:[("V balíku je medvěd.","There's a bear in the parcel.","📦🐻"),("Kód je sedm, sedm, sedm, sedm.","The code is seven, seven, seven, seven.","🔢")],
21:[("V sobotu jde medvěd na trh.","On Saturday the bear goes to the market.","🐻🧺"),("Kočka je doma, medvěd jde domů.","The cat is at home, the bear is going home.","🐈🏠🐻")],
}
C={ # postcards: emoji, title, text, cz phrase, en
1:("🪝","The háček","The little hook on č, š, ž is called a háček. It comes from a 15th-century spelling reform attributed to Jan Hus, and Slovak, Slovene, Croatian and Lithuanian borrowed it.","háček","little hook"),
2:("🥾","Ahoj on the trail","Czechs say Ahoj for hello and goodbye. On mountain trails, hikers greet every stranger they pass.","Ahoj!","Hi! / Bye!"),
3:("🍺","Pencil marks on paper","In a Czech pub the waiter keeps your tab as pencil lines on a slip of paper. Put your beer mat on top of the glass when you don't want another.","Ještě jedno, prosím.","One more, please."),
4:("🕰️","The Orloj","Prague's astronomical clock has been running since 1410. It's the oldest astronomical clock still working.","orloj","astronomical clock"),
5:("🪙","The crown","Czechia kept its own money: the koruna, which means crown. Cashiers often ask if you have small change.","Máte drobné?","Do you have change?"),
6:("🥖","Rohlík nation","The rohlík is the everyday Czech bread roll, so popular that a big grocery delivery company is named after it.","rohlík s máslem","roll with butter"),
7:("📅","Name days","Every day on the Czech calendar belongs to a first name. On your name day (svátek), friends congratulate you.","Všechno nejlepší!","All the best!"),
8:("🐾","Krtek in space","Krtek, the little mole, is a Czech cartoon from 1956. A Krtek toy flew to the International Space Station in 2011.","Ahoj, Krtečku!","Hi, little mole!"),
9:("🥤","Kofola","Created in Czechoslovakia in 1960 as a home-grown cola. Still loved, and still on tap in many pubs.","Jednu Kofolu, prosím.","One Kofola, please."),
10:("👅","No vowels needed","Czech's most famous tongue-twister has no vowels at all. The r does the vowel's job.","Strč prst skrz krk.","Stick a finger through your throat."),
11:("🚋","Tram city","Prague has one of the largest tram networks in the world, with about 140 km of track. Ride line 22 for a free sightseeing tour.","Dveře se zavírají.","The doors are closing."),
12:("🕝","Half third","Czechs say 2:30 as 'půl třetí', half of the third hour: they count toward the next hour.","půl třetí","half past two"),
13:("👁️","Contact lenses","Soft contact lenses were invented by Czech chemist Otto Wichterle, who made early prototypes with a children's building set.","kontaktní čočky","contact lenses"),
14:("🤖","Robot is Czech","The word robot comes from Karel Čapek's 1920 play R.U.R. His brother Josef suggested it, from 'robota': hard work.","robot","robot"),
15:("🐟","Carp in the bathtub","Before Christmas, many families buy a live carp and keep it in the bathtub for a few days before the Christmas dinner.","kapr","carp"),
16:("🎩","Jára Cimrman","The greatest Czech genius never existed. Fictional inventor Jára Cimrman nearly won a national TV poll of the greatest Czechs.","Jára Cimrman","the genius who never lived"),
17:("🏡","Off to the chata","Many Czech families have a weekend cottage, a chata or chalupa. On Friday afternoons the roads out of town fill up.","Jedeme na chatu.","We're going to the cottage."),
18:("🌧️","Weather sayings","Czechs love weather proverbs. If it rains on St Medard's day (8 June), expect forty days of rain.","Medardova kápě, čtyřicet dní kape.","Medard's rain, forty days of dripping."),
19:("🧊","The sugar cube","The sugar cube was invented in the Czech town of Dačice in 1843, after a sugar factory director's wife cut her finger on a sugar loaf.","kostka cukru","sugar cube"),
20:("🐟","The @ sign is a herring","Czechs call @ 'zavináč', a rolled pickled herring. So your email is jméno zavináč gmail tečka com.","zavináč","rolled herring (@)"),
21:("🏰","Castle country","Czechia has around 2,000 castles and chateaux, one of the densest collections in the world.","hrad","castle"),
}
for n in range(1,22):
  p=f"lessons/{n:03d}.json";d=json.load(open(p))
  d["silly"]=[dict(cz=a,en=b,emoji=c) for a,b,c in S[n]]
  e,t,x,cz,en=C[n];d["postcard"]=dict(emoji=e,title=t,text=x,cz=cz,en=en)
  json.dump(d,open(p,"w"),ensure_ascii=False,indent=1)
print("ok")
