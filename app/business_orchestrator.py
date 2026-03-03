# app/business_orchestrator.py

from dataclasses import dataclass

from app.growth.growth_orchestrator import GrowthOrchestrator
from app.growth.strategy_engine import StrategyInput
from app.growth.revenue.offer_generator import OfferGenerator
from app.growth.revenue.angle_generator import AngleGenerator
from app.growth.revenue.proposal_builder import ProposalBuilder
from app.growth.revenue.outreach_engine import OutreachEngine


@dataclass
class BusinessOutput:
    growth_report: object
    offer: object
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
        reviews: int
    ) -> BusinessOutput:

        # ---------------------------
        # 1️⃣ Growth System
        # ---------------------------
        growth_report = GrowthOrchestrator.run(
            lead_tier=lead_tier,
            core_problem=core_problem,
            social_status=social_status,
            rating=rating,
            reviews=reviews
        )

        # Rebuild strategy input (needed for Revenue layer)
        strategy_input = StrategyInput(
            lead_tier=lead_tier,
            core_problem=core_problem,
            social_status=social_status,
            rating=rating,
            reviews=reviews
        )

        from app.growth.strategy_engine import StrategyEngine
        strategy = StrategyEngine.generate_strategy(strategy_input)

        # ---------------------------
        # 2️⃣ Revenue Layer
        # ---------------------------
        offer = OfferGenerator.generate(strategy, core_problem, lead_tier)

        angle = AngleGenerator.generate(strategy, offer)

        proposal = ProposalBuilder.build(strategy, offer, angle)

        outreach = OutreachEngine.generate(strategy, offer, angle, proposal)

        return BusinessOutput(
            growth_report=growth_report,
            offer=offer,
            angle=angle,
            proposal=proposal,
            outreach=outreach
        )