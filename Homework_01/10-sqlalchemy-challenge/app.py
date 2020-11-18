from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/v1.0/precipitation")
def precipitation():

    return jsonify()
    
@app.route("/api/v1.0/stations")
def stations():

    return jsonify()

@app.route("")
/api/v1.0/<start> 

@app.route
/api/v1.0/<start>/</end>

if ___name__ == "__main__":
    app.run(debug=True)
