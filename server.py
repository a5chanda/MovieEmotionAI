from flask import Flask, jsonify, request
import os, requests, uuid, json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    print("Info: ")
    print(request.data)
    obj = {'data': 'Test'}
    return jsonify(obj), 200
