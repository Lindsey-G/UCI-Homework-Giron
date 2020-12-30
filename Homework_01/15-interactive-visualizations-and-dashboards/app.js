// run python -m http.server for local host 8000

d3.json("samples.json").then((data) => {

    function init() {
        // Create default variables for otu_ids, sample_values, and otu_labels
        var defaultOTUsIds = data.samples[0].otu_ids;
        var defaultSampleValues = data.samples[0].sample_values;
        var defaultText = data.samples[0].otu_labels;

        // Slice default variables to contain only top 10 
        var slicedDefaultOTUsIds = defaultOTUsIds.slice(0, 10);
        var slicedDefaultSampleValues = defaultSampleValues.slice(0, 10);
        var slicedDefaultText = defaultText.slice(0, 10);

        // Turn Id numbers into string and added "OTU" so that when plotting 
        // bar chart it displays as a string value instead of a range of integer vaules
        var stringIds = [];
        slicedDefaultOTUsIds.forEach(item => {
            stringIds.push("OTU" + " " + item + "");
        });
        
        // .reverse() so that list are in decending order
        stringIds.reverse();
        slicedDefaultSampleValues.reverse();
        slicedDefaultText.reverse();

        // Confirm data is correct on console
        // console.log(stringIds);
        // console.log(slicedDefaultSampleValues);
        // console.log(slicedDefaultText);

        // Create default plot
        var defaultBarChart = [{
            type: 'bar',
            x: slicedDefaultSampleValues,
            y: stringIds,
            text: slicedDefaultText,
            orientation: 'h',
            marker: {
                color: 'rgba (50,171,96,0.6)',
                line: {
                    color: 'rgba (50, 171, 96, 1.0)',
                    width: 1
                }
            },
    
        }];

        var barChartLayout = {
            title: "Top Ten OTU's",
            // yaxis: {title: "IDS"},
            xaxis: {title: "Sample Values"},
            range: [0, 20],
            domain: [0, 0.5],
            zeroline: false,
            showline: false,
            showticklabels: true,
            showgrid: true,
            legend: {
                x: 0.029,
                y: 1.238,
                font: {
                    family: 'Arial',
                    size: 10
                }
            },
            width: 300,
            height: 500,
            paper_bgcolor: 'rgb (248,248,255)',
            plot_bgcolor: 'rgb(248,248,255)',
            font: {
                family: 'Arial'
            }

        };

        Plotly.newPlot("OTUs-top-ten", defaultBarChart, barChartLayout);
        
        // Create Bubble Chart

        var currentName = data.names[0];
        // console.log(currentName);
        var defaultBubbleChart = [{
            x: defaultOTUsIds,
            y: defaultSampleValues,
            text: defaultText,
            mode: 'markers',
            marker: {
                color: defaultOTUsIds,
                size: defaultSampleValues
            }
        }];

        var bubbleLayout = {
            title: `All of ${currentName}'s OTU Samples`,
            xaxis: {title: "OTU ID"},
            yaxis: {title: "Sample Values"},
            height: 600,
            width: 1200,
            paper_bgcolor: 'rgb (248,248,255)',
            plot_bgcolor: 'rgb(248,248,255)',
            font: {
                family: 'Arial'
            }
        };
        
        Plotly.newPlot("bubble", defaultBubbleChart, bubbleLayout);

        // Create Demographic chart
        var defaultMetadata = data.metadata[0];
        // console.log(defaultMetadata);


        // // var metaReady = [];
        // // defaultMetadata.forEach(function([key, value]){
        // //     metaReady.push(`${key}: ${value}`);
        // //     // var panelBody = d3.select("ul").append("li");
        // //     // panelBody.text(Object.entries(metaReady));
        // // });
        // // console.log(metaReady);

        // // console.log(Object.entries(defaultMetadata));
        // var panelBody = d3.select("ul").append("li");
        // // panelBody.text(Object.entries(metaReady));
        // // var panelBody = d3.select("ul").append("li");
        // // panelBody.text(Object.entries(defaultMetadata));

        // defaultMetadata.forEach((item) => {
        //     console.log(item);
        //     Object.entries(item).forEach(([key, value]) => {
        //         panelBody.text(`${key}: ${value}`);
        //     });
        // });

    };
    init()
    // var defaultTrace = {
    //     y: data.samples[0].id,
    //     x: data.samples[0].sample_values,
    //     text: data.samples[0].otu_labels,
    //     type: "bar",
    //     orientation: "h"
    // };
    // Plotly.newPlot("plot", defaultTrace);

    // var dropdownMenu = 940;
    // var getId = data.samples[0];
    // console.log(getId);
    // // Pull otu_ids data
    // var OTUsIds = getId.otu_ids;
    // console.log(OTUsIds.slice(0, 10));
    // //Pull sample_values
    // var OTUsValues = getId.sample_values;
    // console.log(OTUsValues.slice(0, 10));
    // // Pull otu_labels
    // var OTUsLabels = getId.otu_labels;
    // console.log(OTUsLabels.slice(0, 10));

    // var trace1 = {
    //     y: OTUsIds.slice(0, 10),
    //     x: OTUsValues.slice(0, 10),
    //     text: OTUsLabels.slice(0, 10), 
    //     type: "bar",
    //     orientation: "h"
    // };
    // Plotly.newPlot("plot", trace1);
    //get array of ids
    // var dropdownMenu = data.names;
    // console.log(dropdownMenu);
    // var dropdownMenu = 940;
    // create dropdownmenu
    // var sel = document.getElementById("#selDataset");
    // var fragment = document.createDocumentFragment();

    // dropdownMenu.forEach(function (dropdown, index){
    //     var opt = document.createElement('optionChanged');
    //     opt.innerHTML = dropdown;
    //     opt.value = dropdown;
    //     fragment.appendChild(opt);
    // });
    // sel.appendChild(fragment);

    // for (var i = 0; i < data.length; i++)

    //     if (dropdownMenu === data.samples[0].id)
    //         // get id as an object
    //         var getId = data.samples[0];
    //         console.log(getId);
    //         // Pull otu_ids data
    //         var OTUsIds = getId.otu_ids;
    //         console.log(OTUsIds);
    //         //Pull sample_values
    //         var OTUsValues = getId.sample_values;
    //         console.log(OTUsValues);
    //         // Pull otu_labels
    //         var OTUsLabels = getId.otu_labels;
    //         console.log(OTUsLabels);

    //     var trace1 = {
    //         y: OTUsIds.slice(0, 10),
    //         x: OTUsValues.slice(0, 10),
    //         text: OTUsLabels.slice(0, 10), 
    //         type: "bar",
    //         orientation: "h"
    //     };
    //     Plotly.newPlot("plot", trace1);

});