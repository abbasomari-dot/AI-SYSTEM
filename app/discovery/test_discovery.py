from app.discovery.google_places_collector import GooglePlacesCollector
from app.discovery.opportunity_scorer import OpportunityScorer
from app.social.social_audit_engine import SocialAuditEngine
from app.discovery.insight_engine import InsightEngine


def run_test():
    print("Collecting businesses...")

    collector = GooglePlacesCollector()
    businesses = collector.collect("restaurant Doha")

    print(f"Collected {len(businesses)} businesses")

    scorer = OpportunityScorer(businesses)
    ranked = scorer.score()

    social_engine = SocialAuditEngine()
    insight_engine = InsightEngine()

    print("\nTop 5 With Insight Engine:\n")

    for b in ranked[:5]:
        details = collector.get_place_details(b["place_id"])
        website = details.get("website")

        social_result = social_engine.analyze_from_website(website)

        # attach social_status to business for insight layer
        b["social_status"] = social_result["social_status"]

        insight = insight_engine.generate(b)

        print(
            f"{b['rank']} | {b['name']}\n"
            f"  Score: {b['opportunity_score']} | Label: {b['opportunity_label']}\n"
            f"  Social: {social_result['social_status']}\n"
            f"  Lead Tier: {insight['lead_tier']}\n"
            f"  Core Problem: {insight['core_problem']}\n"
            f"  Recommended Focus: {insight['recommended_focus']}\n"
        )


if __name__ == "__main__":
    run_test()