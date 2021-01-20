// USGS endpoint for 'All Earthqukes from the Past 7 Days'
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

// Pull data from USGS endpoint and call .features 
d3.json(queryUrl, function(data) {
    // Call createFeatures with data.features
    createFeatures(data.features);
    // console.log(data.features);
}); 

// Create function pullData
function createFeatures(earthquakeDataFeatures){

    // function highlightFeature(e) {

    //     var layer = e.target;

    //     layer.setStyle({
    //         weight: 5,
    //         color: '#666',
    //         dashArray: '',
    //         fillOpacity: 0.7

    //     });

    //     if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
    //         layer.bringToFront();
    //     }
    // }

    // function resetHighlight(e) {
    //     geojson.resetStyle(e.target);
    // }

    // function zoomToFeature(e) {
    //     map.fitBounds(e.target.getBounds());
    // }

    function onEachFeature(feature, circle) {

        if (feature.properties.place && feature.properties.time && feature.properties.mag && feature.geometry.coordinates[1] && feature.geometry.coordinates[0] && feature.geometry.coordinates[2] !== null) {            

        // layer.on({
        //     mouseover: highlightFeature,
        //     mouseout: resetHighlight,
        //     click: zoomToFeature
        // });
        
        // if statement to filter out any null values
        // Set up pop up with place, mag and time data
        circle.bindPopup("<h3>" + feature.properties.place + "<h3><p>" +
        feature.properties.mag + " magnitudes</p><p>" + feature.geometry.coordinates[2] +
        " depth</p><p>" + new Date(feature.properties.time) + "</p>");   
        // console.log(+feature.geometry.coordinates[2]);
        }

        

    }    // Create function for radius to return mag * 2000 for better visualization
    function radiusMag(mag) { 
        return mag * 25000;
    }

    // Create function for color scale base on mag value
    function circleColor(depth) {
        if (depth  < -10) {
            return "#fffb2"
        }
        else if (depth < 10) {
            return "#fed976"
        }
        else if (depth < 30) {
            return "#feb24c"
        }
        else if (depth < 50) {
            return "#fd8d3c"
        }
        else if (depth < 70) {
            return "#f03b20"
        }
        else if (depth < 90) {
            return "#bd0026"
        }
    }
    // Create a GeoJSON layer containing the features array on the earthquakeData object
    // Run the onEachFeature function once for each piece of data in the array
    var earthquakes = L.geoJSON(earthquakeDataFeatures, {
        
        pointToLayer: function(earthquakeDataFeatures, latlng) {
            return L.circle(latlng, {
                radius: radiusMag(earthquakeDataFeatures.properties.mag),
                color: circleColor(earthquakeDataFeatures.geometry.coordinates[2]),
                fillColor: circleColor(earthquakeDataFeatures.geometry.coordinates[2]),
                fillOpacity: 0.7
            
            });
        },
        onEachFeature: onEachFeature
    });
    // console.log(earthquakes);
    // Sending our earthquakes layer to the createMap function
    // var info = L.control();

    // info.onAdd = function(map) {
    //     this._div = L.DomUtil.create('div', 'info'); 
    //     this.update();
    //     return this._div;
    // };

    // info.update = function (feature) {
    //     this._div.innerHTML = '<h4>Latest Earthquakes - Past 7 Days</h4>' + (feature ?
    //         '<b>' + feature.properties.place + '</b><br /><b>' + feature.properties.mag + ' Magnitude</b>' + 
    //         '<p>' + feature.geometry.coordinates.depth + '</p><p>' + new Date(feature.properties.time) + '</p>': 'Hover over circle');
    // };

    // info.addTo(map);

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
    var map = L.map("map", {
        center: [34.1902, -118.1313],
        zoom: 3,
        layers: [streetmap, earthquakes]
    });

    // Create a layer control
    // Pass in our baseMaps and overlayMaps
    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(map);

    // // Create legend
    // function for legend colors
    function getColor(c) {

        return  c > 90 ? "#bd0026":
                c > 70 ? "#f03b20":
                c > 50 ? "#fd8d3c":
                c > 30 ? "#feb24c":
                c > 10 ? "#fed976":
                         "#ffffb2";


    }

    function style(feature) {
        return {
            fillColor: getColor(feature.properties.depth),
            weight: 2,
            opacity: 1,
            color: getColor(feature.properties.depth),
            fillOpacity: 0.7
        };
    }
    L.geoJSON(earthquakeDataFeatures, {style: style}).addTo(map)

    
    var legend = L.control({position: "bottomright"});

    legend.onAdd = function(map) {
        
        var div = L.DomUtil.create("div", "info legend");
        var mags = [-10, 10, 30, 50, 70, 90];
        var labels = [];

        for (var i = 0; i < mags.length; i++) {
            div.innerHTML +=
            '<i style="background:' + getColor(mags[i] + 1) + '"></i>' +
            mags[i] + (mags[i + 1] ? '&ndash;' + mags[i + 1] + '<br>' : '+');
        }
        return div;
    };
    legend.addTo(map);
}
}
