import os, requests, json, pyrebase, firebase_admin
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from yelp.client import Client
from user import assignPreferences
from dayPlan import makeDay


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/userPreferences', methods=['GET', 'POST'])
@cross_origin()
def userPreferences():
    try:
        data = request.get_json()
        assignPreferences(data)
        return "ok"
    except Exception as e:
        return(e)

@app.route('/testData', methods=['GET', 'POST'])
@cross_origin()
def testData():
    try:
        data = request.get_json()
        makeDay(data)
        return data
    except Exception as e:
        return(e)

@app.route('/makeDay', methods=['GET'])
@cross_origin()
def makeDay():
    try:
        data = request.get_json()
        dayPlan = makeDay(data)
        return dayPlan
    except Exception as e:
        return(e)