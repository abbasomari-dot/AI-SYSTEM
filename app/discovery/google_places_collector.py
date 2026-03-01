import requests
import time
from app.core.config import GOOGLE_PLACES_API_KEY


class GooglePlacesCollector:
    BASE_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"

    def collect(self, query):
        params = {
            "query": query,
            "key": GOOGLE_PLACES_API_KEY
        }

        results = []
        page_count = 0

        while True:
            response = requests.get(self.BASE_URL, params=params)
            data = response.json()

            for place in data.get("results", []):
                results.append({
                    "name": place.get("name"),
                    "rating": place.get("rating"),
                    "reviews": place.get("user_ratings_total"),
                    "address": place.get("formatted_address"),
                    "lat": place.get("geometry", {}).get("location", {}).get("lat"),
                    "lng": place.get("geometry", {}).get("location", {}).get("lng"),
                    "place_id": place.get("place_id"),
                })

            page_count += 1

            # Stop after 3 pages (~60 results)
            if page_count >= 3:
                break

            next_page_token = data.get("next_page_token")

            if not next_page_token:
                break

            # Google requires short delay before using next_page_token
            time.sleep(2)

            params = {
                "pagetoken": next_page_token,
                "key": GOOGLE_PLACES_API_KEY
            }

        return results

    def get_place_details(self, place_id):
        params = {
            "place_id": place_id,
            "fields": "website,url",
            "key": GOOGLE_PLACES_API_KEY
        }

        response = requests.get(self.DETAILS_URL, params=params)
        data = response.json()

        result = data.get("result", {})

        return {
            "website": result.get("website"),
            "google_maps_url": result.get("url")
        }