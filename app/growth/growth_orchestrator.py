# app/growth/growth_orchestrator.py

from app.growth.strategy_engine import StrategyEngine, StrategyInput
from app.growth.action_plan_generator import ActionPlanGenerator
from app.growth.execution_blueprint import ExecutionBlueprintBuilder
from app.growth.growth_report_generator import GrowthReportGenerator


class GrowthOrchestrator:

    @staticmethod
    def run(
        lead_tier: str,
        core_problem: str,
        social_status: str,
        rating: float,
        reviews: int
    ):

        # ---------------------------
        # 1️⃣ Strategy Layer
        # ---------------------------
        strategy_input = StrategyInput(
            lead_tier=lead_tier,
            core_problem=core_problem,
            social_status=social_status,
            rating=rating,
            reviews=reviews
        )

        strategy = StrategyEngine.generate_strategy(strategy_input)

        # ---------------------------
        # 2️⃣ Action Plan Layer
        # ---------------------------
        action_plan = ActionPlanGenerator.generate_plan(strategy)

        # ---------------------------
        # 3️⃣ Execution Blueprint Layer
        # ---------------------------
        blueprint = ExecutionBlueprintBuilder.build(strategy)

        # ---------------------------
        # 4️⃣ Reporting Layer
        # ---------------------------
        report = GrowthReportGenerator.generate(
            strategy=strategy,
            plan=action_plan,
            blueprint=blueprint
        )

        return report