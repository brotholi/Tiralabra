from flask import (
    Flask,
    render_template,
    request,
)
from services.vocabulary_service import VocabularyService

app = Flask(__name__)
vocabulary_service = VocabularyService("src/data/sanasto.txt")


@app.route("/")
def index():
    """Metodi, joka palauttaa index.html-sivun

    Returns:
        index.html-sivu
    """
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    """Metodi, joka ottaa vastaan käyttäjän syöttämän sanan ja tarkistaa sen 
    oikeinkirjoituksen service-luokkien avulla

    Returns:
        result.html-sivu, jossa annetaan käyttäjälle palautetta syötetystä sanasta
    """
    input_text = request.form.get("input")
    if vocabulary_service.find_word_in_vocabulary(input_text):
        return render_template("result.html", input=input_text,
                               message="(Ei kirjoitusvirheitä)")

    similar_words = vocabulary_service.find_similar_words(input_text)
    if len(similar_words) == 0:
        return render_template("result.html", input=input_text,
                               message="Sanaa ei löytynyt sanastosta")
    return render_template("result.html", result=similar_words, input=input_text)


@app.route("/correct", methods=["POST"])
def correct():
    """Metodi, joka ottaa vastaan käyttäjän syöttämän tekstin ja korjaa sen 
    oikeinkirjoituksen service-luokkien avulla

    Returns:
        result.html-sivu, jossa on korjattu teksti
    """
    input_words = vocabulary_service.parse_text(request.form.get("input"))
    correction_output = vocabulary_service.fix_typos(input_words)
    corrected_words = vocabulary_service.combine_text(correction_output[0])
    unable_to_correct = correction_output[1]
    if unable_to_correct:
        return render_template("correction.html", correction=corrected_words,
                               message="Huom! Kaikkia sanoja ei voitu korjata")

    return render_template("correction.html", correction=corrected_words,
                           message="Korjaus onnistui!")


@app.route("/<input>/add", methods=["POST"])
def add(input: str):
    """Metodi, joka ottaa vastaan käyttäjän syöttämän sanan ja lisää sen sanastoon

    Returns:
        message.html-sivu, joka sisältää palautteen sanan lisäämisen onnnistumisesta
    """
    input_text = input
    if input_text and vocabulary_service.add_word_to_vocabulary(input_text):
        return render_template("message.html", message="Sana lisätty sanastoon!")

    return render_template("message.html", message="Valitettavasti sanaa ei voitu lisätä sanastoon")
