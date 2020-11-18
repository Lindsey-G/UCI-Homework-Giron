###############################################################
# import dependencies
###############################################################
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

###############################################################
# Database Setup
###############################################################

# create_engine using sqlite to path to file
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# Reflect database into a new model using Base = automap()
Base = automap()

# Setup .prepare(engine, reflect=True) to reflect tables
Base.prepare(engine, reflect=True)

# Save reference to measurement table
Measurement = Base.classes.measurement
Station = Base.classes.station

###################################################################
# Set up Flask
###################################################################

app = Flask(__name__)

################################################
# Flask Routes
#####################################################

@app.route("/")
def welome():
    print("Server received request from home page.")
    """ List of all avaiable routes."""
    return (
        f"Avaiable Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start><br/>"
    )

# associate endpoint
@app.route("/api/v1.0/precipitation")
def precipitation():
   
   session = Session(engine)

   """ Return precipitation data"""
    date_prcp_results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    precipitation_data = []
    for date, prcp in date_prcp_results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation_data.append(precipitation_dict)

    return jsonify(precipitation_data)
    
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    station_results = session.query(Measurement.station).all()

    session.cloe()

    station_list = list(np.ravel(station_results))

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    top_stations_tobs_results = (session.query(Measurement.date, Measurement.tobs)
                .filter(Measurement.station == 'USC00519281')
                .filter(Measurement.date > '2016-08-23')
                .all())
    session.close()

    top_stations_tobs_last_year_data = []
    for date, tobs in top_stations_tobs_last_year_data:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        top_stations_tobs_last_year_data.append(tobs_dict)
    
    return jsonify(top_stations_tobs_last_year_data)

@app.route("/api/v1.0/<start>")
def start:
    
@app.route("/api/v1.0/<start>/</end>")
def start_end:

#######################################################################
# app.run
########################################################################

if ___name__ == "__main__":
    app.run(debug=True)
