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

    // Create a variable result for date-input
    var dateResult = d3.select("#date-input").property("value");    
    
    // Create filteredResults variable to .filter() through ufo_data to match input results
    var filteredResults = ufo_data.filter(request => request.datetime === dateResult);

    // Clear table for filteredResults
    tbody.html("");

    // Create table with filteredResults
    filteredResults.forEach((info) => {
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
