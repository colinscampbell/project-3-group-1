import os
#from dotenv import load_dotenv
#load_dotenv()
from sqlalchemy.sql import func
from sqlalchemy import create_engine, func, or_
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import matplotlib.pyplot as plt
from sqlalchemy import Column, Integer, String, Float
import numpy as np
import pandas as pd

#Below Flask Import added by Prina##
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

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

States_list = [2, 3, 4, 8, 11, 18, 30, 45, 41,42]
df1 = df.loc[((df['Year'] >= 2012) & (df['Year'] <= 2021) & (df['State'].isin(States_list)))] ### this is where put the 10 states and the years that we are planning to use
df1 = df1.drop(['Element' , 'County', 'Code'] ,  axis=1)

df_avg = round(df1.groupby(['State_1', 'Year']).mean(), 2)
df_avg = df1.drop(['State_1'] ,  axis=1)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
print(__name__)
print(__file__)

# ---------------------------------------------------------
# Web site
@app.route("/")
def weather_html():
   return render_template("index.html")

@app.route("/data_table")
def data():

    return render_template("data_table.html")

# API
@app.route("/api/weather_table")

def weather_grid():
    session = Session(engines)
    results = session.query( Wtr , St_Cd ).filter(Wtr.State == St_Cd.Code).statement
    df = pd.read_sql_query(results, session.bind)

    States_list = [2, 3, 4, 8, 11, 18, 30, 45, 41,42]
    df1 = df.loc[((df['Year'] >= 2012) & (df['Year'] <= 2021) & (df['State'].isin(States_list)))] ### this is where put the 10 states and the years that we are planning to use
    df1 = df1.drop(['Element' , 'County', 'Code','State'] ,  axis=1)

    df_avg = round(df1.groupby(['State_1', 'Year']).mean(), 2)
    
    df_avg = df_avg.reset_index()

    df_list = df_avg.values.tolist() # convert data frame to list as datatables only accepts list

    session.close()

    return jsonify(df_list)

if __name__ == "__main__":
    app.run()   