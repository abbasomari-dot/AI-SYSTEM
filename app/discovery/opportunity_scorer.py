from typing import List, Dict
from app.discovery.scoring_strategies import StrongTargetingStrategy


class OpportunityScorer:
    def __init__(self, businesses: List[Dict], strategy=None):
        self.businesses = businesses
        self.strategy = strategy or StrongTargetingStrategy()

    def _base_label(self, score: float) -> str:
        if score >= 50:
            return "High"
        elif score >= 30:
            return "Medium"
        else:
            return "Low"

    def score(self) -> List[Dict]:
        ranked = []

        for i, business in enumerate(self.businesses, start=1):
            rating = business.get("rating", 0)
            reviews = business.get("reviews", 0)

            opportunity_score = self.strategy.calculate(
                rating,
                reviews
            )

            label = self._base_label(opportunity_score)

            business["opportunity_score"] = opportunity_score
            business["rank"] = i
            business["opportunity_label"] = label

            ranked.append(business)

        return ranked