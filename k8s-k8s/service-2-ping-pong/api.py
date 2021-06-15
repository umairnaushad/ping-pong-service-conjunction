from flask import Flask, request
from flask_restful import Resource, Api
import requests, json, os

app = Flask(__name__)
api = Api(app)

SERVICE_URL = os.getenv('SERVICE_URL') #'http://service-1-ping-pong-svc:5000/pong'

@app.route('/')
def welcome():
    return {
        'message': 'welcome to the service-2-ping-pong',
        'endpoint': '/'
    }

@app.route('/ping', methods=['GET'])
def ping():
    if request.method == 'GET':
        data = {'service': 'lambda'}
        response = requests.post(
            SERVICE_URL+"pong", data=json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )
    return response.content

@app.route("/pong", methods=['POST'])
def pong():
   return {
       'app': 'lambda ping pong',
       'endpoint': 'pong'
    }

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5000)
