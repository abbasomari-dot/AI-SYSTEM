class RiskDetectionEngine:

    def detect(self, strategy):

        risks = []

        discount = strategy.get("discount_percentage", 0)
        strength = strategy.get("offer_strength", "")
        angle = strategy.get("sales_angle", "")

        # Risk 1: Weak discount but aggressive angle
        if discount < 15 and angle in ["price_shock", "market_domination"]:
            risks.append(
                "Weak discount may not support aggressive messaging."
            )

        # Risk 2: Moderate offer with domination claim
        if strength == "moderate" and angle == "market_domination":
            risks.append(
                "Moderate offer may struggle to dominate the market."
            )

        # Risk 3: Weak offer overall
        if strength == "weak":
            risks.append(
                "Offer strength is weak and may reduce campaign performance."
            )

        risk_score = max(0, 100 - len(risks) * 25)

        return {
            "risk_score": risk_score,
            "warnings": risks
        }