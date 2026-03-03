# app/growth/execution_blueprint.py

from dataclasses import dataclass
from typing import List, Dict
from app.growth.strategy_engine import StrategyOutput


@dataclass
class ExecutionBlueprint:
    daily_checklist: List[str]
    kpi_targets: Dict[str, str]
    measurable_metrics: List[str]


class ExecutionBlueprintBuilder:

    @staticmethod
    def build(strategy: StrategyOutput) -> ExecutionBlueprint:

        daily_checklist = ExecutionBlueprintBuilder._build_daily_checklist(strategy)
        kpi_targets = ExecutionBlueprintBuilder._define_kpi_targets(strategy)
        measurable_metrics = ExecutionBlueprintBuilder._define_measurable_metrics(strategy)

        return ExecutionBlueprint(
            daily_checklist=daily_checklist,
            kpi_targets=kpi_targets,
            measurable_metrics=measurable_metrics
        )

    # ---------------------------
    # Daily Execution Checklist
    # ---------------------------

    @staticmethod
    def _build_daily_checklist(strategy: StrategyOutput) -> List[str]:

        checklist = [
            "Check and respond to all comments and messages",
            "Publish scheduled content",
            "Monitor ad performance",
            "Track daily engagement metrics"
        ]

        if strategy.strategic_direction == "Reputation Recovery":
            checklist.append("Request at least 3 new reviews daily")
            checklist.append("Respond to all negative reviews within 24h")

        if strategy.strategic_direction == "Authority Building":
            checklist.append("Request 5 new reviews daily")
            checklist.append("Highlight one testimonial daily")

        if strategy.strategic_direction == "Premium Positioning":
            checklist.append("Promote premium offer daily")
            checklist.append("Upgrade one visual asset weekly")

        return checklist

    # ---------------------------
    # KPI Targets
    # ---------------------------

    @staticmethod
    def _define_kpi_targets(strategy: StrategyOutput) -> Dict[str, str]:

        kpis = {
            "Engagement Rate": "+20%",
            "Reach Growth": "+30%",
            "Follower Growth": "+15%"
        }

        # Strategic Direction KPIs
        if strategy.strategic_direction == "Reputation Recovery":
            kpis["Rating Improvement"] = "Reach 4.2+"
            kpis["New Reviews"] = "+50 reviews"

        if strategy.strategic_direction == "Authority Building":
            kpis["New Reviews"] = "+40 reviews"
            kpis["Review Velocity"] = "5+ per day"

        if strategy.strategic_direction == "Premium Positioning":
            kpis["Average Order Value"] = "+20%"
            kpis["High-Ticket Conversions"] = "+15%"

        # Growth Focus KPIs
        if strategy.growth_focus == "Revenue Optimization":
            kpis["Revenue Increase"] = "+25%"

        if strategy.growth_focus == "Market Expansion":
            kpis["New Audience Reach"] = "+35%"

        if strategy.growth_focus == "Lead Generation":
            kpis["Leads Collected"] = "+200 leads"

        # Strategic Override KPIs
        if strategy.growth_focus == "Stabilization":
            kpis["Negative Review Reduction"] = "-50%"
            kpis["Customer Sentiment Score"] = "Improve monthly"

        if strategy.growth_focus == "Foundation Building":
            kpis["Posting Consistency"] = "5 posts per week"
            kpis["Profile Optimization Score"] = "100%"

        return kpis

    # ---------------------------
    # Measurable Metrics
    # ---------------------------

    @staticmethod
    def _define_measurable_metrics(strategy: StrategyOutput) -> List[str]:

        metrics = [
            "Number of posts published",
            "Ad spend vs return",
            "Weekly engagement rate",
            "New followers per week"
        ]

        if strategy.strategic_direction in ["Authority Building", "Reputation Recovery"]:
            metrics.append("Number of new reviews")

        if strategy.growth_focus == "Revenue Optimization":
            metrics.append("Monthly revenue growth")

        if strategy.growth_focus == "Lead Generation":
            metrics.append("Cost per lead")

        return metrics