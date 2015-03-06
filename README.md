# Dangerous Intersections

This is the repository for Lucio Tolentino's work on the NYPD crash data set. The data was geo-tagged, aggregated to intersections, and is not hosted from BetaNYC's data portal (http://data.beta.nyc/dataset/crash-data). The final product is on heroku and you can check it out here http://walksafer.herokuapp.com. 

Installing and Exploring
----------------

First, download the [intersection data] (http://data.beta.nyc/dataset/crash-data) into the "crash_data" subfolder. Second, download the [speed hump data] (http://data.beta.nyc/dataset/speed-humps) into the "intervention_data" subfolder. You can then open map.html with your broswer.

Additionally I've provided the ipython notebooks (IntersectionExploration.ipynb in the ipython_notebook subfolder) for exploring the data some. [Click here] (http://ipython.org/notebook.html) to learn how to use ipython notebooks. 

Overview of Program Flow
-------------------

The front end is a single php file (index.php) in the web subfolder. When it is opened it makes a call to a flask api (host_data.py) that is currently running on a digitial ocean instance. 

Call for help
-----------------------

If you're interested in the project and want to contribute consider cloning / forking the project and tackling some of the issues (click that little "issues" tab between "code" and "pull requests"). If you need clarification about an issue, write a comment on it and I'll get back to you. 
 
