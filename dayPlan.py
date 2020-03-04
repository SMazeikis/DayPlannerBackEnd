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
from bussiness import distance_calculator

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


def yelp_business_info(tag, limit=10):
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
    times = [0]

    if duration >= 6:
        restaurant_counter = 2

    elif duration >= 3:
        restaurant_counter = 1

    else:
        restaurant_counter = 0

    activity_by_option = random.choice(activities)
    activity = activity_by_option.popitem()
    day[0] = activity


    for event_number in range(1, duration):
            if event_number % 2 == 0 and event_number != 0 and restaurant_counter != 0:
                restaurant_by_cuisine = random.choice(restaurants)
                restaurant = restaurant_by_cuisine.popitem()
                last_event_location = str(day[event_number - 1][1]['location']['longitude']), str(day[event_number - 1][1]['location']['latitude'])
                time = distance_calculator(last_event_location[0], last_event_location[1], str(restaurant[1]['location']['longitude']), str(restaurant[1]['location']['latitude']))
                times.append(time)
                day[event_number] = restaurant
                restaurant_counter -= 1
            else:
                activity_by_option = random.choice(activities)
                activity = activity_by_option.popitem()
                last_event_location = str(day[event_number - 1][1]['location']['longitude']), str(day[event_number - 1][1]['location']['latitude'])
                time = distance_calculator(last_event_location[0], last_event_location[1], str(activity[1]['location']['longitude']), str(activity[1]['location']['latitude']))
                times.append(time)
                day[event_number] = activity
    
    day["times"] = times
    return day

#print(makeDay(data))