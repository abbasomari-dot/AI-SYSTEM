import pandas as pd
from openai import OpenAI

client = OpenAI(api_key="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")

data = pd.read_csv("ads_data.csv")

data["CPA"] = data["spend"] / data["conversions"]
data["ROAS"] = data["revenue"] / data["spend"]

summary = data.to_string()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a senior marketing strategist."},
        {"role": "user", "content": f"Analyze this campaign data and give professional recommendations:\n{summary}"}
    ]
)

print("\nAI Marketing Report:\n")
print(response.choices[0].message.content)