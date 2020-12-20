// Create Table//
// Create variable for data
var ufo_data = data;
// console.log(ufo_data);

// Create a variable for tbody tag in html
var tbody = d3.select("tbody");

// Create table 
ufo_data.forEach((info) => {
    // console.log(info); 
    // Create rows to tbody with .append with <tr>
    var row = tbody.append("tr");

   // with Object create entries to get key an value for each on to then append value
    Object.entries(info).forEach(([key, value]) => {
        // console.log(key, value);
        // .append <td> to table for data
        var cell = tbody.append("td");
        // Enter data as text into cell variable (<td>)
        cell.text(value);
    });
});

// Select the button
var button = d3.select("#button");
var form = d3.select("#form");

// console.log(button);
// console.log(form);

button.on("click", runEnter);
form.on("submit", runEnter);

function runEnter() {
    //Prevent the page from refreshing
    d3.event.preventDefault();

    // Create a variable result for each cell input 
    var dateSearch = d3.select("#date-input").property("value");
    var citySearch = d3.select("#city-input").property("value");
    var stateSearch = d3.select("#state-input").property("value");
    var countrySearch = d3.select("#country-input").property("value");
    var shapeSearch = d3.select("#shape-input").property("value");

    // Create variables for filtered results
    var dateResult = ufo_data.filter(request => request.datetime === dateSearch);
    var cityResult = ufo_data.filter(request => request.city === citySearch);
    var stateResult = ufo_data.filter(request => request.state === stateSearch);
    var countryResult = ufo_data.filter(request => request.country === countrySearch);
    var shapeResult = ufo_data.filter(request => request.shape === shapeSearch);
    var filteredResults = ufo_data.filter(request => request.datetime === dateResult && request.city === cityResult.toLowerCase() && request.state === stateResult.toLowerCase());
    
    if (dateSearch)
        newResults(dateResult);
        
    else if (citySearch)
        newResults(citySearch);
         
    else if (stateSearch)
        newResults(stateResult);
                
    else if (countrySearch)
        newResults(button === countryResult);
                    
    else if (shapeSearch)
        newResults(shapeResult);
    
    else if (dateSearch && citySearch && stateSearch) 
        newResults(filteredResults);            
        
    else

        // Clear table for filteredResults
        tbody.html("");

        // Create table with filteredResults
        function newResults(info) {
            ufo_data.forEach((info) => {
            // console.log(info);
                // Create rows to tbody with .append with tr tag
                var row = tbody.append("tr");
    
                    // with Object create entries to get key an value for each on to then append value
                    Object.entries(info).forEach(([key, value]) => {
                    // console.log(key, value);
                    // .append <td> to table for data
                    var cell = tbody.append("td");
                    // Enter data as text into cell variable (<td>)
                    cell.text(value);
                });
            });
        };    
   
};

