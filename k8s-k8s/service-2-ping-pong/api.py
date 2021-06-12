from flask import Flask, request
from flask_restful import Resource, Api
import requests,json

app = Flask(__name__)
api = Api(app)

url = 'http://localhost:5000/pong'

@app.route('/')
def welcome():
    return "welcome to the service-2-ping-pong"

@app.route('/about', methods=['GET'])
def home():
    return {
       'revision': '1.0.0'
       }

@app.route('/ping', methods=['GET'])
def ping():
    if request.method == 'GET':
        data = {'service': 'lambda'}
        response = requests.post(
            url, data=json.dumps(data),
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
    app.run(host ='0.0.0.0', port = 5001, debug = True)