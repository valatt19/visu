from app import app
from flask import render_template, redirect
from flask import url_for, request

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


    return render_template("location.html")

# Visualisation (for comparison) ##########################
@app.route("/comparaison/", methods=["GET","POST"])
def comparaison():
    return render_template("comparaison.html")

#######
# RUN #
#######
if __name__ == "__main__":
        app.run()