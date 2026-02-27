# ==========================================
# AI MARKETING SYSTEM V2.1 (STRUCTURED)
# ==========================================

import os
import time
import json
from openai import OpenAI

print("\n=== AI MARKETING SYSTEM V2.1 STARTED ===\n")

# Load API Key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found.")

client = OpenAI(api_key=api_key)

# Test Restaurant
restaurant = {
    "name": "Burger Zone",
    "type": "Burger Restaurant",
    "target_audience": "Youth 18-30",
    "offer": "Burger + Fries for 29 QAR",
    "location": "Doha"
}

# ==========================================
# AI GENERATOR (STRUCTURED JSON OUTPUT)
# ==========================================

def generate_ai_marketing_plan(data):

    prompt = f"""
You are a professional restaurant marketing strategist.

Return the result ONLY as valid JSON.

Structure:

{{
  "strategy": {{
      "positioning": "",
      "tone": "",
      "marketing_channels": ""
  }},
  "instagram_reel": {{
      "hook": "",
      "script": ""
  }},
  "poster": {{
      "headline": "",
      "cta": ""
  }},
  "budget_strategy": "",
  "kpis": []
}}

Restaurant Details:
Name: {data['name']}
Type: {data['type']}
Target Audience: {data['target_audience']}
Offer: {data['offer']}
Location: {data['location']}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You generate structured JSON marketing plans."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print("⚠ AI did not return valid JSON. Raw output:")
        print(content)
        return None


# ==========================================
# EXECUTION
# ==========================================

start_time = time.time()

result = generate_ai_marketing_plan(restaurant)

if result:

    print("\n=== STRATEGY ===")
    print(result["strategy"])

    print("\n=== INSTAGRAM REEL ===")
    print(result["instagram_reel"])

    print("\n=== POSTER ===")
    print(result["poster"])

    print("\n=== BUDGET STRATEGY ===")
    print(result["budget_strategy"])

    print("\n=== KPIs ===")
    for kpi in result["kpis"]:
        print("-", kpi)

end_time = time.time()

print("\nExecution Time:", round(end_time - start_time, 2), "seconds")
print("\n=== V2.1 STRUCTURED COMPLETED 🚀 ===")