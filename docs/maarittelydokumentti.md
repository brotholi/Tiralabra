# Määrittelydokumentti
Tämä määrittelydokumentti määrittelee Helsingin yliopiston Aineopintojen harjoitustyö: Algoritmit ja tekoäly -kurssilla tehtävän harjoitustyön. Suoritan kurssin Tietojenkäsittelytieteen kandiohjelmassa (TKT).

## Aihe
Toteutan harjoitustyössä kirjoitusvirheiden korjaajan, joka korjaa käyttäjän antamassa tekstisyötteessa kirjoitusvirheet vertaamalla niiden eroavaisuutta Suomen kielen sanastossa oleviin sanoihin. Hyödynnän tässä merkkijonojen etäisyysmitan laskentaa, Damerau–Levenshteinin -etäisyyttä, jonka avulla etsin ne sanat, joiden etäisyysmitta korjattavista sanoista on pienin.

 Suomen kielen sanasto talletetaan itse toteutettavaan Tre-tietorakenteeseen, jolloin eri sanojen etsiminen on suhteellisen tehokasta. Aikavaativuutena tässä etsinnässä on O(n). Olen valinnut kyseiset tietorakenteet ja algorimit kurssin aihe-ehdotusten perusteella ajan säästämiseksi.

**(kesken)** Sovellukselle voidaan antaa käyttöliittymällä tekstiä, jonka sovellus analysoi ja korjaa suoraan tekstikenttään. Mikäli läheisiä sanoja eli ehdotuksia on useita, sovellus näyttää nämä käyttäjälle.

## Ohjelmointikielet
Harjoitustyö totetetaan Pythonilla.

Vertaisarvioinnissa voin arvioida ainakin myös Javalla toteutettuja harjoitustöitä, myös muut yleiset kielet onnistuvat.

## Lähteet **(kesken)**
Harjoitustyössä käytän seuraavia lähteitä:

- [Damerau–Levenshtein etäisyys](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Trie-tierakenne (Wikipedia)](https://en.wikipedia.org/wiki/Trie)
