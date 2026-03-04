# app/creative/sales_creative_engine.py

from copy import deepcopy
from .hook_generator import HookGenerator
from .reel_idea_generator import ReelIdeaGenerator
from .poster_generator import PosterGenerator
from .prompt_builder import PromptBuilder
from .strategy_scoring import StrategyScorer
from .conversion_estimator import ConversionEstimator
from .roi_projection import ROIProjector


class CreativeStrategyBuilder:

    def _calculate_discount(self, original_price, new_price):
        if not original_price or not new_price:
            return 0
        if original_price == 0:
            return 0

        discount = ((original_price - new_price) / original_price) * 100
        return round(discount, 1)

    def _classify_strength(self, discount_percentage):
        if discount_percentage >= 40:
            return "aggressive"
        elif discount_percentage >= 20:
            return "strong"
        elif discount_percentage >= 10:
            return "moderate"
        else:
            return "weak"

    def build_base(self, creative_input: dict) -> dict:

        original_price = creative_input.get("original_price")
        new_price = creative_input.get("new_price")

        discount_percentage = self._calculate_discount(
            original_price,
            new_price
        )

        strength = self._classify_strength(discount_percentage)

        return {
            "offer_name": creative_input.get("offer_name"),
            "brand_name": creative_input.get("brand_name"),
            "original_price": original_price,
            "new_price": new_price,
            "discount_percentage": discount_percentage,
            "offer_strength": strength,
            "platform": creative_input.get("platform", "instagram"),
            "target_audience": creative_input.get("target_audience")
        }

    def expand_angles(self, base_strategy: dict):

        strength = base_strategy["offer_strength"]

        angle_map = {
            "aggressive": [
                "price_shock",
                "urgency_attack",
                "market_domination"
            ],
            "strong": [
                "smart_savings",
                "comparison",
                "testimonial"
            ],
            "moderate": [
                "bonus_angle",
                "limited_upgrade"
            ],
            "weak": [
                "value_focus",
                "benefit_focus"
            ]
        }

        selected_angles = angle_map.get(strength, ["value_focus"])

        strategies = []

        for angle in selected_angles:
            strategy_copy = deepcopy(base_strategy)
            strategy_copy["sales_angle"] = angle
            strategies.append(strategy_copy)

        return strategies


class CreativeEngine:

    def __init__(self):

        self.builder = CreativeStrategyBuilder()
        self.hook_generator = HookGenerator()
        self.reel_generator = ReelIdeaGenerator()
        self.poster_generator = PosterGenerator()
        self.prompt_builder = PromptBuilder()
        self.scorer = StrategyScorer()
        self.converter = ConversionEstimator()
        self.roi_projector = ROIProjector()

    def generate_multi(self, creative_input: dict) -> dict:

        base_strategy = self.builder.build_base(creative_input)
        strategies = self.builder.expand_angles(base_strategy)

        results = []

        for strategy in strategies:

            hooks = self.hook_generator.generate(strategy)
            reels = self.reel_generator.generate(strategy)
            posters = self.poster_generator.generate(strategy)

            prompts = self.prompt_builder.build_all(
                hooks=hooks,
                reels=reels,
                posters=posters,
                strategy=strategy
            )

            score_data = self.scorer.score(strategy)
            conversion_data = self.converter.estimate(score_data)

            roi_data = self.roi_projector.project(
                strategy=strategy,
                conversion_data=conversion_data,
                creative_input=creative_input
            )

            results.append({
                "strategy": strategy,
                "score_breakdown": score_data,
                "conversion_estimation": conversion_data,
                "roi_projection": roi_data,
                "hooks": hooks,
                "reels": reels,
                "posters": posters,
                "prompts": prompts
            })

        ranked = sorted(
            results,
            key=lambda x: x["roi_projection"]["expected_revenue"],
            reverse=True
        )

        return {
            "strategies_ranked_by_revenue": ranked,
            "best_strategy": ranked[0] if ranked else None
        }