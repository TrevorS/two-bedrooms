""" Two Bedrooms """


class Slack:
    """ Slack Client using Webhooks """

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send(self, message):
        """ Sends a formatted message """
        print(self.webhook_url)
        print(message)
