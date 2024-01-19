# Määrittelydokumentti
Tämä määrittelydokumentti määrittelee Helsingin yliopiston Aineopintojen harjoitustyö: Algoritmit ja tekoäly -kurssilla tehtävän harjoitustyön. Suoritan kurssin Tietojenkäsittelytieteen kandiohjelmassa (TKT).

## Aihe
Toteutan harjoitustyössä kirjoitusvirheiden korjaajan, joka korjaa käyttäjän antamassa tekstisyötteessa kirjoitusvirheet vertaamalla niiden eroavaisuutta Suomen kielen sanastossa oleviin sanoihin. Hyödynnän tässä merkkijonojen etäisyysmitan laskentaa, Damerau–Levenshteinin -etäisyyttä, jonka avulla etsin ne sanat, joiden etäisyysmitta korjattavista sanoista on pienin.

 Suomen kielen sanasto talletetaan itse toteutettavaan Tre-tietorakenteeseen, jolloin eri sanojen etsiminen on suhteellisen tehokasta. Olen valinnut kyseiset tietorakenteet ja algorimit kurssin aihe-ehdotusten perusteella ajan säästämiseksi. Aiheen olen valinnut, koska olen tehnyt työkseni oikolukua ja opiskellut Suomen kieltä.

**(kesken)** Sovellukselle voidaan antaa käyttöliittymällä tekstisyötteenä sanoja, jotka analysoidaan vertaamalla niiden etäisyyttä sanastossa oleviin sanoihin. Sovellus antaa korjausehdotuksen kertomalla sanat, joita kirjoitettu sana on lähimpänä. Ainakin ensimmäisessä toteutuksessa sovellukselle voidaan antaa kerrallaan yksi sana, jonka se analysoi, ja ehdotuksia lähellä olevista sanoista voi olla useampi kuin yksi.

## Ohjelmointikielet
Harjoitustyö totetetaan Pythonilla.

Vertaisarvioinnissa voin arvioida ainakin myös Javalla toteutettuja harjoitustöitä, myös muut yleiset kielet onnistuvat.

## Projektin kieli

Projektin dokumentaatio kirjoitetaan suomeksi. Myös koodissa olevat kommentit tulevat olemaan suomeksi, mutta itse koodi ja muuttujanimet englanniksi.

## Lähteet 
Harjoitustyössä käytän seuraavia lähteitä:

- [Damerau–Levenshtein etäisyys](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Trie-tierakenne (Wikipedia)](https://en.wikipedia.org/wiki/Trie)


