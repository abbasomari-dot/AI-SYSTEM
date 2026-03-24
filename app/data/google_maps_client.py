import requests


class GoogleMapsClient:

    def __init__(self):
        self.api_key = "AIzaSyAkUxevCNCeXgwnLvWBHxgWCRntoBnL0qs"

    # ---------------------------
    # GET MAIN PLACE DATA
    # ---------------------------
    def get_place_data(self, query):
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

        params = {
            "query": query,
            "key": self.api_key
        }

        response = requests.get(url, params=params)
        data = response.json()

        if "results" not in data or len(data["results"]) == 0:
            return {
                "name": query,
                "rating": 0,
                "reviews": 0,
                "address": "Not found"
            }

        place = data["results"][0]

        return {
            "name": place.get("name", query),
            "rating": place.get("rating", 0),
            "reviews": place.get("user_ratings_total", 0),
            "address": place.get("formatted_address", "Not available")
        }

    # ---------------------------
    # GET COMPETITORS
    # ---------------------------
    def get_competitors(self, query, location="Doha", limit=3):

        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

        params = {
            "query": f"{query} in {location}",
            "key": self.api_key
        }

        response = requests.get(url, params=params)
        data = response.json()

        competitors = []

        for place in data.get("results", [])[:limit]:
            competitors.append({
                "name": place.get("name"),
                "rating": place.get("rating", 0),
                "reviews": place.get("user_ratings_total", 0)
            })

        return competitors