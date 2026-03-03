# app/reporting/growth_report_generator.py

from dataclasses import dataclass
from typing import Dict, List
from app.growth.strategy_engine import StrategyOutput
from app.growth.action_plan_generator import ActionPlan
from app.growth.execution_blueprint import ExecutionBlueprint


@dataclass
class GrowthReport:
    executive_summary: str
    strategic_overview: Dict[str, str]
    monthly_plan_snapshot: List[str]
    kpi_targets: Dict[str, str]
    execution_priorities: List[str]


class GrowthReportGenerator:

    @staticmethod
    def generate(
        strategy: StrategyOutput,
        plan: ActionPlan,
        blueprint: ExecutionBlueprint
    ) -> GrowthReport:

        executive_summary = GrowthReportGenerator._build_executive_summary(
            strategy
        )

        strategic_overview = {
            "Strategic Direction": strategy.strategic_direction,
            "Campaign Framework": strategy.campaign_framework,
            "Content Structure": strategy.content_structure,
            "Growth Focus": strategy.growth_focus
        }

        monthly_plan_snapshot = plan.weekly_focus

        kpi_targets = blueprint.kpi_targets

        execution_priorities = GrowthReportGenerator._build_execution_priorities(
            blueprint.daily_checklist
        )

        return GrowthReport(
            executive_summary=executive_summary,
            strategic_overview=strategic_overview,
            monthly_plan_snapshot=monthly_plan_snapshot,
            kpi_targets=kpi_targets,
            execution_priorities=execution_priorities
        )

    # ---------------------------
    # Executive Summary
    # ---------------------------

    @staticmethod
    def _build_executive_summary(strategy: StrategyOutput) -> str:

        return (
            f"The business requires a '{strategy.strategic_direction}' approach. "
            f"The primary campaign framework will focus on '{strategy.campaign_framework}'. "
            f"Content will follow a '{strategy.content_structure}' model, "
            f"with growth efforts centered on '{strategy.growth_focus}'."
        )

    # ---------------------------
    # Execution Priorities
    # ---------------------------

    @staticmethod
    def _build_execution_priorities(daily_checklist: List[str]) -> List[str]:

        # أول 5 عناصر نعتبرها أولويات تشغيلية
        return daily_checklist[:5]