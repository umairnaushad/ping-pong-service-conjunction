from flask import Flask, request
from flask_restful import Resource, Api
import requests,json, os

app = Flask(__name__)
api = Api(app)

url = USER = os.getenv('SERVICE_2_ENDPOINT') #'http://127.0.0.1:5001/pong'

@app.route('/')
def welcome():
    return {
        'message': 'welcome to the k8s-ping-pong',
        'endpoint': '/'
    }

@app.route('/ping', methods=['GET'])
def ping():
    if request.method == 'GET':
        data = {'service': 'k8s'}
        response = requests.post(
            url+"pong", data=json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )
        return response.content

@app.route("/pong", methods=['POST'])
def pong():
   return {
       'app': 'k8s ping pong',
       'endpoint': '/pong'
    }

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5000, debug = True)