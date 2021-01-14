// Create Chart variables
// Set svg dimesions
var svgWidth = 900;
var svgHeight = 600;

// Set margin dimensions for scatter plot
var margin = {
    top: 30,
    right: 30,
    bottom: 90,
    left: 90
};

// Set width and height for scatter plot with above dimensions 
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create SVG wrapper
var svg = d3
    .select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

// Append a SVG Group to SVG wrapper by .append("g")
var chartGroup = svg.append("g")
    // using transform to translate the left and top margin of the scatter plot
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Create variable for chosenXAxis
var chosenXAxis = "obesity";
var chosenYAxis = "poverty";

// Create function to calculate xLinearScale from chosenXAxis
function xScale(newsData, chosenXAxis) {
    var xLinearScale = d3.scaleLinear()
        .domain([d3.min(newsData, d => d[chosenXAxis]) * 0.8,
            d3.max(newsData, d => d[chosenXAxis]) * 1.2 
        ])
        .range([0, width]);
    
    return xLinearScale;
}
// Create function to calculate yLinearScale from chosenYAxis
function yScale(newsData, chosenYAxis) {
    var yLinearScale = d3.scaleLinear()
        .domain([d3.min(newsData, d => d[chosenYAxis]) * 0.8, 
            d3.max(newsData, d => d[chosenYAxis])* 1.2
        ])
        // for y axis to appear with the zero at the botto height is the first parameter
        .range([height, 0]);
    
    return yLinearScale;
}
// Create function to update new selected xAxis when clicked on x label 
function renderBottomAxes(newXScale, xAxis) {
    var bottomAxis = d3.axisBottom(newXScale);

    xAxis.transition()
        .duration(1000)
        .call(bottomAxis);

    return xAxis;
}
// Create function to update new selected yAxis when clicked on y label
function renderLeftAxes(newYScale, yAxis) {
    var leftAxis = d3.axisLeft(newYScale);

    xAxis.transition()
        .duration(1000)
        .call(leftAxis);

    return yAxis;
}
// function to update circles
function renderCircles(circlesGroup, newXScale, newYScale, chosenXAxis, chosenYAxis) {
    circlesGroup.transition()
        .duration(1000)
        .attr("cx", d => newXScale(d[chosenXAxis]))
        .attr("cy", d => newYScale(d[chosenYAxis]));
        
    return circlesGroup;
}
// function to render textGroup
function renderText(textGroup, newXScale, newYScale, chosenXAxis, chosenYAxis) {
    textGroup.transition()    
        .durattion(1000)
        .attr("x", d => newXScale(d[chosenXAxis]))
        .attr("y", d => newYScale(d[chosenYAxis]));

    return textGroup;   
}

