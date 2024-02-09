## Viikko 4

Neljännellä viikolla itse sovelluksen koodaamista on ollut suhteellisen vähän, sillä aikaa on kulunut testaamiseen ja dokumentaatioon. Olen muokannut hiukan aiempien viikkojen yksikkötestejä lisäämällä mock-olioita vocabularyService-luokan testeihin, jotta yksikkötestaus keskittyisi vain tämän luokan toiminnallisuuden testaamiseen eikä testattaisi niinkään Trie- tai DamerauLevenshtein-luokkia, joita vocabularyService kutsuu. Sovelluksen toimintaan ei ole tullut suuria muutoksia, joitain luokkien sisäisiä toimintoja on siistinyt ja refaktoroinut yksikkötestien tekemisen ohessa.

Lisäksi olen perehtynyt invarianttitestaamiseen ja suoritustestaamiseen kurssimateriaalin avulla ja lisäsin yksikkötesteihin muutaman testin jotka hyödyntävät hypothesis-kirjastoa. Aloitin myös suorituskykytestauksen trie-luokan metodeilla.

Tällä viikolla olen myös kirjoittanut toteus- ja testausdokumenttia sekä laatinut käyttöohjeen sovellukselle.

Uutena asiana olen oppinut tällä viikolla invarianttitestauksesta, sillä aihe oli itselleni jokseenkin tuntematon. Myös suorituskykytestauksesta olen oppinut uutta. Suorituskykytestauksen miettiminen on ollut ehkä haasteellisinta tällä viikolla.

Ensi viikolla ajattelin keskittyä vertaisarvioinnin lisäksi laajentamaan sovelluksen käsittelemään pitempiä syötteitä. Myös suorituskykytestaus jatkuu ensi viikolla etenkin Damerau-Levenshteinin algoritmin osalta, mihin en tällä viikolla ehtinyt.

## Tuntikirjanpito

| Päivä | Käytetty aika | Kuvaus |
| ----- | ------------- | ------ |
| 6.2.  | 2 h            | Dokumentaatiota yms. |
| 8.2.  | 8 h 			| Suorituskykyestausta ja yksikkötestien kirjoittamista |

 Yhteensä  10 h    
