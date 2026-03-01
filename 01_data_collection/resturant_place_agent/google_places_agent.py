import requests
import pandas as pd
import time

API_KEY = "AIzaSyCCSTHIcJfWWpxgDkZwMEqUdk7IT2a2TLA"

url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

params = {
    "query": "restaurants in Doha Qatar",
    "key": API_KEY
}

results = []

while True:
    response = requests.get(url, params=params)
    data = response.json()

    for place in data.get("results", []):
        results.append({
            "Name": place.get("name"),
            "Rating": place.get("rating"),
            "Reviews": place.get("user_ratings_total"),
            "Address": place.get("formatted_address"),
            "Latitude": place.get("geometry", {}).get("location", {}).get("lat"),
            "Longitude": place.get("geometry", {}).get("location", {}).get("lng")
        })

    if "next_page_token" in data:
        time.sleep(2)  # مهم جدًا قبل استخدام التوكن
        params = {
            "pagetoken": data["next_page_token"],
            "key": API_KEY
        }
    else:
        break

df = pd.DataFrame(results)
# تنظيف البيانات
df = df.dropna(subset=["Rating", "Reviews"])

df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df["Reviews"] = pd.to_numeric(df["Reviews"], errors="coerce")

# تصنيف المطاعم
def classify(row):
    if row["Rating"] >= 4.3 and row["Reviews"] >= 500:
        return "🔥 High Potential"
    elif row["Rating"] >= 4.0 and row["Reviews"] >= 200:
        return "🟡 Medium Potential"
    else:
        return "⚪ Low Potential"

df["Category"] = df.apply(classify, axis=1)

# ترتيب حسب عدد المراجعات
df = df.sort_values(by="Reviews", ascending=False)
df.to_csv("doha_restaurants_classified.csv", index=False)
print(f"تم إنشاء ملف doha_restaurants_google_places_full.csv بعدد {len(results)} مطعم")