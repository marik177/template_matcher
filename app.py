from flask import Flask, jsonify, request
from tinydb import TinyDB

from services import process_form

# Server
app = Flask(__name__)
app.secret_key = "tO$&!|0wkamvVia0?n$NqIRVWOG"
app.config["DEBUG"] = True
# Database
db = TinyDB("db.json")


@app.route("/", methods=["GET"])
def index():
    return jsonify(db.all())


@app.route("/get-form", methods=["POST"])
def get_form():
    resp = process_form(db, request.json)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
