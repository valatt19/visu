import math
import geopy.distance as dist
import json

def compute_distance(coord1, coord2):
    """ Computes a distance in KM between two coordinates

    Parameters
    ----------
    - coord1 (list) : [latitude, longitude] of the first place
    - coord2 (list) : [latitude, longitude] of the second place

    Returns
    -------
    - distance (float) : distance in KM between the two coordinates
    """

    return dist.distance(coord1, coord2).km

def get_events_in_radius(coord,radius):
    """ Gets all the events that happened in the radius of a place

    Parameters
    ----------
    - coord (list) : [latitude, longitude] of the place
    - radius (float) : distance of the max radius in KM

    Returns
    -------
    - events (dict) : all the event that appened in the radius 
    """
    # Import json files into dicts
    with open("earthquakes_events.json") as eq_file:
        eq = json.load(eq_file)

    with open("tsunamis_events.json") as ts_file:
        ts = json.load(ts_file)
    
    with open("volcano_events.json") as ve_file:
        ve = json.load(ve_file)
    
    with open("volcano_locations.json") as vl_file:
        vl = json.load(vl_file)

    with open("helper_dataset.json") as hd_file:
        hd = json.load(hd_file)

    events = {"earthquakes":[],"tsunamis":[],"volcanos":[]}
    
    # Check all the earthquakes events
    for earthquake in eq :
        if "latitude" in earthquake and "longitude" in earthquake :
            eq_coord = (earthquake["latitude"],earthquake["longitude"])
            eq_distance = compute_distance(coord,eq_coord)

            if eq_distance <= radius :
                # Complete the infos of an event with the helper dataset
                eq_event = earthquake
                eq_event["distance"] = eq_distance

                if "intensity" in earthquake :
                    eq_event["intensity"] = hd["earthquakes"]["intensity"][earthquake["intensity"]-1]

                if (not ("deaths" in earthquake)) and "deathsAmountOrder" in earthquake :
                     deaths_mins = [0,1,51,101,1001]
                     # deaths_maxs = [0,50,100,1000,1001]
                     eq_event["deaths"] = deaths_mins[earthquake["deathsAmountOrder"]]

                if (not ("housesDamaged" in earthquake)) and "housesDamagedAmountOrder" in earthquake :
                     dam_mins = [0,1,51,101,1001]
                     # dam_maxs = [0,50,100,1000,1001]
                     eq_event["housesDamaged"] = dam_mins[earthquake["housesDamagedAmountOrder"]]

                if (not ("injuries" in earthquake)) and "injuriesAmountOrder" in earthquake :
                     inj_mins = [0,1,51,101,1001]
                     # inj_maxs = [0,50,100,1000,1001]
                     eq_event["injuries"] = inj_mins[earthquake["injuriesAmountOrder"]]

                if "damageMillionsDollars" in earthquake :
                     eq_event["damages"] = earthquake["damageMillionsDollars"]
                elif "damageAmountOrder" in earthquake : 
                     mil_mins = [0,1,2,5,25]
                     # mil_maxs = [0,50,100,1000,1001]
                     eq_event["damages"] = mil_mins[earthquake["damageMillionsDollars"]]

                events["earthquakes"].append(eq_event)

    # Finally, returns all the events            
    return events

print(get_events_in_radius([50.411461,4.44424],100))
            