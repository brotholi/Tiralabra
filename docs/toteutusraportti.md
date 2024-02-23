# Totetustusraportti

## Ohjelman yleisrakenne
Typotarkistin-sovellus tarkastaa käyttäjän antamasta syötteestä kirjoitusvirheet vertailemalla niitä trie-tietorakenteessa olevaan sanastoon. Vertailu suoritetaan algoritmilla, joka tutkii Damerau-Levenshteinin etäisyyttä kahden sanan välillä. Algoritmi määrittelee kahden sanan etäisyydelle eräänlaisen kustannuksen sen mukaan, miten toisesta sanasta saadaan muokkaamalla toinen sana. Tämä kustannus on jaettu seuraaviin luokkiin: kirjaimen poistoon, lisäykseen ja korvaamiseen, sekä vierekkäisten merkkien paikkojen vaihtamiseen. Typotarkistin laskee näiden operaatioiden kustannusten perusteella etäisyyden sanaston sanoille ja käyttäjän antamalle syötteelle. 

Kun sovellus käynnistyy, tallennetaan aivan aluksi vocabularyService-luokalle annetussa tekstitiedostossa olevat sanat trie-tietorakenteeseen. Käytännössä nämä sanat on saatu avoindata.fi-sivustolta löydetystä avoimeen käyttöön tarkoitetusta postegreSQL Joukahainen-tietokannasta, jonne on kerätty paljon yleisiä suomen sanoja. Nämä sanat on harjoitustyön yksinkertaistamiseksi talletettu yhteen tekstitiedostoon. 

Ohjelman käynnistämisen jälkeen käyttäjälle avataan etusivu, jonka tekstikenttään käyttäjä voi syöttää joko yksittisen tarkistettavan sanan tai pitemmän tekstin. Jos syötettiin ainoastaan yksi tana, käyttäjälle annetaan joko ilmoitus siitä, että sanassa ei ole virhettä, eli se on löytynyt trie-rakenteesta, tai korjausehdotuksena sanat, jotka ovat lähellä sanaa. Korjausehdotuksina annetut sanat ovat korkeintaan yhden etäisyyden päässä toisistaan. Jos läheistä sanaa ei löydy sanastosta, tästä ilmoitetaan käyttäjälle.

Jos käyttäjä antaa pitemmän tekstin, sovellus korjaa sen suoraan tekstikentään. Jos sana löytyy sanastosta tai jos sille ei löydy läheisiä sanoja, sanaa ei korjata. Sen sijaan virheelliset sanat korvataan ensimmäisellä läheisellä sanalla, joka löydetään etäisyyksiä tutkimalla.

Käyttäjän on mahdollista pyytää sanan lisäämistä sanastoon, mikä ei onnistu, jos sana löytyy jo sanastosta.

## Tila- ja aikavaativuudet
[TODO]

Damerau-Lehvensteinin algoritmin aikavaativuus: 

Trien aikavaativuus:



## Puutteet ja jatkokehitysmahdollisuudet

Kirjoitusvirheiden korjaaja osaa korjata vain suomen kielen perusmuotoisia sanoja. Se ei tunnista eri sijapäätteissä olevia sanoja tai verbien eri aika- tai persoonamuotoja, sillä näitä ei ole tallennettu trie:hen lukuun ottamatta muutamien yleisten verbien persoonamuotoja. Taivutusmuotojen käsittelyä olisi mahdollista kehittää tulevaisuudessa, sillä tämän kurssin puitteissa tähän ei ole ollut aikaa. Sinänsä suomen kielen sanojen syntaksin tarkistaminen olisi jokseenkin haasteellinen tehtävä ja vaatisi sen, että jokaisesta sanasta tallennettaisiin muistiin, mihin taivutusluokkaan ne kuuluisivat. Myös erilaiset liitepartikkelit pitäisi ottaa huomioon. Korjattaessa otettaisiin tällöin huomioon myös taivutusluokka ja -muodot, mikäli ei haluttaisi tallentaan yksittäisinä sanoina jokaista taivutusmuotoa.

Lisäksi typotarkistin korjaa pitemmän tekstin virheelliset sanat aina ensimmäisellä sanalla, joka löydetään trie-tietorakennetta läpi käymällä ja jonka etäisyys väärästä sanasta on 1. Tämä aiheuttaa sen, että kaikki tehtävät korjaukset suosivat sellaisia sanoja, jotka on talletettu trie-tietorakenteeseen sanastosta aiemmin, eli todennäköisesti aakkosissa aikaisemmin olevia. Tämä olisi haastavaa korjata, koska ei voi olettaa, minkä sanan käyttäjä oli aikeissa kirjoittaa. Mahdollista olisi ottaa kaikki löydetyt sanat talteen ja jotenkin tutkia eroja kirjaimissa ja valita se korjaus, joka sisältää sellaisia kirjaimia, jotka ovat tietokoneen näppäimistössä lähellä toisiaan.


## Laajojen kielimallien käyttö
Kielimalleja on käytetty työn aikataulutuksen suunnitteluun kurssin ensimmäisellä viikolla. ChatGPT:ltä on kysytty, mitä työvaiheita kirjoitusvirheitä korjaavan sovelluksen tekemisessä on ja miten ne kannattaisi järjestää. Vastausta on lähinnä käytetty ajan säästämiseen ja hahmottamaan sitä, mitä kokonaisuudessaan kehittämisessä tulisi ottaa huomioon.

## Viitteet

- [Damerau–Levenshtein distance (Wikipedia)](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Hyperskill: Damerau–Levenshtein distance](https://hyperskill.org/learn/step/18819)
- [Trie (Wikipedia)](https://en.wikipedia.org/wiki/Trie)
- [Joukahainen-tietokanta](https://joukahainen.puimula.org/)

