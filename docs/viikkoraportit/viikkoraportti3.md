## Viikko 3

Tällä viikolla koodasin sovellukseen trie-tietorakenteelle uuden metodin, joka palauttaa kaikki sen sisältämät sanat listana. Muokkasin myös search-metodia niin, että se palauttaa etsityt sanat ja hyödyntää samaa syvyyshakua kuin trien koko sisällön palauttava metodi. Lisäksi toteutin ensimmäisen version Damerau-Levensteinin etäisyyttä hyödyntävästä algoritmista. Aloin kirjoittaa testausraporttia ja lisäsin luokkiin yksikkötestejä erilaisille rajatapauksille. Koodasin myös uuden ominaisuuden käyttöliittymälle: käyttöliittymältä voi lisätä sanan sanastoon, jos sitä ei ole vielä siellä.

Nyt sovellus toimii niin, että kun sille antaa sanan syötteenä, se ensin tarkistaa, löytyykö sitä trie-sanastosta ja jos ei, se käy läpi sanaston sanat ja vertaa niiden etäisyyttä käyttäjän antamaan merkkijonoon. Jos etäisyys on 1 tai alle, sanat palautetaan käyttöliittymälle. Jos sanastosta ei löydy läheistä sanaa käyttäjän antamalle sanalle, voidaan pyytää sanan lisäämistä sanastoon. Mietinnässä on vielä, pitäisikö pyyntöä validoida enemmän, sillä käytännössä käyttäjä voisi pyytää minkä tahansa "väärän" sanan lisäämistä sanastoon, jos sitä ei löydy jo sieltä.

Tällä viikolla opin tarkemmin merkkijonojen "etäisyyttä" tutkivan algoritmin toiminnasta, kun luin pseudokoodia ja toteutin oman versioni siitä. Kertasin jotakin tira-kurssien verkkoja ja syvyyshakua käsittelevää materiaalia, jota tarvitsin toteutukseen. 

Suurempia ongelmia toteutuksessa ei ole ollut, vaikka välillä algoritmien toimintalogiikan hahmottaminen vie aikaa. 

Ensi viikolla on tarkoitus tehdä enemmän käyttöliittymätestausta ja suorituskyvyn testausta algorimeille. Ainakin Damerau-Lehvenshtein algoritmi vaatii todennäköisesti nopeuttamista, sillä toteutin ensimmäisen version yksinkertaisella tavalla niin, että ymmärtäisin miten se toimii. Ajatuksena olisi myös miettiä tarkemmin, miten ohjelma käsittelee pitempiä käyttäjän antamia syötteitä ja miten sanan lisääminen toimii.

## Tuntikirjanpito

| Päivä | Käytetty aika | Kuvaus |
| ----- | ------------- | ------ |
| 1.2.  | 6 h            | Trien search-metodin muokkausta, Damerau-Lehvenshtein algoritmin ensimmäinen versio |
| 2.2.  | 8 h 			| Testausta, testausraportin kirjoittamista ja viikkoraportin kirjoittamista, uusi feature: käyttöliittymältä voi lisätä uuden sanan sanastoon ja trie-tietorakenteeseen
| Yhteensä | 14 h    
