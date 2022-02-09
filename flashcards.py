from email import message
from flask import Flask, render_template, abort, jsonify
from model import db

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        message="Here is a simple Bootstrap page designed for use with Flask as the backend, This message is emitted by the Jinja template",
        cards=db
        )

@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card = card, index=index, max_index=len(db)-1)
    except IndexError:
        msg = "Card does not exist"
        return render_template("error.html", message=msg)

@app.route("/error")
def error():
    msg = "Error"
    return render_template("error.html", message=msg)


@app.route("/api/card/")
def api_card_list():
    return jsonify(db)

@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)