## Viikko 5

Tällä viikolla koodasin sovellukseen ominaisuuden, jolla voi suoraan syöttää pitemmän tekstin käyttöliittymälle ja sovellus korjaa sen virheet suoraan tekstiin. Korjattu teksti annetaan käyttäjälle tekstiboksin sisällä, joten käyttäjä voi vielä muokata sitä, jos korjaaja teki virheen. Lisäksi tekstiboksissa olevan tekstin voi suoraan kopioida. 

Lisäksi jatkoin algoritmien testausta. Testasin Damerau-Levensthein  -algoritmia muutamilla isoilla syötteillä ja tein siihen pieniä muokkauksia. Lisäksi tein enimmäkseen käyttöliittymätestausta erilaisilla syötteillä ja muokkasin syötteen minimipituuden kahteen merkkiin, että sovellus osaisi korjata kahden merkin pituiset sanat ja antaa näille oikeat korjausehdotukset (eikä vain yksittäisiä kirjaimia).

Jatkoin testausraportin ja toteutusraportin kirjoittamista sekä tein vertaisarvion toisen opiskelijan projektiin.

Opin tällä viikolla eniten uutta vertaisarviota tehdessä, kun tutustuin 2048-solveriin, joka käyttää expectimax-algoritmia. 

Haasteita oli siinä, kuinka sovellus osaisi tunnistaa sanojen taivutusmuodot. Suomen kielen sanoilla on todella paljon eri taivutusmuotoja ja sanastoni ei sisällä suurimpaa osaa niitä, ainoastaan muutaman yleisen verbin eri taivutusmuodot. Tämä tuottaa ongelmia, sillä teksin korjaus ei aina tunnista kaikkia taivutettuja sanoja ja korjaa siis sanat, vaikka ne olisivat oikein. En tiedä onko mahdollista saada edes kaikkia sanoja sanastoon kurssin puutteissa, mutta ainakin tällä hetkellä käyttöliittymältä voi lisätä puuttuvan taivutetun sanan sanastoon. 

Ensi viikolla aion ainakin jatkaa sovelluksen testaamista ja valmistautua loppupalautukseen. Lisäksi ensi viikolla on toinen vertaisarviointi.


## Tuntikirjanpito

| Päivä | Käytetty aika | Kuvaus |
| ----- | ------------- | ------ |
| 15.2. | 2 h            | Vertaisarviota ja dokumentointia |
| 16.2.  | 8 h 			| Toteutusta ja testausta  |
 Yhteensä  10 h    
