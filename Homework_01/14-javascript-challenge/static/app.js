var ufo_data = data;

var submit = d3.select("#submit");

submit.on("click", function() {
    
    d3.event.preventDefaul();

    var inputElement = d3.select("date-button");

    var inputValue = inputElement.property("value");

    console.log(inputValue);
    console.log(ufo_data);

    var filteredDate = ufo_data.filter(search => search.datetime === inputValue);
    console.log(filteredDate);

)};
