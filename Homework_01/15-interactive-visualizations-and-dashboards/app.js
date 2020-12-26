// run python -m http.server for local host 8000

d3.json("samples.json").then((data) => {
    
    var dropdownMenu = data.names;
    console.log(dropdownMenu);
    // var testId = data.samples[0].id;
    // console.log(testId);
    // // Pull otu_ids data
    // var testOTUsIds = data.samples.map(item => item.otu_ids);
    // console.log(testOTUsIds);
    // //Pull sample_values
    // var OTUsValues = data.samples.map(item => item.sample_values);
    // console.log(OTUsValues);
    // // Pull otu_labels
    // var OTUsLabels = data.samples.map(item => item.otu_labels);
    // console.log(OTUsLabels);

    for (var i = 0; i < data.length; i++)

        if (dropdownMenu === data.samples[0].id)

            // var getId = data.samples[0].id;
            // console.log(getId);
            // Pull otu_ids data
            var OTUsIds = data.samples.map(item => item.otu_ids);
            console.log(OTUsIds);
            //Pull sample_values
            var OTUsValues = data.samples.map(item => item.sample_values);
            console.log(OTUsValues);
            // Pull otu_labels
            var OTUsLabels = data.samples.map(item => item.otu_labels);
            console.log(OTUsLabels);
            // var eachIdsOTUs = dropdownMenu.samples[2];
            // console.log(eachIdsOTUs);
            // slice data for top 10 
            var topTenOTUs = OTUsIds.slice(0, 10);
            // reverse data to get decending order
            var reversedTopTenOTUs = topTenOTUs.reverse();
            console.log(reversedTopTenOTUs);


        // var trace1 = {
        //     y: reversedTopTenOTUs.map(item => item.otu_ids),
        //     x: reversedTopTenOTUs.map(item => item.sample_values),
        //     text: reversedTopTenOTUs.map(item => item.otu_labels)
        // };
        // Plotly.newPlot("OTUs-top-ten", trace1)

});
 
