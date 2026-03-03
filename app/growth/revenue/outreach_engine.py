# app/growth/revenue/outreach_engine.py

from dataclasses import dataclass
from app.growth.strategy_engine import StrategyOutput
from app.growth.revenue.offer_generator import Offer
from app.growth.revenue.angle_generator import Angle
from app.growth.revenue.proposal_builder import Proposal


@dataclass
class Outreach:
    cold_dm: str
    follow_up: str
    email_pitch: str
    call_script: str


class OutreachEngine:

    @staticmethod
    def generate(
        strategy: StrategyOutput,
        offer: Offer,
        angle: Angle,
        proposal: Proposal
    ) -> Outreach:

        cold_dm = OutreachEngine._build_cold_dm(angle)
        follow_up = OutreachEngine._build_follow_up(strategy)
        email_pitch = OutreachEngine._build_email_pitch(proposal)
        call_script = OutreachEngine._build_call_script(strategy, offer)

        return Outreach(
            cold_dm=cold_dm,
            follow_up=follow_up,
            email_pitch=email_pitch,
            call_script=call_script
        )

    # ---------------------------
    # Cold DM (Improved)
    # ---------------------------

    @staticmethod
    def _build_cold_dm(angle: Angle) -> str:
        return (
            "Hi — quick question.\n\n"
            f"We help businesses {angle.primary_angle.lower()} and see measurable results within 90 days.\n"
            "Would you be open to a brief conversation to explore if this fits your current growth goals?"
        )

    # ---------------------------
    # Follow Up (Improved)
    # ---------------------------

    @staticmethod
    def _build_follow_up(strategy: StrategyOutput) -> str:
        return (
            "Just following up in case this got buried.\n\n"
            f"If improving {strategy.growth_focus.lower()} is a priority this quarter, "
            "I’d be happy to share a short, structured plan tailored to your situation."
        )

    # ---------------------------
    # Email Pitch (Cleaner Flow)
    # ---------------------------

    @staticmethod
    def _build_email_pitch(proposal: Proposal) -> str:
        return (
            "Subject: Strategic Growth Initiative\n\n"
            f"{proposal.executive_pitch}\n\n"
            "Current Situation:\n"
            f"{proposal.problem_diagnosis}\n\n"
            "Proposed Plan:\n"
            f"{proposal.proposed_solution}\n\n"
            "Investment Model:\n"
            f"{proposal.investment}\n\n"
            f"{proposal.closing_statement}"
        )

    # ---------------------------
    # Call Script (More Natural)
    # ---------------------------

    @staticmethod
    def _build_call_script(strategy: StrategyOutput, offer: Offer) -> str:
        return (
            "Opening:\n"
            "Thanks for taking the call. Based on our analysis, "
            f"there’s a strong opportunity to improve your {strategy.growth_focus.lower()}.\n\n"
            "Insight:\n"
            f"Right now, your business would benefit most from a "
            f"{strategy.strategic_direction.lower()} approach.\n\n"
            "Solution:\n"
            f"We’ve structured a {offer.offer_type} specifically to address this.\n\n"
            "Close:\n"
            "If this direction makes sense, we can outline the next steps and timeline."
        )