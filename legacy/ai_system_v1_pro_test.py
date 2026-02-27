# ==========================================
# AI MARKETING SYSTEM - V1 PROFESSIONAL TEST
# ==========================================

import time
import random

print("\n=== AI SYSTEM V1 PROFESSIONAL TEST STARTED ===\n")

# ==========================================
# CORE ENGINE
# ==========================================

def validate_input(data):
    for key, value in data.items():
        if not value:
            raise ValueError(f"Missing value for: {key}")
    return True


def detect_tone(restaurant_type):
    t = restaurant_type.lower()

    if "luxury" in t or "steak" in t:
        return "Premium & Exclusive"
    elif "shawarma" in t:
        return "Affordable & Fast"
    elif "cafe" in t:
        return "Cozy & Social"
    elif "burger" in t:
        return "Trendy & Youth Focused"
    else:
        return "General Mass Market"


def generate_strategy(data):
    tone = detect_tone(data["type"])

    return {
        "restaurant": data["name"],
        "tone": tone,
        "audience": data["target_audience"],
        "offer": data["offer"]
    }


def generate_poster(data):
    return {
        "headline": f"Best {data['type']} in {data['location']}!",
        "offer": data["offer"],
        "cta": "Order Now!"
    }


def generate_video(data):
    return f"Promote {data['offer']} at {data['name']} in {data['location']}"


def calculate_metrics(views, interactions, sales):
    if views <= 0:
        raise ValueError("Views must be greater than zero")

    engagement = (interactions / views) * 100
    conversion = (sales / views) * 100

    return {
        "engagement_rate": round(engagement, 2),
        "conversion_rate": round(conversion, 2)
    }


# ==========================================
# TEST CASES
# ==========================================

test_restaurants = [
    {
        "name": "Burger Zone",
        "type": "Burger Restaurant",
        "target_audience": "Youth 18-30",
        "offer": "Burger + Fries 29 QAR",
        "location": "Doha"
    },
    {
        "name": "Doha Steak House",
        "type": "Luxury Steakhouse",
        "target_audience": "High Income Adults",
        "offer": "Premium Steak 199 QAR",
        "location": "West Bay"
    },
    {
        "name": "Al Doha Shawarma",
        "type": "Shawarma Restaurant",
        "target_audience": "Families",
        "offer": "2 Shawarma 18 QAR",
        "location": "Al Sadd"
    }
]


# ==========================================
# FULL PROFESSIONAL TEST EXECUTION
# ==========================================

start_time = time.time()

for i, restaurant in enumerate(test_restaurants):
    print(f"\n--- TEST CASE {i+1} ---")

    try:
        validate_input(restaurant)

        strategy = generate_strategy(restaurant)
        poster = generate_poster(restaurant)
        video = generate_video(restaurant)

        views = random.randint(5000, 20000)
        interactions = random.randint(100, 500)
        sales = random.randint(5, 50)

        metrics = calculate_metrics(views, interactions, sales)

        print("Strategy:", strategy)
        print("Poster:", poster)
        print("Video:", video)
        print("Metrics:", metrics)

    except Exception as e:
        print("Error during test:", e)


# ==========================================
# STRESS TEST
# ==========================================

print("\n--- STRESS TEST (100 RUNS) ---")

try:
    for _ in range(100):
        generate_strategy(test_restaurants[0])
    print("Stress test passed ✅")
except Exception as e:
    print("Stress test failed:", e)


# ==========================================
# BREAK TEST
# ==========================================

print("\n--- BREAK TEST ---")

broken_restaurant = {
    "name": "",
    "type": "",
    "target_audience": "",
    "offer": "",
    "location": ""
}

try:
    validate_input(broken_restaurant)
except Exception as e:
    print("Break test successful (caught error) ✅")
    print("Error:", e)


# ==========================================
# FINAL REPORT
# ==========================================

end_time = time.time()

print("\nExecution Time:", round(end_time - start_time, 2), "seconds")
print("\n=== V1 PROFESSIONAL TEST COMPLETED 🚀 ===")