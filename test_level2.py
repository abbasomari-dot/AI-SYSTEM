from app.creative.sales_creative_engine import SalesCreativeEngine
from pprint import pprint


def run_test():

    engine = SalesCreativeEngine()

    creative_input = {

        "brand_name": "Doha Bites",

        "offer_name": "Ramadan Family Box",

        "original_price": 300,
        "new_price": 180,

        "platform": "instagram",

        "target_audience": "Families in Doha",

        "audience_size": 8000
    }

    result = engine.generate_multi(creative_input)

    pprint(result)


if __name__ == "__main__":
    run_test()