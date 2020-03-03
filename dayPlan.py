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


def makeDay(data):
    userId = data["userId"]
    snapshot = db.collection('users').document(userId)
    doc_ref = snapshot.get()
    doc_items = doc_ref.to_dict()
    restaurants = []
    activities = []
    for cuisine in doc_items["food"]:
        for restaurant in yelp_business_info(cuisine):
            restaurants.append(restaurant)
    for activity in doc_items["activities"]:
        for activity_business in yelp_business_info(activity):
            activities.append(activity_business)
    plannedDay = arrange_in_order(restaurants, activities, data["duration"])
    return(plannedDay)


def yelp_business_info(name, limit=1):
    yelp_business_names = []
    parameters = {'term': name,
                  'limit': limit,
                  'location': 'Dublin'}
    response = requests.get(url=endpoint, params=parameters, headers=header)
    business_data = response.json()
    for business in business_data['businesses']:
        yelp_business_names.append(business['name'])
    return yelp_business_names


def arrange_in_order(restaurants, activities, duration):
    day = {}

    if duration >= 6:
        restaurant_limit = 2
        day[random.choice(activities)] = "first"
        day[random.choice(activities)] = "second"
        day[random.choice(restaurants)] = "third"
        day[random.choice(activities)] = "fourth"
        day[random.choice(restaurants)] = "fifth"

    elif duration >= 3:
        restaurant_limit = 1
        day[random.choice(activities)] = "first"
        day[random.choice(activities)] = "second"
        day[random.choice(restaurants)] = "third"

    else:
        restaurant_limit = 0
        day[random.choice(activities)] = "first"
        day[random.choice(activities)] = "second"
    
    return day
