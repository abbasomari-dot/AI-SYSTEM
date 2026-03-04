from dataclasses import dataclass
from app.growth.strategy_engine import StrategyOutput
from app.growth.revenue.offer_generator import Offer
from app.growth.revenue.angle_generator import Angle


@dataclass
class Proposal:
    title: str
    executive_pitch: str
    problem_diagnosis: str
    proposed_solution: str
    investment: str
    financial_section: str
    closing_statement: str


class ProposalBuilder:

    @staticmethod
    def build(
        strategy: StrategyOutput,
        offer: Offer,
        angle: Angle,
        revenue_impact,
        selected_package
    ) -> Proposal:

        title = ProposalBuilder._build_title(offer)
        executive_pitch = ProposalBuilder._build_executive_pitch(angle)
        problem_diagnosis = ProposalBuilder._build_problem_section(strategy)
        proposed_solution = ProposalBuilder._build_solution_section(offer)
        investment = ProposalBuilder._build_investment_section(selected_package)
        financial_section = ProposalBuilder._build_financial_section(
            revenue_impact,
            selected_package
        )
        closing_statement = ProposalBuilder._build_closing(angle)

        return Proposal(
            title=title,
            executive_pitch=executive_pitch,
            problem_diagnosis=problem_diagnosis,
            proposed_solution=proposed_solution,
            investment=investment,
            financial_section=financial_section,
            closing_statement=closing_statement
        )

    # ---------------------------
    # Title
    # ---------------------------

    @staticmethod
    def _build_title(offer: Offer) -> str:
        return f"{offer.offer_type} – Strategic Growth Proposal"

    # ---------------------------
    # Executive Pitch
    # ---------------------------

    @staticmethod
    def _build_executive_pitch(angle: Angle) -> str:
        return (
            f"{angle.primary_angle}. "
            f"This initiative is designed around {angle.core_hook.lower()}."
        )

    # ---------------------------
    # Problem Diagnosis
    # ---------------------------

    @staticmethod
    def _build_problem_section(strategy: StrategyOutput) -> str:
        return (
            f"Based on our analysis, the business currently requires a "
            f"{strategy.strategic_direction.lower()} strategy, "
            f"with emphasis on {strategy.growth_focus.lower()}."
        )

    # ---------------------------
    # Proposed Solution
    # ---------------------------

    @staticmethod
    def _build_solution_section(offer: Offer) -> str:
        return (
            f"We recommend implementing the {offer.offer_type}. "
            f"This program includes:\n\n"
            f"{offer.offer_structure}"
        )

    # ---------------------------
    # Investment Section
    # ---------------------------

    @staticmethod
    def _build_investment_section(selected_package) -> str:
        return (
            f"Selected Package: {selected_package.name}\n"
            f"Investment Range: {selected_package.price_range}"
        )

    # ---------------------------
    # Financial ROI Section
    # ---------------------------

    @staticmethod
    def _build_financial_section(revenue_impact, selected_package) -> str:

        annual_gain = revenue_impact.yearly_increase
        monthly_gain = revenue_impact.monthly_increase

        annual_investment = ProposalBuilder._extract_annual_investment(
            selected_package.price_range
        )

        net_gain = annual_gain - annual_investment

        if annual_investment > 0:
            roi_percentage = (net_gain / annual_investment) * 100
            payback_months = (
                annual_investment / monthly_gain
                if monthly_gain > 0 else 0
            )
        else:
            roi_percentage = 0
            payback_months = 0

        return (
            f"Estimated Annual Revenue Increase: ${annual_gain:,.0f}\n"
            f"Estimated Annual Investment: ${annual_investment:,.0f}\n"
            f"Net Positive Value: ${net_gain:,.0f}\n"
            f"ROI: {roi_percentage:,.0f}%\n"
            f"Estimated Payback Period: {payback_months:,.1f} months"
        )

    # ---------------------------
    # Closing
    # ---------------------------

    @staticmethod
    def _build_closing(angle: Angle) -> str:
        return (
            f"This proposal positions your business for "
            f"{angle.positioning_statement.lower()}. "
            f"Based on the projected financial impact, this investment "
            f"is structured to generate measurable and scalable growth."
        )

    # ---------------------------
    # Helper: Extract Investment
    # ---------------------------

    @staticmethod
    def _extract_annual_investment(price_range: str) -> float:
        try:
            monthly_price = price_range.split("–")[0]
            monthly_price = monthly_price.replace("$", "").replace(",", "").strip()
            monthly_price = float(monthly_price)
            return monthly_price * 12
        except:
            return 0