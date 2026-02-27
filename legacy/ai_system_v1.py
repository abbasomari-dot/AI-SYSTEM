# ==========================================
# AI MARKETING SYSTEM - PROFESSIONAL V1
# ==========================================

import time

print("\n=== AI MARKETING SYSTEM V1 STARTED ===\n")

# ==========================================
# STEP 1 — INPUT
# ==========================================

restaurant = {
    "name": "Burger Zone",
    "type": "Burger Restaurant",
    "target_audience": "Youth 18-30",
    "offer": "Burger + Fries for 29 QAR",
    "location": "Doha"
}


# ==========================================
# STEP 2 — VALIDATION
# ==========================================

def validate_input(data):
    for key, value in data.items():
        if not value:
            raise ValueError(f"Missing value for: {key}")
    return True


# ==========================================
# STEP 3 — STRATEGY ENGINE (Dynamic Rules)
# ==========================================

def detect_tone(restaurant_type):
    restaurant_type = restaurant_type.lower()

    if "luxury" in restaurant_type or "steak" in restaurant_type:
        return "Premium & Exclusive"
    elif "shawarma" in restaurant_type:
        return "Affordable & Fast"
    elif "cafe" in restaurant_type:
        return "Cozy & Social"
    elif "burger" in restaurant_type:
        return "Trendy & Youth Focused"
    else:
        return "General Mass Market"


def generate_strategy(data):
    tone = detect_tone(data["type"])

    return f"""
STRATEGY REPORT
---------------
Restaurant: {data['name']}
Location: {data['location']}

Target Audience: {data['target_audience']}
Offer: {data['offer']}
Brand Tone: {tone}

Marketing Plan:
- Focus messaging around {tone} positioning
- Use Instagram Reels as primary channel
- Promote limited-time urgency
- Encourage user-generated content
"""


# ==========================================
# STEP 4 — POSTER ENGINE
# ==========================================

def generate_poster(data):
    headline = f"Experience the Best {data['type']} in {data['location']}!"

    return {
        "headline": headline,
        "offer": data["offer"],
        "cta": "Order Now!",
        "design_prompt": f"High-end food photography of {data['type']}, dramatic lighting, professional ad style"
    }


# ==========================================
# STEP 5 — VIDEO SCRIPT ENGINE
# ==========================================

def generate_video_script(data):
    return f"""
VIDEO SCRIPT
------------
HOOK (3 sec):
"Looking for the best {data['type']} in {data['location']}?"

Scene 2:
Show close-up cinematic food shots.

Scene 3:
Highlight offer: {data['offer']}

Scene 4:
Call to action:
Visit {data['name']} today!
"""


# ==========================================
# STEP 6 — ANALYTICS ENGINE
# ==========================================

def calculate_metrics(views, interactions, sales):
    if views <= 0:
        raise ValueError("Views must be greater than zero")

    engagement_rate = (interactions / views) * 100
    conversion_rate = (sales / views) * 100

    return {
        "engagement_rate (%)": round(engagement_rate, 2),
        "conversion_rate (%)": round(conversion_rate, 2)
    }


# ==========================================
# STEP 7 — FULL PIPELINE EXECUTION
# ==========================================

start_time = time.time()

try:
    validate_input(restaurant)
    print("Input validation passed ✅\n")
except ValueError as e:
    print("Validation Error:", e)
    exit()

strategy = generate_strategy(restaurant)
poster = generate_poster(restaurant)
video = generate_video_script(restaurant)
metrics = calculate_metrics(10000, 150, 8)

print(strategy)
print("POSTER OUTPUT:", poster, "\n")
print(video)
print("ANALYTICS:", metrics)

end_time = time.time()

print("\nExecution Time:", round(end_time - start_time, 2), "seconds")
print("\n=== V1 PIPELINE COMPLETED SUCCESSFULLY 🚀 ===")