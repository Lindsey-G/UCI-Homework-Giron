// Create Chart variables
// Set svg dimesions
var svgWidth = 900;
var svgHeight = 600;

// Set margin dimensions for scatter plot
var margin = {
    top: 30,
    right: 30,
    bottom: 60,
    left: 30
};

// Set width and height for scatter plot with above dimensions 
var width = svgWidth - margin.right - margin.left;
var height = svgHeight - margin.top - margin.bottom;

// Create SVG wrapper
var svg = d3.select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

// append a SVG Group to SVG wrapper by .append("g")
var chartGroup = svg.append("g")
    // using transform to translate the left and top margin of the scatter plot
    .attr("transform", `translate ${margin.left}, ${margin.top}`);

// Create variable for chosenXAxis
var chosenXAxis = "obesity";

// Create function to calculate xLinearScale from chosenXAxis
function xScale(newsData, chosenXAxis) {
    var xLinearScale = d3.scaleLinear()
        .domian([d3.min(newsData, d => d[chosenXAxis]) * 0.8,
        d3.max(newsData, d => d[chosenXAxis]) * 1.2 
        ])
        .range([0, width]);
    return xLinearScale;
}
// Create function to update new selected xAxis when clicked on x label 
function renderAxes(newXScale, xAxis) {
    var bottomAxis = d3.axisBottom(newXScale);

    xAxis.transition()
        .duration(1000)
        .call(bottomAxis);

    return xAxis;
}

function renderCircles(circlesGroup, newXScale, chosenXAxis) {
    circlesGroup.transition()
        .duration(1000)
        .call();
    
    return circlesGroup;
}
// Read in csv
d3.csv("/assets/data/data.csv").then(function(newsData) {
    console.log(newsData);
}); 

