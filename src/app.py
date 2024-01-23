from flask import (
    Flask,
    render_template,
    request,
)
from services.damerau_levenshtein import DamerauLevenshtein

app = Flask(__name__)
damerau_levenshtein = DamerauLevenshtein()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    input_text = request.form.get("input")
    checked_text = damerau_levenshtein.check(input_text)
    return render_template("result.html", output=checked_text)

