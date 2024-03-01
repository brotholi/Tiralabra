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

![image](https://github.com/brotholi/tiralabra/assets/91954165/8f663963-8426-4c0e-95ec-89755f1e7041)


Sovellus antaa tämän jälkeen ilmoituksen siitä, onko syötetty sana oikein. Listattuna ovat kaikki triestä löytyneet tekstisyötettä muistuttavat sanat:

![image](https://github.com/brotholi/tiralabra/assets/91954165/5f7c3cd6-1f49-44be-9218-b039ad794744)


Jo sana on syötetty oikein, annetaan palaute tästä: 

![image](https://github.com/brotholi/tiralabra/assets/91954165/6fc2ae67-6bc0-4938-901d-8aca7cf08da5)

Kun tekstiä muistuttavia sanoja ei löydetä, annetaan ilmoitus "sanaa ei löytynyt sanastosta:
![image](https://github.com/brotholi/tiralabra/assets/91954165/16ef68c5-6783-4c5d-a855-e07b47091211)

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
