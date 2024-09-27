import json
import requests

def send_to_teams():
    webhook_url = "<webhook URL that you geenrate from teams channel>"
    message = {
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "summary": "Delivery Updates",
    "sections": [{
        "activityTitle": "projects in Progress",
        "activitySubtitle": "Update every 15 mins",
        "facts": [{
            "name": "Progress:",
            "value": "75%"
        }],
        "markdown": True
    }]
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(message), headers=headers)
    print("Status Code:", response.status_code)
    print("Response:", response.text)

def lambda_handler(event, context):
    send_to_teams()
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent to Teams!')
    }