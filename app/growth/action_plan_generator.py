from dataclasses import dataclass
from typing import List
from app.growth.strategy_engine import StrategyOutput


@dataclass
class ActionPlan:
    month_objective: str
    weekly_focus: List[str]
    key_actions: List[str]


class ActionPlanGenerator:

    @staticmethod
    def generate_plan(strategy: StrategyOutput) -> ActionPlan:

        month_objective = ActionPlanGenerator._determine_month_objective(
            strategy.strategic_direction
        )

        weekly_focus = ActionPlanGenerator._determine_weekly_focus(
            strategy.campaign_framework
        )

        key_actions = ActionPlanGenerator._determine_key_actions(
            strategy
        )

        return ActionPlan(
            month_objective=month_objective,
            weekly_focus=weekly_focus,
            key_actions=key_actions
        )

    # ---------------------------
    # Month Objective
    # ---------------------------

    @staticmethod
    def _determine_month_objective(direction: str) -> str:

        mapping = {
            "Reputation Recovery": "Improve public perception and raise rating",
            "Authority Building": "Increase review count and brand credibility",
            "Social Activation": "Establish consistent social presence",
            "Premium Positioning": "Strengthen high-value brand perception",
            "Structured Growth": "Stabilize and optimize marketing foundation"
        }

        return mapping.get(direction, "Build stable growth system")

    # ---------------------------
    # Weekly Focus (Dynamic)
    # ---------------------------

    @staticmethod
    def _determine_weekly_focus(framework: str) -> List[str]:

        if framework == "Offer Amplification Campaign":
            return [
                "Create irresistible limited-time offers",
                "Design high-converting promotional content",
                "Launch paid campaigns focused on offers",
                "Track conversions and optimize performance"
            ]

        if framework == "Trust Rebuild Campaign":
            return [
                "Respond to all negative reviews",
                "Improve customer experience touchpoints",
                "Encourage happy customers to leave reviews",
                "Monitor rating improvement weekly"
            ]

        if framework == "Awareness Campaign":
            return [
                "Define target audience clearly",
                "Launch reach-focused content",
                "Boost posts for visibility",
                "Track impressions and reach"
            ]

        if framework == "Engagement Boost Campaign":
            return [
                "Increase posting frequency",
                "Create interactive content (polls, questions)",
                "Engage with comments actively",
                "Track engagement rate"
            ]

        if framework == "Brand Identity Campaign":
            return [
                "Define brand visual identity",
                "Create storytelling content",
                "Align messaging across platforms",
                "Audit brand consistency"
            ]

        return ["Execute general marketing tasks"]

    # ---------------------------
    # Key Actions
    # ---------------------------

    @staticmethod
    def _determine_key_actions(strategy: StrategyOutput) -> List[str]:

        return [
            "Define campaign objectives",
            "Prepare content calendar",
            "Launch campaigns",
            "Track performance metrics"
        ]