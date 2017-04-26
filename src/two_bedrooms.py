""" Two Bedrooms """
import os
from scraper import Scraper
from formatter import Formatter
from slack import Slack

ASCENT_URL = os.environ["TWO_BEDROOMS_ASCENT_URL"]
WEBHOOK_URL = os.environ["TWO_BEDROOMS_SLACK_URL"]


def main():
    """ Starts the Two Bedrooms Scraper """
    scraper = Scraper(ASCENT_URL)
    results = scraper.get_available_floor_plans()

    formatter = Formatter(results)
    message = formatter.create_slack_message()

    slack = Slack(WEBHOOK_URL)
    slack.send(message)


if __name__ == "__main__":
    main()
