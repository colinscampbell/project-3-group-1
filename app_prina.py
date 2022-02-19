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
# Save reference to the table
print(Base.classes.keys())

Wtr = Base.classes.weather_data_project
wtr_data = session.query( Wtr).statement

df = pd.read_sql_query(wtr_data, session.bind)
df

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# ---------------------------------------------------------
# Web site
@app.route("/")
def weather_html():
   return render_template("index.html")

    # ---------------------------------------------------------
# API
@app.route("/api/weather")

def weather_grid():
    session = Session(engines)
    results = session.query(Wtr.Jan_Avg,Wtr.State).all()

    results = [list(r) for r in results]

    table_results = {
        "table": results
    }

    print(table_results)
    session.close()

    return jsonify(table_results)
    

if __name__ == "__main__":
    app.run()