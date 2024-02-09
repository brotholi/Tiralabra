# Totetustusraportti

## Ohjelman yleisrakenne
Typotarkistin-sovellus tarkastaa käyttäjän antamasta syötteestä kirjoitusvirheet vertailemalla niitä trie-tietorakenteessa olevaan sanastoon. Vertailu suoritetaan algoritmilla, joka tutkii Damerau-Levenshteinin etäisyyttä kahden sanan välillä. Algoritmi määrittelee kahden sanan etäisyydelle eräänlaisen kustannuksen sen mukaan, miten toisesta sanasta saadaan muokkaamalla toinen sana. Tämä kustannus on jaettu seuraaviin luokkiin: kirjaimen poistoon, lisäykseen ja korvaamiseen, sekä vierekkäisten merkkien paikkojen vaihtamiseen. Typotarkistin laskee näiden operaatioiden kustannusten perusteella etäisyyden sanaston sanoille ja käyttäjän antamalle syötteelle. 

Kun sovellus käynnistyy, tallennetaan aivan aluksi vocabularyService-luokalle annetussa csv-tiedostossa olevat sanat trie-tietorakenteeseen. Käytännössä nämä sanat on saatu avoindata.fi-sivustolta löydetystä avoimeen käyttöön tarkoitetusta Joukahainen-tietokannasta, jonne on kerätty paljon yleisiä suomen sanoja. Nämä sanat on harjoitustyön yksinkertaistamiseksi talletettu csv-tiedostoon. Käyttäjälle sanaston tallentamista ei näytetä, vaan ohjelman käynnistämisen jälkeen käyttäjälle avataan etusivu, jonka tekstikenttään käyttäjä voi syöttää enintään 20 merkkisen tekstin. Tarkistamisen jälkeen käyttäjälle annetaan joko ilmoitus siitä, että sanassa ei ole virhettä, eli se on löytynyt trie-rakenteesta, tai korjausehdotuksena sanat, jotka ovat lähellä sanaa. Korjausehdotuksina annetut sanat ovat korkeintaan yhden etäisyyden päässä toisistaan. Jos läheistä sanaa ei löydy sanastosta, tästä ilmoitetaan käyttäjälle.

Käyttäjän on mahdollista pyytää sanan lisäämistä sanastoon, mikä ei onnistu, jos sana löytyy jo sanastosta. Tämä on vielä työn alla [TODO].

## Tila- ja aikavaativuudet
[TODO]

Damerau-Lehvensteinin algoritmin aikavaativuus: 

Trien aikavaativuus:



## Puutteet ja parannusmahdollisuudet
[TODO]

Kirjoitusvirheiden korjaaja osaa korjata vain perusmuotoisia sanoja, eli se ei tunnista eri sijapäätteissä olevia sanoja tai verbien eri aika- tai persoonamuotoja, sillä näitä ei ole tallennettuna triessä. Tätä olisi mahdollista kehittää tulevaisuudessa, sillä tämän kurssin puitteissa tähän ei ole ollut aikaa.

Hitaus?


## Laajojen kielimallien käyttö
Kielimalleja on käytetty työn aikataulutuksen suunnitteluun kurssin ensimmäisellä viikolla. ChatGPT:ltä on kysytty, mitä työvaiheita kirjoitusvirheitä korjaavan sovelluksen tekemisessä on ja miten ne kannattaisi järjestää. Vastausta on lähinnä käytetty ajan säästämiseen ja hahmottamaan sitä, mitä kokonaisuudessaan kehittämisessä tulisi ottaa huomioon.

## Viitteet

- [Damerau–Levenshtein distance (Wikipedia)](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Hyperskill: Damerau–Levenshtein distance](https://hyperskill.org/learn/step/18819)
- [Trie (Wikipedia)](https://en.wikipedia.org/wiki/Trie)
- [Joukahainen-tietokanta](https://joukahainen.puimula.org/)

