# run_scenarios.py

from app.growth.growth_orchestrator import GrowthOrchestrator


SCENARIOS = [
    {
        "name": "Low Reviews – High Potential",
        "lead_tier": "high",
        "core_problem": "low_visibility",
        "social_status": "weak",
        "rating": 4.3,
        "reviews": 20,
    },
    {
        "name": "Bad Reputation Case",
        "lead_tier": "mid",
        "core_problem": "bad_reviews",
        "social_status": "active",
        "rating": 3.2,
        "reviews": 120,
    },
    {
        "name": "No Social Presence",
        "lead_tier": "low",
        "core_problem": "weak_branding",
        "social_status": "no_presence",
        "rating": 4.0,
        "reviews": 60,
    },
    {
        "name": "Premium Brand Ready",
        "lead_tier": "high",
        "core_problem": "low_engagement",
        "social_status": "active",
        "rating": 4.6,
        "reviews": 300,
    },
]


def print_divider():
    print("\n" + "=" * 70)


def run_scenarios():
    print_divider()
    print("GROWTH BRAIN — SCENARIO TEST MODE")
    print_divider()

    for scenario in SCENARIOS:
        print_divider()
        print(f"Scenario: {scenario['name']}")
        print_divider()

        report = GrowthOrchestrator.run(
            lead_tier=scenario["lead_tier"],
            core_problem=scenario["core_problem"],
            social_status=scenario["social_status"],
            rating=scenario["rating"],
            reviews=scenario["reviews"],
        )

        print("Strategic Direction:", report.strategic_overview["Strategic Direction"])
        print("Growth Focus:", report.strategic_overview["Growth Focus"])
        print("KPIs:", list(report.kpi_targets.keys()))

    print_divider()
    print("Scenario Testing Complete ✅")
    print_divider()


if __name__ == "__main__":
    run_scenarios()