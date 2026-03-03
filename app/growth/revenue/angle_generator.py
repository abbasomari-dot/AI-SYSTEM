from dataclasses import dataclass
from app.growth.strategy_engine import StrategyOutput
from app.growth.revenue.offer_generator import Offer


@dataclass
class Angle:
    primary_angle: str
    emotional_trigger: str
    core_hook: str
    positioning_statement: str


class AngleGenerator:

    @staticmethod
    def generate(strategy: StrategyOutput, offer: Offer) -> Angle:

        primary_angle = AngleGenerator._determine_primary_angle(strategy)
        emotional_trigger = AngleGenerator._determine_emotional_trigger(strategy)
        core_hook = AngleGenerator._build_core_hook(strategy)
        positioning_statement = AngleGenerator._build_positioning(strategy, offer)

        return Angle(
            primary_angle=primary_angle,
            emotional_trigger=emotional_trigger,
            core_hook=core_hook,
            positioning_statement=positioning_statement
        )

    # ---------------------------
    # Primary Angle Logic
    # ---------------------------

    @staticmethod
    def _determine_primary_angle(strategy: StrategyOutput) -> str:

        if strategy.strategic_direction == "Reputation Recovery":
            return "Restore Trust & Protect Brand Image"

        if strategy.strategic_direction == "Authority Building":
            return "Dominate Local Market Authority"

        if strategy.strategic_direction == "Premium Positioning":
            return "Elevate to Premium Market Status"

        if strategy.growth_focus == "Lead Generation":
            return "Turn Visibility into Qualified Leads"

        return "Structured Growth & Scalable Results"

    # ---------------------------
    # Emotional Trigger Logic
    # ---------------------------

    @staticmethod
    def _determine_emotional_trigger(strategy: StrategyOutput) -> str:

        if strategy.strategic_direction == "Reputation Recovery":
            return "Fear of losing customers"

        if strategy.strategic_direction == "Authority Building":
            return "Desire to be the #1 choice"

        if strategy.strategic_direction == "Premium Positioning":
            return "Prestige & exclusivity"

        if strategy.growth_focus == "Lead Generation":
            return "Consistent pipeline security"

        return "Business stability & control"

    # ---------------------------
    # Core Hook Builder
    # ---------------------------

    @staticmethod
    def _build_core_hook(strategy: StrategyOutput) -> str:

        return (
            f"A focused {strategy.strategic_direction} system "
            f"designed to drive {strategy.growth_focus} in 90 days."
        )

    # ---------------------------
    # Positioning Statement
    # ---------------------------

    @staticmethod
    def _build_positioning(strategy: StrategyOutput, offer: Offer) -> str:

        return (
            f"Our {offer.offer_type} is built specifically for businesses "
            f"needing {strategy.strategic_direction.lower()}, "
            f"with a direct focus on {strategy.growth_focus.lower()}."
        )