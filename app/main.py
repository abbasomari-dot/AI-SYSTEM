from app.discovery.discovery_pipeline import DiscoveryPipeline


def main():
    print("Running Discovery Pipeline...\n")

    pipeline = DiscoveryPipeline()
    results = pipeline.run("restaurant Doha", limit=3)

    for r in results:
        print("=" * 60)
        print(f"Business: {r['name']}")
        print(f"Lead Tier: {r['lead_tier']}")
        print(f"Opportunity: {r['opportunity_score']} ({r['opportunity_label']})")
        print(f"Social Status: {r['social_status']}\n")

        print("Executive Summary:\n")
        print(r["executive_summary"])
        print("\n")


if __name__ == "__main__":
    main()