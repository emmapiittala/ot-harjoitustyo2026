# Vaatimusmäärittely

## Sovelluksen tarkoitus
- Smart10 - tyylinen yksin pelattava visailupeli, jossa käyttäjä saa kysymyksen ja 10 vastausta joista osa on oikein ja osa väärin. Jos käyttäjä vastaa väärin, häviää hän pelin. Käyttäjä pystyy valitsemaan monta oikeaa vastausta ja täten pistesaldo kasvaa enemmän.


## Käyttäjät
Sovelluksessa on vain normaali-käyttäjä, joka pystyy:
- Syöttämään nimimerkin
- pelata peliä
- kerätä pisteitä
- tarkistella top 5 tilastoja
- aloittaa uuden pelin

## Käyttöliittymäluonnos
![Käyttöliittymäluonnos](kayttoliittymaluonnos.png)

Sovelluksessa aukeaa etusivu jossa käyttäjä syöttää nimimerkin. Etusivulla lukee myös ohjeet miten peliä pelataan.

### Nimimerkin syöttäminen
Käyttäjän syötettyä nimimerkin ja painamalla tallenna tulee näkyviin "Aloita peli"- nappula josta pääsee pelaamaan. 

### Tallenna napin jälkeen
Käyttäjä voi aloittaa pelin, jossa vastataan kysymyksiin ja kerää mahdollisimmann paljon pisteitä oikeista vasauksista. Kerätyt pisteet näkyvät ajantasaisesti kysymyksen alla.

-Jos käyttäjä vastaa kaikkiin kysymyksiin oikein, voittaa hän ja päätyy win näkymään jossa käyttäjälle kerrotaan pisteet ja top5 pelaajat.

-Jos taas käyttäjä vastaa väärin, näytetään hänelle kerätyt pisteet ja top 5 tilastot. 

Kummastakin näkymästä käyttäjä voi aloittaa uuden pelin tai palata etusivulle.

## Jatkokehitysideoita
- Jatkossa voisi olla myös ylläpitäjä joka voisi keksiä uusia kategorioita/lisää kysymyksiä.
- Moninpeli mahdollisuus.
- Kirjautuminen sekä rekisteröityminen.
- Käyttäjät voisivat luoda Kahoot! - tyylisesti omia kysymyksiä
- Timeri kauanko yhteen kysymykseen saisi vastata.
- "Elämiä" - peli ei päättyisi ensimmäisestä väärästä vastauksesta, vaan esimerkiksi 3 elämää.
- Skippaus nappula millä pystyisi ohittamaan kysymyksen, mutta saisi aikasakkoa/menettäisi elämän. 
