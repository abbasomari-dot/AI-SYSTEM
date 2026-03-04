# app/creative/strategy_scoring.py


class StrategyScorer:

    STRENGTH_WEIGHTS = {
        "aggressive": 40,
        "strong": 30,
        "moderate": 20,
        "weak": 10
    }

    ANGLE_WEIGHTS = {
        "price_shock": 30,
        "urgency_attack": 25,
        "market_domination": 22,
        "smart_savings": 20,
        "comparison": 18,
        "testimonial": 18,
        "bonus_angle": 15,
        "limited_upgrade": 15,
        "value_focus": 12,
        "benefit_focus": 10
    }

    def score(self, strategy: dict) -> dict:

        strength = strategy["offer_strength"]
        angle = strategy["sales_angle"]
        discount = strategy["discount_percentage"]

        strength_score = self.STRENGTH_WEIGHTS.get(strength, 0)
        angle_score = self.ANGLE_WEIGHTS.get(angle, 0)

        total_score = strength_score + angle_score + discount

        return {
            "strength_score": strength_score,
            "angle_score": angle_score,
            "discount_score": discount,
            "total_score": round(total_score, 1)
        }