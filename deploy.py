import os
import requests
import json
import pyrebase
import firebase_admin
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from yelp.client import Client
from user import assignPreferences
from dayPlan import makeDay
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

if (not len(firebase_admin._apps)):
    cred = credentials.Certificate('./confidential.json')
    default_app = firebase_admin.initialize_app(cred)


@app.route('/userPreferences', methods=['GET', 'POST'])
@cross_origin()
def userPreferences():
    try:
        data = request.get_json()
        assignPreferences(data)
        return "ok"
    except Exception as e:
        return(e)

# @app.route('/testData', methods=['GET', 'POST'])
# @cross_origin()
# def testData():
#     try:
#         data = request.args.get('userId', type = str)
#         makeDay(data)
#         return data
#     except Exception as e:
#         return(e)


@app.route('/planDay', methods=['GET'])
@cross_origin()
def planDay():
    userId = request.args.get('userId', type=str)
    try:
        dayPlan = makeDay(userId)
        return dayPlan
    except Exception as e:
        return e
