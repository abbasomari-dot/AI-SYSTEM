from app.creative.hook_generator import HookGenerator
from app.creative.reel_idea_generator import ReelIdeaGenerator
from app.creative.poster_generator import PosterGenerator
from app.creative.prompt_builder import PromptBuilder

from app.intelligence.strategy_scoring import StrategyScoring
from app.intelligence.conversion_estimator import ConversionEstimator
from app.intelligence.roi_projection import ROIProjection
from app.intelligence.lever_suitability_engine import LeverSuitabilityEngine
from app.intelligence.risk_detection_engine import RiskDetectionEngine


class SalesCreativeEngine:

    def __init__(self):

        # Creative generators
        self.hook_generator = HookGenerator()
        self.reel_generator = ReelIdeaGenerator()
        self.poster_generator = PosterGenerator()
        self.prompt_builder = PromptBuilder()

        # Intelligence engines
        self.strategy_scoring = StrategyScoring()
        self.conversion_estimator = ConversionEstimator()
        self.roi_projection = ROIProjection()
        self.lever_suitability = LeverSuitabilityEngine()
        self.risk_detector = RiskDetectionEngine()

    # -------------------------------------------------

    def analyze_offer(self, data):

        original_price = data["original_price"]
        new_price = data["new_price"]

        discount_percentage = round(
            ((original_price - new_price) / original_price) * 100, 2
        )

        if discount_percentage >= 40:
            offer_strength = "aggressive"
        elif discount_percentage >= 25:
            offer_strength = "strong"
        elif discount_percentage >= 10:
            offer_strength = "moderate"
        else:
            offer_strength = "weak"

        return discount_percentage, offer_strength

    # -------------------------------------------------

    def generate_strategies(self, data):

        discount_percentage, offer_strength = self.analyze_offer(data)

        base_strategy = {
            "brand_name": data["brand_name"],
            "offer_name": data["offer_name"],
            "original_price": data["original_price"],
            "new_price": data["new_price"],
            "discount_percentage": discount_percentage,
            "offer_strength": offer_strength,
            "platform": data["platform"],
            "target_audience": data["target_audience"],
            "audience_size": data.get("audience_size", 8000)
        }

        strategies = []

        if discount_percentage >= 30:

            strategies.append({**base_strategy, "sales_angle": "price_shock"})
            strategies.append({**base_strategy, "sales_angle": "urgency_attack"})
            strategies.append({**base_strategy, "sales_angle": "market_domination"})

        elif discount_percentage >= 15:

            strategies.append({**base_strategy, "sales_angle": "value_offer"})
            strategies.append({**base_strategy, "sales_angle": "smart_saver"})

        else:

            strategies.append({**base_strategy, "sales_angle": "bonus_angle"})
            strategies.append({**base_strategy, "sales_angle": "limited_upgrade"})

        return strategies

    # -------------------------------------------------

    def generate_single_strategy(self, strategy):

        # Generate creatives
        hooks = self.hook_generator.generate(strategy)
        reels = self.reel_generator.generate(strategy)
        posters = self.poster_generator.generate(strategy)

        prompts = self.prompt_builder.build_all(
            hooks=hooks,
            reels=reels,
            posters=posters,
            strategy=strategy
        )

        # Strategy scoring
        score = self.strategy_scoring.score(strategy)

        # Conversion estimation
        conversion = self.conversion_estimator.estimate(score)

        # ROI projection
        roi = self.roi_projection.project(
            strategy=strategy,
            conversion_probability=conversion["conversion_probability_percent"]
        )

        # Suitability analysis
        suitability = self.lever_suitability.evaluate(strategy, strategy)

        # Risk detection
        risk = self.risk_detector.detect(strategy)

        return {
            "strategy": strategy,
            "score_breakdown": score,
            "conversion_estimation": conversion,
            "roi_projection": roi,
            "suitability_analysis": suitability,
            "risk_analysis": risk,
            "hooks": hooks,
            "reels": reels,
            "posters": posters,
            "prompts": prompts
        }

    # -------------------------------------------------

    def generate_multi(self, data):

        strategies = self.generate_strategies(data)

        results = []

        for strategy in strategies:
            result = self.generate_single_strategy(strategy)
            results.append(result)

        results_sorted = sorted(
            results,
            key=lambda x: x["roi_projection"]["expected_revenue"],
            reverse=True
        )

        return {
            "best_strategy": results_sorted[0],
            "strategies_ranked_by_revenue": results_sorted
        }