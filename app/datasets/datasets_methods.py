import geopy.distance as dist
import json 

from geographiclib.geodesic import Geodesic

from math import sin, cos, radians, pi
def point_pos(x0, y0, d, theta):
    theta_rad = 3*pi/2 + radians(theta)
    return x0 + d*cos(theta_rad), y0 + d*sin(theta_rad)


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

def compute_bearing(coord1, coord2):
    """ Computes a bearing between two coordinates

    Parameters
    ----------
    - coord1 (list) : [latitude, longitude] of the first place
    - coord2 (list) : [latitude, longitude] of the second place

    Returns
    -------
    - bearing (float) : distance in KM between the two coordinates
    """
    return Geodesic.WGS84.Inverse(float(coord1[0]), float(coord1[1]), float(coord2[0]), float(coord2[1]))['azi1']

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
    with open("app/datasets/earthquakes_events.json") as eq_file:
        eq = json.load(eq_file)

    with open("app/datasets/tsunamis_events.json") as ts_file:
        ts = json.load(ts_file)
    
    with open("app/datasets/volcano_events.json") as ve_file:
        ve = json.load(ve_file)
    
    with open("app/datasets/volcano_locations.json") as vl_file:
        vl = json.load(vl_file)

    with open("app/datasets/helper_dataset.json") as hd_file:
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
                eq_event["bearing"] = compute_bearing(coord,eq_coord)
                eq_event["proj"] = point_pos(0,0,eq_distance,eq_event["bearing"])

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
                     eq_event["damages"] = mil_mins[earthquake["damageAmountOrder"]]

                events["earthquakes"].append(eq_event)

    # Check all the tsunami events
    for tsunami in ts :
        if "latitude" in tsunami and "longitude" in tsunami :
            ts_coord = (tsunami["latitude"],tsunami["longitude"])
            ts_distance = compute_distance(coord,ts_coord)

            if ts_distance <= radius :
                # Complete the infos of an event with the helper dataset
                ts_event = tsunami
                ts_event["distance"] = ts_distance
                ts_event["bearing"] = compute_bearing(coord,ts_coord)
                ts_event["proj"] = point_pos(0,0,ts_distance,ts_event["bearing"])
                
                if "causeCode" in tsunami :
                    for c in hd["tsunamis"]["causes"]:
                        if str(tsunami["causeCode"]) == c["id"]:
                            ts_event["cause"] = c["description"]

                if (not ("deaths" in tsunami)) and "deathsAmountOrder" in tsunami :
                     deaths_mins = [0,1,51,101,1001]
                     # deaths_maxs = [0,50,100,1000,1001]
                     ts_event["deaths"] = deaths_mins[tsunami["deathsAmountOrder"]]

                if (not ("housesDamaged" in tsunami)) and "housesDamagedAmountOrder" in tsunami :
                     dam_mins = [0,1,51,101,1001]
                     # dam_maxs = [0,50,100,1000,1001]
                     ts_event["housesDamaged"] = dam_mins[tsunami["housesDamagedAmountOrder"]]

                if (not ("injuries" in tsunami)) and "injuriesAmountOrder" in tsunami :
                     inj_mins = [0,1,51,101,1001]
                     # inj_maxs = [0,50,100,1000,1001]
                     ts_event["injuries"] = inj_mins[tsunami["injuriesAmountOrder"]]

                if "damageMillionsDollars" in tsunami :
                     ts_event["damages"] = tsunami["damageMillionsDollars"]
                elif "damageAmountOrder" in tsunami : 
                     mil_mins = [0,1,2,5,25]
                     # mil_maxs = [0,50,100,1000,1001]
                     ts_event["damages"] = mil_mins[tsunami["damageAmountOrder"]]

                events["tsunamis"].append(ts_event)

    # Check all the volcanos locations
    volcanos_id = [] # list of all id of the volcanos in the scope of the location
    for volcano in vl :
        if "latitude" in volcano and "longitude" in volcano :
            vl_coord = (volcano["latitude"],volcano["longitude"])
            vl_distance = compute_distance(coord,vl_coord)

            if vl_distance <= radius :
                volcanos_id.append(volcano["id"])
                vlocation = volcano
                vlocation["distance"] = vl_distance
                vlocation["bearing"] = compute_bearing(coord,vl_coord)
                vlocation["proj"] = point_pos(0,0,vl_distance,vlocation["bearing"])
                vlocation["erruptions"] = []

                events["volcanos"].append(vlocation)

    # Check all the erruptions and add it in the erruptions of the correspondant volcano
    for erruption in ve :
        for i in range(len(volcanos_id)):
            if str(erruption["volcanoLocationId"]) == str(volcanos_id[i]) :
                vevent = erruption

                if (not ("deaths" in erruption)) and "deathsAmountOrder" in erruption :
                        deaths_mins = [0,1,51,101,1001]
                        # deaths_maxs = [0,50,100,1000,1001]
                        vevent["deaths"] = deaths_mins[erruption["deathsAmountOrder"]]

                if (not ("housesDamaged" in erruption)) and "housesDamagedAmountOrder" in erruption :
                        dam_mins = [0,1,51,101,1001]
                        # dam_maxs = [0,50,100,1000,1001]
                        vevent["housesDamaged"] = dam_mins[erruption["housesDamagedAmountOrder"]]

                if (not ("injuries" in erruption)) and "injuriesAmountOrder" in erruption :
                        inj_mins = [0,1,51,101,1001]
                        # inj_maxs = [0,50,100,1000,1001]
                        vevent["injuries"] = inj_mins[erruption["injuriesAmountOrder"]]

                if "damageMillionsDollars" in erruption :
                        vevent["damages"] = erruption["damageMillionsDollars"]
                elif "damageAmountOrder" in erruption : 
                        mil_mins = [0,1,2,5,25]
                        # mil_maxs = [0,50,100,1000,1001]
                        vevent["damages"] = mil_mins[erruption["damageAmountOrder"]]

                events["volcanos"][i]["erruptions"].append(vevent)

    # Finally, returns all the events            
    return events

