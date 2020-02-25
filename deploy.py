import os
import requests
import json
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from yelp.client import Client
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

config = {
  "apiKey" : "AIzaSyDQT78_79sRW4nPY2hj_2zu6TX_V3VoD8k",
  "authDomain" : "dayplanner-740b3.firebaseapp.com",
  "databaseURL" : "https://dayplanner-740b3.firebaseio.com",
  "projectId" : "dayplanner-740b3",
  "storageBucket" : "dayplanner-740b3.appspot.com",
  "messagingSenderId" : "930720206669",
  "appId" : "1:930720206669:web:2d15a4b9f7ec24b1b7f104",
  "measurementId" : "G-QZFMJ335XN"
}

firebase = pyrebase.initialize_app(config)

# cred = credentials.Certificate('./nothing.json')
# default_app = firebase_admin.initialize_app(cred)
# db = firestore.client()
# snapshot = db.collection('users').document("NUB1BGl5H0gqDi2JPYRzflO6GEF3")
# print(snapshot.get().to_dict())

MY_API_KEY = "b7wSeZeFykMFbPx-n7VpQD9gwi8EZWYYjaPEoa3ExSZv5c4LlGpANEhKR-sUW51218X6M3RO6t90tQGvbBAcX7pP9A3KnEo8FRfYZ1t1efZ_SXvj7POdAmmyqptTXnYx"

app = Flask(__name__)
CORS(app)
client = Client(MY_API_KEY)

endpoint = "https://api.yelp.com/v3/businesses/search"
header = {'Authorization': 'bearer %s' % MY_API_KEY}


@app.route('/list', methods=['GET'])
def read():
    try:
        return("hello")
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/parse_data', methods=['GET', 'POST'])
def parse():
    try:
        data = request.get_json()
        resolved_data = restaurant_info(data["html"])
        return(make_response(json.dumps(resolved_data)))
    except:
        return(":)")



def restaurant_info(name):
    restaurant_names = []
    parameters = {'term' : name,
              'limit': 10,
              'radius': 1000,
              'location': 'Dublin'}
    response = requests.get(url = endpoint, params = parameters, headers= header)
    business_data = response.json()
    for business in business_data['businesses']:
        restaurant_names.append(business['name'])
    return restaurant_names