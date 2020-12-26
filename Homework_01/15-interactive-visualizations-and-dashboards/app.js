// run python -m http.server for local host 8000

d3.json("samples.json").then((data) => {
    var defaultTrace = {
        y: data.samples[0].id,
        x: data.samples[0].sample_values,
        text: data.samples[0].otu_labels,
        type: "bar",
        orientation: "h"
    };
    Plotly.newPlot("plot", defaultTrace);

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
 
