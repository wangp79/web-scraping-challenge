from re import I
from flask import Flask, redirect, render_template
import scrape_mars
from flask_pymongo import PyMongo
import pymongo

app = Flask(__name__)

conn = "mongodb://localhost:27017/"
Client = pymongo.MongoClient(conn)

db = Client.mission_db


db.mission.mission.drop()

@app.route('/')
def index():
    data_dict = db.mission.mission.find({})
    data_list = []
    for i in data_dict:
        data_list.append(i)
    
    return render_template("index.html", py_dictionary=data_list)

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/scrape')
def scraper():
    py_dict = db.mission
    listings_data = scrape_mars.scrape()
    print(len(listings_data))
    for i in listings_data:
        py_dict.mission.insert(i)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

 