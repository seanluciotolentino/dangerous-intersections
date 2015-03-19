from flask import Flask
from flask import jsonify
from flask_cors import CORS
import math
import pandas as pd
import os
import datetime
import numpy as np
import time

app = Flask(__name__)
cors = CORS(app)

"""
CODE SNIPPED TO PRINT COLUMNS AND COLUMN NUMBERS
f = open('../crash_data/intersections.csv', 'r')
cols = f.readline().strip().split(',')
for i in range(len(cols)): print i, cols[i]
key = {}
for i in range(len(cols)): key[cols[i]] = i
"""
key = {'NUMBER OF CYCLIST KILLED': 0, 'ZIP CODE': 5, 'FOUR_SQUARE_DRINK': 21, 'YELP_SHOW': 20, 'YELP_DRINK': 17, 'OFF STREET NAME': 15, 'NUMBER OF MOTORIST KILLED': 8, 'YELP_MUSIC': 19, 'ON STREET NAME': 1, 'CROSS STREET NAME': 9, 'YELP_FOOD': 18, 'NUMBER OF MOTORIST INJURED': 4, 'LONGITUDE': 6, 'NUMBER OF PEDESTRIANS INJURED': 11, 'NUMBER OF PEDESTRIANS KILLED': 10, 'CRASHES': 2, 'NUMBER OF PERSONS KILLED': 3, 'NUMBER OF CYCLIST INJURED': 7, 'YELP_BAR': 16, 'LATITUDE': 12, 'NUMBER OF PERSONS INJURED': 13, 'BOROUGH': 14, 'FOUR_SQUARE_FOOD': 22}


@app.route("/")
def default():
    return jsonify({"msg":"Flask API working!"})
    
@app.route("/explore/")
@app.route("/explore/<danger>&<n>&<loc_type>&<loc_spec>&<start>&<end>", methods=['GET'])
def explore(danger=None, n=None, loc_type=None, loc_spec=None, start=0, end=0):
    #sort the intersection data by danger
    #return jsonify({'loc_type':loc_type, 'loc_spec':loc_spec,
    #                'start':start, 'end':end})
    start_time = time.time()
    #get for a specific time slice
    if start == '0':  # no time slice -- use pre-grouped
        df = pd.read_csv('crash_data/intersections.csv')
    else:
        # get specific time frame
        global crashes
        s = datetime.datetime.strptime(start, '%b %Y')
        e = datetime.datetime.strptime(end, '%b %Y')+datetime.timedelta(days=30)
        crashes = crashes[(crashes.DATE >= s) & (crashes.DATE <= e)]
        if len(crashes) == 0:  # no crashes in that time frame
            print "Zero crashes for that time period"
            return jsonify({'markers':[], 'success':False})

        # do the grouping procedure
        df = group(crashes)
        
    #get for the specific location
    if loc_type == "CITYWIDE":
        intersections = df.sort(danger, ascending=False).head(n=int(n)).iterrows()
    else:
        if loc_type is not "BOROUGH":
            loc_spec = int(loc_spec)
        intersections = df[df[loc_type]==loc_spec].sort(danger, ascending=False).head(n=int(n)).iterrows()
    
    #get top n and make them into markers
    j = {'markers':[], 'success':True}
    rank=0
    for intersection in intersections:
        lat = intersection[1].LATITUDE
        lon = intersection[1].LONGITUDE
        rank+=1
        main_text = "<b>{0}</b><br>{1}".format(rank, intersection[1][danger])
        popup_text = """<b>Rank: {0}</b><br>
                        {1}: {2}<br>
                        Street 1: {3}<br>
                        Street 2: {4}"""
        popup_text = popup_text.format(rank,
                                       danger,
                                       intersection[1][danger], 
                                       intersection[1]["ON STREET NAME"],
                                       intersection[1]["CROSS STREET NAME"])
    
        j['markers'].append({'lon':lon, 
                             'lat':lat, 
                             'main_text':main_text,
                             'popup_text':popup_text,
                             'color':'#%02x%02x%02x' % (255, 0, 0)
                             })
    return jsonify(j)

