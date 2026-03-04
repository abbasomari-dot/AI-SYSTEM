# run_consultant.py

from app.business_orchestrator import BusinessOrchestrator


def print_section(title: str):
    print("\n" + "=" * 60)
    print(title.upper())
    print("=" * 60)


def main():

    print_section("Consultant Mode")

    client_name = input("Client Name: ").strip()
    lead_tier = input("Lead Tier (high/mid/low): ").strip().lower()
    core_problem = input("Core Problem: ").strip().lower()
    social_status = input("Social Status: ").strip().lower()

    rating = float(input("Current Rating: ").strip())
    reviews = int(input("Total Reviews: ").strip())

    print_section("Revenue Model Inputs")

    avg_order_value = float(input("Average Order Value ($): ").strip())
    monthly_customers = int(input("Active Monthly Customers: ").strip())
    current_frequency = float(input("Current Purchase Frequency (per month): ").strip())
    improvement_rate = float(
        input("Target Improvement % (e.g. 0.15 for 15%): ").strip()
    )

    result = BusinessOrchestrator.run(
        lead_tier=lead_tier,
        core_problem=core_problem,
        social_status=social_status,
        rating=rating,
        reviews=reviews,
        avg_order_value=avg_order_value,
        monthly_customers=monthly_customers,
        current_frequency=current_frequency,
        improvement_rate=improvement_rate
    )

    # ---------------------------
    # STRATEGIC LEVER
    # ---------------------------
    print_section("Strategic Lever")
    print(result.revenue_plan.primary_lever)

    # ---------------------------
    # REVENUE IMPACT
    # ---------------------------
    print_section("Revenue Impact Projection")
    print(f"Annual Increase (Strategic Lever): "
          f"${result.revenue_impact.yearly_increase:,.0f}")

    # ---------------------------
    # COMPARATIVE IMPACT
    # ---------------------------
    print_section("Comparative Financial Impact")

    for lever, value in result.comparative_impact.impacts.items():
        print(f"{lever}: ${value:,.0f} annually")

    print("\nHighest Financial Lever:")
    print(result.comparative_impact.best_lever)
    print(f"Estimated Annual Increase: "
          f"${result.comparative_impact.best_annual_increase:,.0f}")

    # ---------------------------
    # PROPOSAL SUMMARY
    # ---------------------------
    print_section("Proposal Summary")
    print(result.proposal.title)
    print()
    print(result.proposal.executive_pitch)

    print_section("Financial ROI Analysis")
    print(result.proposal.financial_section)

    print_section("Closing Statement")
    print(result.proposal.closing_statement)

    print("\nConsultant Execution Complete ✅")


if __name__ == "__main__":
    main()