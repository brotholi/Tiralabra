# Testausraportti

## Yksikkötestit

Yksikkötesteissä on käytetty unnittest-kirjastoa ja ne on suunniteltu suoritettavaksi src/services hakemiston koodille, joka sisältää tällä hetkellä luokat vocabolary_service, trie, damerau_levenshtein. Nämä luokat on valittu testaukseen, koska ne sisältävät varsinaisen ohjelmalogiikan, kun taas käyttölittymään liittyvä koodi on jätetty yksikkötestauksen ulkopuolelle.

**Testikattavuusraportti**

![image](https://github.com/brotholi/tiralabra/assets/91954165/400f6665-97d0-45ef-9097-10d5cee1a175)


## Suorituskyvyn testaus

Sovelluksen suorituskykyä on testattu ajamalla manuaalisesti testejä, joissa annetaan suuria syötteitä algoritmeille ja tutkimalla aikavaativuuksia.

### Trie
Trie-luokalle on tehty seuraavanlaisia testejä:
Haku-, lisäys ja trien koko sisällön palauttaville metodeille on tehty testejä, joissa tutkitaan, toimivatko ne, jos lisättävien merkkijonojen pituudet ovat todella pitkiä, yli 1000 mittaisia. Aikavaativuutta on testattu testeillä, joissa kasvatetaan syötteen kokoa kymmenkertaiseksi joka testauskerralla ja katsotaan suhteellinen ajan kasvu. 

Esimerkkitulosteita aikavaativuustesteistä:

#### add-metodi
- Adding 1000 character words took 0.00490963899937924 seconds
- Adding 10000 character words took 0.04868726700078696 seconds
- Adding 100000 character words took 0.5059331439988455 seconds
- Adding 1000000 character words took 5.09806443799971 seconds

#### get_trie_content-metodi

- Getting content of 1000 word trie took 1.126500137615949e-05 seconds
- Getting content of 10000 word trie took 9.692001185612753e-06 seconds
- Getting content of 100000 word trie took 9.75500006461516e-06 seconds
- Getting content of 1000000 word trie took 1.0677998943720013e-05 seconds


#### search-metori
- Searching 1000 character words took 0.004396901997097302 seconds
- Searching 10000 character words took 0.046685143002832774 seconds
- Searching 100000 character words took 0.6359621279989369 seconds
- Searching 1000000 character words took 4.71832493400143 seconds

## Damerau-Levenshtein

[tbd]
