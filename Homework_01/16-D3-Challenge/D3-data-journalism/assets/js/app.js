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
var chosenYAxis = "poverty"
function yScale(newsData, chosenYAxis) {
    var yLinearScale = d3.scaleLinear()
        .domian([0, d3.max(newsData, d => d[chosenYAxis])])
        .range([height, 0]);
    return yLinearScale;
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
        .attr("c", d => newXScale(d[chosenXAxis]));
    
    return circlesGroup;
}

function updateToolTip(chosenXAxis, circlesGroup) {
    var label;
    if (chosenXAxis === "obesity") {
        label = "obesity";
    }
    else {
        label = "poverty";
    }

    var toolTip = d3.tip()
        .attr("class", "toolTip")
        .offset([80, -60])
        .html(function(d) {
            return (`${d.abbr}<br>${label}${d[chosenXAxis]}`);
        });

    circlesGroup.call(toolTip);

    circlesGroup.on("mouseover", function(data) {
        toolTip.show(data);
    })
        .on("mouseout", function(data, index) {
            toolTip.hide(data);
        });
    
    return circlesGroup;
}

// Read in csv
d3.csv("/assets/data/data.csv").then(function(newsData, err) {
    if (err) throw err;

    newsData.forEach(function(data) {
        data.obesity = +data.obesity;
        data.poverty = +data.poverty;
        // console.log(data.obesity);
        // console.log(data.poverty);
    })
    var xLinearScale = xScale(newsData, chosenXAxis);
    var yLinearScale = yScale(newsData, chosenYAxis);

    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    var xAxis = chartGroup.append("g")
        .classed("x-axis", true)
        .attr("transform", `translate(0, ${height})`)
        .call(bottomAxis);

    chartGroup.append("g")
        .call(leftAxis);

    var circlesGroup = chartGroup.selectAll("cirlce")
        .data(newsData)
        .enter()
        .append("cirlce")
        .attr("cx", d => xLinearScale(d[chosenXAxis]))
        .attr("cy", d => yLinearScale(d[chosenYAxis]))
        .attr("r", 20)
        .attr("fill", "purple")
        .attr("opacity", ".5");

    var labelsGroup = chartGroup.append("g")
        .attr("transform", `translate(${width / 2}${height + 20 })`);
    
    var obesityData = labelsGroup.append("text")
        .attr("x", 0)
        .attr("y", 20)
        .attr("value", "obesity")
        .classed("")


}); 



