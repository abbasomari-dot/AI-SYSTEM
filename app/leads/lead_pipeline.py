from app.leads.google_maps_finder import GoogleMapsFinder
from app.leads.lead_scoring import LeadScoring


class LeadPipeline:

    def run(self):

        API_KEY = "AIzaSyAkUxevCNCeXgwnLvWBHxgWCRntoBnL0qs"

        finder = GoogleMapsFinder(API_KEY)

        restaurants = finder.search_restaurants("Doha")

        scorer = LeadScoring()

        leads = []

        for r in restaurants:

            score = scorer.score(r)

            if score >= 3:

                leads.append({
                    "name": r["name"],
                    "rating": r["rating"],
                    "reviews": r["reviews"],
                    "location": r["location"]
                })

        return leads