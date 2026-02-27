print("=== STEP 2: STRATEGY GENERATOR ===\n")

restaurant = {
    "name": "Burger Zone",
    "type": "Burger Restaurant",
    "target_audience": "Youth 18-30",
    "offer": "Burger + Fries for 29 QAR",
    "location": "Doha"
}

def generate_strategy(data):
    if "Luxury" in data["type"]:
        tone = "Premium & Exclusive"
    elif "Shawarma" in data["type"]:
        tone = "Affordable & Fast"
    else:
        tone = "Trendy & Youth Focused"

    return f"""
Strategy for {data['name']}
Tone: {tone}
Target: {data['target_audience']}
Main Offer: {data['offer']}
Marketing Channel: Instagram Reels
"""

strategy = generate_strategy(restaurant)
print(strategy)