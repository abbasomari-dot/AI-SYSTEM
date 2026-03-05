class ROIProjection:

    def project(self, strategy, conversion_probability):

        audience_size = strategy.get("audience_size", 8000)

        reach_percent = 1.0
        expected_reach = audience_size * reach_percent

        conversion_rate = conversion_probability / 100
        expected_conversions = expected_reach * conversion_rate

        new_price = strategy["new_price"]

        expected_revenue = expected_conversions * new_price

        roi_score = round(expected_revenue / 20000, 3)

        return {
            "expected_reach": expected_reach,
            "expected_conversions": expected_conversions,
            "expected_revenue": expected_revenue,
            "roi_score": roi_score
        }