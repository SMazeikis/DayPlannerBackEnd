import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/list', methods=['GET'])
def read():
    try:
        return("hbo")
    except Exception as e:
        return f"An Error Occured: {e}"