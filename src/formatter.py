""" Two Bedrooms """


class Formatter:
    """ Prepares a message for sending """

    def __init__(self, results):
        self.results = results

    def create_slack_message(self):
        """ Creates a message formatted for Slack """
        return self.results
