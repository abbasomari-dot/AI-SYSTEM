from app.leads.google_maps_finder import GoogleMapsFinder

# ضع API Key هنا
API_KEY = "AIzaSyAkUxevCNCeXgwnLvWBHxgWCRntoBnL0qs"

finder = GoogleMapsFinder(API_KEY)

restaurants = finder.search_restaurants("Doha")

for r in restaurants:
    print(r)