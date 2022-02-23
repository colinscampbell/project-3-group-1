from operator import index
import os
#from dotenv import load_dotenv
#load_dotenv()
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
#import matplotlib.pyplot as plt
#from sqlalchemy import Column, Integer, String, Float
import numpy as np
import pandas as pd

#Below Flask Import added by Prina##
# from flask import ( Flask, Render_template, jsonify, request, redirect)

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
##### THIS IS THE DATAFRAMA METHOD, IT IS IDENTICAL TO THE SESSION QUERY METHOD BELOW
join = session.query( Wtr , St_Cd ).filter(Wtr.State == St_Cd.Code).statement
df = pd.read_sql_query(join, session.bind)
#print(df)
### this is where put the 10 states and the years that we are planning to use
States_list = [2, 3, 4, 8, 11, 18, 30, 45, 41,42]

df1 = df.loc[((df['Year'] >= 2012) & (df['Year'] <= 2021) & (df['State'].isin(States_list)))] 
df1 = df1.drop(['Element' , 'County', 'Code' ] ,  axis=1)
df_avg = round(df1.groupby(['State_1', 'Year']).mean(), 2)
df_avg = df_avg.reset_index()
print(df_avg)


#####This the  same list I was using for the Pandas dataframe but instead I am passing in the session query 
# States_list = [2, 3, 4, 8, 11, 18, 30, 45, 41,42] 
# result = session.query(St_Cd.State, Wtr.Year, func.round(func.avg(Wtr.Jan), 2).label('Jan'), func.round(func.avg(Wtr.Feb), 2).label('Feb'), func.round(func.avg(Wtr.Mar), 2).label('Mar'),\
#                                               func.round(func.avg(Wtr.Apr), 2).label('Apr'), func.round(func.avg(Wtr.May), 2).label('May'), func.round(func.avg(Wtr.Jun), 2).label('Jun'),\
#                                               func.round(func.avg(Wtr.Jul), 2).label('Jul'), func.round(func.avg(Wtr.Aug), 2).label('Aug'), func.round(func.avg(Wtr.Sep), 2).label('Sep'),
#                                               func.round(func.avg(Wtr.Oct), 2).label('Oct'), func.round(func.avg(Wtr.Nov), 2).label('Nov'), func.round(func.avg(Wtr.Dec), 2).label('Dec'))\
# .filter(Wtr.State == St_Cd.Code).filter(Wtr.State.in_(States_list)) \
# .filter((Wtr.Year > 2011) & (Wtr.Year < 2022 )).group_by(St_Cd.State, Wtr.Year).statement
# ###******** THIS IS TO PRINT AND VIEW THE RESULT USING THE SESSION QUERY METHOD ********
# df = pd.read_sql_query(result, session.bind)
# print(df)
# # Sending output to a CSV file to get the full picture
# #df.to_csv(r'C:\Users\georg\project-3-group-1\Datasetsr', index=True, header=True)
session.close()

#################################################
# Flask Setup
#################################################
# app = Flask(__name__)


# # ---------------------------------------------------------
# # Web site
# @app.route("/")
# def weather_html():
#    return render_template("index.html")

#     # ---------------------------------------------------------
# # API
# @app.route("/api/weather")

# def show_tables():
#     data = pd.read_excel('dummy_data.xlsx')
#     data.set_index(['Name'], inplace=True)
#     data.index.name=None
#     females = data.loc[data.Gender=='f']
#     males = data.loc[data.Gender=='m']
#     return render_template('index.html',tables=[df_avg.to_html(classes='data'), males.to_html(classes='male')],
#     titles = ['na', 'Female surfers', 'Male surfers'])

# # def weather_grid():
# #     session = Session(engines)
# #     results = session.query(Wtr.Jan_Avg,Wtr.State).all()

# #     results = [list(r) for r in results]

# #     table_results = {
# #         "table": results
# #     }

# #     print(table_results)
# #     session.close()

# #     return jsonify(table_results)
    

# if __name__ == "__main__":
#     app.run()






