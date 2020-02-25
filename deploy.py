import os, requests, json, pyrebase, firebase_admin
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from yelp.client import Client
from user import test

MY_API_KEY = "b7wSeZeFykMFbPx-n7VpQD9gwi8EZWYYjaPEoa3ExSZv5c4LlGpANEhKR-sUW51218X6M3RO6t90tQGvbBAcX7pP9A3KnEo8FRfYZ1t1efZ_SXvj7POdAmmyqptTXnYx"

app = Flask(__name__)
CORS(app)
client = Client(MY_API_KEY)

endpoint = "https://api.yelp.com/v3/businesses/search"
header = {'Authorization': 'bearer %s' % MY_API_KEY}

# @app.route('/parse_data', methods=['GET', 'POST'])
# def parse():
#     try:
#         data = request.get_json()
#         resolved_data = restaurant_info(data["html"])
#         return(make_response(json.dumps(resolved_data)))
#     except Exception as e:
#         return(e)

@app.route('/userPreferences', methods=['GET', 'POST'])
def userPreferences():
    try:
        data = request.get_json()
        resolved_data = data
        return(make_response(json.dumps(resolved_data)))
    except Exception as e:
        return(e)

# def restaurant_info(name):
#     restaurant_names = []
#     parameters = {'term' : name,
#               'limit': 10,
#               'radius': 1000,
#               'location': 'Dublin'}
#     response = requests.get(url = endpoint, params = parameters, headers= header)
#     business_data = response.json()
#     for business in business_data['businesses']:
#         restaurant_names.append(business['name'])
#     return restaurant_names