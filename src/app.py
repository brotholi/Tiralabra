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
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    input_text = request.form.get("input")
    if finnish_vocabulary.search(input_text):
        return render_template("result.html", output=input_text)
    else:
        return render_template("result.html", output="Sanaa ei löytynyt sanastosta")
