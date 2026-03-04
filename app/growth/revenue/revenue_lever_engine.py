# app/growth/revenue/revenue_lever_engine.py

from dataclasses import dataclass
from typing import List
from app.growth.strategy_engine import StrategyOutput


@dataclass
class RevenueLeverPlan:
    primary_lever: str
    supporting_levers: List[str]
    action_steps: List[str]


class RevenueLeverEngine:

    @staticmethod
    def generate(strategy: StrategyOutput, rating: float, reviews: int) -> RevenueLeverPlan:

        primary = RevenueLeverEngine._determine_primary_lever(strategy)
        supporting = RevenueLeverEngine._determine_supporting_levers(strategy)
        steps = RevenueLeverEngine._build_action_steps(primary, rating, reviews)

        return RevenueLeverPlan(
            primary_lever=primary,
            supporting_levers=supporting,
            action_steps=steps
        )

    # ---------------------------
    # Primary Lever
    # ---------------------------

    @staticmethod
    def _determine_primary_lever(strategy: StrategyOutput) -> str:

        if strategy.growth_focus == "Revenue Optimization":
            return "Average Order Value Increase"

        if strategy.strategic_direction == "Reputation Recovery":
            return "Conversion Rate Improvement"

        if strategy.strategic_direction == "Premium Positioning":
            return "High-Ticket Upsell Strategy"

        return "Customer Frequency Increase"

    # ---------------------------
    # Supporting Levers
    # ---------------------------

    @staticmethod
    def _determine_supporting_levers(strategy: StrategyOutput) -> List[str]:

        return [
            "Bundle Offers",
            "Limited-Time Promotions",
            "Upsell Add-ons",
            "Review Highlight Campaign",
            "Loyalty Incentives"
        ]

    # ---------------------------
    # Action Steps
    # ---------------------------

    @staticmethod
    def _build_action_steps(primary: str, rating: float, reviews: int) -> List[str]:

        steps = []

        if primary == "Average Order Value Increase":
            steps.extend([
                "Create bundled offers with price advantage",
                "Introduce premium add-ons at checkout",
                "Launch limited-time combo deals"
            ])

        if primary == "Conversion Rate Improvement":
            steps.extend([
                "Improve trust signals across social platforms",
                "Highlight 5-star reviews in ads",
                "Add clear call-to-action in all campaigns"
            ])

        if primary == "High-Ticket Upsell Strategy":
            steps.extend([
                "Design premium package with exclusive benefits",
                "Position higher-tier product as best value",
                "Use comparison pricing psychology"
            ])

        if primary == "Customer Frequency Increase":
            steps.extend([
                "Launch loyalty reward system",
                "Offer return-customer discount",
                "Run reminder campaigns"
            ])

        if rating < 4:
            steps.append("Launch aggressive review acquisition campaign")

        if reviews < 200:
            steps.append("Implement review generation funnel")

        return steps