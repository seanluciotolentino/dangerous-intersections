from flask import Flask
from flask import jsonify
from flask_cors import CORS
import numpy as np
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
key = { 'INTERSECTION': 0,
        'NUMBER OF CYCLIST KILLED': 1,
        'ON STREET NAME': 2,
        'CRASHES': 3,
        'NUMBER OF PERSONS KILLED': 4,
        'NUMBER OF MOTORIST INJURED': 5,
        'ZIP CODE': 6,
        'LONGITUDE': 7,
        'NUMBER OF CYCLIST INJURED': 8,
        'NUMBER OF MOTORIST KILLED': 9,
        'CROSS STREET NAME': 10,
        'NUMBER OF PEDESTRIANS KILLED': 11,
        'NUMBER OF PEDESTRIANS INJURED': 12,
        'LATITUDE': 13,
        'NUMBER OF PERSONS INJURED': 14,
        'BOROUGH': 15,
        'OFF STREET NAME': 16,
        'SPEED HUMP': 17,
        'YELP_BAR_80': 18,
        'YELP_DRINK_80': 19,
        'YELP_FOOD_80': 20,
        'YELP_MUSIC_80': 21,
        'YELP_SHOW_80': 22
        }

@app.route("/")
def default():
    return jsonify({"msg":"Don't forget to specify a map type!"})

@app.route("/intersections/")
@app.route("/intersections/<danger>&<traffic>", methods=['GET'])
def intersections(danger=None, traffic=None):
    #return jsonify({'message':"hello", 'danger':danger, "traffic":traffic})
    j = {'circles':[]}
    
    f = open('crash_data/intersections.csv', 'r')
    f.readline()  # skip header
    for line in f:
        line = line.strip().split(',')
        if line[key['BOROUGH']] != 'MANHATTAN': # np.random.random() > 0.5:# and 
            continue
        
        #add circles
        d,t = line[key[danger]], line[key[traffic]]
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
        text = """<html><b> {0} </b><br>
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


if __name__ == "__main__":
    app.debug = True
    app.run()

