import json
import os
import random

import requests
import yaml

# Create the webhook url at https://my.slack.com/services/new/incoming-webhook/
SLACK_WEBHOOK_URL = os.environ.get(
    'SLACK_WEBHOOK_URL',
    'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'
)


def send_slack_message(slack_data):
    response = requests.post(
        SLACK_WEBHOOK_URL,
        data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(f"Slack request returned a '{response.status_code}' error with response '{response.text}'")


def main(event, context):
    random_joke = random.choice(get_jokes())
    random_emoji = random.choice(get_emojis())
    slack_data = {
        "username": "joker daddy",
        "icon_emoji": f":{random_emoji}:",
        "text": f"{random_joke['q']}\n{random_joke['a']}",
    }
    slack_response = send_slack_message(slack_data)
    return serverless_response(event, slack_data, slack_response)


def get_jokes():
    yaml_file = "data/jokes.yml"
    return read_yaml_file(yaml_file)


def get_emojis():
    yaml_file = "data/emojis.yml"
    return read_yaml_file(yaml_file)


def read_yaml_file(yaml_file):
    with open(yaml_file, 'r', encoding="utf-8") as stream:
        data = yaml.safe_load(stream)
    return data


def serverless_response(event, slack_data, slack_response):
    body = {
        "slack_data": slack_data,
        "slack_response": slack_response,
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response


if __name__ == '__main__':
    print(main({}, None))
