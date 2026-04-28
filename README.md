# Ohjelmistotekniikka 2026
* [Työaikakirjanpito](Visailupeli/Dokumentaatio/tyoaikakirjanpito.md)
 * [Changelog](Visailupeli/Dokumentaatio/changelog.md)
 * [Vaatimusmäärittely](Visailupeli/Dokumentaatio/vaatimusmaarittely.md)
  * [Käyttöliittymäluonnos](Visailupeli/Dokumentaatio/kayttoliittymaluonnos.png)
  * [Arkkitehtuurikuvaus](Visailupeli/Dokumentaatio/arkkitehtuuri.md)
  * [Github release](https://github.com/emmapiittala/ot-harjoitustyo2026/releases/tag/Viikko5)
## **Ohjelmistotekniikka, harjoitustyö**
Yksin pelattava visailupeli.

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

- Testejä voi tarkastella suorittamalla komentorivillä:
```bash
  poetry run invoke coverage-report
  ```

- Pylint-tarkistus:
 ```bash
  poetry run pylint src
 ```
