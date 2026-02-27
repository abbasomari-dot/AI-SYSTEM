from app.core.ai_engine import AIEngine


class BrandDiagnosticAgent:

    def __init__(self):
        self.ai = AIEngine()

    def run(self, restaurant_data):

        prompt_data = {
            "name": restaurant_data["name"],
            "type": restaurant_data["type"],
            "target_audience": restaurant_data["target_audience"],
            "offer": restaurant_data["offer"],
            "location": restaurant_data["location"]
        }

        result = self.ai.generate_marketing_plan(prompt_data)

        return result