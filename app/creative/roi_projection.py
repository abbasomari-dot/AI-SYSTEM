# app/creative/roi_projection.py


class ROIProjector:

    def project(self, strategy: dict, conversion_data: dict, creative_input: dict):

        audience_size = creative_input.get("audience_size", 0)
        reach_percent = creative_input.get("expected_reach_percent", 30)
        new_price = strategy.get("new_price", 0)

        conversion_probability = conversion_data.get(
            "conversion_probability_percent", 0
        )

        expected_reach = audience_size * (reach_percent / 100)

        expected_conversions = expected_reach * (conversion_probability / 100)

        expected_revenue = expected_conversions * new_price

        roi_score = 0
        if audience_size > 0:
            roi_score = expected_revenue / audience_size

        return {
            "expected_reach": round(expected_reach, 1),
            "expected_conversions": round(expected_conversions, 1),
            "expected_revenue": round(expected_revenue, 2),
            "roi_score": round(roi_score, 4)
        }