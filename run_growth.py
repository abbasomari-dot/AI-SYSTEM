# run_growth.py

from app.growth.growth_orchestrator import GrowthOrchestrator


def print_section(title: str):
    print("\n" + "=" * 60)
    print(f"{title.upper()}")
    print("=" * 60)


def main():

    print_section("Growth Brain CLI")

    # ---------------------------
    # Collect Inputs
    # ---------------------------
    lead_tier = input("Lead Tier (high/mid/low): ").strip().lower()
    core_problem = input(
        "Core Problem (low_visibility / low_engagement / weak_branding / bad_reviews): "
    ).strip().lower()
    social_status = input(
        "Social Status (no_presence / weak / active): "
    ).strip().lower()

    try:
        rating = float(input("Current Rating (e.g., 4.1): ").strip())
        reviews = int(input("Total Reviews (e.g., 32): ").strip())
    except ValueError:
        print("Invalid rating or reviews input. Please enter numeric values.")
        return

    # ---------------------------
    # Run Growth System
    # ---------------------------
    report = GrowthOrchestrator.run(
        lead_tier=lead_tier,
        core_problem=core_problem,
        social_status=social_status,
        rating=rating,
        reviews=reviews
    )

    # ---------------------------
    # Display Report
    # ---------------------------

    print_section("Executive Summary")
    print(report.executive_summary)

    print_section("Strategic Overview")
    for key, value in report.strategic_overview.items():
        print(f"{key}: {value}")

    print_section("30-Day Plan Snapshot")
    for week, focus in enumerate(report.monthly_plan_snapshot, start=1):
        print(f"Week {week}: {focus}")

    print_section("KPI Targets")
    for kpi, target in report.kpi_targets.items():
        print(f"{kpi}: {target}")

    print_section("Execution Priorities")
    for item in report.execution_priorities:
        print(f"- {item}")

    print("\nGrowth Brain Execution Complete ✅")


if __name__ == "__main__":
    main()