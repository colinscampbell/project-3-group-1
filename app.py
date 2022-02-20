import os
#from dotenv import load_dotenv
#load_dotenv()
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from sqlalchemy import Column, Integer, String, Float
import numpy as np
import pandas as pd

#Below Flask Import added by Prina##
from flask import (Flask, render_template, jsonify, request,redirect)



#################################################
# Database Setup
#################################################
engines = create_engine("sqlite:///Datasets//Weather_3.db")

# Save reference to the table

conn = engines.connect()
Base = automap_base()
Base.prepare(engines, reflect=True)
session = Session(conn)
Base.classes.keys()
# Performs database schema inspection
#insp = sqlalchemy.inspect(engines)
#print(insp.get_table_names())
Wtr = Base.classes.Weather_Raw
St_Cd = Base.classes.State_Code
join = session.query( Wtr , St_Cd ).filter(Wtr.State == St_Cd.Code).statement
df = pd.read_sql_query(join, session.bind)
print(df)

States_list = [2, 3, 4, 8, 11, 18, 30, 45, 41,42]
df1 = df.loc[((df['Year'] >= 2012) & (df['Year'] <= 2021) & (df['State'].isin(States_list)))] ### this is where put the 10 states and the years that we are planning to use
df1 = df1.drop(['Element' , 'County', 'Code'] ,  axis=1)

df_avg = round(df1.groupby(['State_1', 'Year']).mean(), 2)
print(df_avg)
# Sending output to a CSV file to get the full picture
#df_avg.to_csv(r'C:\Users\georg\project-3-group-1\Datasetsr', index=True, header=True)
session.close()

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    return render_template("index.html")

#################################################
# BAR CHART #####################################
@app.route("/weather_bar")

def bar_chart():
    # Create our session (link) from Python to the DB
    session = Session(engines)
    """Return a list of all passenger names"""
    # Query all passengers
    # results = session.query(Passenger.name).all()
    results = session.query(Wtr).all()

    session.close()

    # # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)


if __name__ == '__main__':
    app.run(debug=True)


# // // ----------------INIT and GRAPHS ------------------------
# function init_plot_graphs(){
#    d3.json(url).then(function(data) {
#         sample_values =  data.samples[0].sample_values.slice(0,10).reverse();
#         console.log(`OTU Value ${sample_values}`);
#         otu_ids =  data.samples[0].otu_ids.slice(0,10);
#         console.log (`OTU ID ${otu_ids}`); 
#         otu_labels = data.samples[0].otu_labels.slice(0,10);
#         console.log(`OTU label ${otu_labels}`);
#         yticks = otu_ids.slice(0, 10).map(otuId => `OTU ${otuId}`).reverse();

#     // // -----BAR GRAPH PLOT OTU sample values
#         let data2 = [{
#           x: sample_values,
#           y: yticks,
#           text: otu_labels,
#           type: "bar",
#           orientation: "h"
#         }];

#         var layout = {
#           height: 600,
#           width: 1050
#         };

#       Plotly.newPlot("bar", data2, layout);
#       console.log("bar working");
