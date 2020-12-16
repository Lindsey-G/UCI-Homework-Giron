// Create Table//
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
