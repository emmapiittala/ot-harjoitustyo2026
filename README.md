# Ohjelmistotekniikka 2026
* [Työaikakirjanpito](Dokumentaatio/tyoaikakirjanpito.md)
 * [Changelog](Dokumentaatio/changelog.md)
  
## **Ohjelmistotekniikka, harjoitustyö**
Yksin pelattava visailupeli.

## **Miten sovellusta voi käyttää?**

- Kopioi projektin linkki oikealta ylhäältä painamalla vihreätä Code-nappia > SSH > ota linkki talteen Clonesta tai;
```bash
git@github.com:emmapiittala/ot-harjoitustyo2026.git
```
- Avaa komentorivi ja kloonaa projekti:
```bash
git clone git@github.com:emmapiittala/ot-harjoitustyo2026.git
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
