import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os, requests, json, pyrebase, firebase_admin
from flask import Flask, request, jsonify, make_response
from yelp.client import Client

MY_API_KEY = "b7wSeZeFykMFbPx-n7VpQD9gwi8EZWYYjaPEoa3ExSZv5c4LlGpANEhKR-sUW51218X6M3RO6t90tQGvbBAcX7pP9A3KnEo8FRfYZ1t1efZ_SXvj7POdAmmyqptTXnYx"

client = Client(MY_API_KEY)

db = firestore.client()

data = {"userId": "GFxKdNh7WQhiwgX5zIMHMyzAuN93",
                 "date" : "wfr",
                 "price" : "fea",
                 "time" : "fas",
                 "duration" : "feaf"
       }

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
        restaurants.append(restaurant_info(cuisine))
    for activity in doc_items["activities"]:
        activities.append(restaurant_info(activity))
    all_restaurants = restaurants[0] + restaurants[1]
    all_activities = activities[0] + activities[1]
    return({"restaurants" : all_restaurants,
            "activities" : all_activities})

def restaurant_info(name):
    restaurant_names = []
    parameters = {'term' : name,
              'limit': 1,
              'location': 'Dublin'}
    response = requests.get(url = endpoint, params = parameters, headers= header)
    business_data = response.json()
    for business in business_data['businesses']:
        restaurant_names.append(business['name'])
    return (restaurant_names)

print(makeDay(data))
