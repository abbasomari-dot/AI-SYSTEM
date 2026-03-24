from app.growth.strategy_engine import StrategyEngine, StrategyInput
from app.growth.action_plan_generator import ActionPlanGenerator
from app.growth.execution_blueprint import ExecutionBlueprintBuilder
from app.reporting.growth_report_generator import GrowthReportGenerator

# ✅ NEW
from app.data.instagram_finder import InstagramFinder


class GrowthOrchestrator:

    @staticmethod
    def run(
        lead_tier: str,
        core_problem: str,
        social_status: str,
        rating: float,
        reviews: int,
        name: str  # ✅ NEW
    ):

        # ---------------------------
        # Instagram Fetch (SERP)
        # ---------------------------
        finder = InstagramFinder(
            api_key="d73e7006625d69fb60e0aa7daef0da018513f08de467114fe01804a4b6e633ad"
        )

        instagram_data = finder.get_instagram_data(name)
        instagram = instagram_data["link"]

        # ---------------------------
        # Strategy Input
        # ---------------------------
        strategy_input = StrategyInput(
            lead_tier=lead_tier,
            core_problem=core_problem,
            social_status=social_status,
            rating=rating,
            reviews=reviews
        )

        # Strategy
        strategy = StrategyEngine.generate_strategy(strategy_input)

        # Action Plan
        plan = ActionPlanGenerator.generate_plan(strategy)

        # Execution Blueprint
        blueprint = ExecutionBlueprintBuilder.build(strategy)

        # ---------------------------
        # Final Report
        # ---------------------------
        report = GrowthReportGenerator.generate(
            strategy=strategy,
            plan=plan,
            blueprint=blueprint,
            rating=rating,
            reviews=reviews,
        )

        # ---------------------------
        # 🔥 Inject Instagram Insight
        # ---------------------------
        if instagram:
            report.key_insight += (
                f" The business has an active Instagram presence ({instagram}), "
                "which can be leveraged to accelerate growth through content and campaigns."
            )
        else:
            report.key_insight += (
                " The business lacks a visible Instagram presence, representing a major growth opportunity "
                "through social media activation."
            )

        return report