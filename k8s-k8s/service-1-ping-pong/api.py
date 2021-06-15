from flask import Flask, request
from flask_restful import Resource, Api
import requests,json, os

app = Flask(__name__)
api = Api(app)

SERVICE_1_PORT = os.getenv('SERVICE_1_PORT')
SERVICE_2_URL = os.getenv('SERVICE_2_URL') #'http://service-2-ping-pong-svc:5001/pong'

@app.route('/')
def welcome():
    return {
        'message': 'welcome to the service-1-ping-pong',
        'endpoint': '/'
    }

@app.route('/ping', methods=['GET'])
def ping():
    if request.method == 'GET':
        data = {'service': 'k8s-service-1'}
        response = requests.post(
            SERVICE_2_URL+"pong", data=json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )
    return response.content

@app.route("/pong", methods=['POST'])
def pong():
   return {
       'app': 'k8s service 1 ping pong',
       'endpoint': 'pong'
    }

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = SERVICE_1_PORT, debug = True)
