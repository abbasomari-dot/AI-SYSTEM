from typing import Dict


class SummaryEngine:
    """
    V4.4 - Executive Summary Generator (Refined Logic)
    """

    def generate(self, result: Dict) -> str:
        name = result.get("name")
        rating = result.get("rating")
        reviews = result.get("reviews")
        opportunity_label = result.get("opportunity_label")
        social_status = result.get("social_status")
        core_problem = result.get("core_problem")
        recommended_focus = result.get("recommended_focus")
        lead_tier = result.get("lead_tier")

        summary = (
            f"{name} maintains a strong local reputation with a {rating} rating "
            f"across {reviews} reviews. Based on current visibility indicators, "
            f"this business is classified as a {opportunity_label} growth opportunity.\n\n"
            f"Primary Observation: {core_problem}.\n\n"
        )

        # Tier-based narrative control
        if lead_tier.startswith("Tier A"):
            summary += (
                f"Strategic Direction: {recommended_focus}. "
                "This business presents a high-priority opportunity for structured "
                "visibility expansion and digital positioning."
            )

        elif lead_tier.startswith("Tier B"):
            summary += (
                f"Strategic Direction: {recommended_focus}. "
                "There is measurable growth potential with focused strategic refinement."
            )

        else:  # Tier C
            summary += (
                "Strategic Assessment: Current indicators suggest limited short-term "
                "acquisition priority. Monitoring or selective engagement may be more appropriate at this stage."
            )

        return summary