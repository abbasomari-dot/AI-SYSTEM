from typing import Dict, Optional
from app.social.instagram_audit import InstagramAudit


class SocialAuditEngine:
    """
    Generic Social Audit Layer
    Supports smart detection from website field.
    """

    def __init__(self):
        self.instagram_audit = InstagramAudit()

    def analyze_from_website(self, website: Optional[str]) -> Dict:

        results = {
            "instagram": None,
            "facebook": None,
        }

        if not website:
            return {
                "platforms": results,
                "social_health_score": 0,
                "social_status": "Missing"
            }

        website_lower = website.lower()

        # Instagram detection
        if "instagram.com" in website_lower:
            insta_result = self.instagram_audit.analyze(website)
            results["instagram"] = insta_result

        # Facebook detection
        if "facebook.com" in website_lower:
            results["facebook"] = {
                "account_exists": True
            }

        score = 0
        if results["instagram"]:
            score = results["instagram"].get("snapshot_score", 0)

        status = self._classify_social_status(score)

        return {
            "platforms": results,
            "social_health_score": score,
            "social_status": status
        }

    def _classify_social_status(self, score: int) -> str:
        if score >= 70:
            return "Strong"
        elif score > 0:
            return "Weak"
        else:
            return "Missing"