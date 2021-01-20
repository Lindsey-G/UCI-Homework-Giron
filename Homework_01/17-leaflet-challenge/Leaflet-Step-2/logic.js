// USGS endpoint for 'All Earthqukes from the Past 7 Days'
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

// Pull data from USGS endpoint and call .features 
d3.json(queryUrl, function(data) {
    pullData(data.features);
    // console.log(data.features);
}); 

// Create function pullData
function pullData(earthquakeData){

    function onEachFeature(feature, circle) {

        if (feature.properties.place && feature.properties.time && feature.properties.mag && feature.geometry.coordinates[0] && feature.geometry.coordinates[1] !== null) {
            circle.bindPopup("<h3>" + feature.properties.place + "<h3><p>" +
            feature.properties.mag + "magnitudes</p><p>" + new Date(feature.properties.time) + "</p>");
        // console.log(feature.properties.place);
        // console.log(feature.properties.mag);
        // console.log(feature.properties.time);
            var circle = L.circle([feature.geometry.coordinates[0], feature.geometry.coordinates[1]], {
                color: 'purple',
                fillColor: 'light purple',
                fillOpacity: 0.5,
                radius:`${feature.properties.mag}`
            });
        }

    
    }

    // Create a GeoJSON layer containing the features array on the earthquakeData object
    // Run the onEachFeature function once for each piece of data in the array
    var earthquakes = L.geoJSON(earthquakeData, {
        onEachFeature: onEachFeature
    });
    console.log(earthquakes);
    // Sending our earthquakes layer to the createMap function
    createMap(earthquakes);
    // console.log(earthquakes);
}
// Select which data to pull from endpoint


// Create variables from pulled data

// Start mapping process
function createMap(earthquakes) {
    // Define streetmap and darkmap layers
    var satellitemap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
        maxZoom: 18,
        zoomOffset: -1,
        id: "mapbox/satellite-v9",
        accessToken: API_KEY
    });

    var satellitemap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
        maxZoom: 18,
        zoomOffset: -1,
        id: "mapbox/satellite-v9",
        accessToken: API_KEY
    });

    // Define a baseMaps object to hold our base layers
    var baseMaps = {
        "Street Map": streetmap,
        "Satellite Map": satellitemap
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
}
