class CreativeAgent:

    def run(self, data):

        return {
            **data,
            "creative": {
                "reel_hook": f"Discover why {data['name']} is becoming a favorite in {data['location']}!",
                "reel_script": f"Showcase the unique value of {data['offer']} targeting {data['target_audience']}.",
                "poster_headline": f"Experience the Best {data['type']} in {data['location']}!",
                "poster_cta": "Visit Today & Taste the Difference!"
            }
        }