from flask import Flask
from flask import jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import pickle

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
    return jsonify({"msg":"Don't forget to specify a map type!"})
    
@app.route("/explore/")
@app.route("/explore/<danger>&<n>", methods=['GET'])
def explore(danger=None, n=None):
    #sort the intersection data by danger
    df = pd.read_csv('crash_data/intersections.csv')
    df.sort(danger, ascending=False, inplace=True)
    df.to_csv('crash_data/intersections.csv', index=False)
    
    #get top n and make them into markers
    j = {'markers':[]}
    f = open('crash_data/intersections.csv', 'r')
    f.readline()  # skip header
    count = 0
    for line in f:
        count+=1
        if count > int(n):
            break
        line = line.strip().split(',')
        lat = float(line[key['LATITUDE']])
        lon = float(line[key['LONGITUDE']])
        main_text = "<b>{0}</b><br>{1}".format(count, line[key[danger]])
        popup_text = """<b>Rank: {0}</b><br>
                        {1}: {2}<br>
                        Street: {3}"""
        popup_text = popup_text.format(count,
                                       danger,
                                       line[key[danger]], 
                                       line[key['ON STREET NAME']])
    
        j['markers'].append({'lon':lon, 
                             'lat':lat, 
                             'main_text':main_text,
                             'popup_text':popup_text,
                             'color':'#%02x%02x%02x' % (255, 0, 0)
                             })
    return jsonify(j)

@app.route("/intersections/")
@app.route("/intersections/<danger>&<traffic>", methods=['GET'])
def intersections(danger=None, traffic=None):
    if not danger or not traffic:
        return jsonify({'error':True, "message":"Not all parameters specified", 'danger':danger, "traffic":traffic})
    if "FOUR SQUARE" in traffic:
        transform = lambda x: 20*np.log(x)
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

@app.route("/humps")
def humps():
    #return "hello world"
    j = {'markers':[]}
    f = open('intervention_data/speed_humps.csv', 'r')
    f.readline()  # skip header
    #return 'hello world'
    for line in f:
        line = line.strip().split(',')
        lat = float(line[-2].replace("(","").replace('"',''))
        lon = float(line[-1].replace(")","").replace('"',''))
        pd3 = float(line[-5])
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
                
        text = text.format(line[11], float(line[-5]), float(line[-4]), line[21],  line[20], line[23], line[22])
    
        j['markers'].append({'lon':lon, 
                             'lat':lat, 
                             'text':text,
                             'color':color
                             })
    return jsonify(j)

@app.route("/clusters/<n_clusters>", methods=['GET'])
def clusters(n_clusters=None):
    if not n_clusters:
        return jsonify({'error':True, "message":"Not all parameters specified", 'n_clusters':n_clusters})
    #define some stuff
    j = {'circles':[]}
    colors = ["#000000", "#ff0000", "#0000ff", "#40e0d0", "#660066", "#ffff00",
              "#ff00ff", "#00ff00", "#008000", "#ff69b4"]

    #run the clustering algorithm
    intersections = pd.read_csv('crash_data/clean_intersections.csv')
    learning_columns = filter(lambda x: x not in ['name', 'lat', 'lon', 'street1', 
                                                  'street2', 'month', 'year', 'borocode'],
                                                  intersections.columns)
    k_means = KMeans(n_clusters=int(n_clusters)).fit(intersections[learning_columns])
    #k_means = pickle.load(open('mapping/clusters/{0}_means.pickle'.format(n_clusters), 'r'))
    intersections["cluster"] = k_means.labels_
    j['inertia']=k_means.inertia_
    
    #build the json to return
    for row in intersections.iterrows():
        
        j['circles'].append({'lon':float(row[1].lon),
                             'lat':float(row[1].lat),
                             'color':colors[row[1].cluster%len(colors)]})
    return jsonify(j)


if __name__ == "__main__":
    #app.debug = True
    app.run()

