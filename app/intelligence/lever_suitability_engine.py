class LeverSuitabilityEngine:

    def evaluate(self, business_data, strategy):

        rating = business_data.get("rating", 4.5)
        reviews = business_data.get("reviews", 100)
        frequency = business_data.get("frequency", 1)
        angle = strategy["sales_angle"]

        suitability_score = 100
        warnings = []

        # Rating check
        if rating < 4:
            suitability_score -= 20
            warnings.append("Low rating may reduce campaign effectiveness")

        # Reviews check
        if reviews < 50:
            suitability_score -= 15
            warnings.append("Low social proof (reviews)")

        # Frequency check
        if frequency < 1:
            suitability_score -= 15
            warnings.append("Customer return frequency is low")

        # Strategy specific checks
        if angle == "market_domination" and reviews < 100:
            suitability_score -= 20
            warnings.append("Market domination angle needs stronger social proof")

        if angle == "price_shock" and rating < 4:
            suitability_score -= 10
            warnings.append("Discount campaign may not compensate weak rating")

        return {
            "suitability_score": suitability_score,
            "warnings": warnings
        }