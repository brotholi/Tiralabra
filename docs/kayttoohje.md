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
Yhden sanan tekstikenttään voi syöttää 2-20 merkkiä pitkän merkkijonon, joka tarkistetaan painamalla tarkista-nappia:

![image](https://github.com/brotholi/tiralabra/assets/91954165/8f663963-8426-4c0e-95ec-89755f1e7041)


Sovellus antaa tämän jälkeen ilmoituksen siitä, onko syötetty sana oikein. Listattuna ovat kaikki triestä löytyneet tekstisyötettä muistuttavat sanat:

![image](https://github.com/brotholi/tiralabra/assets/91954165/5f7c3cd6-1f49-44be-9218-b039ad794744)


Jo sana on syötetty oikein, annetaan palaute tästä: 

![image](https://github.com/brotholi/tiralabra/assets/91954165/6fc2ae67-6bc0-4938-901d-8aca7cf08da5)

Kun tekstiä muistuttavia sanoja ei löydetä, annetaan ilmoitus "sanaa ei löytynyt sanastosta":

![image](https://github.com/brotholi/tiralabra/assets/91954165/ad3f857a-7aa7-4336-b49e-2c32f97547d9)


### Pitemmän tekstin korjaaminen
Etusivun alempaan kenttään voi syöttää pitemmän tekstin, joka saa olla 2-100 merkkiä pitkä. Korjaus käynnistyy painamalla korjaa-nappia:

![image](https://github.com/brotholi/tiralabra/assets/91954165/52e865b3-e6dd-49aa-9479-c3937ce4e9e2)

Korjaus tulostetaan tekstikenttään, jota voi muokata. Tekstin voi kopioida painamalla kopioi-nappia:

![image](https://github.com/brotholi/tiralabra/assets/91954165/1a1f6e14-a0dd-4acb-a61b-088c70d5208f)


Jos kaikkea ei pystytty korjaamaan, annetaan palaute "Kaikkia sanoja ei voitu korjata":


![image](https://github.com/brotholi/tiralabra/assets/91954165/833682f4-d4b9-4d4d-b55c-eb8486da16f5)



## Sanan lisääminen sanastoon
Sanan voi lisätä sanastoon, kun on ensin pyytänyt sen korjausta. Painamalla lisää sana -nappia voidaan pyytää sanan lisäämistä sanastoon:


![image](https://github.com/brotholi/tiralabra/assets/91954165/3c0c5fc4-b76b-4c9b-a298-0db3c468d5ef)

Sana lisätään sanastoon vain silloin, kun sitä ei ollut sanastossa aiemmin: 


![image](https://github.com/brotholi/tiralabra/assets/91954165/d6913ad7-c122-4c4e-aba9-6ee81dbaee57)
