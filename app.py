from flask import Flask, json
from importer.import_movies import import_all

app = Flask(__name__)

# FIXME: Delete file or rewrite each 6 hours @FIXME
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = import_all()


@app.route("/")
def hello_world():
    return json.jsonify(data)


@app.route("/available")
def return_available():
    return json.jsonify(data["available"])


@app.route("/upcoming")
def return_upcoming():
    return json.jsonify(data["upcoming"])


if __name__ == "__main__":
    app.run()
