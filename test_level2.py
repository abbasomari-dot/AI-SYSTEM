from app.creative.sales_creative_engine import CreativeEngine
import pprint

def run_test():

    engine = CreativeEngine()

    creative_input = {
        "offer_name": "Ramadan Family Box",
        "brand_name": "Doha Bites",
        "original_price": 300,
        "new_price": 270,
        "platform": "instagram",
        "target_audience": "Families in Doha",
        "audience_size": 20000,
        "expected_reach_percent": 40
    }

    result = engine.generate_multi(creative_input)

    pprint.pprint(result)


if __name__ == "__main__":
    run_test()