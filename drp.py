import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/list', methods=['GET'])
def read():
    try:
        return("FUCK YOU")
    except Exception as e:
        return f"An Error Occured: {e}"