function updateToolTip(chosenXAxis, chosenYAxis, circlesGroup) {

    var xLabel;
    if (chosenXAxis === "age") {
        xLabel = "Age (Median)";
    }
    if (chosenXAxis === "income") {
        xLabel = "Household Income (Median)";
    }
    else {
        xLabel = "In Poverty (%)";
    }

    var yLabel;
    if (chosenYAxis === "smokes") {
        yLabel = "Smokes (%)";
    }
    if (chosenYAxis === "healthcareLow") {
        yLabel = "Lacks Healthcare (%)"
    }
    else {
        yLabel = "Obesity (%)";
    }

    var toolTip = d3.tip()
        .attr("class", "tooltip")
        .offset([80, -60])
        .html(function(d) {
            return (`${d.state}<br>${xLabel}: ${d[chosenXAxis]}<br>${yLabel}: ${d[chosenYAxis]}`);
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

        data.poverty = +data.poverty;
        data.income = +data.income;
        data.age = +data.age;
        data.obesity = +data.obesity;
        data.smokes = +data.smokes;
        data.healthcareLow = +data.healthcareLow;
        data.abbr = data.abbr;
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

    var circlesGroup = chartGroup.selectAll("circle")
        .data(newsData)
        .enter()
        .append("circle")
        .attr("cx", d => xLinearScale(d[chosenXAxis]))
        .attr("cy", d => yLinearScale(d[chosenYAxis]))
        .attr("r", 20)
        .attr("fill", "purple")
        .attr("opacity", ".5");

    // var textGroup = chartGroup.selectAll("text")    
    //     .append("text")
    //     .text(d => d.abbr)
    //     .classed(".stateText", true)
    //     .attr("text=anchor", "middle")
    //     .attr("fill", "gold")
    //     .attr("font-size", "10px")
    //     .attr("x", d => xLinearScale(d[chosenXAxis]))
    //     .attr("y", d => yLinearScale(d[chosenYAxis]));;

    // Create xLabelsGroup
    var xLabelsGroup = chartGroup.append("g")
        .attr("transform", `translate(${width / 2}, ${height + 20 })`);

    // Create labels for all xLabelsGroup
    var povertyLabel = xLabelsGroup.append("text")
        .attr("x", 0)
        .attr("y", 20)
        .attr("value", "poverty")
        .classed("active", true)
        .text("In Poverty (%)");

    var ageLabel = xLabelsGroup.append("text")
        .attr("x", 0)
        .attr("y", 40)
        .attr("value", "age")
        .classed("inactive", true)
        .text("Age (Median)");
    
    var incomeLabel = xLabelsGroup.append("text")
        .attr("x", 0)
        .attr("y", 60)
        .attr("value", "income")
        .classed("inactive", true)
        .text("Household Income(Median)");

    // Create yLabelsGroup
    var yLabelsGroup = chartGroup.append("g")

    // Create labels for all yLabelsGroup        
    var obesityLabel = yLabelsGroup.append("text")
        .attr("transform", `translate(-40, ${height / 2})rotate(-90)`)
        .attr("dy", "1em")
        .attr("class", "axis-text-y")
        .classed("axis-text", true)
        .attr("value", "obesity")
        .classed("active", true)
        .text("Obesity (%)");

    var smokesLabel = yLabelsGroup.append("text")
        .attr("transform", `translate(-60, ${height / 2})rotate(-90)`)
        .attr("dy", "1em")
        .attr("class", "axis-text-y")
        .attr("value", "smokes")
        .classed("inactive", true)
        .text("Smokes (%");

    var healthcareLabel = yLabelsGroup.append("text")
        .attr("transform", `translate(-80, ${height / 2})rotate(-90)`)
        .attr("dy", "1em")
        .attr("class", "axis-text-y")       
        .attr("value", "healthcare")
        .classed("inactive", true)
        .text("Lacks Healthcare (%)");
    
    // Set up circlesGroup that calls on updateToolTop function 
    var circlesGroup = updateToolTip(chosenXAxis, chosenYAxis, circlesGroup);

    xLabelsGroup.selectAll("text")
        .on("click", function (){
        var value = d3.select(this).attr("value");

        if (value !== chosenXAxis) {

            chosenXAxis = value;
        
            xLinearScale = xScale(newsData, chosenXAxis);
              
            xAxis = renderBottomAxes(xLinearScale, xAxis);

            circlesGroup = renderCircles(circlesGroup, xLinearScale, chosenXAxis);

            // textGroup = renderText(textGroup, newXScale, chosenXAxis);

            circlesGroup = updateToolTip(chosenXAxis, circlesGroup);

            if (chosenXAxis === "age") {

                ageLabel
                .classed("active", true)
                .classed("inactive", false);

                incomeLabel
                .classed("active", false)
                .classed("inactive", true);

                povertyLabel
                .classed("active", false)
                .classed("inactive", true);
            }
            if (chosenXAxis === "income") {

                incomeLabel
                .classed("active", true)
                .classed("inactive", false);

                povertyLabel
                .classed("active", false)
                .classed("inactive", true);

                ageLabel
                .classed("active", false)
                .classed("inactive", true);
            }
            else {
                povertyLabel
                .classed("active", true)
                .classed("inactive", false);

                ageLabel
                .classed("active", false)
                .classed("inactive", true);

                incomeLabel
                .classed("active", false)
                .classed("inactive", true);
            }         
        }
    });

    yLabelsGroup.selectAll("text")
    .on("click", function (){
    var value = d3.select(this).attr("value");      

        if (value !== chosenYAxis) {

            chosenYAxis = value;
        
            yLinearScale = yScale(newsData, chosenYAxis);
              
            yAxis = renderLeftAxes(yLinearScale, yAxis);

            circlesGroup = renderCircles(circlesGroup, yLinearScale, chosenYAxis);

            circlesGroup = updateToolTip(chosenYAxis, circlesGroup);

            if (chosenYAxis === "smokes") {

                smokesLabel
                .classed("active", true)
                .classed("inactive", false);

                healthcareLabel
                .classed("active", false)
                .classed("inactive", true);

                obesityLabel
                .classed("active", false)
                .classed("inactive", true);
            }
            if (chosenYAxis === "healthcareLow") {

                healthcareLabel
                .classed("active", true)
                .classed("inactive", false);

                obesityLabel
                .classed("active", false)
                .classed("inactive", true);

                smokesLabel
                .classed("active", false)
                .classed("inactive", true);
            }
            else {
                obesityLabel
                .classed("active", true)
                .classed("inactive", false);

                smokesLabel
                .classed("active", false)
                .classed("inactive", true);

                healthcareLabel
                .classed("active", false)
                .classed("inactive", true);
            }
        }
    });
}).catch(err => console.log(err)); 



