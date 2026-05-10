
**Käyttöohje** 
Lataa projektin viieisin releaseen Assets-oosion alta
## **Huom. Python-versiosta**
Sovellusta on testattu Python-versiolla 3.14.4. Vanhempien versioiden kannssa saattaa ilmentyä ongelmia.

## **Miten sovellusta voi käyttää?**

- Avaa komentorivi ja kloonaa projekti:
```bash
git clone https://github.com/emmapiittala/ot-harjoitustyo2026.git
```
- Kun olet saanut kloonattua siirry:
 ```bash
  cd ot-harjoitustyo2026
  ```

 - Asenna projektin riippuvuudet:
```bash
  poetry install
  ```

- Käynnistä peli kirjoittamalla komentoriville:
```bash
  poetry run invoke start
  ```
**Pelaaminen**
Sovellus käynnistyy ja pääset pelaamaan peliä
Ensimmäisenä keksi itsellesi nimimerkki ja paina kohtaa Aloita peli.
Eteesi ilmestyy kysymys ja siihen 10 vastausta.
Valitse mielestäsi oikeat vastaukset ja paina 'Tarkista'
Jos vastasit väärin/et valinnut mitään, hävisit pelin. Voit päättää haluatko aloittaa uuden pelin.
Mikäli vastasit oikein, saat yhtämonta pistettä.
Pääset jatkamaan seuraavaan kysymykseen painamalla 'Seuraava kysymys'