from flask import Flask
import os, requests, uuid, json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
    'Ocp-Apim-Subscription-Key': '{b0a2771ffd4744b7a30833d471940aa8}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'shortAudio': '{boolean}',
})

try:
    conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com/')
    conn.request("POST", "/spid/v1.0/identificationProfiles/{identificationProfileId}/enroll?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################