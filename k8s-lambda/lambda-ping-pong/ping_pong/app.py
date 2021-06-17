import json, os, requests

SERVICE_URL = os.getenv('SERVICE_URL')

def lambda_handler_ping(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            'app': 'lambda ping pong',
            'endpoint': '/ping'
        }),
    }

def lambda_handler_pong(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            'app': 'lambda ping pong',
            'endpoint': '/pong'
        }),
    }

def lambda_handler_default(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            'message': 'welcome to the lambda-ping-pong',
            'endpoint': '/'
        }),
    }