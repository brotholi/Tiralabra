# Testausraportti

## Yksikkötestit

Yksikkötesteissä on käytetty unnittest-kirjastoa ja ne on suunniteltu suoritettavaksi src/services hakemiston koodille, joka sisältää tällä hetkellä luokat vocabolary_service, trie, damerau_levenshtein. Nämä luokat on valittu testaukseen, koska ne sisältävät varsinaisen ohjelmalogiikan, kun taas käyttölittymään liittyvä koodi on jätetty yksikkötestauksen ulkopuolelle.

**Testikattavuusraportti**

![image](https://github.com/brotholi/tiralabra/assets/91954165/400f6665-97d0-45ef-9097-10d5cee1a175)


## Manuaalinen testaus käyttöliittymältä

Sovellukselle on tehty käyttöliittymältä manuaalista testausta antamalla sille erilaisia tekstisyötteitä ja varmistamalla, että sana joko tunnistetaan tai annetaan korjausehdotus. Myös sanan lisäämistä sanastoon on testattu.

## Testitapaukset:
 ### 1.) Yhden sanan tarkistus:
   #### Virheetön sana
   - syötä sanastossa oleva sana, esimerkiksi "koira"
   - sovelluksen pitäisi tulostaa: *syötit sanan koira (ei kirjoitusvirheitä)*
   
   #### Sana, jossa on pieni kirjoitusvirhe
   - syötä sana, jossa on pieni kirjoitusvirhe, esimerkiksi "koifa"
   - sovelluksen pitäisi tulostaa: *syötit sanan koifa, tarkoititko [lista ehdotuksia]*
   - ehdotuksissa pitäisi olla ainakin sana koira ja mahdollisesti muita sanoja, joiden etäisyys koifa-syötteestä on 1.
   
   #### Muu tekstisyöte, jota ei voi korjata
   - syötä sana tai teksti, joka ei muistuta mitään sanaa, esimerkiksi "aaaaaaaaa"
   - sovelluksen pitäisi tulostaa: *syötit sanan aaaaaaaaa, sanaa ei löytynyt sanastosta*

 
### 2.) Sanan lisääminen sanakirjaan:
Kun olet pyytänyt sanan korjaamista, pyydä sovellusta lisäämään seuraavat sanat:

**a) sana, joka on jo sanastossa (esimerkiksi pankkiiri)**

   - sovelluksen pitäisi tulostaa: valitettavasti sanaa ei voitu lisätä sanastoon

**b) sana, jota ei löytynyt korjauksessa sanastosta**

   - sovelluksen pitäisi tulostaa: *sana lisätty sanastoon!*


### 3.) Pitemmän tekstin korjaaminen
   #### Virheetön teksti 
   - syötä teksi, jossa on ei ole kirjoitusvirheitä. Koska sanastossa ei välttämättä ole kaikkia taivutusmuotoja, syötä teksti, jossa sanat ovat perusmuodossa, esimerkiksi: hei maailma!
   - sovelluksen pitäisi antaa teksti samassa muodossa kuin se annettiin
   #### Teksti, jossa on typoja
   - syötä teksti, joka sisältää pieniä kirjoitusvirheitä (esimerkiksi heip maailma!)
   - sovelluksen pitäisi palauttaa korjattu teksti ("hei maailma!") ja ilmoitus: *Korjaus onnistui!*
   #### Virheellinen teksti, jossa ei oikeita sanoja
   - syötä jokin teksti, joka ei muistuta mitään oikeita sanoja (esimerkiksi aaaaaaaa)
   - sovelluksen pitäisi palauuttaa muokkaamaton teksti ja ilmoitus: *Kaikkia sanoja ei voitu korjata"*


## Suoritusaikaa mittaavat testit

Algoritmeja on testattu ajamalla manuaalisesti testejä, joissa annetaan suuria syötteitä algoritmeille. Tällä tutkitaan sitä, pystyvätkö algoritmit käsittelemään pitkiä syötteitä useita kertoja. Testaus on tehty, jotta pitemmän tekstin korjaus -ominaisuus toimisi odotetulla tavalla.

## Trie
**Trie-luokalle on tehty seuraavanlaisia testejä:**
Haku-, lisäys- ja trien koko sisällön palauttaville metodeille on tehty testejä, joissa tutkitaan, toimivatko ne, jos lisättävien merkkijonojen pituudet ovat todella pitkiä, yli 1000 mittaisia. Aikavaativuutta on testattu testeillä, joissa kasvatetaan syötteen kokoa kymmenkertaiseksi joka testauskerralla ja katsotaan suhteellinen ajan kasvu. 

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


#### search-metodi
- Searching 1000 character words took 0.004396901997097302 seconds
- Searching 10000 character words took 0.046685143002832774 seconds
- Searching 100000 character words took 0.6359621279989369 seconds
- Searching 1000000 character words took 4.71832493400143 seconds

## Damerau-Levenshtein
Etäisyyden laskentaa suorittavaa distance-algoritmia on testattu antamalla sille suuria syötteitä useita kertoja putkeen. Tällä on varmistettu, että algoritmi toimii, jos läpi käytävä sanasto on suuri ja algoritmia kutsutaan useita kertoja putkeen. Esimerkiksi 1-100 -kokoiselle syötteelle etäisyyden laskenta kestää keskimäärin 0.0012 sekuntia. 

