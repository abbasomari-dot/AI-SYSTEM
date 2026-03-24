import requests

# 🔑 حط مفاتيحك هنا
GOOGLE_API_KEY = "AIzaSyAkUxevCNCeXgwnLvWBHxgWCRntoBnL0qs"
SERP_API_KEY = "d73e7006625d69fb60e0aa7daef0da018513f08de467114fe01804a4b6e633ad"


# ---------------------------
# Google Data (Maps)
# ---------------------------
def get_google_data(place_name):

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    params = {
        "query": place_name,
        "key": GOOGLE_API_KEY
    }

    res = requests.get(url, params=params).json()

    if not res.get("results"):
        return None

    place = res["results"][0]

    return {
        "name": place.get("name"),
        "rating": place.get("rating"),
        "reviews": place.get("user_ratings_total"),
        "address": place.get("formatted_address")
    }


# ---------------------------
# Instagram (SERP API)
# ---------------------------
def get_instagram(name):

    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google",
        "q": f"{name} instagram",
        "api_key": SERP_API_KEY
    }

    res = requests.get(url, params=params).json()

    results = res.get("organic_results", [])

    for r in results:
        link = r.get("link", "")
        if "instagram.com" in link:
            return link

    return None


# ---------------------------
# RUN TEST
# ---------------------------
place = "Nusr Et Doha"

google_data = get_google_data(place)
instagram = get_instagram(place)

print("GOOGLE DATA:")
print(google_data)

print("\nINSTAGRAM:")
print(instagram)