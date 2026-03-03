# app/growth/action_plan_generator.py

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
    # Weekly Focus
    # ---------------------------

    @staticmethod
    def _determine_weekly_focus(framework: str) -> List[str]:

        mapping = {
            "Awareness Campaign": [
                "Audience targeting setup",
                "Launch awareness content",
                "Boost reach with ads",
                "Analyze visibility metrics"
            ],
            "Engagement Boost Campaign": [
                "Engagement content launch",
                "Interactive posts",
                "Community interaction",
                "Optimize engagement strategy"
            ],
            "Brand Identity Campaign": [
                "Visual identity refinement",
                "Brand story content",
                "Consistent branding rollout",
                "Brand perception review"
            ],
            "Trust Rebuild Campaign": [
                "Review response strategy",
                "Customer testimonial campaign",
                "Reputation ads",
                "Rating improvement push"
            ]
        }

        return mapping.get(framework, [
            "Offer content creation",
            "Conversion optimization",
            "Promotion launch",
            "Performance evaluation"
        ])

    # ---------------------------
    # Key Actions
    # ---------------------------

    @staticmethod
    def _determine_key_actions(strategy: StrategyOutput) -> List[str]:

        actions = []

        # Direction Based Actions
        if strategy.strategic_direction == "Reputation Recovery":
            actions.append("Respond to all negative reviews")
            actions.append("Request new reviews from happy customers")

        if strategy.strategic_direction == "Authority Building":
            actions.append("Launch review acquisition campaign")
            actions.append("Highlight customer testimonials")

        if strategy.strategic_direction == "Premium Positioning":
            actions.append("Upgrade visuals and brand assets")
            actions.append("Promote premium offers")

        # Content Structure Actions
        if strategy.content_structure == "Setup + Intro Content":
            actions.append("Create brand introduction posts")
            actions.append("Launch initial posting schedule")

        if strategy.content_structure == "Consistency + Proof Content":
            actions.append("Post case studies and proof content")
            actions.append("Establish weekly posting calendar")

        if strategy.content_structure == "Conversion-Oriented Content":
            actions.append("Create strong call-to-action posts")
            actions.append("Launch limited-time offers")

        # Growth Focus Actions
        if strategy.growth_focus == "Revenue Optimization":
            actions.append("Optimize pricing strategy")
            actions.append("Launch upsell campaigns")

        if strategy.growth_focus == "Market Expansion":
            actions.append("Target new audience segments")
            actions.append("Expand geographic reach")

        if strategy.growth_focus == "Lead Generation":
            actions.append("Run lead magnet campaign")
            actions.append("Collect customer contact data")

        return actions