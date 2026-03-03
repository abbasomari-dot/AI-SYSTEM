from typing import Dict


class InsightEngine:
    """
    Rule-Based Insight Layer (V4.2)
    Converts scores into structured business insight.
    """

    def generate(self, business: Dict) -> Dict:
        opportunity_score = business.get("opportunity_score", 0)
        opportunity_label = business.get("opportunity_label", "Low")
        social_status = business.get("social_status", "Missing")
        rating = business.get("rating", 0)
        reviews = business.get("reviews", 0)

        lead_tier = self._classify_lead_tier(opportunity_score, opportunity_label)
        core_problem = self._identify_core_problem(opportunity_label, social_status)
        recommended_focus = self._recommend_focus(lead_tier, social_status)

        return {
            "lead_tier": lead_tier,
            "core_problem": core_problem,
            "recommended_focus": recommended_focus,
            "rating": rating,
            "reviews": reviews,
        }

    def _classify_lead_tier(self, score: float, label: str) -> str:
        if label == "High":
            return "Tier A - High Growth Potential"
        elif label == "Medium":
            return "Tier B - Moderate Growth Potential"
        else:
            return "Tier C - Low Priority"

    def _identify_core_problem(self, label: str, social_status: str) -> str:
        if label == "High" and social_status == "Missing":
            return "Strong reputation but weak digital presence"

        if label == "Medium" and social_status == "Missing":
            return "Untapped digital amplification opportunity"

        if social_status == "Strong":
            return "Digital presence exists but growth optimization needed"

        return "Limited strategic opportunity at this stage"

    def _recommend_focus(self, lead_tier: str, social_status: str) -> str:
        if lead_tier.startswith("Tier A"):
            return "Visibility Expansion + Strategic Content Positioning"

        if lead_tier.startswith("Tier B"):
            return "Structured Digital Growth Strategy"

        return "Low acquisition priority"