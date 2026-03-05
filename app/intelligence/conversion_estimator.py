# app/creative/conversion_estimator.py


class ConversionEstimator:

    MAX_THEORETICAL_SCORE = 170

    def estimate(self, score_data: dict) -> dict:

        total_score = score_data["total_score"]

        probability = (total_score / self.MAX_THEORETICAL_SCORE) * 100
        probability = round(min(probability, 100), 1)

        if probability >= 75:
            tier = "High Conversion"
            recommendation = "Scale Immediately"
        elif probability >= 50:
            tier = "Strong Potential"
            recommendation = "Run A/B Test"
        elif probability >= 30:
            tier = "Moderate"
            recommendation = "Optimize Hooks"
        else:
            tier = "Weak"
            recommendation = "Rework Offer"

        return {
            "conversion_probability_percent": probability,
            "performance_tier": tier,
            "recommendation": recommendation
        }