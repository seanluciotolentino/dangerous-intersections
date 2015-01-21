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

"""


@app.route("/")
def default():
    return jsonify({"msg":"Don't forget to specify a map type!"})

@app.route("/intersections")
def intersections():
    #return "hello world"
    j = {'markers':[], 'circles':[]}
    f = open('crash_data/intersections.csv', 'r')
    f.readline()  # skip header
    count = 0
    #return 'hello world'
    for line in f:
        count+=1
        #if count > 20000:
        #    break
        line = line.strip().split(',')
        if np.random.random() > 0.8 and line[-4] != 'MANHATTAN':
            continue
        

        #add circles
        yelp80 = float(line[17])/20
        crashes = min((255, int(line[3])))
        color = '#%02x%02x%02x' % (255-(255*yelp80), 255-crashes, 0)
        
        j['circles'].append({'lon':float(line[7]),
                             'lat':float(line[13]),
                             'color':color,
                             'yelp80':yelp80})

        #add markers (first X only)
        if count > 10:
            continue        
        
        text = """CRASHES: {0} <br>
                YELP80: {1} <br>
                PEDESTRIAN INJURIES: {2} <br>
                PEDESTRIAN DEATHS: {3}""".format(line[3], 
                                                 line[17],
                                                 line[12],
                                                 line[11])
        j['markers'].append({'lon':float(line[7]),
                             'lat':float(line[13]), 
                             'text':text})
    #return 'hello world'
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

