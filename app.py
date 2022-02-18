import os
import sqlalchemy
#from dotenv import load_dotenv
#load_dotenv()
from sqlalchemy.sql import func
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Float

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

from flask import Flask, jsonify

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
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home(/):
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )

# @app.route("/api/v1.0/names")
# def names():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(Passenger.name).all()

#     session.close()

#     # Convert list of tuples into normal list
#     all_names = list(np.ravel(results))

#     return jsonify(all_names)


# @app.route("/api/v1.0/passengers")
# def passengers():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # Query all passengers
#     results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_passengers = []
#     for name, age, sex in results:
#         passenger_dict = {}
#         passenger_dict["name"] = name
#         passenger_dict["age"] = age
#         passenger_dict["sex"] = sex
#         all_passengers.append(passenger_dict)

#     return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)
