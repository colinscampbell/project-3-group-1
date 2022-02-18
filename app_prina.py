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

Wtr = Base.classes.Weather_Raw
St_Cd = Base.classes.State_Code
join = session.query( Wtr , St_Cd ).filter(Wtr.State == St_Cd.Code).statement

df = pd.read_sql_query(join, session.bind)
df

#################################################
# Flask Setup
#################################################
#app = Flask(__name__)


# ---------------------------------------------------------
# Web site
#@app.route("/")
#def home():
#    return render_template("index.html")

    # ---------------------------------------------------------
# API
#@app.route("/api/weather")
#def weather_grid():
#    session = Session(engine)
#    results = session.query(St_Cd.state).all()
#    results = [list(r) for r in results]
#    table_results = {
#        "table": results
#    }
#    session.close()
#    return jsonify(table_results)