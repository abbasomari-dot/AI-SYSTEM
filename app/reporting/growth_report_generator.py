from dataclasses import dataclass
from typing import Dict, List


@dataclass
class GrowthReport:
    executive_summary: str
    key_insight: str
    strategic_overview: Dict[str, str]
    monthly_plan_snapshot: List[str]
    kpi_targets: Dict[str, str]
    execution_priorities: List[str]


class GrowthReportGenerator:

    @staticmethod
    def generate(
        strategy,
        plan,
        blueprint,
        rating,
        reviews
    ) -> GrowthReport:

        # ---------------------------
        # Insight
        # ---------------------------
        if reviews > 1000:
            insight = f"Strong demand with {reviews}+ reviews, indicating high market traction."
        else:
            insight = "Moderate demand with room for growth."

        # ---------------------------
        # Executive Summary
        # ---------------------------
        summary = (
            f"This business holds a {rating} rating with {reviews}+ reviews. "
            f"Strategy focuses on {strategy.strategic_direction} using {strategy.campaign_framework}."
        )

        # ---------------------------
        # Strategy Overview
        # ---------------------------
        strategic_overview = {
            "Strategic Direction": strategy.strategic_direction,
            "Campaign Framework": strategy.campaign_framework,
            "Content Structure": strategy.content_structure,
            "Growth Focus": strategy.growth_focus
        }

        # ---------------------------
        # Monthly Plan
        # ---------------------------
        monthly_plan_snapshot = plan.weekly_focus

        # ---------------------------
        # KPIs
        # ---------------------------
        kpi_targets = blueprint.kpi_targets

        # ---------------------------
        # Execution
        # ---------------------------
        execution_priorities = blueprint.daily_checklist[:5]

        return GrowthReport(
            executive_summary=summary,
            key_insight=insight,
            strategic_overview=strategic_overview,
            monthly_plan_snapshot=monthly_plan_snapshot,
            kpi_targets=kpi_targets,
            execution_priorities=execution_priorities
        )