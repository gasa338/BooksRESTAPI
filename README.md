# Books Store API

Opis Projekta
Pregled

Ovaj projekat predstavlja složen Django REST API za upravljanje knjigama i povezanim entitetima u okviru sistema za online knjižaru. API pruža različite funkcionalnosti za upravljanje knjigama, korisničkim profilima, recenzijama, korpom za kupovinu, rezervacijama i još mnogo toga. Projekt uključuje i Swagger dokumentaciju za jednostavno istraživanje i testiranje API-ja.

## Ključne Komponente

1. **Book**:

    Opis:Model koji predstavlja knjige dostupne u sistemu.
    Polja: Naslov, opis, datum objave, autor, žanr, cena, slike (pokrijte sve relevantne detalje koji su deo modela).
2. Cart:
        Opis: Model za upravljanje korpom korisnika za kupovinu knjiga.
        Polja: ID korisnika, lista knjiga u korpi, količina, ukupna cena.
3. Review:
        Opis: Model koji omogućava korisnicima da ostave recenzije za knjige.
        Polja: ID korisnika, ID knjige, ocena, tekst recenzije, datum recenzije.
4. Writer:
        Opis: Model koji predstavlja autore knjiga.
        Polja: Ime, biografija, slike, lista knjiga koje je napisao autor.
5. Genre:
        Opis: Model za upravljanje žanrovima knjiga.
        Polja: Naziv žanra, opis žanra, lista knjiga koje pripadaju tom žanru.
6. Profile:
        Opis: Model za upravljanje korisničkim profilima.
        Polja: Korisničko ime, email, lozinka, adresa, slike profila.
7. Reservation:
        Opis: Model za rezervaciju knjiga.
        Polja: ID korisnika, ID knjige, datum rezervacije, status rezervacije.

## Funkcionalnosti

Upravljanje Knjigama: Dodavanje, uređivanje i brisanje knjiga, pretraga i filtriranje prema različitim kriterijumima.
Korisnički Profil: Registracija, prijava, uređivanje profila, pregled i ažuriranje korisničkih informacija.
Korp: Dodavanje knjiga u korpu, ažuriranje količine, pregled i finalizacija kupovine.
Recenzije: Pisanje, pregled i brisanje recenzija knjiga.
Autori i Žanrovi: Upravljanje informacijama o autorima i žanrovima knjiga.
Rezervacije: Rezervisanje knjiga, praćenje statusa rezervacija.

## Swagger Dokumentacija

Swagger dokumentacija omogućava vizuelno predstavljanje API-ja, olakšava testiranje i pruža sve potrebne informacije za interakciju sa API-em. Dokumentacija se automatski generiše i ažurira na osnovu definicija API endpoint-a.
Tehnologije

**Django**: Framework za razvoj web aplikacija.
**Django REST Framework**: Za izgradnju RESTful API-ja.
**Swagger**: Za dokumentaciju i testiranje API-ja.