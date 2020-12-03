from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# initate app
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017"
mongo = PyMongo(app)

@app.route("/")
def index():

    return render_template("index.html", =)




if __name__ == "__main__":
    app.run(debug=True) 