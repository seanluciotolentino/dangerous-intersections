# Dangerous Intersections

This is the repository for Lucio Tolentino's work on the NYPD crash data set. The 
data is hosted from the open data portal (https://data.cityofnewyork.us/) -- I 
can't host it here because of GitHub's file limit size.

IPython Notebooks
----------------

After downloading the [crash data] (https://data.cityofnewyork.us/NYC-BigApps/NYPD-Motor-Vehicle-Collisions/h9gi-nx95?) place it
in a subfolder called "crash_data". Use DataBuilding.ipynb (in the ipython_notebook
 subfolder) to build the intersections data set. You can then use DataExploring.ipynb
to *explore* the data a bit.

Mapping
-------------------

To check out the maps, run 

```
  python host_data.py
```

This will start a server for the data and you can just open the *.html files
with your browser. You might have to change the *.html files to reflect the
IP address and port number return from host_data.

Disclaimer
-----------------------

As I write all this I realize how confusing it all is. I'll eventually put it 
into an easier to digest form. Until then, I apologize.
 
