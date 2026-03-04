# app/growth/revenue/multi_offer_generator.py

from dataclasses import dataclass
from typing import List
from app.growth.strategy_engine import StrategyOutput


@dataclass
class OfferTier:
    name: str
    features: List[str]
    positioning: str
    price_range: str


@dataclass
class MultiOffer:
    starter: OfferTier
    growth: OfferTier
    premium: OfferTier


class MultiOfferGenerator:

    @staticmethod
    def generate(strategy: StrategyOutput, lead_tier: str, rating: float, reviews: int) -> MultiOffer:

        opportunity_score = MultiOfferGenerator._calculate_opportunity_score(
            lead_tier, rating, reviews
        )

        starter = MultiOfferGenerator._build_starter(strategy, opportunity_score)
        growth = MultiOfferGenerator._build_growth(strategy, opportunity_score)
        premium = MultiOfferGenerator._build_premium(strategy, opportunity_score)

        return MultiOffer(
            starter=starter,
            growth=growth,
            premium=premium
        )

    # ---------------------------
    # Opportunity Score
    # ---------------------------

    @staticmethod
    def _calculate_opportunity_score(lead_tier: str, rating: float, reviews: int) -> int:

        score = 0

        if lead_tier == "high":
            score += 3
        elif lead_tier == "mid":
            score += 2
        else:
            score += 1

        if rating < 3.5:
            score += 3
        elif rating < 4.2:
            score += 2
        else:
            score += 1

        if reviews > 800:
            score += 3
        elif reviews > 200:
            score += 2
        else:
            score += 1

        return score  # 3 – 9

    # ---------------------------
    # Base Multiplier
    # ---------------------------

    @staticmethod
    def _base_multiplier(score: int) -> float:
        return 1 + (score * 0.015)

    # ---------------------------
    # Strategic Adjustment Layer
    # ---------------------------

    @staticmethod
    def _strategic_adjustment(strategy: StrategyOutput, package_type: str) -> float:

        adjustment = 1.0

        # 🔥 Revenue Optimization → Premium أقوى
        if strategy.growth_focus == "Revenue Optimization":
            if package_type == "premium":
                adjustment += 0.06  # +6%
            elif package_type == "growth":
                adjustment += 0.03  # +3%

        # 🔥 Reputation Recovery → Growth أهم
        if strategy.strategic_direction == "Reputation Recovery":
            if package_type == "growth":
                adjustment += 0.05
            elif package_type == "premium":
                adjustment += 0.02

        return adjustment

    # ---------------------------
    # Price Builder
    # ---------------------------

    @staticmethod
    def _build_price_range(base_min: int, base_max: int, score: int,
                           strategy: StrategyOutput, package_type: str) -> str:

        multiplier = MultiOfferGenerator._base_multiplier(score)
        multiplier *= MultiOfferGenerator._strategic_adjustment(strategy, package_type)

        min_price = int(base_min * multiplier)
        max_price = int(base_max * multiplier)

        return f"${min_price:,} – ${max_price:,} / month"

    # ---------------------------
    # Starter
    # ---------------------------

    @staticmethod
    def _build_starter(strategy: StrategyOutput, score: int) -> OfferTier:

        price = MultiOfferGenerator._build_price_range(
            800, 1200, score, strategy, "starter"
        )

        return OfferTier(
            name="Starter Growth Package",
            features=[
                "Basic content strategy",
                "8 posts per month",
                "Review optimization setup",
                "Monthly performance report"
            ],
            positioning="Ideal for businesses starting structured growth.",
            price_range=price
        )

    # ---------------------------
    # Growth
    # ---------------------------

    @staticmethod
    def _build_growth(strategy: StrategyOutput, score: int) -> OfferTier:

        price = MultiOfferGenerator._build_price_range(
            1500, 2500, score, strategy, "growth"
        )

        return OfferTier(
            name="Growth Acceleration Package",
            features=[
                "Full content strategy",
                "12–16 posts per month",
                "Reel production",
                "Ad campaign management",
                "Review & authority building",
                "Bi-weekly optimization"
            ],
            positioning="Designed for businesses serious about scaling revenue.",
            price_range=price
        )

    # ---------------------------
    # Premium
    # ---------------------------

    @staticmethod
    def _build_premium(strategy: StrategyOutput, score: int) -> OfferTier:

        premium_features = [
            "Advanced brand positioning",
            "20+ content pieces monthly",
            "Full funnel ad strategy",
            "Conversion optimization",
            "Upsell & pricing strategy",
            "Weekly performance optimization"
        ]

        if strategy.growth_focus == "Revenue Optimization":
            premium_features.append("Advanced revenue modeling")

        price = MultiOfferGenerator._build_price_range(
            3000, 5000, score, strategy, "premium"
        )

        return OfferTier(
            name="Premium Market Domination Package",
            features=premium_features,
            positioning="For businesses ready to dominate their market.",
            price_range=price
        )