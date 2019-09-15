from flask import Flask, jsonify
import os, requests, uuid, json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    obj = {'data': 'Test'}
    return jsonify(obj), 200
