class StrategyAgent:

    def run(self, data):

        strategy = {
            "positioning": f"{data['name']} has the potential to dominate the {data['type']} segment in {data['location']} by refining its digital positioning.",

            "tone": "Confident, modern, and growth-oriented brand voice.",

            "marketing_channels": "Instagram (Primary), TikTok (Growth), Google Reviews (Reputation).",

            "gap_analysis": {
                "strengths": [
                    "Clear core offering",
                    "Defined target audience",
                    "Strong local positioning potential"
                ],
                "weaknesses": [
                    "Limited structured content strategy",
                    "Inconsistent brand messaging",
                    "Underutilized short-form video potential"
                ],
                "growth_opportunity": [
                    "High potential for Reels-driven visibility",
                    "Influencer collaboration potential",
                    "Conversion-focused campaign structure"
                ]
            },

            "growth_roadmap": {
                "month_1": [
                    "Conduct full content audit",
                    "Define visual identity guidelines",
                    "Optimize Instagram bio & highlights",
                    "Launch 6 high-quality Reels",
                    "Establish consistent posting schedule"
                ],
                "month_2": [
                    "Launch micro-influencer collaborations",
                    "Run initial paid ad testing campaign",
                    "Implement engagement-focused CTAs",
                    "Track content performance weekly"
                ],
                "month_3": [
                    "Launch retargeting ad campaigns",
                    "Introduce limited-time promotional offers",
                    "Optimize content based on analytics",
                    "Build loyalty-focused community campaigns"
                ]
            }
        }

        return {
            **data,
            "strategy": strategy
        }