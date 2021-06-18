import json, os, requests

SERVICE_URL = os.getenv('SERVICE_URL')

def lambda_handler_ping(event, context):
    data = {'service': 'lambda-service'}
    
    print("#############################################")
    print("SERVICE_URL="+SERVICE_URL)
    response = requests.post(
        SERVICE_URL+"pong", data=json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )
    return {
        "statusCode" : 200,
        "body" : json.dumps(
            {"message" : response.content}
        )
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