def group(crashes):
    """
    Helper function for doing the groupby operation when looking
    for crashes within a specific time slice.
    """
    #add index and crash counter
    crashes['INTERSECTION'] = crashes['LATITUDE'].apply(str) + "_" + crashes['LONGITUDE'].apply(str)
    crashes['CRASHES'] = 1
    
    #group and aggregate
    gb = crashes.groupby(by='INTERSECTION', as_index=False)
    longest = lambda x: x.get(x.map(lambda x: len(str(x))).idxmax())  # longest string
    mirror = lambda x: x.iget(0)
    agg_fun = {u'BOROUGH':mirror,
               u'DISTRICT':mirror,
               u'PRECINCT':mirror,
               u'ZIP CODE':mirror,
               u'LATITUDE':mirror,
               u'LONGITUDE':mirror,
               u'ON STREET NAME':mirror,
               u'CROSS STREET NAME':mirror,
               u'OFF STREET NAME':mirror,
               u'NUMBER OF PERSONS INJURED':np.sum,
               u'NUMBER OF PERSONS KILLED':np.sum,
               u'NUMBER OF PEDESTRIANS INJURED':np.sum,
               u'NUMBER OF PEDESTRIANS KILLED':np.sum,
               u'NUMBER OF CYCLIST INJURED':np.sum,
               u'NUMBER OF CYCLIST KILLED':np.sum,
               u'NUMBER OF MOTORIST INJURED':np.sum,
               u'NUMBER OF MOTORIST KILLED':np.sum,
               'CRASHES':np.sum
               }

    return gb.aggregate(agg_fun)

@app.route("/intersections/")
@app.route("/intersections/<danger>&<traffic>", methods=['GET'])
def intersections(danger=None, traffic=None):
    if not danger or not traffic:
        return jsonify({'error':True, "message":"Not all parameters specified", 'danger':danger, "traffic":traffic})
    if "FOUR SQUARE" in traffic:
        transform = lambda x: 20*math.log(x)
    else:
        transform = lambda x: x
    j = {'circles':[]}
    
    f = open('crash_data/intersections.csv', 'r')
    f.readline()  # skip header
    for line in f:
        line = line.strip().split(',')
        #if np.random.random() > 0.5:# and line[key['BOROUGH']] != 'MANHATTAN': #
        #    continue
        
        #add circles
        d,t = line[key[danger]], transform(line[key[traffic]])
        red = 255 - ((float(t)/20) * 255)
        green = 255 - min((255, int(d)))
        blue = 0
        color = '#%02x%02x%02x' % (red, green, blue)
        
        j['circles'].append({'lon':float(line[key['LONGITUDE']]),
                             'lat':float(line[key['LATITUDE']]),
                             'color':color})
    f.close()
    return jsonify(j)

@app.route("/humps/")
def humps():
    #return "hello world"
    j = {'markers':[]}
    f = open('intervention_data/speed_humps.csv', 'r')
    f.readline()  # skip header
    #return 'hello world'
    for line in f:
        line = line.strip().split(',')
        lat = float(line[-8].replace("(","").replace('"',''))
        lon = float(line[-7].replace(")","").replace('"',''))
        pd3 = float(line[-10])
        if pd3<0: color = '#%02x%02x%02x' % (255*-max((-1,pd3)), 0, 0)
        elif pd3 > 0: color = '#%02x%02x%02x' %  (0, 255*min((1,pd3)), 0)
        else: color = '#%02x%02x%02x' %  (0, 0, 255)
        text = """<html><b> Date Built: {0} </b><br>
                3 month percent decrease: {1} <br>
                6 month percent decrease:  {2} <br>
                =========================<br>
                Crashes 3 month before:  {3}  <br>
                Crashes 3 month after:  {4} <br>
                Crashes 6 month before: {5} <br>
                Crashes 6 month after: {6} </html>"""
                
        text = text.format(line[11], float(line[-11]), float(line[-10]), line[21],  line[20], line[23], line[22])
    
        j['markers'].append({'lon':lon, 
                             'lat':lat, 
                             'text':text,
                             'color':color
                             })
    return jsonify(j)

@app.route("/clusters/")
def clusters():
    #define some stuff
    j = {'circles':[]}
    colors = ["#FF00FF", "#000000", "#008000", "#FFFF00",
              "#0000FF", "#FF0000", "#00FFFF", "#FFFFFF"]

    #build the json to return
    intersections = pd.read_csv('crash_data/clean_intersections.csv')
    for row in intersections.iterrows():   
        j['circles'].append({'lon':float(row[1].lon),
                             'lat':float(row[1].lat),
                             'color':colors[row[1].cluster%len(colors)]})
    return jsonify(j)

@app.route("/schools/") # NOT IMPLEMENTED YET!
def schools():
    #define some stuff
    j = {'circles':[]}
    colors = ["#FF00FF", "#000000", "#008000", "#FFFF00",
              "#0000FF", "#FF0000", "#00FFFF", "#FFFFFF"]

    #build the json to return
    intersections = pd.read_csv('crash_data/clean_intersections.csv')
    for row in intersections.iterrows():   
        j['circles'].append({'lon':float(row[1].lon),
                             'lat':float(row[1].lat),
                             'color':colors[row[1].cluster%len(colors)]})

port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
    #preload crash data
    print "loading crash data..."
    crashes = pd.read_csv('crash_data/crashes_clean.csv')
    crashes.DATE = crashes.DATE.apply(pd.to_datetime)
    print 'done.'
    #app.run(debug = True)
    app.run(host='0.0.0.0', port=int(port))
