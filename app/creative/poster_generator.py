# app/creative/poster_generator.py


class PosterGenerator:

    def generate(self, strategy: dict):

        offer = strategy.get("offer_name")
        discount = strategy.get("discount_percentage", 0)
        angle = strategy.get("sales_angle")
        strength = strategy.get("offer_strength")

        posters = []

        if angle == "price_shock":
            posters.append(f"Big bold {discount}% OFF layout")
            posters.append(f"Explosive discount design for {offer}")

        elif angle == "urgency_attack":
            posters.append("Limited time countdown layout")
            posters.append("Only today badge design")

        elif angle == "market_domination":
            posters.append("Market leader headline layout")
            posters.append("Best deal in town poster")

        elif angle == "smart_savings":
            posters.append("Clean savings breakdown layout")
            posters.append("Compare old vs new price design")

        elif angle == "comparison":
            posters.append("Side-by-side comparison poster")

        elif angle == "testimonial":
            posters.append("Customer review highlight layout")

        elif angle == "bonus_angle":
            posters.append("Bonus value included design")

        elif angle == "limited_upgrade":
            posters.append("Upgrade now premium layout")

        elif angle == "value_focus":
            posters.append("Value centered clean layout")

        elif angle == "benefit_focus":
            posters.append("Feature highlight poster")

        # تعزيز إضافي حسب قوة العرض
        if strength == "aggressive":
            posters.append("High contrast red urgency theme")

        return posters