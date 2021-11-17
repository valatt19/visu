from app import app
from flask import render_template, redirect
from flask import url_for, request

from app.datasets.datasets_methods import get_events_in_radius

##########
# ROUTES #
##########

# Homepage (for searching a location) ######################
@app.route("/", methods=["GET","POST"])
def index():


    return render_template("homepage.html")

# Visualisation (for  a location) ##########################
@app.route("/location/", methods=["GET","POST"])
def location():
    if request.args.get("lat", None) and request.args.get("long", None):
        coord = (request.args["lat"],request.args["long"])

        # Get all the events in the radius of a location 
        events = get_events_in_radius(coord,100)
        nb_earthquakes = len(events["earthquakes"])
        nb_volcanos = len(events["volcanos"])
        nb_tsunamis = len(events["tsunamis"])

        return render_template("location.html",summary=[nb_volcanos,nb_earthquakes,nb_tsunamis],events = events)

    return redirect(url_for("index"))

# Visualisation (for comparison) ##########################
@app.route("/comparaison/", methods=["GET","POST"])
def comparaison():
    return render_template("comparaison.html")

#######
# RUN #
#######
if __name__ == "__main__":
        app.run()