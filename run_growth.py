# run_growth.py

from app.growth.growth_orchestrator import GrowthOrchestrator
from app.services.pdf_report_builder import PDFReportBuilder
from app.discovery.google_places_collector import GooglePlacesCollector
import os


def print_section(title: str):
    print("\n" + "=" * 60)
    print(f"{title.upper()}")
    print("=" * 60)


def main():

    print_section("Growth Brain CLI")

    # Inputs
    lead_tier = input("Lead Tier (high/mid/low): ").strip().lower()
    core_problem = input(
        "Core Problem (low_visibility / low_engagement / weak_branding / bad_reviews): "
    ).strip().lower()
    social_status = input(
        "Social Status (no_presence / weak / active): "
    ).strip().lower()

    # ---------------------------
    # ✅ Google Places Input
    # ---------------------------

    place_name = input("Restaurant Name: ").strip()

    data = GooglePlacesCollector.get_place_details(place_name)

    rating = data["rating"]
    reviews = data["reviews"]

    print(f"\n📊 Found: Rating={rating}, Reviews={reviews}")

    # ---------------------------
    # Run System
    # ---------------------------

    report = GrowthOrchestrator.run(
        lead_tier=lead_tier,
        core_problem=core_problem,
        social_status=social_status,
        rating=rating,
        reviews=reviews
    )

    # ---------------------------
    # Print Output
    # ---------------------------

    print_section("Executive Summary")
    print(report.executive_summary)

    print_section("Key Insight")
    print(report.key_insight)

    print_section("Strategic Overview")
    for k, v in report.strategic_overview.items():
        print(f"{k}: {v}")

    print_section("30-Day Plan Snapshot")
    for i, week in enumerate(report.monthly_plan_snapshot, 1):
        print(f"Week {i}: {week}")

    print_section("KPI Targets")
    for k, v in report.kpi_targets.items():
        print(f"{k}: {v}")

    print_section("Execution Priorities")
    for task in report.execution_priorities:
        print(f"- {task}")

    # ---------------------------
    # ✅ Generate PDF
    # ---------------------------

    os.makedirs("clients", exist_ok=True)

    safe_name = place_name.replace(" ", "_")

    pdf_data = {
        "rating": rating,
        "reviews": reviews,
        "recommendation": report.executive_summary,
        "primary_lever": report.strategic_overview["Strategic Direction"],
        "campaign_type": report.strategic_overview["Campaign Framework"],
        "offer_strategy": report.strategic_overview["Content Structure"],
        "month1": report.monthly_plan_snapshot[0],
        "month2": report.monthly_plan_snapshot[1],
        "month3": report.monthly_plan_snapshot[2],
        "insight": report.key_insight
    }

    pdf = PDFReportBuilder(safe_name, pdf_data)
    file_path = pdf.build()

    print("\n✅ PDF Generated:", os.path.abspath(file_path))


if __name__ == "__main__":
    main()