import json
from flask import Flask, render_template
from flask import make_response
from flask import jsonify

app = Flask('app')

@app.route("/")
def hello():
    return "Hello World in Flask!"

@app.route("/<name>")
def index(name):
    if name.lower() == "lorena":
        return "Olá {}".format(name), 200
    else:
        return "Not Found", 404

@app.route("/html_page/<nome>")
def html_page(nome):

    return render_template("html_page.html", nome=nome)

@app.route("/json")
def json_api():
    pessoas = [{"nome": "Bruno Rocha"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]

    return json.dumps(pessoas), 200, {"Content-Type": "application/json"}

@app.route("/jsonify")
def json_api_jsonify():
    pessoas = [{"nome": "Bruno Rocha"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]

    return jsonify(pessoas=pessoas, total=len(pessoas))

app.run(debug=True, use_reloader=True)

if __name__ == "__main__":
    app.run()

