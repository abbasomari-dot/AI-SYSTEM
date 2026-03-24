class RevenueEngine:

    def estimate_revenue(self, rating, reviews, lead_tier):

        # base customers estimate
        monthly_customers = reviews * 0.3

        # average order value (QAR)
        if lead_tier == "high":
            aov = 180
        elif lead_tier == "medium":
            aov = 90
        else:
            aov = 45

        current_revenue = monthly_customers * aov

        # growth multiplier
        if rating >= 4.5:
            growth_factor = 1.25
        elif rating >= 4.0:
            growth_factor = 1.15
        else:
            growth_factor = 1.1

        projected_revenue = current_revenue * growth_factor

        increase = projected_revenue - current_revenue

        return {
            "current_revenue": int(current_revenue),
            "projected_revenue": int(projected_revenue),
            "increase": int(increase)
        }