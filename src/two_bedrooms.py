""" Two Bedrooms """
from scraper import Scraper

URL = "http://www.ascentwalnutcreek.com/floorplans.aspx"


def main():
    """ Starts the Two Bedrooms Scraper """
    scraper = Scraper(URL)
    results = scraper.get_available_floor_plans()

    print(results)


if __name__ == "__main__":
    main()
