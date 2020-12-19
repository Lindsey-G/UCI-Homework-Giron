// Create Table//
// Create variable for data
var ufo_data = data;

// Create a variable for tbody tag in html
var tbody = d3.select("tbody");
// console.log(ufo_data);

// 
ufo_data.forEach((info) => {
    // console.log(info);
    // Create rows to tbody with .append with tr tag
    var row = tbody.append("tr");

    Object.entries(info).forEach(([key, value]) => {
        // console.log(key, value);
        // Input value into 
        var cell = tbody.append("td");
        cell.text(value);
    });
});

// Select the button
var button = d3.select("#button");
var form = d3.select("#form");

// console.log(button);
// console.log(form);

button.on("click", function() {
    //Prevent the page from refreshing
    d3.event.preventDefault();

    var dateInput = d3.select(".date-input");
    var dateResult = dateInput.property("value");
    console.log(dateResult);
    var cityInput = d3.select();
    var cityResult = cityInput.property("value");

    var stateInput = d3.select("");
    var stateResult = stateInput.property("value");

    var countryInput = d3.select();
    var countryResult = countryInput.property("value");

    var shapeInput = d3.select("");
    var shapeResults = shapeInput.property("value");

    var durationInput = d3.select("");
    var durationResult = durationInput.property("value");

    var commentsInput = d3.select("");
    var commnetsResult = commentsInput.property("value");

    var filteredResults = ufo_data.filter(request => request.datetime === dateResults && request.city === cityResult.tolowercare() && request.state === stateResult);

    tbody.html("");

    filteredResults.forEach((info) => {
        // console.log(info);
        // Create rows to tbody with .append with tr tag
        var row = tbody.append("tr");
    
        Object.entries(info).forEach(([key, value]) => {
            // console.log(key, value);
            // Input value into 
            var cell = tbody.append("td");
            cell.text(value);
        });
    });
    
});
