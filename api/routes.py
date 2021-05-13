from api import app
from api import processing
from flask import render_template


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/manufacturers")
def manufacturers():
    return processing.get_list_of_manufacturers()


@app.route("/manufacturers/all")
def all_manufacturers():
    return processing.get_list_of_manufacturers(find_all=True)


@app.route("/makes/<manufacturer>")
def makes_from_manufacturer(manufacturer):
    return processing.get_all_makes_for_manufacturer(manufacturer)


@app.route("/<vin>")
def info_from_vin(vin):
    return processing.get_vehicle_info_from_vin(vin)
