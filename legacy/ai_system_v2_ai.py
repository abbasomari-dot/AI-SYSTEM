# ==========================================
# AI MARKETING SYSTEM - V2 (REAL AI ENGINE)
# ==========================================

import os
import time
from openai import OpenAI

print("\n=== AI MARKETING SYSTEM V2 STARTED ===\n")

# ==========================================
# LOAD API KEY FROM ENVIRONMENT
# ==========================================

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it using setx command.")

client = OpenAI(api_key=api_key)

# ==========================================
# TEST RESTAURANT DATA
# ==========================================

restaurant = {
    "name": "Burger Zone",
    "type": "Burger Restaurant",
    "target_audience": "Youth 18-30",
    "offer": "Burger + Fries for 29 QAR",
    "location": "Doha"
}

# ==========================================
# AI MARKETING GENERATOR
# ==========================================

def generate_ai_marketing_plan(data):

    prompt = f"""
You are a professional restaurant marketing strategist.

Create a full marketing campaign for:

Restaurant Name: {data['name']}
Type: {data['type']}
Target Audience: {data['target_audience']}
Offer: {data['offer']}
Location: {data['location']}

Provide:

1) Marketing Strategy (positioning + tone)
2) Instagram Reel idea (30-second script)
3) Poster headline + CTA
4) Suggested ad budget strategy
5) Key KPIs to track

Make it specific, professional, and tailored to this restaurant.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert restaurant marketing strategist."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


# ==========================================
# EXECUTION
# ==========================================

start_time = time.time()

try:
    result = generate_ai_marketing_plan(restaurant)
    print(result)
except Exception as e:
    print("Error:", e)

end_time = time.time()

print("\nExecution Time:", round(end_time - start_time, 2), "seconds")
print("\n=== AI V2 COMPLETED 🚀 ===")