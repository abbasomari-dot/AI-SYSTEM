from dataclasses import dataclass
from app.growth.strategy_engine import StrategyOutput


@dataclass
class Offer:
    offer_type: str
    value_proposition: str
    offer_structure: str
    pricing_tier: str


class OfferGenerator:

    @staticmethod
    def generate(strategy: StrategyOutput, core_problem: str, lead_tier: str) -> Offer:

        offer_type = OfferGenerator._determine_offer_type(strategy)
        value_proposition = OfferGenerator._build_value_proposition(strategy)
        offer_structure = OfferGenerator._build_offer_structure(strategy)
        pricing_tier = OfferGenerator._determine_pricing(lead_tier)

        return Offer(
            offer_type=offer_type,
            value_proposition=value_proposition,
            offer_structure=offer_structure,
            pricing_tier=pricing_tier
        )

    # ---------------------------
    # Offer Type Logic
    # ---------------------------

    @staticmethod
    def _determine_offer_type(strategy: StrategyOutput) -> str:

        if strategy.strategic_direction == "Reputation Recovery":
            return "Reputation Recovery Program"

        if strategy.strategic_direction == "Authority Building":
            return "Authority Growth Package"

        if strategy.strategic_direction == "Premium Positioning":
            return "Premium Brand Expansion Package"

        if strategy.growth_focus == "Lead Generation":
            return "Lead Generation Accelerator"

        return "Structured Growth Program"

    # ---------------------------
    # Value Proposition Builder
    # ---------------------------

    @staticmethod
    def _build_value_proposition(strategy: StrategyOutput) -> str:

        return (
            f"We help businesses achieve {strategy.growth_focus} "
            f"through a structured {strategy.strategic_direction} approach."
        )

    # ---------------------------
    # Offer Structure Builder
    # ---------------------------

    @staticmethod
    def _build_offer_structure(strategy: StrategyOutput) -> str:

        return (
            "Phase 1: Strategic Fix & Foundation\n"
            "Phase 2: Campaign Execution\n"
            "Phase 3: Optimization & Scaling"
        )

    # ---------------------------
    # Pricing Logic
    # ---------------------------

    @staticmethod
    def _determine_pricing(lead_tier: str) -> str:

        if lead_tier == "high":
            return "High-Ticket (Premium Retainer)"

        if lead_tier == "mid":
            return "Mid-Tier Monthly Package"

        if lead_tier == "low":
            return "Starter Growth Package"

        return "Custom Pricing"