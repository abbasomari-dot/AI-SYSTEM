# app/creative/hook_generator.py


class HookGenerator:

    def generate(self, strategy: dict):

        offer = strategy["offer_name"]
        discount = strategy["discount_percentage"]
        angle = strategy["sales_angle"]

        hooks = []

        if angle == "price_shock":
            hooks.append(f"🚨 {discount}% OFF — This changes everything!")
            hooks.append(f"{offer} almost half price!")

        elif angle == "urgency_attack":
            hooks.append("Last chance before it's gone!")
            hooks.append("Act now or regret later.")

        elif angle == "market_domination":
            hooks.append("The strongest deal in the market.")
            hooks.append("No competitor comes close.")

        elif angle == "smart_savings":
            hooks.append(f"Save smart with {offer}.")
            hooks.append("Best value for your money.")

        elif angle == "comparison":
            hooks.append("Why pay more elsewhere?")
            hooks.append("Compare and decide wisely.")

        elif angle == "testimonial":
            hooks.append("Customers are loving this deal.")
            hooks.append("Rated top choice.")

        elif angle == "bonus_angle":
            hooks.append("Extra value included.")
            hooks.append("More than just a discount.")

        elif angle == "limited_upgrade":
            hooks.append("Upgrade opportunity for limited time.")

        elif angle == "value_focus":
            hooks.append("Maximum value for your investment.")

        elif angle == "benefit_focus":
            hooks.append("Experience the real benefits today.")

        return hooks