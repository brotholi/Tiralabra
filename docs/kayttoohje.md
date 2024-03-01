# Käyttöohje

Kun olet kloonannut repositorion omalle koneellesi, käynnistä poetry projektin juurihakemistossa komennolla

```bash
poetry shell
```

Tämä vaatii siis, että koneelle on asennettu poetry. Tämän jälkeen luo virtuaaliympäristö ja lataa projektin riippuvuudet komennolla
```bash
poetry install
```

Sovelluksen voi tämän jälkeen käynnistää komennolla

```bash
poetry run invoke start
```	

Sovelluksen web-käyttöliittymä aukeaa terminaalin antamaan osoitteeseen, josta klikkaamalla pääsee etusivulle. Lokaalisti pyörivän sovelluksen saa suljettua antamalla terminaaliin ctrl + C.

Jos haluat ajaa sovellukselle yksikkötestejä, sen voi tehdä komennolla

```bash
poetry run invoke test
```

Testikattavuusraportin voi muodostaa komennolla

```bash
poetry run invoke coverage
```

# Sovelluksen käyttö
Typotarkistin sovelluksen käyttöliittymällä voi syöttää korjattavaksi joko yhden sanan tai pitemmän tekstin. Molemmat syöttökentät ovat etusivulla.

## Korjaaminen

### Sanan korjaaminen 
Yhden sanan tekstikenttään voi syöttää 2-20 merkkiä pitkän merkkijonon, joka tarkistetaan painamalla tarkista nappia:

![alt text](image-1.png)

Sovellus antaa tämän jälkeen ilmoituksen siitä, onko syötetty sana oikein. Listattuna ovat kaikki triestä löytyneet tekstisyötettä muistuttavat sanat:

![alt text](image-2.png)

Jo sana on syötetty oikein, annetaan palaute tästä: 

![alt text](image-3.png)

Kun tekstiä muistuttavia sanoja ei löydetä, annetaan ilmoitus "sanaa ei löytynyt sanastosta:
![alt text](image-4.png)

### Pitemmän tekstin korjaaminen
Etusivun alempaan kenttään voi syöttää pitemmän tekstin, joka saa olla 2-100 merkkiä pitkä. Korjaus käynnistyy painamalla korjaa-nappia:
![alt text](image-5.png)

Korjauksesta annetaan palaute:
![alt text](image-6.png)

Jos kaikkea ei pystytty korjaamaan, annetaan palaute "Kaikkia sanoja ei voitu korjata".

## Sanan lisääminen sanastoon
Sanan voi lisätä sanastoon, kun on ensin pyytänyt sen korjausta. Painamalla lisää-nappia voidaan pyytää sanan lisäämistä sanastoon:

![alt text](image-7.png)

Sana lisätään sanastoon vain silloin, kun sitä ei ollut sanastossa aiemmin: 
![alt text](image-8.png)