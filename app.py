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
#print(df)

States_list = [2, 3, 4, 8, 11, 18, 30, 45, 41,42]
df1 = df.loc[((df['Year'] >= 2012) & (df['Year'] <= 2021) & (df['State'].isin(States_list)))] ### this is where put the 10 states and the years that we are planning to use
df1 = df1.drop(['Element' , 'County', 'Code'] ,  axis=1)

df_avg = round(df1.groupby(['State_1', 'Year']).mean(), 2)
print(df_avg)
# Sending output to a CSV file to get the full picture
#df_avg.to_csv(r'C:\Users\georg\project-3-group-1\Datasetsr', index=True, header=True)
session.close()