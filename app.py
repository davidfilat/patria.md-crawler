from flask import Flask, json
from importer.import_movies import import_all
app = Flask(__name__)
data = import_all()


@app.route('/')
def hello_world():
    return json.jsonify(data)


if __name__ == '__main__':
    app.run()
