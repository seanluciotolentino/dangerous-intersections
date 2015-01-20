import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import time

# CLEAN CRASH DATA SET
crashes = open('../crash_data/crashes.csv', 'r')
heading = crashes.readline().strip().split(',')  # skip the first line
w = open('../crash_data/crashes_clean.csv', 'w')
 
    
# Example: METROPOLITAN AVENUE and 74 AVENUE
def latlon_geocode(latlon):
    time.sleep(0.25)
    r = requests.get('http://nominatim.openstreetmap.org/search?q='+latlon+'&addressdetails=1&format=json')
    return r.json()

def address_geocode(address):
    time.sleep(0.5)
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+address+',new york,ny')
    return r.json()

#go through each line and clean it
count = 0
for crash in crashes:
    #time.sleep(1)i
    print count,
    count+=1
    #if count < 2831:
    #    continue
        
    #parse the line
    line = crash.strip().split(',')
    print line[:9],
    bor = line[2]
    zip_ = line[3]
    lat = line[4]
    lon = line[5]
    st1 = line[6]
    st2 = line[7]
    st3 = line[8]

    #find missing info if needed
    try:
        if bor != '' and zip_ != '' and lat != '' and lon != '': # this line is okay
            print 'okay'
            pass
        elif lat != '' and lon != '': # get streets
            print 'lat/lon geocoding st1:', st1, 'st2:', st2
            geo = latlon_geocode(lat+','+lon)
            bor = geo[0]['address']['county'][:geo[0]['address']['county'].index(' ')]
            zip_ = geo[0]['address']['postcode']
            st1 = geo[0]['address']['road']
            #print geo
            #break
        elif st1 != '' and st2 != '':
            print 'st1/st2 geocoding'
            geo = address_geocode(st1+' and '+st2)            
            #print geo['results'][0]
            bor = [ac['short_name'] for ac in geo['results'][0]['address_components'] if 'sublocality' in ac['types']][0]
            zip_ = [ac['short_name'] for ac in geo['results'][0]['address_components'] if 'postal_code' in ac['types']][0]
            lat = geo['results'][0]['geometry']['location']['lat']
            lon = geo['results'][0]['geometry']['location']['lng']
            #neigh = [ac['short_name'] ac in geo['results'][0]['address_components'] if 'neighborhood' in ac['types']][0]
        elif st3 != '' and False: #I can't geocode this correctly
            print 'st3 geocoding'
            geo = address_geocode(st3)
            #print geo['results'][0]
            #break
            bor = [ac['short_name'] for ac in geo['results'][0]['address_components'] if 'sublocality' in ac['types']][0]
            zip_ = [ac['short_name'] for ac in geo['results'][0]['address_components'] if 'postal_code' in ac['types']][0]
            lat = geo['results'][0]['geometry']['location']['lat']
            lon = geo['results'][0]['geometry']['location']['lng']
            #neigh = [ac['short_name'] ac in geo['results'][0]['address_components'] if 'neighborhood' in ac['types']][0]
        else:
            print "not enough location details!"
    except Exception as e:
        print '---start exception---'
        print 'st1', st1, 'st2', st2
        print geo
        print '---end exception---'
        lat, lon = (-1, -1)  # set lat / lon so we don't try to geocode again on next pass

    #replace line entries
    line[2] = bor.upper()
    line[3] = zip_
    line[4] = str(lat)
    line[5] = str(lon)
    line[6] = st1.upper()
    line[7] = st2.upper()
    
    w.write(','.join(line)+'\n')
    
crashes.close()
w.close()

