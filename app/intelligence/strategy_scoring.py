class StrategyScoring:

    def score(self, strategy):

        discount = strategy["discount_percentage"]
        strength = strategy["offer_strength"]
        angle = strategy["sales_angle"]

        score = 0

        # Discount score
        discount_score = discount
        score += discount_score

        # Offer strength score
        if strength == "aggressive":
            strength_score = 40
        elif strength == "strong":
            strength_score = 30
        elif strength == "moderate":
            strength_score = 20
        else:
            strength_score = 10

        score += strength_score

        # Angle score
        if angle == "price_shock":
            angle_score = 30
        elif angle == "urgency_attack":
            angle_score = 25
        elif angle == "market_domination":
            angle_score = 22
        elif angle == "value_offer":
            angle_score = 18
        elif angle == "smart_saver":
            angle_score = 16
        elif angle == "bonus_angle":
            angle_score = 15
        else:
            angle_score = 15

        score += angle_score

        return {
            "discount_score": discount_score,
            "strength_score": strength_score,
            "angle_score": angle_score,
            "total_score": score
        }