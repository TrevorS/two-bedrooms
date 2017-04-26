""" Two Bedrooms """
from bs4 import BeautifulSoup
import requests


class Scraper:
    # pylint: disable=too-few-public-methods

    """ Used to retrieve floor plans """
    def __init__(self, url):
        self.url = url

    def get_available_floor_plans(self):
        """ Retrieves the list of available floor plans """
        return list(filter(lambda floor_plan: floor_plan["available"], self.get_floor_plans()))

    def get_floor_plans(self):
        """ Retrieves the list of floor plans """
        results = BeautifulSoup(
            self.__get_html(), "html.parser").find_all(scope="row")

        return list(map(self.__extract_row, results))

    def __get_html(self):
        return requests.get(self.url).text

    def __extract_row(self, row):
        return {
            "floor_plan": self.__floor_plan(row),
            "beds": self.__beds(row),
            "sqft": self.__sqft(row),
            "rent": self.__rent(row),
            "availability": self.__availability(row),
            "available": self.__available(row)
        }

    def __floor_plan(self, row):
        return row.find(attrs={"data-label": "Floor Plan"}).text.replace("Floor Plan", "")

    def __beds(self, row):
        return row.find(attrs={"data-label": "Beds"}).text.replace("Bed/Bath", "")

    def __sqft(self, row):
        return row.find(attrs={"data-label": "SQ. FT."}).text \
                  .replace("Square feet", "").replace("-", "")

    def __rent(self, row):
        return row.find(attrs={"data-label": "Rent"}).text \
                  .replace("Monthly Rent", "").replace("-", "")

    def __availability(self, row):
        return row.find(attrs={"data-label": "Availability"}).text \
            .replace("Availability", "").replace("\n", "")

    def __available(self, row):
        return self.__availability(row) != "Contact Us"
