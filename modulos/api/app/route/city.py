from flask import Flask, request, render_template
from app.controller.controller_city import Controller_City

app = Flask("app")
controller = Controller_City()

@app.route("/city/")
def get_cities(cidade):

    # controller.get_cities()
    cidades = list()

    return cidades

@app.route("/city/<city>")
def get_city(cidade):

    city = request.args.get("city")
    # controller.get_city(city)
    dados_cidade = list()

    return dados_cidade

@app.route("/city/number/<int: number>")
def get_city(cidade):

    city = request.args.get("number")
    # controller.get_city(city)
    dados_cidade = list()

    return dados_cidade