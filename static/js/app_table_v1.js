d3.json("api/weather").then((data) => {

    console.log(data)
  
    // $(document).ready(function() {
    $('#example').DataTable( {
        data: data['table'],
        columns: [
            { title: "State" },
            { title: "Year" },
            { title: "Jan_Avg" },
            { title: "Feb_Avg" },
            { title: "Mar_Avg" },
            { title: "Apr_Avg" },
            { title: "May_Avg" },
            { title: "Jun_Avg" },
            { title: "Jul_Avg" },
            { title: "Aug_Avg" },
            { title: "Sep_Avg" },
            { title: "Oct_Avg" },
            { title: "Nov_Avg" },
            { title: "Dec_Avg" }

        ]
    } );
  
  })