## Testausraportti

### Yksikkötestit

Yksikkötesteissä on käytetty unnittest-kirjastoa ja ne on suunniteltu suoritettavaksi src/services hakemiston koodille, joka sisältää tällä hetkellä luokat vocabolary_service, trie, damerau_levenshtein. Nämä luokat on valittu testaukseen, koska ne sisältävät varsinaisen ohjelmalogiikan, kun taas käyttölittymään liittyvä koodi on jätetty yksikkötestauksen ulkopuolelle.

**Testikattavuusraportti**

Name                                  Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------------
src/services/damerau_levenshtein.py      18      0     14      0   100%
src/services/trie.py                     36      0     12      0   100%
src/services/vocabulary_service.py       18      0      6      0   100%
---------------------------------------------------------------------------------
TOTAL                                    72      0     32      0   100%


## Suorituskyvyn testaus

Ohjelmaa tullaan testaamaan suorituskyvyn osalta.


## Käyttölittymätestaus

Käyttöliittymältä tehtyä testausta.