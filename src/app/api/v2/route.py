import json

def handler(event, context):
    # Crear el objeto JSON
    response = {
        "message": "Hello from the Python API!"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }