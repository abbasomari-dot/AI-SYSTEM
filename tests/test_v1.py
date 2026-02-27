# ==============================
# AI MARKETING SYSTEM - V1 TEST
# ==============================

print("=== AI SYSTEM V1 STARTED ===\n")

# ------------------------------
# STEP 1: INPUT DATA
# ------------------------------

restaurant = {
    "name": "Burger Zone",
    "type": "Burger Restaurant",
    "target_audience": "Youth 18-30",
    "offer": "Burger + Fries for 29 QAR",
    "location": "Doha"
}

def validate_input(data):
    for key, value in data.items():
        if not value:
            raise ValueError(f"Missing value for: {key}")
    return True

try:
    validate_input(restaurant)
    print("Input validation passed ✅\n")
except ValueError as e:
    print("Input Error:", e)
    exit()


# ------------------------------
# STEP 2: STRATEGY GENERATOR
# ------------------------------

def generate_strategy(data):
    return f"""
Marketing Strategy for {data['name']}

Target Audience: {data['target_audience']}
Offer: {data['offer']}

Strategy:
- Focus on {data['type']} lovers
- Promote via Instagram Reels
- Highlight affordability & quality
- Use urgency marketing

Content Plan:
- 3 Reels weekly
- 2 Story promotions
"""


# ------------------------------
# STEP 3: POSTER GENERATOR
# ------------------------------

def generate_poster(data):
    return {
        "headline": f"Best {data['type']} in {data['location']}!",
        "offer_text": data["offer"],
        "cta": "Order Now!",
        "design_prompt": f"Modern {data['type']} ad, vibrant colors, close-up food, trendy style"
    }


# ------------------------------
# STEP 4: VIDEO SCRIPT GENERATOR
# ------------------------------

def generate_video_script(data):
    return f"""
Scene 1 (Hook):
"Stop scrolling! Craving the best {data['type']}?"

Scene 2:
Show delicious food close-up.

Scene 3:
Highlight offer: {data['offer']}

Scene 4:
Visit {data['name']} today in {data['location']}!
"""


# ------------------------------
# STEP 5: ANALYTICS CALCULATION
# ------------------------------

def calculate_metrics(views, interactions, sales):
    if views == 0:
        return {"error": "Views cannot be zero"}

    engagement_rate = (interactions / views) * 100
    conversion_rate = (sales / views) * 100

    return {
        "engagement_rate": round(engagement_rate, 2),
        "conversion_rate": round(conversion_rate, 2)
    }


# ------------------------------
# STEP 6: FULL PIPELINE EXECUTION
# ------------------------------

strategy = generate_strategy(restaurant)
poster = generate_poster(restaurant)
video = generate_video_script(restaurant)
metrics = calculate_metrics(10000, 150, 8)

print("=== STRATEGY ===")
print(strategy)

print("=== POSTER ===")
print(poster)

print("=== VIDEO SCRIPT ===")
print(video)

print("=== METRICS ===")
print(metrics)

print("\n=== V1 TEST COMPLETED SUCCESSFULLY 🚀 ===")