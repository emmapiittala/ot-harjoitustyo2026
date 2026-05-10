**31.3.2026**
- No ei oikee mitää saanu aikasks, meni hermot. 
- Käyttäjä näkee ruudun jossa lukee tähän tulee peli ja klikkaamalla menee 
peliruutuun mihin tule kysymykset

**13.4.2026**
  - Aloitettu projekti alusta. Vaihdoin pygamesista tkinteriin ja päivä on mennyt opetellessa sitä.
  - Saatu tehtyä "etusivu"(Menu) jossa nappi mistä pääsee peliin -> ja game.py missä nappi että pelin voi lopettaa -> siirtyy etusivulle.

    
**14.4.2026**
  - Tehty testejä sekä napit mistä voi valita vastauksen(ei vielä toiminnallisuutta.

**20.4.2026**
- Projektiin lisätty quizzes.py mistä haetaan kysymykset, vastausvaihtoehdot ja oikeat vastaukset, jottei game.py menisi aivan tukkoon.
- Game.py lisätty kysymys näkyviin sekä checkbuttoneita muokattu niin että niissä näkyvät oikeat vastausvaihdot.
    
**21.4.2026**
- Gameover tehty sekä siirretty game.py logiikkaa logic.py
- Vastausten tarkistusnappi jossa toiminnallisuus.
- Seuraava kysymys-nappi ja toiminnallisuus
- poistettu vanhat testit ja tehty muutama uusi.
- lisätty muutama testikysymys.
    

**28.4.2026**
- Muutettu projektin kansiorakennnetta selkeämmäksi.
- Korjattu importteja uuden rakenteen takia. 
- Pylintin konfigurointia. Toivottavast toimii nytten.
- Korjattu testejä sekä lisätty uusia testejä.
- Siivottu koodia ja lisätty docstringit.

**5.5.2026**
- Peliin lisätty pisteet mitä pystyy seuraamaan peliä pelatessa.
- Gameoverissa näkyy kierroksen pisteet sekä kaikki aikaisempien pelien pisteet.
- Pisteet tallennetaan JSON-tiedostoon.

**7.5.2026**
- Siirretty kysymykset JSON-tiedostoon.
- Pelaaja pystyy antamaan itselleen käyttäjänimen.
- Pelaaja voi nähdä top-5 pisteet
- Yhdistetty winning ja gameover samaan jottei olisi niin paljon toistoa.
- Siistitty koodia ja korjattu pylint virheitä.
  
**8.5.2026**
- Lisätty random.shuffle, jotta kysymykset näkyisivät randomissa järjestyksessä.
- Korjattu palaa etusivulle nappi. Kysymykset eivät jää enää taustalle jos käyttäjä haluaakin palata etusivulle kesken pelin.

**10.5.2026**
- Lisätty testejä
- Tarkistettu että kaikki toimii
- Lisätty kysymyksiä

