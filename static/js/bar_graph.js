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
 
  // // -----BAR GRAPH PLOT--------------------
  //  REF -- > https://plotly.com/javascript/bar-charts/ < -- REF
      // console.log(`LINE35: Start plot bar graph`);

      state1 = String(data[0].slice(0,1));
      state2 = String(data[10].slice(0,1));
      year = String(data[0].slice(1,2));

      // console.log(`This is state1: ${state1}`);
      // console.log(state2);
      
      months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
      state1_temp = (data[0].slice(2,14));
      state2_temp = (data[10].slice(2,14));

      // console.log(`This is State1_temp ${state1_temp}`);

      // Create our first trace
      let trace1 = {
        x: months,
        y: state1_temp,
        name: state1,
        type: "bar"
        };

        // Create our second trace
      let trace2 = {
        x: months,
        y: state2_temp,
        name: state2,
        type: "bar"
      };

      var layout = {
        height: 600,
        width: 800,
        barmode: 'group',
        title: `${state1} vs ${state2} | ${year}`
      };
            
      // The data array consists of both traces
      let bar_data = [trace1, trace2];

      Plotly.newPlot("bar", bar_data, layout);
    });

    dropdown_populate()
}

// ////////////////////////////////////////////////////////
// // ---------------------Drop Down LISTENER ------------------
d3.select("#selDataset0").on("change", dropdown_populate);

// This function is called when a dropdown menu item is selected
function dropdown_populate() {
  // Use D3 to select the dropdown menu
    var dropdownMenu0 = d3.select("#selDataset0");
    var dropdownMenu1 = d3.select("#selDataset1");
    var dropdownMenu2 = d3.select("#selDataset2");

// Assign the value of the dropdown menu option to a variable
// Fetch the JSON data and console log it
    d3.json(url).then((data) => {
      
      for (var i = 0; i < data.length; i += 10) {  
        // console.log(data[i].State_1)
        dropdownMenu0.append("option").text(data[i].slice(0,1)).property("value")
        dropdownMenu1.append("option").text(data[i].slice(0,1)).property("value")
      }

      for (var i = 0; i < 10; i++) {  
        // console.log(data[i].Year)
        dropdownMenu2.append("option").text(data[i].slice(1,2)).property("value")
      }

      // console.log(`Statename: ${list_statename}`);
      // console.log(`Years: ${list_years}`);
      // console.log(`LINE109: END dropdown_populate()`);  

    // create variable that calls data AFTER fetch data
    var dataset0 = dropdownMenu0.property("value");
    var dataset1 = dropdownMenu1.property("value");
    var dataset2 = dropdownMenu2.property("value");
  
    updatechart(dataset0, dataset1, dataset2);
  
    // console.log(`This is dataset: ${dataset0}`);
    // console.log(`This is dataset: ${dataset1}`);
    // console.log(`This is dataset: ${dataset2}`);
  });
}


// ////////////////////////////////////////////////////////
// // ------------------update graphs using LISTENER-------
function updatechart(subjectid0, subjectid1, subjectid2){
  d3.json(url).then((data) => {    
          
    for (var i = 0; i < data.length; i++) {
      if (data[i].slice(0,1) == subjectid0 && data[i].slice(1,2) == subjectid2){
        target_index1 = i;
      }
    }

    for (var j = 0; j < data.length; j++) {
      if (data[j].slice(0,1) == subjectid1 && data[j].slice(1,2) == subjectid2){
        target_index2 = j;
      }
    }

      console.log(`subjectID1: ${subjectid0}`);
      console.log(`subjectID2: ${subjectid1}`);
      console.log(`subjectID3: ${subjectid2}`);
      console.log(`targetIndex1: ${target_index1}`);
      console.log(`targetIndex2: ${target_index2}`);
      
      state1 = String(data[target_index1].slice(0,1));
      state2 = String(data[target_index2].slice(0,1));
      year = String(data[target_index1].slice(1,2));
    
      months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
      state1_temp = (data[target_index1].slice(2,14));
      state2_temp = (data[target_index2].slice(2,14));
      
      console.log(state1_temp);
      
      // Plotly.restyle("bar","x", [sample_values]);
      // Plotly.restyle("bar","labels", [otu_ids]);
      // Plotly.restyle("bar","y", [yticks]);
      // Plotly.restyle("bar","text", [otu_labels]);
  
      // Plotly.restyle("bubble", "x", [otu_ids]);
      // Plotly.restyle("bubble","y",[sample_values])
      // Plotly.newPlot("bubble", data3, layout2);
  });
}

  init_plot_graphs()