d3.json("api/weather_table").then((data) => {

  console.log(data)

  // $(document).ready(function() {
  $('#example').DataTable( {
      data: data,
      columns: [
          { title: "State" },
          { title: "Year" },
          { title: "Jan" },
          { title: "Feb" },
          { title: "Mar" },
          { title: "Apr" },
          { title: "May" },
          { title: "Jun" },
          { title: "Jul" },
          { title: "Aug" },
          { title: "Sep" },
          { title: "Oct" },
          { title: "Nov" },
          { title: "Dec" }                                                      
        ]
  } );

})