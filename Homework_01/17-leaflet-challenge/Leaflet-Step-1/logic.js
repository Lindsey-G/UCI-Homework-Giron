// USGS endpoint for 'All Earthqukes from the Past 7 Days'
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

// Pull data from USGS endpoint and call .features 
d3.json(queryUrl, function(data) {
    createFeatures(data.features);
    // console.log(data.features);
}); 

// Create function pullData
function createFeatures(earthquakeDataFeatures){

    function onEachFeature(feature, circle) {
        // if statement to filter out any null values
        if (feature.properties.place && feature.properties.time && feature.properties.mag && feature.geometry.coordinates[1] && feature.geometry.coordinates[0] && feature.geometry.coordinates[2] !== null) {            
            // Set up pop up with place, mag and time data
            circle.bindPopup("<h3>" + feature.properties.place + "<h3><p>" +
            feature.properties.mag + " magnitudes</p><p>" + feature.geometry.coordinates[2] +
            " depth</p><p>" + new Date(feature.properties.time) + "</p>");   
            // console.log(+feature.geometry.coordinates[2]);
        }
    }
    // Create function for radius to return mag * 2000
    function radiusMag(mag) { 
        return mag;
    }

    // Create function for color scale base on mag value
    function circleColor(depth) {
        if (depth  < -10) {
            return "#fffc00"
        }
        else if (depth < 10) {
            return "#cff000"
        }
        else if (depth < 30) {
            return "#b5d300"
        }
        else if (depth < 50) {
            return "#bc7900"
        }
        else if (depth < 70) {
            return "#c55400"
        }
        else if (depth < 90) {
            return "#cf0000"
        }
    }
    // Create a GeoJSON layer containing the features array on the earthquakeData object
    // Run the onEachFeature function once for each piece of data in the array
    var earthquakes = L.geoJSON(earthquakeDataFeatures, {
        
        pointToLayer: function(earthquakeDataFeatures, latlng) {
            return L.circle(latlng, {
                radius: radiusMag(earthquakeDataFeatures.properties.mag),
                color: circleColor(earthquakeDataFeatures.geometry.coordinates[2]),
                fillOpacity: 0.9
            
            });
        },
        onEachFeature: onEachFeature
    });
    // console.log(earthquakes);
    // Sending our earthquakes layer to the createMap function
    createMap(earthquakes);
    // console.log(earthquakes);
// Select which data to pull from endpoint


// Create variables from pulled data

// Start mapping process
function createMap(earthquakes) {
    
    // Define streetmap layer
    var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
        tileSize: 512,
        maxZoom: 18,
        zoomOffset: -1,
        id: "mapbox/streets-v11",
        accessToken: API_KEY
    });

    // Define a baseMaps object to hold our base layers
    var baseMaps = {
        "Street Map": streetmap
    };

    // Create overlay object to hold our overlay layer
    var overlayMaps = {
        Earthquakes: earthquakes
    };

    // Create our map, giving it the streetmap and earthquakes layers to display on load
    var myMap = L.map("map", {
        center: [34.1902, -118.1313],
        zoom: 4,
        layers: [streetmap, earthquakes]
    });

    // Create a layer control
    // Pass in our baseMaps and overlayMaps
    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(myMap);

    // // Create legend
    // function for legend colors
    function legendColors(c) {

        return  c > 90 ? "#cf0000":
                c > 70 ? "#c55400":
                c > 50 ? "#bc79000":
                c > 30 ? "#b5d300":
                c > 10 ? "#cff000":
                         "#fffc00";


    }

    var legend = L.control({position: "bottomright"});

    legend.onAdd = function(legendMag) {
        
        var div = L.DomUtil.create("div", "info legend");
        var labels = ["-10-10", "10-30", "30-50", "50-70", "70-90", "90+"];

        for (var i = 0; i < labels.length; i++) {
            div.innerHTML +=
            '<i style="background:' + legendColors(labels[i] + 1) + '"></i>' +
            labels[i] + (labels[i + 1] ? '&ndash;' + labels[i + 1] + '<br>' : '+');
        }
        return div;
    };
    legend.addTo(myMap);
}
}
