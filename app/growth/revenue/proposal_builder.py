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
    closing_statement: str


class ProposalBuilder:

    @staticmethod
    def build(strategy: StrategyOutput, offer: Offer, angle: Angle) -> Proposal:

        title = ProposalBuilder._build_title(offer)
        executive_pitch = ProposalBuilder._build_executive_pitch(angle)
        problem_diagnosis = ProposalBuilder._build_problem_section(strategy)
        proposed_solution = ProposalBuilder._build_solution_section(offer)
        investment = ProposalBuilder._build_investment_section(offer)
        closing_statement = ProposalBuilder._build_closing(angle)

        return Proposal(
            title=title,
            executive_pitch=executive_pitch,
            problem_diagnosis=problem_diagnosis,
            proposed_solution=proposed_solution,
            investment=investment,
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
    def _build_investment_section(offer: Offer) -> str:
        return (
            f"Recommended Investment Model: {offer.pricing_tier}."
        )

    # ---------------------------
    # Closing
    # ---------------------------

    @staticmethod
    def _build_closing(angle: Angle) -> str:
        return (
            f"This proposal positions your business for "
            f"{angle.positioning_statement.lower()}. "
            f"Let’s move forward strategically."
        )