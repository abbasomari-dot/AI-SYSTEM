# run_consultant.py

import os
import json
from datetime import datetime

from app.business_orchestrator import BusinessOrchestrator


def print_section(title: str):
    print("\n" + "=" * 60)
    print(title.upper())
    print("=" * 60)


def save_output(client_name: str, result):

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = f"clients/{client_name}_{timestamp}"

    os.makedirs(folder_name, exist_ok=True)

    # ---------------------------
    # Save Growth Report
    # ---------------------------
    report_data = {
        "executive_summary": result.growth_report.executive_summary,
        "strategic_overview": result.growth_report.strategic_overview,
        "monthly_plan_snapshot": result.growth_report.monthly_plan_snapshot,
        "kpi_targets": result.growth_report.kpi_targets,
        "execution_priorities": result.growth_report.execution_priorities,
    }

    with open(f"{folder_name}/growth_report.json", "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4)

    # ---------------------------
    # Save Proposal (TXT)
    # ---------------------------
    proposal_text = (
        f"{result.proposal.title}\n\n"
        f"{result.proposal.executive_pitch}\n\n"
        f"{result.proposal.problem_diagnosis}\n\n"
        f"{result.proposal.proposed_solution}\n\n"
        f"{result.proposal.investment}\n\n"
        f"{result.proposal.closing_statement}"
    )

    with open(f"{folder_name}/proposal.txt", "w", encoding="utf-8") as f:
        f.write(proposal_text)

    # ---------------------------
    # Save Outreach
    # ---------------------------
    outreach_text = (
        f"=== COLD DM ===\n\n{result.outreach.cold_dm}\n\n"
        f"=== FOLLOW UP ===\n\n{result.outreach.follow_up}\n\n"
        f"=== EMAIL ===\n\n{result.outreach.email_pitch}\n\n"
        f"=== CALL SCRIPT ===\n\n{result.outreach.call_script}"
    )

    with open(f"{folder_name}/outreach.txt", "w", encoding="utf-8") as f:
        f.write(outreach_text)

    print(f"\nAll files saved in: {folder_name}")


def main():

    print_section("Consultant Mode")

    client_name = input("Client Name: ").strip().replace(" ", "_")

    lead_tier = input("Lead Tier (high/mid/low): ").strip().lower()
    core_problem = input(
        "Core Problem (low_visibility / low_engagement / weak_branding / bad_reviews): "
    ).strip().lower()
    social_status = input(
        "Social Status (no_presence / weak / active): "
    ).strip().lower()

    try:
        rating = float(input("Current Rating: ").strip())
        reviews = int(input("Total Reviews: ").strip())
    except ValueError:
        print("Invalid numeric input.")
        return

    result = BusinessOrchestrator.run(
        lead_tier=lead_tier,
        core_problem=core_problem,
        social_status=social_status,
        rating=rating,
        reviews=reviews
    )

    print_section("Strategic Direction")
    print(result.growth_report.strategic_overview["Strategic Direction"])

    print_section("Offer")
    print(result.offer.offer_type)

    print_section("Primary Angle")
    print(result.angle.primary_angle)

    save_output(client_name, result)

    print("\nConsultant Execution Complete ✅")


if __name__ == "__main__":
    main()