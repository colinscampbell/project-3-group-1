// // IF geting data from local file ***MUST USE LIVE SERVER***
const url = "api/weather";

// // /////  TESTING DATA   /////////////////////////////////////////

// d3.json(url).then((data) => {
//   console.log(`TEST this is from js`);
//   console.log(`TEST This is state ID: ${data[0].State}`)
//   console.log(`TEST This is state NAME: ${data[0].State_1}`)
//   console.log(`TEST This is YEAR: ${data[0].Year}`)
//   console.log(`TEST This is Jan Temp: ${data[0].Jan}`)
// })

// // ////////////////////////////////////////////////////////
// // ----------------INIT and GRAPHS ------------------------
// FOR REFERENCE --- > url = API endpoint

function init_plot_graphs(){
  d3.json(url).then(function(data) {
    var data_keys = Object.keys(data);
    console.log(`this is data keys: ${data_keys}`);

    var datastate_keys = Object.keys(data.State);
    console.log(`this is data State keys: ${datastate_keys}`);
    
    console.log(`this is from js`);
    console.log(`This is state ID: ${data[0].State}`);
    console.log(`This is state NAME: ${data[0].State_1}`);
    console.log(`This is YEAR: ${data[0].Year}`);
    console.log(`This is Jan Temp: ${data[0].Jan}`);
    // console.log(`This is Data Keys: ${data[0].keys()}`);
    
    // sample_values =  data.samples[0].sample_values.slice(0,10).reverse();
    // console.log(`OTU Value ${sample_values}`);
    // otu_ids =  data.samples[0].otu_ids.slice(0,10);
    // console.log (`OTU ID ${otu_ids}`); 
    // otu_labels = data.samples[0].otu_labels.slice(0,10);
    // console.log(`OTU label ${otu_labels}`);
    // yticks = otu_ids.slice(0, 10).map(otuId => `OTU ${otuId}`).reverse();
  // // -----BAR GRAPH PLOT--------------------
  //  REF -- > https://plotly.com/javascript/bar-charts/ < -- REF
      console.log(`Start plot bar graph`);

      state1 = data[0].State_1;
      state2 = data[19].State_1;
      // console.log(state2);
      // console.log(state1);

      month_year = ["2010","2011","2012","2013"];
      state1_temp = [45,50,75,100];
      state2_temp = [-5, 10, 20, 5];

      let trace1 = {
        x: month_year,
        y: state1_temp,
        name: state1,
        type: "bar"
        };

        //     //   // Create our second trace
      let trace2 = {
        x: month_year,
        y: state2_temp,
        name: state2,
        type: "bar"
      };

      var layout = {
        height: 600,
        width: 800,
        barmode: 'group'
      };
            
      // The data array consists of both traces
      let bar_data = [trace1, trace2];

      Plotly.newPlot("bar", bar_data, layout);
      console.log(`End plot bar graph`);
    })
}

// ////////////////////////////////////////////////////////
// // ---------------------Drop Down LISTENER ------------------
d3.select("#selDataset").on("change", dropdown_populate);

// This function is called when a dropdown menu item is selected
function dropdown_populate() {
    // Use D3 to select the dropdown menu
    var dropdownMenu = d3.select("#selDataset");
    // Assign the value of the dropdown menu option to a variable

// Fetch the JSON data and console log it
    d3.json(url).then((data) =>{
    data.names.forEach(element => {
        dropdownMenu.append("option").text(element).property("value")
    });
    
    // create variable that calls data AFTER fetch data
    var dataset = dropdownMenu.property("value");
    demo_info(dataset);
    updatechart(dataset);
    console.log(`This is dataset: ${dataset}`);
  });
}

  init_plot_graphs()