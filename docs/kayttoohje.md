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