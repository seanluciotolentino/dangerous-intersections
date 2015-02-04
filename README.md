# Dangerous Intersections

This is the repository for Lucio Tolentino's work on the NYPD crash data set. The data is hosted from the open data portal (https://data.cityofnewyork.us/) -- I can't host it here because of GitHub's file limit size. You can check out the final product at http://walksafer.herokuapp.com. 

Installing and Exploring
----------------

First, download the [crash data] (https://data.cityofnewyork.us/NYC-BigApps/NYPD-Motor-Vehicle-Collisions/h9gi-nx95?) as a CSV and place it
in a subfolder called "crash_data". Use IntersectionBuilding.ipynb (in the ipython_notebook
 subfolder) to build the intersections data set. You can then use IntersectionExploration.ipynb
to *explore* the data a bit.

Mapping
-------------------

To check out the maps open map.html from your browser. It'll make calls to the API living on my digital ocean instance. The code for the api is in host_data.py in the main directory. 

Disclaimer
-----------------------

I'm awesome. 
 
