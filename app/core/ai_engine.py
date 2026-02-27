import os
import json
from openai import OpenAI


class AIEngine:

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found.")
        self.client = OpenAI(api_key=api_key)

    def generate_marketing_plan(self, restaurant_data):

        prompt = f"""
Return ONLY valid JSON.

Structure:

{{
  "executive_summary": "",
  "strategy": {{
      "positioning": "",
      "tone": "",
      "marketing_channels": ""
  }},
  "creative": {{
      "reel_hook": "",
      "reel_script": "",
      "poster_headline": "",
      "poster_cta": ""
  }},
  "kpis": []
}}

Restaurant:
Name: {restaurant_data['name']}
Type: {restaurant_data['type']}
Target Audience: {restaurant_data['target_audience']}
Offer: {restaurant_data['offer']}
Location: {restaurant_data['location']}
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You generate structured professional marketing reports."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return json.loads(response.choices[0].message.content)