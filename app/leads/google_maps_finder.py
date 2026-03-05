import requests
import time


class GoogleMapsFinder:

    def __init__(self, api_key):
        self.api_key = api_key

    def search_restaurants(self, location="Doha", pages=3):

        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

        params = {
            "query": f"restaurants in {location}",
            "key": self.api_key
        }

        restaurants = []

        for page in range(pages):

            response = requests.get(url, params=params)
            data = response.json()

            results = data.get("results", [])

            for place in results:

                restaurant = {
                    "name": place.get("name"),
                    "rating": place.get("rating", 0),
                    "reviews": place.get("user_ratings_total", 0),
                    "location": place.get("formatted_address"),
                    "maps_link": f"https://www.google.com/maps/place/?q=place_id:{place.get('place_id')}"
                }

                restaurants.append(restaurant)

            next_page_token = data.get("next_page_token")

            if not next_page_token:
                break

            # Google يحتاج انتظار قبل استخدام token
            time.sleep(2)

            params = {
                "pagetoken": next_page_token,
                "key": self.api_key
            }

        return restaurants