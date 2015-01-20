from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/intersections")
def intersections():
    #return "hello world"
    j = {'markers':[]}
    f = open('crash_data/intersections.csv', 'r')
    f.readline()  # skip header
    count = 0
    #return 'hello world'
    for line in f:
        count+=1
        if count > 20:
            break
        line = line.strip().split(',')
        j['markers'].append({'lon':float(line[5]), 'lat':float(line[13]), 'crashes':line[16]})
    #return 'hello world'
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
        if pd3<0:
            color = 'red'
        elif pd3 == 0:
            color = 'blue'
        else:
            color = 'green'
        j['markers'].append({'lon':lon, 
                             'lat':lat, 
                             'date':line[11],
                             'crashes3b':line[21],
                             'crashes3a':line[20],
                             'crashes6b':line[23],
                             'crashes6a':line[22],
                             'PD3':float(line[-5]),
                             'PD6':float(line[-4]),
                             'color':color
                             })
    return jsonify(j)


if __name__ == "__main__":
    app.debug = True
    app.run()

