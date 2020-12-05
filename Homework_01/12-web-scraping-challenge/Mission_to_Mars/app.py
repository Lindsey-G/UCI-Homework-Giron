from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Initiate Flask app
app = Flask(__name__)

# Connect to mongodb to mission_to_mars_app
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    # Create variable from mongo db mars to .find_one()
    mars = mongo.db.mars.find_one()
    # return render_template with "index.html" and mars=mars arguments
    return render_template("index.html", mars=mars)

# /scrape endpoint and def scrape() function
@app.route("/scrape")
def scrape():
    # Create variable from mongo db mars
    mars = mongo.db.mars
    # Call on all def functions from scrape_mars.py
    mars_data = scrape_mars.latest_news()
    mars_data = scrape_mars.featured_image()
    mars_data = scrape_mars.mars_facts()
    mars_data = scrape_mars.mars_hem()
    # Call on updated data 
    mars.update({}, mars_data, upsert=True)
    # Using return redirect to index page
    return redirect("/", code=302)

# Run app
if __name__ == "__main__":
    app.run(debug=True) 