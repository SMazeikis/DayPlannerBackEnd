import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import requests
import json
import pyrebase
import firebase_admin
import random
from flask import Flask, request, jsonify, make_response
from yelp.client import Client

MY_API_KEY = "b7wSeZeFykMFbPx-n7VpQD9gwi8EZWYYjaPEoa3ExSZv5c4LlGpANEhKR-sUW51218X6M3RO6t90tQGvbBAcX7pP9A3KnEo8FRfYZ1t1efZ_SXvj7POdAmmyqptTXnYx"

client = Client(MY_API_KEY)

if (not len(firebase_admin._apps)):
    cred = credentials.Certificate('./confidential.json')
    default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

endpoint = "https://api.yelp.com/v3/businesses/search"
header = {'Authorization': 'bearer %s' % MY_API_KEY}


data = {"userId" : "PUGAMfSoEZgvT2C9mthlpOmTo453",
"date": {},
"price": {"$": "false", "$$": "true", "$$$": "false"},
"time": {"h": "1", "m": "15", "a": "pm"},
"duration": 7
}

def makeDay(data):
    userId = data["userId"]
    snapshot = db.collection('users').document(userId)
    doc_ref = snapshot.get()
    doc_items = doc_ref.to_dict()
    restaurants = []
    activities = []
    for cuisine in doc_items["food"]:
        restaurant_info = yelp_business_info(cuisine)
        restaurants.append(restaurant_info)
    for activity in doc_items["activities"]:
        activity_info = yelp_business_info(activity)
        activities.append(activity_info)
    plannedDay = arrange_in_order(restaurants, activities, data["duration"])
    return(plannedDay)


def yelp_business_info(tag, limit=1):
    yelp_business_names = {}
    parameters = {'term': tag,
                  'limit': limit,
                  'location': 'Dublin'}
    response = requests.get(url=endpoint, params=parameters, headers=header)
    business_data = response.json()
    for business in business_data['businesses']:
        yelp_business_names[business['name']] = {
                                'location' : business['coordinates'],
                                'url' : business['url'],
                                'tag' :  tag}
    return yelp_business_names


def arrange_in_order(restaurants, activities, duration):
    day = {}

    if duration >= 6:
        restaurant_limit = 2
        day[0] = random.choice(activities)
        day[1] = random.choice(activities)
        day[2] = random.choice(restaurants)
        day[3] = random.choice(activities)
        day[4] = random.choice(restaurants)

    elif duration >= 3:
        restaurant_limit = 1
        day[0] = random.choice(activities)
        day[1] = random.choice(activities)
        day[2] = random.choice(restaurants)

    else:
        restaurant_limit = 0
        day[0] = random.choice(activities)
        day[1] = random.choice(activities)
    
    return day

print(makeDay(data))