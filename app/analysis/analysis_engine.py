class AnalysisEngine:

    @staticmethod
    def analyze(
        name,
        rating,
        reviews,
        location,
        instagram_followers,
        competitors
    ):

        # ---------------------------
        # MARKET AVERAGE
        # ---------------------------
        avg_market_rating = sum(c["rating"] for c in competitors) / len(competitors)

        # ---------------------------
        # POSITION
        # ---------------------------
        if rating >= avg_market_rating:
            position = "Competitive"
        else:
            position = "Below competitors"

        # ---------------------------
        # INSTAGRAM STATUS
        # ---------------------------
        if not instagram_followers:
            ig_status = "Weak presence or data unavailable"
        elif instagram_followers < 5000:
            ig_status = "Low social media presence"
        else:
            ig_status = "Strong social presence"

        # ---------------------------
        # GROWTH ESTIMATE
        # ---------------------------
        rating_gap = max(c["rating"] for c in competitors) - rating

        if rating_gap <= 0.1:
            growth = "5%-10%"
        elif rating_gap <= 0.3:
            growth = "10%-20%"
        else:
            growth = "20%-35%"

        # ---------------------------
        # RISK
        # ---------------------------
        if rating < 4.0:
            risk = "High risk due to low rating and customer perception issues"
        else:
            risk = "Moderate risk — competitors may capture demand"

        # ---------------------------
        # MAPS POSITION (تقدير بسيط)
        # ---------------------------
        sorted_competitors = sorted(competitors, key=lambda x: x["rating"], reverse=True)

        maps_position = 1
        for i, c in enumerate(sorted_competitors):
            if rating < c["rating"]:
                maps_position = i + 2

        # ---------------------------
        # REVENUE LEAKAGE (NEW)
        # ---------------------------
        if maps_position == 1:
            lost_customers = 0
        elif maps_position == 2:
            lost_customers = 15
        elif maps_position == 3:
            lost_customers = 25
        else:
            lost_customers = 35

        avg_order_value = 30

        low_estimate = lost_customers * avg_order_value
        high_estimate = (lost_customers + 10) * avg_order_value

        # ---------------------------
        # FINAL OUTPUT
        # ---------------------------
        return {
            "name": name,
            "rating": rating,
            "reviews": reviews,
            "avg_market_rating": round(avg_market_rating, 2),
            "position": position,
            "growth": growth,
            "risk": risk,
            "ig_status": ig_status,
            "maps_position": maps_position,

            # 🔥 الجديد
            "lost_customers_range": f"{lost_customers}-{lost_customers + 10}",
            "revenue_loss_range": f"{low_estimate}-{high_estimate}",
            "avg_order_value": avg_order_value
        }