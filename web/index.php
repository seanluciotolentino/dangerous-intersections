
<!doctype html>

<html lang="en">

<head>
  <meta charset="utf-8">
  <title>Walk Safer</title>
  <meta name="description" content="Walk Safer">
  <meta name="author" content="Lucio Tolentino">
  <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.css" />
  <link href='http://fonts.googleapis.com/css?family=Oxygen' rel='stylesheet' type='text/css'>
  <script src="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.js"></script>
  <script src="../javascript/Leaflet.MakiMarkers.js"></script>
  <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
  <script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
    <link rel="stylesheet" type="text/css" href="style.css" media="screen" />
 </head>

<body class="body">

	<div id = "header">
		<a href="map.html">Top</a>
	    <a href="#exploratory_analysis">Exploratory Analysis</a>
	    <a href="#pedestrian_traffic">Pedestrian Traffic</a>
	    <a href="#speed_humps">Speed Humps</a>
	</div>
    
    <div id = "introduction">
    	<h1> 
    		<img src="images/car.png" alt="car" style="height:25px"></img>
    		WalkSafer
    		<img src="images/car.png" alt="car" style="height:25px"></img>
    	</h1>
	    <h3> Every year in New York City about 4,000 people are seriously injured in traffic crashes and around  200 are killed. This is a disturbing statistic for anyone that walks in New York City (i.e. everyone in New York City). This project uses the NYPD's crash data, which includes around 600,000 crashes in the city since 01/01/2013, to identify the dangerous intersections and determine the salient features that make them dangerous.</h3>
	</div>	

	<!-- END EXPLORATORY ANALYSIS-->
	<a name="exploratory_analysis"></a> 
	<div id = "exploratory_analysis" class="application">		
        <div id="exploratory_analysis_explanation" class="explanation">
            <h1>Exploratory Analysis</h1>
            <p>We start the analysis with a few exploratory questions about the data.</p>
        </div>

        <div id="exploratory_analysis_application">
        	What are the top <span id = 'ea_dd2'></span> intersections for <span id = 'ea_dd1'></span>?<button onclick="draw_ea_map()" type="button">(update)</button>  	
        </div>

        <div id = 'exploratory_analysis_maps' style="width: 100%; height: 500px; background-color: lightgray;"></div>

        
	</div>

	<!-- END EXPLORATORY ANALYSIS-->

	<!-- PED TRAFFIC-->
	<div id = "pedestrian_traffic" class="application">
		<a name="pedestrian_traffic"></a> 
        <div id="pedestrian_traffic_explanation" class="explanation">
            <h1>Lots of foot traffic = lots of crashes</h1>
            <p>Here we map the crash data by coloring each intersection based on a metric of danger (number of crashes, number of pedestrian injuries, etc.) and the amount of foot traffic. As a proxy for foot traffic we used the number of businesses as returned by yelp (with different query terms) or the number of check-ins from Four Square (also with different query terms).  </p>

            <p>The result shows that there's a significant correlation between foot traffic and crashes (holy crap! look at times square!), but many high crash intersections are near the entrances to Manhattan (Queensboro Bridge and Lincoln Tunnel). This suggests that it's not a perponderance of pedestrians, but an excess of anxious drivers.</p>
        </div>

        <div id="map_controls" style="width:30%; float:left">
        	<p>Measure of danger</p>
            <div id = 'pd_dd1'></div>
            <p>Measure of foot traffic</p>
            <div id = 'pd_dd2'></div>
            <p>Redraw the map:</p>
            <button onclick="draw_pt_map()" type="button">Redraw Map</button>
            <img src="images/colorscale.png" alt="Color Scale" style="width:250px; height:250px"></img>
        </div>

        <div id="map_output">
			<div id="ped_map" style="width:70%; height:700px;"></div>
        </div>

        <div style="clear: both; display: block;"></div>

	</div>

	<script>
		//define dropdowns here
	    var dropdowns = [
	    				{"name":"ea_danger", 
	    				  "select":"span#ea_dd1",
	                      "values": ["CRASHES",
	                                "NUMBER OF PERSONS INJURED",
	                                "NUMBER OF PERSONS KILLED",
	                                "NUMBER OF CYCLIST INJURED",
	                                "NUMBER OF CYCLIST KILLED",
	                                "NUMBER OF MOTORIST INJURED",                                    
	                                "NUMBER OF MOTORIST KILLED",
	                                "NUMBER OF PEDESTRIANS INJURED",
	                                "NUMBER OF PEDESTRIANS KILLED",
	                                ]},
	                    {"name": "ea_top",
	                     "select":"span#ea_dd2",
	                     "values": ["10",
	                                "25",
	                                "50",
	                                "100",
	                                ]},
	    				{"name":"pt_danger", 
	    				  "select":"div#pd_dd1",
	                      "values": ["CRASHES",
	                                "NUMBER OF PERSONS INJURED",
	                                "NUMBER OF PERSONS KILLED",
	                                "NUMBER OF CYCLIST INJURED",
	                                "NUMBER OF CYCLIST KILLED",
	                                "NUMBER OF MOTORIST INJURED",                                    
	                                "NUMBER OF MOTORIST KILLED",
	                                "NUMBER OF PEDESTRIANS INJURED",
	                                "NUMBER OF PEDESTRIANS KILLED",
	                                ]},
	                    {"name": "pt_traffic",
	                     "select":"div#pd_dd2",
	                     "values": ["YELP_BAR",
	                                "YELP_DRINK",
	                                "YELP_FOOD",
	                                "YELP_MUSIC",
	                                "YELP_SHOW",
	                                "FOUR_SQUARE_DRINK",
	                                "FOUR_SQUARE_FOOD",]},
	                    ];
	    //draw dropdowns from lists
	    for(var i=0; i<dropdowns.length; i++){
	        dropdown = dropdowns[i]
			//add the dropdown
			d3.select(dropdown.select)
			 	.append("select")
			 	.attr("class", "dropdown")
			 	.attr("name", dropdown.name)
			 	.attr("id", dropdown.name);

			//add each value of the dropdown
			for(var j=0; j<dropdown.values.length; j++){
	            value = dropdown.values[j]
	            //console.log("dropdown:"+dropdown.name+" value:" + value)
					d3.select("select#"+dropdown.name)
						.append("option")
						.attr("value", this.value)
						.html(value.replace("_", " ").replace("_", " "))
						.on("select", function(v){
							d3.select(dropdown.select)
	    						.html(v)
	    						.attr("value", this.value);


					});
				}
			};

	    //make map
	    function draw_pt_map(){
	        //clear map
	        ped_map.remove()
	        ped_map = L.map("ped_map").setView([40.753597, -73.986808], 13);
	        L.tileLayer('http://{s}.tiles.mapbox.com/v3/seanluciotolentino.jhknj4m5/{z}/{x}/{y}.png',{
	        		maxZoom: 18
	        	}).addTo(ped_map);

	        //dropdowns
	        var danger = d3.select("#pt_danger")[0][0].selectedOptions[0].getAttribute("value")
	        var traffic = d3.select("#pt_traffic")[0][0].selectedOptions[0].getAttribute("value")
	        var call = "http://127.0.0.1:5000/intersections/"+danger+"&"+traffic
        	$.get(call,{}).then(function(data){
	            //add circles
	            for(var i =0; i<data.circles.length; i++){
	                c = data.circles[i]
        	    	L.circle([c.lat, c.lon], 50, {
           	    	    color: c.color,
        	    	    fillColor: c.color,
        	    	    fillOpacity: 0.5
        	    	}).addTo(ped_map);
        	    };
        	});
	    }

	    function draw_ea_map(){
    		//God forgive me for all the copy pasting (and horriable naming conventions) -- I'm on a deadline 
			ea_map.remove()
	        ea_map = L.map("exploratory_analysis_maps").setView([40.686106, -73.946747], 11);
			L.tileLayer('http://{s}.tiles.mapbox.com/v3/seanluciotolentino.jhknj4m5/{z}/{x}/{y}.png', {
				attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
				maxZoom: 15
			}).addTo(ea_map);
			
			//define points
	        var danger = d3.select("#ea_danger")[0][0].selectedOptions[0].getAttribute("value")
	        var n = d3.select("#ea_top")[0][0].selectedOptions[0].getAttribute("value")
			$.get("http://127.0.0.1:5000/explore/"+danger+"&"+n,{}).then(function(data){
				//add markers
			    (data.markers).forEach(function(marker){
			        L.marker([marker.lat, marker.lon], {
			            icon: L.divIcon({
			            html: marker.main_text,
			            className: 'count-icon',
			            iconSize: [30, 30]
			        	})
			        }).addTo(ea_map)
			        	.bindPopup(marker.popup_text);
			    });
			});
		}

	    var ped_map = L.map("ped_map").setView([40.753597, -73.986808], 13);
	    draw_pt_map()
	    var ea_map = L.map("exploratory_analysis_maps").setView([40.686106, -73.946747], 11);
	    draw_ea_map()
	</script>
	<!-- END PED TRAFFIC-->

	<!-- SPEED HUMPS-->
	<div id = "speed_humps" class="application">
		<a name="speed_humps"></a> 
        <div id="speed_humps_explanation" class="explanation">
            <h1>Speed humps increase crashes</h1>
            <p>A map of all speed humps constructed in the city in 2014. They are colored by circles indicates the percent decrease in number of crashes 3 months before and after their installation: positive percent decrease (fewer crashes after installation -- green), negative percent decrease (more crashes after installation -- red), or no difference (blue).</p>
        </div>

		<div id = 'humps' style="width: 100%; height: 500px; background-color: lightgray;"></div>
	</div>

	<script>
		//make map of humps
		var hump_map = L.map("humps").setView([40.772125, -73.974792], 13);
		L.tileLayer('http://{s}.tiles.mapbox.com/v3/seanluciotolentino.jhknj4m5/{z}/{x}/{y}.png', {
			attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
			maxZoom: 15
		}).addTo(hump_map);
		
		//define points
		$.get("http://127.0.0.1:5000/humps",{}).then(function(data){
			//add markers
		    (data.markers).forEach(function(marker){
	        var icon = L.MakiMarkers.icon({
	            color: marker.color, 
	            size: "m"}
	        );
	        L.marker([marker.lat, marker.lon], {
	            icon: icon
	        }).addTo(hump_map)
	            .bindPopup(marker.text);
		    });
		});
    </script>
    <!-- END SPEED HUMPS-->

    <!-- CLUSTER STUFF -->
	<div id = "cluster" class="application">
		<a name="cluster"></a> 
        <div id="cluster_explanation" class="explanation">
            <h1>cluster</h1>
            <p>Clustering based on different attributes can reveal geographic clusters that struggle with similar problems.</p>
        </div>

        <div id="cluster_map_output">
			<div id="cluster_map" style="width:70%; height:700px;"></div>
        </div>

        <div style="clear: both; display: block;"></div>

	</div>

	<script>
		//God forgive me for all the copy pasting (and horriable naming conventions) -- I'm on a deadline 
		var cluster_map = L.map("cluster_map").setView([40.753597, -73.986808], 13);
		L.tileLayer('http://{s}.tiles.mapbox.com/v3/seanluciotolentino.jhknj4m5/{z}/{x}/{y}.png', {
			attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
			maxZoom: 15
		}).addTo(cluster_map);
		
		//define points
        //var danger = d3.select("#ea_danger")[0][0].selectedOptions[0].getAttribute("value")
        //var n = d3.select("#ea_top")[0][0].selectedOptions[0].getAttribute("value")
		$.get("http://127.0.0.1:5000/clusters/5",{}).then(function(data){
	            //add circles
	            for(var i =0; i<data.circles.length; i++){
	                c = data.circles[i]
        	    	L.circle([c.lat, c.lon], 50, {
           	    	    color: c.color,
        	    	    fillColor: c.color,
        	    	    fillOpacity: 0.5
        	    	}).addTo(cluster_map);
        	    };
        	});
	</script>

</body>
</html>
