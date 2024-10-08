# Django Model Documentation

Ovaj fajl dokumentuje Django modele za aplikaciju koja upravlja knjigama, piscima, izdavačima i recenzijama. Svaki model predstavlja tabelu u bazi podataka, sa poljima koja mapiraju kolone i odnose na druge modele.

## Pregled modela

- **Image**: Čuva podatke o slikama.
- **Genre**: Predstavlja žanr knjiga i pisaca.
- **Writer**: Sadrži detalje o piscima.
- **Publisher**: Čuva informacije o izdavaču.
- **Book**: Glavni model za knjige.
- **Reservation**: Praćenje rezervacija knjiga od strane korisnika.
- **Review**: Upravljanje recenzijama i ocenama knjiga.
- **Cart**: Rukovanje korisničkim izborom knjiga za kupovinu.
- **Profile**: Čuva korisničke profile i njihove preferencije.

---

### 1. **Image**
Čuva slike korišćene na različitim mestima u sistemu, uključujući korice knjiga i ikone žanrova.

| Polje       | Tip                | Opis                                        |
|-------------|---------------------|---------------------------------------------|
| `title`     | CharField (256)      | Naslov slike (opciono).                     |
| `alt`       | CharField (328)      | Alternativni tekst za pristupačnost (opciono).|
| `src`       | ImageField           | Datoteka slike, skladištena u folderu `images/`.|

- **`__str__`**: Vraća naslov slike.

---

### 2. **Genre**
Predstavlja žanr za knjige ili pisce.

| Polje         | Tip                   | Opis                                      |
|---------------|------------------------|-------------------------------------------|
| `name`        | CharField (32)          | Naziv žanra.                              |
| `image`       | ForeignKey (Image)      | Opciona slika povezana sa žanrom.         |
| `description` | RichTextField           | Detaljan opis (opciono).                  |

- **`__str__`**: Vraća naziv žanra.

---

### 3. **Writer**
Sadrži podatke o piscima.

| Polje           | Tip                      | Opis                                         |
|-----------------|---------------------------|----------------------------------------------|
| `name`          | CharField (32)             | Ime pisca.                                   |
| `date_of_birth` | CharField (32)             | Datum rođenja pisca (opciono).               |
| `date_of_death` | CharField (32)             | Datum smrti (opciono).                       |
| `genre`         | ManyToManyField (Genre)    | Žanrovi povezani sa piscem.                  |
| `about_them`    | RichTextField              | Biografija pisca.                            |

- **`__str__`**: Vraća ime pisca.

---

### 4. **Publisher**
Čuva informacije o izdavaču.

| Polje        | Tip          | Opis                                      |
|--------------|--------------|-------------------------------------------|
| `name`       | CharField (32)| Naziv izdavača.                           |
| `about_them` | RichTextField | Informacije o izdavaču.                   |

- **`__str__`**: Vraća ime izdavača.

---

### 5. **Book**
Predstavlja knjigu i povezane informacije.

| Polje            | Tip                    | Opis                                         |
|------------------|-------------------------|----------------------------------------------|
| `name`           | CharField (32)           | Naziv knjige.                                |
| `genre`          | ManyToManyField (Genre)  | Povezani žanrovi (opciono).                  |
| `writer`         | ManyToManyField (Writer) | Autori knjige (opciono).                     |
| `publisher`      | ForeignKey (Publisher)   | Izdavač knjige (opciono).                    |
| `number_of_page` | IntegerField             | Broj strana u knjizi.                        |
| `publish_data`   | DateField                | Datum objavljivanja.                         |
| `description`    | RichTextField            | Opis knjige.                                 |
| `price`          | DecimalField             | Cena knjige.                                 |
| `quantity`       | IntegerField             | Količina na skladištu, sa minimalnom vrednošću 0.|
| `image`          | ForeignKey (Image)       | Slika korice knjige (opciono).               |

- **`no_of_ratings`**: Vraća broj recenzija.
- **`avg_rating`**: Izračunava prosečnu ocenu knjige.
- **`__str__`**: Vraća naziv knjige.

---

### 6. **Reservation**
Prati rezervacije knjiga od strane korisnika.

| Polje      | Tip               | Opis                                      |
|------------|-------------------|-------------------------------------------|
| `user`     | ForeignKey (User)  | Korisnik koji je napravio rezervaciju.    |
| `books`    | ForeignKey (Book)  | Knjiga koja je rezervisana.               |
| `datetime` | DateTimeField      | Vreme kada je rezervacija napravljena.    |
| `quantity` | IntegerField       | Broj rezervisanih knjiga.                 |

---

### 7. **Review**
Predstavlja recenzije za knjige od strane korisnika, uključujući ocene.

| Polje      | Tip                | Opis                                      |
|------------|--------------------|-------------------------------------------|
| `book`     | ForeignKey (Book)   | Recenzirana knjiga.                       |
| `user`     | ForeignKey (User)   | Korisnik koji je napisao recenziju.       |
| `comment`  | RichTextField       | Komentar recenzije.                       |
| `rating`   | IntegerField        | Ocena dodeljena knjizi (1-5).             |
| `approved` | BooleanField        | Da li je recenzija odobrena.              |
| `create_at`| DateTimeField       | Vreme kada je recenzija kreirana.         |

- **Jedinstvenost**: `(book, user)` osigurava da korisnik može dati samo jednu recenziju po knjizi.

---

### 8. **Cart**
Rukuje narudžbinama knjiga od strane korisnika.

| Polje      | Tip                | Opis                                      |
|------------|--------------------|-------------------------------------------|
| `books`    | ForeignKey (Book)   | Knjiga dodata u korpu.                    |
| `user`     | ForeignKey (User)   | Korisnik koji poseduje korpu.             |
| `quantity` | IntegerField        | Broj knjiga u korpi.                      |
| `status`   | CharField           | Status narudžbine (`pristiglo`, `U toku`, `Otkazano`). |
| `created_at` | DateTimeField     | Vreme kreiranja korpe.                    |
| `updated_at` | DateTimeField     | Vreme poslednje promene korpe.            |

- **Jedinstvenost**: `(user, books)` osigurava da korisnik može imati samo jednu stavku po knjizi.

---

### 9. **Profile**
Predstavlja korisničke profile, uključujući omiljene žanrove i avatare.

| Polje     | Tip                   | Opis                                      |
|-----------|------------------------|-------------------------------------------|
| `user`    | ForeignKey (User)       | Korisnik povezan sa profilom.             |
| `genre`   | ManyToManyField (Genre) | Preferirani žanrovi korisnika.            |
| `about`   | RichTextField           | Biografija ili dodatne informacije.       |
| `image`   | ForeignKey (Image)      | Slika profila (opciono).                  |

- **Jedinstvenost**: `(id, user)` osigurava jedinstveni profil po korisniku.

- **`__str__`**: Vraća korisničko ime povezano sa profilom.

---

## Dodatne napomene:

- **Jedinstvenost** (`unique_together`) je korišćena u nekoliko modela kako bi se sprečilo dupliranje unosa.
- **RichTextField** omogućava čuvanje velike količine teksta sa bogatim formatiranjem.
- **ForeignKey** veze uspostavljaju povezanost između modela (npr. knjiga ima autora, korisnik ima recenzije).
- **DecimalField** i **IntegerField** osiguravaju pravilnu validaciju numeričkih polja kao što su cena i količina.
