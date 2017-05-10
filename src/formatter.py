""" Two Bedrooms """


class Formatter:
    """ Prepares a message for sending """

    # pylint: disable=line-too-long
    image_url = "https://res.cloudinary.com/codaworx/image/upload/w_620,c_fill/v1400510474/project/ascent-03.jpg"

    def __init__(self, results):
        self.results = results

    def create_slack_message(self):
        """ Creates a message formatted for Slack """
        meta = self.__meta()
        floor_plans = self.__format_floor_plans()

        return {
            "attachments": [
                {
                    "pretext": "Apartments available!",
                    "title": "Two Bedrooms - The Ascent @ Walnut Creek",
                    "image_url": self.image_url
                },
                {
                    "fields": [
                        {
                            "title": "Floor plans available",
                            "value": meta["floor_plan_count"]
                        }
                    ],
                }
            ] + floor_plans
        }

    def __meta(self):
        return {
            "floor_plan_count": len(self.results)
        }

    def __format_floor_plans(self):
        return sum(filter(None.__ne__, list(map(self.__format_floor_plan, self.results))), [])

    def __format_floor_plan(self, details):
        if not self.__has_two_bedrooms(details):
            return None

        floor_plan_name = self.__floor_plan_name(details)
        beds = self.__beds(details)
        sqft = self.__sqft(details)
        rent = self.__rent(details)
        availability = self.__availability(details)

        return [
            {
                "color": "#3AA3E3",
                "fields": [
                    {
                        "title": "Floor Plan",
                        "value": floor_plan_name,
                        "short": True
                    },
                    {
                        "title": "Bedrooms / Bathrooms",
                        "value": beds,
                        "short": True
                    }
                ]
            },
            {
                "fields": [
                    {
                        "title": "Square Feet",
                        "value": sqft,
                        "short": True
                    },
                    {
                        "title": "Rent",
                        "value": rent,
                        "short": True
                    }
                ]
            },
            {
                "fields": [
                    {
                        "title": "Vacancy",
                        "value": availability
                    }
                ]
            }
        ]

    def __floor_plan_name(self, details):
        return details["floor_plan"].strip()

    def __beds(self, details):
        return details["beds"].strip()

    def __sqft(self, details):
        return details["sqft"].strip()

    def __rent(self, details):
        return details["rent"].strip()

    def __availability(self, details):
        return details["availability"].strip()

    def __has_two_bedrooms(self, details):
        return self.__beds(details) == "2 / 2"
