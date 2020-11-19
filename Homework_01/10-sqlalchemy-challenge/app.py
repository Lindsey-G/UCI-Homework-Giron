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
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect database into a new model using Base = automap()
Base = automap_base()

# Setup .prepare(engine, reflect=True) to reflect tables
Base.prepare(engine, reflect=True)

# Save reference to measurement and station table
Measurement = Base.classes.measurement
Station = Base.classes.station

###################################################################
# Set up Flask
###################################################################

app = Flask(__name__)

################################################
# Flask Routes
#####################################################

# Welcome page
@app.route("/")
def welcome():
    print("Server received request from home page.")
    """ List of all avaiable routes."""
    return (
        f"Climate App<br/>"
        f"Avaiable Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start><br/>"
    )

# Precipitation page
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Open session to engine
    session = Session(engine)

    
    # Query for date and prcp from Measurement table
    date_prcp_results = session.query(Measurement.date, Measurement.prcp).all()

    # Close session
    session.close()

    # Create variable to hold precipitation list
    precipitation_data = []
    
    # for loop date and prcp from query results
    for date, prcp in date_prcp_results:
        # Create precipitation dictionary
        precipitation_dict = {}
        # Add columns to percipitation_dict and select specific data to store (date, prcp)
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        # Append results to list
        precipitation_data.append(precipitation_dict)
    
    # return jsonify results from precipitation_data
    return jsonify(precipitation_data)

# Station page
@app.route("/api/v1.0/stations")
def stations():
    # Open sessioni to engine
    session = Session(engine)

    # Query results station results from Measuement table 
    station_results = session.query(Measurement.station).group_by(Measurement.station).all()

    # Close session
    session.close()

    # Create list using list(np.ravel()) on station_results
    station_list = list(np.ravel(station_results))

    # return jsonify results from station_list
    return jsonify(station_list)

# TOBS page 
@app.route("/api/v1.0/tobs")
def tobs():
    # Open session to engnine
    session = Session(engine)

    # Query the busiest station USC00519281 (results from jupyter notebook) 
    # from Measurement table on date and tob, .filter() station == USC00519281 
    # .filter date > '2016-08-23' (a year from data results )
    top_stations_tobs_results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date > '2016-08-23').\
                all()

    # Close session
    session.close()
    
    # Create varaible to hold list
    top_stations_tobs_last_year_data = []

    # for loop date tobs on top_stations_tobs_last_year_data results
    for date, tobs in top_stations_tobs_results:
        # Create tobs_dict and select specific data (date, tobs)
        tobs_dict = {}
        # Add columns tobs_dict
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        #Append tobs_dict results to top_stations_tobs_last_year_data list
        top_stations_tobs_last_year_data.append(tobs_dict)
    
    # return jsonify results from top_stations_tobs_last_year_data
    return jsonify(top_stations_tobs_last_year_data)

# start 
@app.route("/api/v1.0/<start>")
def start_date(start):
    
    session = Session(engine)

    start_date_data = start_date_data = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).\
            group_by(Measurement.station).\
                order_by(Measurement.date).\
                    all()
 
    session.close()

    requested_start_date = start

    for date in start_date_data:
        start_search_date = date["start"]

        if start_search_date == requested_start_date:
            return jsonify(date)

    return jsonify({"error": f"{start} date is not found."})

# start/end
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):

    session = Session(engine)

    start_end_date_data = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date < end ).\
            group_by(Measurement.station).\
                order_by(Measurement.date).\
                    all()
        
    session.close()
    
    start_end_request = (start, end)

    for dates in start_end_date_data:
        start_end_search_date = dates[[start][end]]

        if start_end_search_date == start_end_request:
            return jsonify(dates)

    return jsonify({"error:" f"{start} - {end} not found"})
#######################################################################
# app.run
########################################################################

if __name__ == "__main__":
    app.run(debug=True)
