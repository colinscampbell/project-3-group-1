// Create an array of each country's numbers

function init() {
    trace = [{
        // x: [1, 2, 3, 4],
        // y: [1, 2, 3, 4],
        x: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        y: [29.07810009563277, 34.68090532355754, 44.04686005737966, 54.467006694293914, 61.85878227605993, 72.25757092763787, 77.75549888428435, 75.50302837105515, 66.18425247051323, 55.592285623206884, 46.09148868345553, 37.68568696206567],
        mode: 'lines+markers',
        // marker: {
        //     size: 12,
        //     opacity: 0.5
        // }
    }];

    Plotly.newPlot("line", trace);
}

// Call updatePlotly() when a change takes place to the
d3.selectAll("#selDataset_line").on("change", updatePlotly);

// This function is called when a dropdown menu item is selected
function updatePlotly() {
    d3.json('http://127.0.0.1:5000/api/averages').then(function(data) {

        var dropdownMenu = d3.select("#selDataset_line");
        // Assign the value of the dropdown menu option to a variable
        var chosenYear = dropdownMenu.property("value");

        var Jan = data[chosenYear]['Jan'];
        var Feb = data[chosenYear]['Feb'];
        var Mar = data[chosenYear]['Mar'];
        var Apr = data[chosenYear]['Apr'];
        var May = data[chosenYear]['May'];
        var Jun = data[chosenYear]['Jun'];
        var Jul = data[chosenYear]['Jul'];
        var Aug = data[chosenYear]['Aug'];
        var Sep = data[chosenYear]['Sep'];
        var Oct = data[chosenYear]['Oct'];
        var Nov = data[chosenYear]['Nov'];
        var Dec = data[chosenYear]['Dec'];
        var labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        var temps = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec];

        console.log(labels);
        console.log(temps);

        // Note the extra brackets around 'x' and 'y'

        trace = [{
            x: labels,
            y: temps,
            mode: 'scatter',
            // marker: {
            //     size: 12,
            //     opacity: 0.5
            // }
        }];

        Plotly.newPlot("line", trace);
    });
};

init();