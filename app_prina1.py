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
print(df_avg)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# ---------------------------------------------------------
# Web site
@app.route("/")
def weather_html():
   return render_template("index.html")

# API
@app.route("/api/weather")

def weather_grid():
    session = Session(engines)
    results = session.query( Wtr , St_Cd ).filter(Wtr.State == St_Cd.Code).statement
    df = pd.read_sql_query(results, session.bind)

    States_list = [2, 3, 4, 8, 11, 18, 30, 45, 41,42]
    df1 = df.loc[((df['Year'] >= 2012) & (df['Year'] <= 2021) & (df['State'].isin(States_list)))] ### this is where put the 10 states and the years that we are planning to use
    df1 = df1.drop(['Element' , 'County', 'Code'] ,  axis=1)

    df_avg = round(df1.groupby(['State_1', 'Year']).mean(), 2)
    df_avg = df_avg.reset_index()
   # print(df_avg)

    df_json = df_avg.to_json(orient='records')
    #[1:-1].replace('},{', '} {')
    #print(df_json)

    #results = session.query(Wtr.State,Wtr.Year,Wtr.Jan_Avg,Wtr.Feb_Avg, Wtr.Mar_Avg, Wtr.Apr_Avg,Wtr.May_Avg,Wtr.Jun_Avg,Wtr.Jul_Avg,Wtr.Aug_Avg,Wtr.Sep_Avg,Wtr.Oct_Avg,Wtr.Nov_Avg,Wtr.Dec_Avg).all()

   # results = [list(r) for r in df_json]
    #results = [dict(r) for r in df_json]
    #table_results = {
    #    "table": results
    #}

    #print(table_results)
    session.close()

    #return jsonify(table_results)
    #return jsonify(df_json)
    return df_json

if __name__ == "__main__":
    app.run()   