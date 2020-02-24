import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from user import fer
from yelp.client import Client

MY_API_KEY = "b7wSeZeFykMFbPx-n7VpQD9gwi8EZWYYjaPEoa3ExSZv5c4LlGpANEhKR-sUW51218X6M3RO6t90tQGvbBAcX7pP9A3KnEo8FRfYZ1t1efZ_SXvj7POdAmmyqptTXnYx" #  Replace this with your real API key

app = Flask(__name__)
CORS(app)
client = Client(MY_API_KEY)

endpoint = "https://api.yelp.com/v3/businesses/search"
header = {'Authorization': 'bearer %s' % MY_API_KEY}
# parameters = {'term' : "indian",
#               'limit': 10,
#               'radius': 1000,
#               'location': 'Dublin'}
# response = requests.get(url = endpoint, params = parameters, headers= header)
# business_data = response.json()
# for business in business_data['businesses']:
#     print(business['name'])


@app.route('/list', methods=['GET'])
def read():
    try:
        return(fer())
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/parse_data', methods=['GET', 'POST'])
def parse():
    data = request.json
    resolved_data = restaurant_info(data.html)
    try:
        return(resolved_data)
    except:
        return("welp")

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