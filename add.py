import json
import datetime

def add(x, y):
    """Add together two integers."""
    return int(x) + int(y)

def handler(event, context):
    result = add(event['pathParameters']['x'], event['pathParameters']['y'])
    data = {'result': result}
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
