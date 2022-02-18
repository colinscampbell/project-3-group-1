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

Wtr = Base.classes.Weather_Raw
St_Cd = Base.classes.State_Code
join = session.query( Wtr , St_Cd ).filter(Wtr.State == St_Cd.Code).statement

df = pd.read_sql_query(join, session.bind)
df