def get_timeline_events(events):
    """ Gets a dict with all events where the keys are years

    Parameters
    ----------
    - events (dict) : all the event that appened in the radius 

    Returns
    -------
    - timeline (dict) : dict with all events where the keys are years and the values are list of events (type + index)
        Example : {1966:[e1,v2,t1], 1789:[e3], ...}
    """
    # INIT
    timeline = {}

    # EARTHQUAKES
    for i in range(len(events["earthquakes"])):
        e = events["earthquakes"][i]
        
        # The event has an attribute year
        if "year" in e:
            id = "e"+ str(i)

            # Append the list of events in a same year
            if int(e["year"]) in timeline:
                timeline[int(e["year"])].append(id)

            # Create the value for this year
            else:
                timeline[int(e["year"])] = [id]

    # TSUNAMIS
    for i in range(len(events["tsunamis"])):
        e = events["tsunamis"][i]
        
        # The event has an attribute year
        if "year" in e:
            id = "t"+ str(i)

            # Append the list of events in a same year
            if int(e["year"]) in timeline:
                timeline[int(e["year"])].append(id)

            # Create the value for this year
            else:
                timeline[int(e["year"])] = [id]

    # ERRUPTIONS
    for i in range(len(events["volcanos"])):
        v = events["volcanos"][i]
        for j in range(len(v["erruptions"])):
            e = v["erruptions"][j]
        
            # The event has an attribute year
            if "year" in e:
                id = "v"+ str(i) + str(j)

                # Append the list of events in a same year
                if int(e["year"]) in timeline:
                    timeline[int(e["year"])].append(id)

                # Create the value for this year
                else:
                    timeline[int(e["year"])] = [id]


    print(timeline)
    return timeline