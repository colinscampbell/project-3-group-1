from operator import index
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

# ---------------------------------------------------------
# Web site
@app.route("/")
def weather_html():
   return render_template("index.html")

 # API Routes for Bar Chart #####################################
@app.route("/api/weather")

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

# API routes for Weather table    

@app.route("/weather_table")
def data():
    return render_template("weather_table.html")

# API
@app.route("/api/weather_table")
def weather_table():
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

# Line Chart routes
#     # API database #####################################
@app.route("/api/line")

def line_grid():
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
    
@app.route('/averages')
def get_averages():
    return render_template('average_temps.html')

    
@app.route('/api/averages')
def averages():
    engine = create_engine("sqlite:///Datasets//Weather_3.db")
    state = pd.read_sql_table('State_Code',con=engine)
    weather = pd.read_sql_table('Weather_Raw',con=engine)
    df = weather.merge(state,how='inner',left_on='State',right_on='Code')
    df = df.loc[:,'Year':]
    df = df[df.Year.between(2012,2021)]
    df = df.groupby(['Year']).mean().loc[:,'Jan':'Dec']
    df['combined'] = df.apply(lambda x: list([x['Jan'],
                                        x['Feb'],
                                        x['Mar'],
                                          x['Apr'],
                                        x['May'],
                                        x['Jun'],
                                          x['Jul'],
                                        x['Aug'],
                                        x['Sep'],
                                          x['Oct'],
                                        x['Nov'],
                                        x['Dec']
                                         ]),axis=1) 

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']

    datadict = df.combined.to_dict()
    new_dict ={}
    for k,v in datadict.items():
        new_dict[k] = dict(zip(months,datadict[k]))
    return jsonify(new_dict)

if __name__ == "__main__":
    app.run()   