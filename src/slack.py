""" Two Bedrooms """
import requests


class Slack:
    """ Slack Client using Webhooks """

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.headers = {
            'user-agent': 'two-bedrooms/0.0.1',
            'content-type': 'application/json'
        }

    def send(self, message):
        """ Sends a formatted message """
        requests.post(self.webhook_url, headers=self.headers, json=message)
