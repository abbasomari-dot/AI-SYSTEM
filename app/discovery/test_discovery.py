from app.discovery.google_places_collector import GooglePlacesCollector
from app.discovery.opportunity_scorer import OpportunityScorer
from app.social.social_audit_engine import SocialAuditEngine


def run_test():
    print("Collecting businesses...")

    collector = GooglePlacesCollector()
    businesses = collector.collect("restaurant Doha")

    print(f"Collected {len(businesses)} businesses")

    scorer = OpportunityScorer(businesses)
    ranked = scorer.score()

    social_engine = SocialAuditEngine()

    print("\nTop 10 With Social Detection:\n")

    for b in ranked[:10]:
        details = collector.get_place_details(b["place_id"])
        website = details.get("website")

        social_result = social_engine.analyze_from_website(website)

        print(
            f"{b['rank']} | {b['name']} | "
            f"Score: {b['opportunity_score']} | "
            f"Label: {b['opportunity_label']} | "
            f"Website: {website} | "
            f"Social Health: {social_result['social_health_score']} | "
            f"Social Status: {social_result['social_status']}"
        )


if __name__ == "__main__":
    run_test()