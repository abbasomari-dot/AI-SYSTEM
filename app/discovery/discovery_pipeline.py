from typing import List, Dict

from app.discovery.google_places_collector import GooglePlacesCollector
from app.discovery.opportunity_scorer import OpportunityScorer
from app.social.social_audit_engine import SocialAuditEngine
from app.discovery.insight_engine import InsightEngine
from app.discovery.summary_engine import SummaryEngine


class DiscoveryPipeline:
    """
    V4.4 - Discovery Pipeline with Executive Summary
    """

    def __init__(self):
        self.collector = GooglePlacesCollector()
        self.social_engine = SocialAuditEngine()
        self.insight_engine = InsightEngine()
        self.summary_engine = SummaryEngine()

    def run(self, query: str, limit: int = 10) -> List[Dict]:

        # 1️⃣ Collect
        businesses = self.collector.collect(query)

        # 2️⃣ Score
        scorer = OpportunityScorer(businesses)
        ranked = scorer.score()

        results = []

        # 3️⃣ Process top N
        for business in ranked[:limit]:

            # Website
            details = self.collector.get_place_details(business["place_id"])
            website = details.get("website")

            # Social
            social_result = self.social_engine.analyze_from_website(website)
            business["social_status"] = social_result["social_status"]
            business["social_health_score"] = social_result["social_health_score"]

            # Insight
            insight = self.insight_engine.generate(business)

            structured = {
                "name": business.get("name"),
                "rating": business.get("rating"),
                "reviews": business.get("reviews"),
                "opportunity_score": business.get("opportunity_score"),
                "opportunity_label": business.get("opportunity_label"),
                "social_status": business.get("social_status"),
                "lead_tier": insight["lead_tier"],
                "core_problem": insight["core_problem"],
                "recommended_focus": insight["recommended_focus"],
            }

            # Executive Summary
            summary = self.summary_engine.generate(structured)
            structured["executive_summary"] = summary

            results.append(structured)

        return results