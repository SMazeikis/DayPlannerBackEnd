import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from user import fer

app = Flask(__name__)
CORS(app)

@app.route('/list', methods=['GET'])
def read():
    try:
        return(fer())
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/parse_data', methods=['GET', 'POST'])
def parse():
    data = request.json
    if request.method == "POST":
         return(data)
    else:
        return("none")