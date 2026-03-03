# app/growth/strategy_engine.py

from dataclasses import dataclass


@dataclass
class StrategyInput:
    lead_tier: str
    core_problem: str
    social_status: str
    rating: float
    reviews: int


@dataclass
class StrategyOutput:
    strategic_direction: str
    campaign_framework: str
    content_structure: str
    growth_focus: str


class StrategyEngine:

    @staticmethod
    def generate_strategy(data: StrategyInput) -> StrategyOutput:

        strategic_direction = StrategyEngine._determine_strategic_direction(
            data.lead_tier,
            data.rating,
            data.reviews,
            data.social_status
        )

        campaign_framework = StrategyEngine._determine_campaign_framework(
            data.core_problem
        )

        content_structure = StrategyEngine._determine_content_structure(
            data.social_status
        )

        # Base Growth Focus
        growth_focus = StrategyEngine._determine_growth_focus(
            data.lead_tier
        )

        # 🔥 Strategic Override Layer
        growth_focus = StrategyEngine._apply_strategic_override(
            strategic_direction,
            growth_focus
        )

        return StrategyOutput(
            strategic_direction=strategic_direction,
            campaign_framework=campaign_framework,
            content_structure=content_structure,
            growth_focus=growth_focus
        )

    # ---------------------------
    # Strategic Direction Logic
    # ---------------------------

    @staticmethod
    def _determine_strategic_direction(lead_tier, rating, reviews, social_status):

        if rating < 3.5:
            return "Reputation Recovery"

        if reviews < 50:
            return "Authority Building"

        if social_status == "weak":
            return "Social Activation"

        if lead_tier == "high" and rating >= 4.2:
            return "Premium Positioning"

        return "Structured Growth"

    # ---------------------------
    # Campaign Framework Logic
    # ---------------------------

    @staticmethod
    def _determine_campaign_framework(core_problem):

        mapping = {
            "low_visibility": "Awareness Campaign",
            "low_engagement": "Engagement Boost Campaign",
            "weak_branding": "Brand Identity Campaign",
            "bad_reviews": "Trust Rebuild Campaign"
        }

        return mapping.get(core_problem, "Offer Amplification Campaign")

    # ---------------------------
    # Content Structure Logic
    # ---------------------------

    @staticmethod
    def _determine_content_structure(social_status):

        mapping = {
            "no_presence": "Setup + Intro Content",
            "weak": "Consistency + Proof Content",
            "active": "Conversion-Oriented Content"
        }

        return mapping.get(social_status, "Foundational Content")

    # ---------------------------
    # Base Growth Focus Logic
    # ---------------------------

    @staticmethod
    def _determine_growth_focus(lead_tier):

        mapping = {
            "high": "Revenue Optimization",
            "mid": "Market Expansion",
            "low": "Lead Generation"
        }

        return mapping.get(lead_tier, "Balanced Growth")

    # ---------------------------
    # 🔥 Strategic Override Layer
    # ---------------------------

    @staticmethod
    def _apply_strategic_override(strategic_direction, growth_focus):

        if strategic_direction == "Reputation Recovery":
            return "Stabilization"

        if strategic_direction == "Social Activation":
            return "Foundation Building"

        return growth_focus