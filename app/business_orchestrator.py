# app/business_orchestrator.py

from dataclasses import dataclass

from app.growth.growth_orchestrator import GrowthOrchestrator
from app.growth.strategy_engine import StrategyInput, StrategyEngine
from app.growth.revenue.offer_generator import OfferGenerator
from app.growth.revenue.angle_generator import AngleGenerator
from app.growth.revenue.proposal_builder import ProposalBuilder
from app.growth.revenue.outreach_engine import OutreachEngine
from app.growth.revenue.multi_offer_generator import MultiOfferGenerator
from app.growth.revenue.revenue_lever_engine import RevenueLeverEngine
from app.growth.revenue.revenue_impact_engine import RevenueImpactEngine
from app.growth.revenue.comparative_impact_engine import ComparativeImpactEngine


@dataclass
class BusinessOutput:
    growth_report: object
    base_offer: object
    multi_offer: object
    revenue_plan: object
    revenue_impact: object
    comparative_impact: object
    angle: object
    proposal: object
    outreach: object


class BusinessOrchestrator:

    @staticmethod
    def run(
        lead_tier: str,
        core_problem: str,
        social_status: str,
        rating: float,
        reviews: int,
        avg_order_value: float,
        monthly_customers: int,
        current_frequency: float,
        improvement_rate: float
    ) -> BusinessOutput:

        # ---------------------------
        # 1️⃣ Growth Layer
        # ---------------------------
        growth_report = GrowthOrchestrator.run(
            lead_tier=lead_tier,
            core_problem=core_problem,
            social_status=social_status,
            rating=rating,
            reviews=reviews
        )

        strategy_input = StrategyInput(
            lead_tier=lead_tier,
            core_problem=core_problem,
            social_status=social_status,
            rating=rating,
            reviews=reviews
        )

        strategy = StrategyEngine.generate_strategy(strategy_input)

        # ---------------------------
        # 2️⃣ Revenue Layer
        # ---------------------------

        base_offer = OfferGenerator.generate(strategy, core_problem, lead_tier)

        multi_offer = MultiOfferGenerator.generate(
            strategy,
            lead_tier,
            rating,
            reviews
        )

        # 🔹 نختار Premium Package افتراضيًا
        selected_package = multi_offer.premium

        revenue_plan = RevenueLeverEngine.generate(
            strategy,
            rating,
            reviews
        )

        revenue_impact = RevenueImpactEngine.calculate(
            primary_lever=revenue_plan.primary_lever,
            avg_order_value=avg_order_value,
            monthly_customers=monthly_customers,
            current_frequency=current_frequency,
            improvement_rate=improvement_rate
        )

        comparative_impact = ComparativeImpactEngine.calculate(
            avg_order_value=avg_order_value,
            monthly_customers=monthly_customers,
            current_frequency=current_frequency,
            improvement_rate=improvement_rate
        )

        angle = AngleGenerator.generate(strategy, base_offer)

        # ---------------------------
        # 3️⃣ Proposal with ROI
        # ---------------------------
        proposal = ProposalBuilder.build(
            strategy=strategy,
            offer=base_offer,
            angle=angle,
            revenue_impact=revenue_impact,
            selected_package=selected_package
        )

        outreach = OutreachEngine.generate(
            strategy,
            base_offer,
            angle,
            proposal
        )

        return BusinessOutput(
            growth_report=growth_report,
            base_offer=base_offer,
            multi_offer=multi_offer,
            revenue_plan=revenue_plan,
            revenue_impact=revenue_impact,
            comparative_impact=comparative_impact,
            angle=angle,
            proposal=proposal,
            outreach=outreach
        )