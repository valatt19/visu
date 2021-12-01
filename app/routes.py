from app import app
from flask import render_template, redirect
from flask import url_for, request

from app.datasets.datasets_methods import get_events_in_radius, get_timeline_events, get_amount_erruptions

##########
# ROUTES #
##########

# Homepage (for searching a location) ######################
@app.route("/", methods=["GET","POST"])
def index():


    return render_template("homepage.html")

# Visualisation (for  a location) ##########################
@app.route("/location/", defaults={"scale": 50}, methods=["GET","POST"])
@app.route("/location/<int:scale>/", methods=["GET","POST"])
def location(scale):
    # Get the coordinates indicated by the user
    if request.args.get("lat", None) and request.args.get("long", None):
        coord = (request.args["lat"],request.args["long"])

        # Get all the events in the radius of a location 
        events = get_events_in_radius(coord,scale)
        nb_earthquakes = len(events["earthquakes"])
        nb_volcanos = len(events["volcanos"])
        nb_tsunamis = len(events["tsunamis"])
        nb_erruptions = get_amount_erruptions(events)

        #info contains the sum of the damage("damageMillionsDollars", "deaths", "damageAmountOrder",
        # "deathsAmountOrder", "deathsAmountOrder", "housesDestroyedAmountOrder")
        info = dict()

        for event_type, event in events.items():
            for i in event:
                for title, containt in i.items():
                    if title in ["damages", "deaths", "housesDamaged", "injuries"]:
                        if title in info:
                            info[title] = info[title] + int(containt)
                        else:
                            info[title] = int(containt)

        # Get the infos for the timeline
        timeline = get_timeline_events(events)

        return render_template("location.html", summary=[nb_volcanos, nb_earthquakes, nb_tsunamis, nb_erruptions], events=events, info=info, coord=coord, scale=scale, semi_scale=int(scale/2),timeline=timeline)

    return redirect(url_for("index"))

# Visualisation (for comparison) ##########################
@app.route("/comparaison/", defaults={"scale": 50}, methods=["GET","POST"])
@app.route("/comparaison/<int:scale>/", methods=["GET","POST"])
def comparaison(scale):
     # Get the coordinates indicated by the user
    if request.args.get("lat", None) and request.args.get("long", None):
        coord = (request.args["lat"],request.args["long"])

        # Get all the events in the radius of the 1st location
        events = get_events_in_radius(coord,scale)
        nb_earthquakes = len(events["earthquakes"])
        nb_volcanos = len(events["volcanos"])
        nb_tsunamis = len(events["tsunamis"])
        nb_erruptions = get_amount_erruptions(events)

        # Get the infos for the timeline
        tl = get_timeline_events(events)

        if request.args.get("lat2", None) and request.args.get("long2", None):
            coord2 = (request.args["lat2"],request.args["long2"])
            # Get all the events in the radius of the 2nd location
            events2 = get_events_in_radius(coord2,scale)
            nb_earthquakes2 = len(events2["earthquakes"])
            nb_volcanos2 = len(events2["volcanos"])
            nb_tsunamis2 = len(events2["tsunamis"])
            nb_erruptions2 = get_amount_erruptions(events)

            # Get the infos for the timeline
            tl2 = get_timeline_events(events2)

            # Page called with 2 coordinate
            return render_template("comparaison.html",nb_places=2,summary=[nb_volcanos,nb_earthquakes,nb_tsunamis,nb_erruptions,nb_volcanos2,nb_earthquakes2,nb_tsunamis2,nb_erruptions2],events = [events,events2], coord=[coord,coord2],scale=scale, semi_scale=int(scale/2),timeline=[tl,tl2])
        
        # Page called with 1 coordinate
        return render_template("comparaison.html",nb_places=1,summary=[nb_volcanos,nb_earthquakes,nb_tsunamis,nb_erruptions],events = [events], coord=[coord],scale=scale, semi_scale=int(scale/2),timeline=[tl])

    # Page called with 0 coordinate
    return render_template("comparaison.html",nb_places=0)

#######
# RUN #
#######
if __name__ == "__main__":
        app.run()