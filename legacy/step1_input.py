print("=== STEP 1: INPUT & VALIDATION ===\n")

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
    print("Input validation passed ✅")
    print(restaurant)
except ValueError as e:
    print("Validation Error:", e)