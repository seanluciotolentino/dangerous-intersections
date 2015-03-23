
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
  <script src="./Leaflet.MakiMarkers.js"></script>
  <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
  <script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
    <link rel="stylesheet" type="text/css" href="style.css" media="screen" />
 </head>

<body class="body">

	<!-- TOOL BAR-->
	<div id = "header">
		<a href="map.html">Top</a>
		<a href="#exploratory_analysis">Exploratory Analysis</a>
	    <a href="#speed_humps">Speed Humps</a>
		<a href="#pedestrian_traffic">Pedestrian Traffic</a>
	    <!--<a href="#cluster">K-means Clustering</a>-->
	</div>
    
    <!-- INTRODUCTION -->
    <div id = "introduction">
    	<h1> 
    		<img src="images/car.png" alt="car" style="height:25px"></img>
    		WalkSafer
    		<img src="images/car.png" alt="car" style="height:25px"></img>
    	</h1>
	    <h3> Every year in New York City about 4,000 people are seriously injured in traffic crashes and around  200 are killed. This is a disturbing statistic for anyone that walks in New York City (i.e. everyone in New York City). This project uses the NYPD's crash data, which includes around 600,000 crashes in the city since 01/01/2013, to identify the dangerous intersections and determine the salient features that make them dangerous. Check out the code on <a href="https://github.com/seanluciotolentino/dangerous-intersections">GitHub<a>.</h3>
	</div>

	<!-- EXPLORATORY ANALYSIS-->
	<a name="exploratory_analysis"></a> 
	<div id = "exploratory_analysis" class="application">		
		
		<h1>Identifying the most dangerous intersections</h1>

        <div id="exploratory_analysis_application">
        	Number to display: <span id = 'ea_dd1'></span><br>
        	Measure of danger: <span id = 'ea_dd2'></span><br>
        	Specific location: <span id = 'ea_dd3'></span><span id='ea_dd31'></span><br>
        	Specific time: <span id = 'ea_dd4'></span><span id='ea_dd41'></span><span id='ea_dd42'></span>
		</div>

        <button onclick="draw_ea_map()" type="button">(update)</button>  	
        <img src="images/ea_marker.png" alt="marker_legend" style="height:100px float:right"></img>

        <div id = 'exploratory_analysis_maps' class='map'></div>

        <p>The map above shows the top dangerous intersections in New York City. Use the dropdown buttons to select the number of intersections to map and the metric for danger to rank on. Click on the circle to find out more about the intersection. </p>
            
	</div>
	
	<!-- SPEED HUMPS-->
	<div id = "speed_humps" class="application">
		<a name="speed_humps"></a> 
        
        <h1>Speed humps don't reduce crashes</h1>

		<div id = 'humps' class="map"></div>

		<p>I used a <b>k-d tree</b> to join speed humps constructed in 2014 and crashes. I analyzed the number of crashes that occured 3 and 6 months before and after the installation of the speed hump and found that <b>there is no statistical difference in the number of crashes</b>.</p>

		<p>The map above shows all speed humps constructed in the city in 2014. Their color indicates the percent decrease in number of crashes 3 months before and after their installation: positive percent decrease (fewer crashes after installation -- green), negative percent decrease (more crashes after installation -- red), or no difference (blue).</p>

	</div>

	<!-- PED TRAFFIC-->
	<div id = "pedestrian_traffic" class="application">
		<a name="pedestrian_traffic"></a> 
            
        <h1>Lots of foot traffic = lots of crashes</h1>

        <div id="map_controls" style="width:30%; float:left">
        	<p>Select a measure of danger</p>
            <div id = 'pd_dd1'></div>
            <p>Select a measure of foot traffic</p>
            <div id = 'pd_dd2'></div>
            <p>Redraw the map:</p>
            <button onclick="draw_pt_map()" type="button">Redraw Map</button>
            <img src="images/colorscale.png" alt="Color Scale" style="width:250px; height:250px"></img>
        </div>

		<div id="ped_map"  class='map' style="width:70%; height:700px;"></div>

        <div style="clear: both; display: block;"></div>

        <p>Here I map the crash data by coloring each intersection based on a metric of danger (number of crashes, number of pedestrian injuries, etc.) and the amount of foot traffic. As a proxy for foot traffic I queried the <b>Yelp and FourSquare APIs</b> to get the number of businesses and the number of check-ins for each intersections with different query terms. Use the dropdowns to explore different danger metrics and foot traffic proxies.</p>

        <p>The result shows that there's a significant correlation between foot traffic and crashes (notice the black patch near Times Square!), but many high crash intersections are near the entrances to Manhattan (i.e. the Queensboro Bridge and Lincoln Tunnel). This suggests that it's not a perponderance of pedestrians, but an excess of anxious drivers leading to crashes.</p>

	</div>

	<!-- CLUSTER STUFF
	<div id = "cluster" class="application">
		<a name="cluster"></a> 

		<h1>K-means reveals clusters of dangerous intersections</h1>

		<div id="cluster_map"  class="map"></div>

		<img src="images/wordcloud.png" alt="wordcloud" style="display: block; margin-left: auto; margin-right: auto; opacity: 0.7"></img>
            
        <p>Using <i>k-means clustering</i> can reveal clusters of intersections that struggle with similar problems. We ran the algorithm with k=8, and visualized the clusters that intersections were assigned to in the map above. The word cloud below it shows the characteristics most associated with that cluster. The analysis suggests that texting is a large problem in Manhattan and Brooklyn, and on main streets in Queens. </p>
     -->  
        
        
	</div>
 	
	<script>
		$.ajaxSetup({timeout:20000});
	   var ipaddr = "104.236.122.56";
	   //var ipaddr = "127.0.0.1";
	
		//define dropdowns here
	    var dropdowns = [	                    
	    				{"name": "ea_number",
	                     "select":"span#ea_dd1",
	                     "values": ["10",
	                                "25",
	                                "50",
	                                "100",
	                                ]},
	    				{"name":"ea_danger", 
	    				  "select":"span#ea_dd2",
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
	                    {"name": "ea_location",
	                     "select":"span#ea_dd3",
	                     "values": ["CITYWIDE",
	                     			"DISTRICT",
	                     			"PRECINCT",
	                     			"ZIP CODE",
	                     			"BOROUGH"
	                                ]},
	                    {"name": "ea_time",
	                     "select":"span#ea_dd4",
	                     "values": ["ALL TIME",
	                     			"SPECIFIC TIME"
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
	    //BUILD DROPDOWNS 
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
				d3.select("select#"+dropdown.name)
					.append("option")
					.attr("value", this.value)
					.html(value.replace("_", " ").replace("_", " "));
			}
		};

		//set up for location of exploratory analysis
		var location_options = {"CITYWIDE":[],
                     			"DISTRICT":[101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 164, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 226, 227, 228, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 355, 356, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 481, 482, 484, 501, 502, 503, 595],
                     			"PRECINCT":[1, 5, 6, 7, 9, 10, 13, 14, 17, 18, 19, 20, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 81, 83, 84, 88, 90, 94, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 120, 121, 122, 123],
                     			"ZIP CODE":[10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10009, 10010, 10011, 10012, 10013, 10014, 10016, 10017, 10018, 10019, 10020, 10021, 10022, 10023, 10024, 10025, 10026, 10027, 10028, 10029, 10030, 10031, 10032, 10033, 10034, 10035, 10036, 10037, 10038, 10039, 10040, 10065, 10069, 10075, 10111, 10119, 10128, 10280, 10281, 10282, 10301, 10302, 10303, 10304, 10305, 10306, 10307, 10308, 10309, 10310, 10312, 10314, 10451, 10452, 10453, 10454, 10455, 10456, 10457, 10458, 10459, 10460, 10461, 10462, 10463, 10464, 10465, 10466, 10467, 10468, 10469, 10470, 10471, 10472, 10473, 10474, 10475, 10803, 11001, 11004, 11005, 11040, 11101, 11102, 11103, 11104, 11105, 11106, 11109, 11201, 11203, 11204, 11205, 11206, 11207, 11208, 11209, 11210, 11211, 11212, 11213, 11214, 11215, 11216, 11217, 11218, 11219, 11220, 11221, 11222, 11223, 11224, 11225, 11226, 11228, 11229, 11230, 11231, 11232, 11233, 11234, 11235, 11236, 11237, 11238, 11239, 11249, 11354, 11355, 11356, 11357, 11358, 11359, 11360, 11361, 11362, 11363, 11364, 11365, 11366, 11367, 11368, 11369, 11370, 11372, 11373, 11374, 11375, 11377, 11378, 11379, 11385, 11411, 11412, 11413, 11414, 11415, 11416, 11417, 11418, 11419, 11420, 11421, 11422, 11423, 11426, 11427, 11428, 11429, 11430, 11432, 11433, 11434, 11435, 11436, 11691, 11692, 11693, 11694, 11695, 11697],
                     			"BOROUGH":['MANHATTAN', 'BROOKLYN', 'BRONX', 'QUEENS', 'STATEN ISLAND']
	                     		}
		d3.select('#ea_location').attr("onchange", "make_location_dropdown_for(this.value)");
		function make_location_dropdown_for(option){
			//clearn the dropdown
			d3.select('#ea_dd31').html('')
			if (option == "CITYWIDE"){return;}

			//add the dropdown
			d3.select('#ea_dd31')
				.append("select")
				.attr("class", "dropdown")
				.attr("id", "location_specifier")
				.attr("name", "location_specifier");

			//add dropdown options
			locations = location_options[option]
			for(var i=0; i<locations.length; i++){
				loc = locations[i];
				d3.select("select#location_specifier")
					.append("option")
					.attr("value", loc)
					.html(loc);
				};
		}  //function end

		//set up specific time for exploratory analysis
		d3.select('#ea_time').attr("onchange", "make_time_dropdown_for(this.value)");
		function make_time_dropdown_for(option){
			//clearn the dropdown
			if (option == "ALL TIME"){
				d3.select('#ea_dd41').html('')
				d3.select('#ea_dd42').html('')
			} else {
				//add the  start dropdown
				d3.select('#ea_dd41')
					.html('Starting')
					.append("select")
					.attr("class", "dropdown")
					.attr("id", "time_start_specifier")
					.attr("name", "time_start_specifier");

				//add the  end dropdown
				d3.select('#ea_dd42')
					.html('Ending')
					.append("select")
					.attr("class", "dropdown")
					.attr("id", "time_end_specifier")
					.attr("name", "time_end_specifier");

				//add dropdown options
				times = ['Jan 2013', 'Feb 2013', 'Mar 2013', 'Apr 2013', 'May 2013', 'Jun 2013', 'Jul 2013', 'Aug 2013', 'Sep 2013', 'Oct 2013', 'Nov 2013', 'Dec 2013', 'Jan 2014', 'Feb 2014', 'Mar 2014', 'Apr 2014', 'May 2014', 'Jun 2014', 'Jul 2014', 'Aug 2014', 'Sep 2014', 'Oct 2014', 'Nov 2014', 'Dec 2014', 'Jan 2015', 'Feb 2015', 'Mar 2015', 'Apr 2015', 'May 2015', 'Jun 2015', 'Jul 2015', 'Aug 2015', 'Sep 2015', 'Oct 2015', 'Nov 2015', 'Dec 2015'];
				for(var i=0; i<times.length; i++){
					time = times[i];
					//add the time to the start dropdown
					d3.select("select#time_start_specifier")
						.append("option")
						.attr("value", time)
						.html(time);
					//add the time to the end dropdown
					d3.select("select#time_end_specifier")
						.append("option")
						.attr("value", time)
						.html(time);
				}; //end for
				//RESET END TIME TO BE LAST VALUE?
			} // end if-else
		} //end function

		//DRAW CLUSTER MAP
		function draw_cluster_map(){
			//God forgive me for all the copy pasting (and horriable naming conventions) -- I'm on a deadline 
			L.tileLayer('http://{s}.tiles.mapbox.com/v3/seanluciotolentino.jhknj4m5/{z}/{x}/{y}.png', {
				attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
				maxZoom: 15
			}).addTo(cluster_map);
			
			//define points
			$.get("http://"+ipaddr+":5000/clusters",{}).then(function(data){
		            //add circles
		            for(var i =0; i<data.circles.length; i++){
		                c = data.circles[i]
	        	    	L.circle([c.lat, c.lon], 20, {
	           	    	    color: c.color,
	        	    	    fillColor: c.color,
	        	    	    fillOpacity: 0.2
	        	    	}).addTo(cluster_map);
	        	    };
	        	});
		}

	    //REDRAW EXPLORATORY ANALYSIS MAP
	    function draw_ea_map(){
    		//God forgive me for all the copy pasting (and horriable naming conventions) -- I'm on a deadline 
			ea_map.remove()
	        ea_map = L.map("exploratory_analysis_maps").setView([40.686106, -73.946747], 11);
			L.tileLayer('http://{s}.tiles.mapbox.com/v3/seanluciotolentino.jhknj4m5/{z}/{x}/{y}.png', {
				attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
				maxZoom: 18
			}).addTo(ea_map);
			
			//grab variables for mapping
	        var danger = d3.select("#ea_danger")[0][0].selectedOptions[0].getAttribute("value");
	        var n = d3.select("#ea_number")[0][0].selectedOptions[0].getAttribute("value");
	        var loc_type = d3.select("#ea_location")[0][0].selectedOptions[0].getAttribute("value");
			var loc_spec = 0;
	        if (loc_type != "CITYWIDE"){
	        	 loc_spec = d3.select("select#location_specifier")[0][0].selectedOptions[0].getAttribute("value");
	        }
	        var start = 0;
	        var end = 0;
	       	var time_spec = d3.select("#ea_time")[0][0].selectedOptions[0].getAttribute("value");
	       	if (time_spec == "SPECIFIC TIME"){
	        	 start = d3.select("select#time_start_specifier")[0][0].selectedOptions[0].getAttribute("value")
	        	 end = d3.select("select#time_end_specifier")[0][0].selectedOptions[0].getAttribute("value")
	        }

	        //make api call and map data points
			$.get("http://"+ipaddr+":5000/explore/"+danger+"&"+n+"&"+loc_type+"&"+loc_spec+"&"+start+"&"+end,{}).then(function(data){
				//add markers
				if (data.markers.length < n){
			   		alert('There were only'+data.markers.length+' intersections matching that search criteria. (As opposed to the requested '+n+').');
			   	}
			   	for(var i =0 ; i < data.markers.length; i++){
			    	marker = data.markers[i];
			    	L.marker([marker.lat, marker.lon], {
			            icon: L.divIcon({
			            html: marker.main_text,
			            className: 'count-icon',
			            iconSize: [30, 30]
			        	})
			        }).addTo(ea_map)
			        	.bindPopup(marker.popup_text);
			    };
			});
		}

	    //REDRAW PEDESTERIAN TRAFFIC MAP
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
	        var call = "http://"+ipaddr+":5000/intersections/"+danger+"&"+traffic
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

	    //SPEED HUMP MAP
		function draw_speed_hump_map(){
			L.tileLayer('http://{s}.tiles.mapbox.com/v3/seanluciotolentino.jhknj4m5/{z}/{x}/{y}.png', {
				attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
				maxZoom: 15
			}).addTo(hump_map);
			
			//define points
			$.get("http://"+ipaddr+":5000/humps/",{}).then(function(data){
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
		}

		//CREATE MAPS AND CALL RESPECTIVE DRAW FUNCTIONS
		var ea_map = L.map("exploratory_analysis_maps").setView([40.686106, -73.946747], 11);
		draw_ea_map()
		
		var hump_map = L.map("humps").setView([40.772125, -73.974792], 13);
		draw_speed_hump_map()
		
		var ped_map = L.map("ped_map").setView([40.753597, -73.986808], 13);
		draw_pt_map()

		//ar cluster_map = L.map("cluster_map").setView([40.75359, -73.9868],13);
		//draw_cluster_map()

    </script>

</body>
</html>
