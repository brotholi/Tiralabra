# Totetustusraportti

## Ohjelman yleisrakenne
Typotarkistin-sovellus tarkastaa käyttäjän antamasta syötteestä kirjoitusvirheet vertailemalla niitä trie-tietorakenteessa olevaan sanastoon. Vertailu suoritetaan algoritmilla, joka tutkii Damerau-Levenshteinin etäisyyttä kahden sanan välillä. Algoritmi määrittelee kahden sanan etäisyydelle eräänlaisen kustannuksen sen mukaan, miten toisesta sanasta saadaan muokkaamalla toinen sana. Tämä kustannus on jaettu seuraaviin luokkiin: kirjaimen poistoon, lisäykseen ja korvaamiseen, sekä vierekkäisten merkkien paikkojen vaihtamiseen. Typotarkistin laskee näiden operaatioiden kustannusten perusteella etäisyyden sanaston sanoille ja käyttäjän antamalle syötteelle. 

Kun sovellus käynnistyy, tallennetaan aivan aluksi vocabularyService-luokalle annetussa tekstitiedostossa olevat sanat trie-tietorakenteeseen. Käytännössä nämä sanat on saatu avoindata.fi-sivustolta löydetystä avoimeen käyttöön tarkoitetusta PostgreSQL Joukahainen-tietokannasta, jonne on kerätty paljon yleisiä suomen sanoja. Nämä sanat on harjoitustyön yksinkertaistamiseksi talletettu yhteen tekstitiedostoon. 

Ohjelman käynnistämisen jälkeen käyttäjälle avataan etusivu, jonka tekstikenttään käyttäjä voi syöttää joko yksittäisen tarkistettavan sanan tai pitemmän tekstin. Jos syötettiin ainoastaan yksi sana, käyttäjälle annetaan joko ilmoitus siitä, että sanassa ei ole virhettä, eli se on löytynyt trie-rakenteesta, tai korjausehdotuksena sanat, jotka ovat lähellä sanaa. Korjausehdotuksina annetut sanat ovat korkeintaan yhden etäisyyden päässä toisistaan. Jos läheistä sanaa ei löydy sanastosta, tästä ilmoitetaan käyttäjälle.

Jos käyttäjä antaa alempaan tekstikenttään tekstin, sovellus korjaa sen suoraan tekstikentään. Jos sana löytyy sanastosta tai jos sille ei löydy läheisiä sanoja, sanaa ei korjata. Mikäli kirjoitetussa tekstissä on sanoja, joita ei löydetty sanastossa, annetaan käyttäjälle viesti "kaikkia sanoja ei voitu korjata" Sen sijaan virheelliset sanat korvataan ensimmäisellä läheisellä sanalla, joka löydetään etäisyyksiä tutkimalla. Jos teksti oli virheetön tai kaikille väärin kirjoitetuille sanoille löydettiin jokin vastine, annetaan ilmoitus "korjaus onnistui".
Pitemmän korjatun tekstin voi kopioida kopioi-nappulalla suoraan tekstikentästä.

Käyttäjän on myös mahdollista pyytää sanan lisäämistä sanastoon, mikä ei onnistu, jos sana löytyy jo sanastosta.

## Tila- ja aikavaativuudet

Damerau-Lehvensteinin etäisyyttä tutkivan algoritmin aikavaativuus on lähteiden mukainen O(mn), missä m ja n ovat verrattavien merkkijonojen pituuksia.

Trien kaikki metodit, etsintä, lisäys ja koko sisällön palauttaminen, vievät aikaa O(n), missä n on avaimen eli käsiteltävän sanan pituus. Trie-rakenne mahdollistaa sanan nopean etsimisen ja tallettamisen, mikä on välttämätöntä, kun käsiteltävä sanasto on suuri. Trien tilavaativuus on samaten lähteiden mukaan O(n).



## Puutteet ja jatkokehitysmahdollisuudet

Kirjoitusvirheiden korjaaja osaa korjata vain suomen kielen perusmuotoisia sanoja. Se ei tunnista eri sijapäätteissä olevia sanoja tai verbien eri aika- tai persoonamuotoja, ellei näitä ei ole tallennettu trie:hen. Taivutusmuotojen käsittelyä olisi mahdollista kehittää tulevaisuudessa, sillä tämän kurssin puitteissa siihen ei ole ollut aikaa. Suomen kielen sanojen oikeinkirjoituksen tarkistaminen voisi kuitenkin olla melko haasteellinen tehtävä ja vaatisi ehkä sen, että jokaisesta sanasta tallennettaisiin muistiin, mihin taivutusluokkaan ne kuuluisivat. Myös erilaiset liitepartikkelit pitäisi ottaa huomioon. Korjattaessa otettaisiin tällöin huomioon myös taivutusluokka, mikäli ei haluttaisi tallentaan yksittäisinä sanoina jokaista taivutusmuotoa.

Lisäksi typotarkistin korjaa pitemmän tekstin virheelliset sanat aina ensimmäisellä sanalla, joka löydetään trie-tietorakennetta läpi käymällä ja jonka etäisyys väärästä sanasta on 1. Tämä aiheuttaa sen, että kaikki tehtävät korjaukset suosivat sellaisia sanoja, jotka on talletettu trie-tietorakenteeseen sanastosta aiemmin. Koska sanat ovat suurelta osin aakkosjärjestyksessä, ovat ensimmäisenä löydettävät sanat todennäköisemmin ensimmäisiä aakkosjärjestyksessä. Tämä olisi haastavaa korjata, koska ei voi olettaa, minkä sanan käyttäjä oli aikeissa kirjoittaa. Mahdollista olisi ottaa kaikki löydetyt sanat talteen ja jotenkin tutkia eroja kirjaimissa. Algoritmi voisi olettaa, että käyttäjä kirjoittaa näppäimistöllä ja teksti sisältää niin sanottuja "ohilyöntejä". Tällöin voitaisiin valita se korjaus, joka sisältää sellaisia kirjaimia, jotka ovat tietokoneen näppäimistössä lähellä toisiaan.


## Laajojen kielimallien käyttö
Kielimalleja on käytetty työn aikataulutuksen suunnitteluun kurssin ensimmäisellä viikolla. ChatGPT:ltä on kysytty, mitä työvaiheita kirjoitusvirheitä korjaavan sovelluksen tekemisessä on ja miten ne kannattaisi järjestää. Vastausta on lähinnä käytetty ajan säästämiseen ja hahmottamaan sitä, mitä kokonaisuudessaan kehittämisessä tulisi ottaa huomioon.

## Viitteet

- [Damerau–Levenshtein distance (Wikipedia)](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Hyperskill: Damerau–Levenshtein distance](https://hyperskill.org/learn/step/18819)
- [Trie (Wikipedia)](https://en.wikipedia.org/wiki/Trie)
- [Joukahainen-tietokanta](https://joukahainen.puimula.org/)

