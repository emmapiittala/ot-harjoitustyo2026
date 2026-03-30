```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Ruutu "1" -- "1" Toiminto
    Monopolipeli "1" -- "1" Vankila
    Monopolipeli "1" -- "1" Aloitusruutu

    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- Sattuma
    Ruutu <|-- Yhteismaa
    Ruutu <|-- Asema
    Ruutu <|-- Laitos
    Ruutu <|-- NormaalitKatu

    class Pelaaja {
        +raha: int
    }

    class Sattuma 
        +Pelaaja "1" --> "*" Sattuma toiminto
    
    

    class Yhteismaa
        +Pelaaja "1" --> "*" Yhteismaa toiminto
    
    
    NormaalitKatu "0..1" -- "1" Pelaaja

    class NormaalitKatu {
        +omistaja: Pelaaja
        +talojenMaara: "0..4"
        +hotellit: "0..1"
    }
    
    


```
