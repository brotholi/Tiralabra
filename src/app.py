from flask import (
    Flask,
    render_template,
    request,
)
from services.damerau_levenshtein import DamerauLevenshtein
from services.vocabulary_service import VocabularyService

app = Flask(__name__)
damerau_levenshtein = DamerauLevenshtein()
vocabulary_service = VocabularyService("sanasto.csv")
finnish_vocabulary = vocabulary_service.create_vocabulary()


@app.route("/")
def index():
    """Metodi, joka palauttaa index.html-sivun

    Returns:
        index.html-sivu
    """
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    """Metodi, joka tarkistaa, löytyykö sana sanastosta

    Returns:
        result.html-sivu, jossa kerrotaan, löytyikö sana vai ei
    """
    input_text = request.form.get("input")
    similar_words = finnish_vocabulary.search(input_text)
    if len(similar_words) == 0:
        return render_template("result.html")
    return render_template("result.html", result=similar_words)
