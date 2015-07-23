from flask import Flask
from flask import jsonify, render_template
#from flask_cors import CORS
import math
import pandas as pd
import os
import datetime

app = Flask(__name__)

@app.route("/")
def default():
    return render_template('index.html')
    
@app.route('/test')
def test():
    """
    To access this function try:
    var xhr = new XMLHttpRequest()
    xhr.open('GET', '/test', true)
    xhr.send(null)
    xhr.response
    """
    return jsonify({'response':'everything is okay'})
    
@app.route("/explore/")
@app.route("/explore/<danger>&<n>&<loc_type>&<loc_spec>&<start>&<end>", methods=['GET'])
def explore(danger=None, n=None, loc_type=None, loc_spec=None, start=0, end=0):
    #get for a specific time slice
    if start == '0':  # no time slice -- use pre-grouped
        df = pd.read_csv('data/intersections.csv')
    else:
        # get specific time frame
        global crashes
        s = datetime.datetime.strptime(start, '%b %Y')
        e = datetime.datetime.strptime(end, '%b %Y')+datetime.timedelta(days=30)
        df = crashes[(crashes.DATE >= s) & (crashes.DATE <= e)]
        if len(crashes) == 0:  # no crashes in that time frame
            print "Zero crashes for that time period"
            return jsonify({'markers':[], 'success':False})

        # do the grouping procedure
        df = group(df)
        
    #get for the specific location
    if loc_type == "CITYWIDE":
        intersections = df.sort(danger, ascending=False).head(n=int(n)).iterrows()
    else:
        if loc_type != "BOROUGH":
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
    #group and aggregate
    gb = crashes.groupby(by='INTERSECTION', as_index=False)
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
               u'NUMBER OF PERSONS INJURED':sum,
               u'NUMBER OF PERSONS KILLED':sum,
               u'NUMBER OF PEDESTRIANS INJURED':sum,
               u'NUMBER OF PEDESTRIANS KILLED':sum,
               u'NUMBER OF CYCLIST INJURED':sum,
               u'NUMBER OF CYCLIST KILLED':sum,
               u'NUMBER OF MOTORIST INJURED':sum,
               u'NUMBER OF MOTORIST KILLED':sum,
               'CRASHES':sum
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
    
    data = pd.read_csv('data/traffic_intersections.csv')
    for _, row in data.iterrows():  
        d,t = row[danger], transform(row[traffic])
        red = 255 - ((float(t)/20) * 255)
        green = 255 - min((255, int(d)))
        blue = 0
        color = '#%02x%02x%02x' % (red, green, blue)
        
        j['circles'].append({'lon':float(row['LONGITUDE']),
                             'lat':float(row['LATITUDE']),
                             'color':color})
    return jsonify(j)

@app.route("/humps/")
def humps():
    j = {'markers':[]}
    f = open('data/speed_humps.csv', 'r')
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
    #define cirle colors
    j = {'circles':[]}
    colors = ["#FF00FF", "#000000", "#008000", "#FFFF00",
              "#0000FF", "#FF0000", "#00FFFF", "#FFFFFF"]

    #build the json to return
    intersections = pd.read_csv('data/clean_intersections.csv')
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
    crashes = pd.read_csv('data/crashes_clean.csv')
    #crashes = pd.read_csv('data/crashes_test.csv')
    crashes.DATE = crashes.DATE.apply(pd.to_datetime)
    crashes['INTERSECTION'] = crashes['LATITUDE'].apply(str) + "_" + crashes['LONGITUDE'].apply(str)
    crashes['CRASHES'] = 1
    print 'done.'
    
    # run the app
    #app.run(debug = True)
    app.run(host='0.0.0.0', port=int(port))
