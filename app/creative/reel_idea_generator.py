# app/creative/reel_idea_generator.py


class ReelIdeaGenerator:

    def generate(self, strategy: dict) -> list:

        offer = strategy["offer_name"]
        strength = strategy["offer_strength"]
        discount = strategy["discount_percentage"]

        ideas = []

        if strength == "aggressive":
            ideas.append(f"Explosive reveal of {discount}% discount")
            ideas.append("High energy price drop animation")

        elif strength == "strong":
            ideas.append(f"Break down savings of {offer}")
            ideas.append("Customer testimonial style reel")

        elif strength == "moderate":
            ideas.append("Explain added bonus value")

        else:
            ideas.append("Focus on product benefits")

        return ideas