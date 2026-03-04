# app/creative/prompt_builder.py


class PromptBuilder:

    def build_hook_prompt(self, hook: str, strategy: dict) -> str:

        return f"""
Platform: {strategy.get('platform')}
Audience: {strategy.get('target_audience')}
Sales Angle: {strategy.get('sales_angle')}

Write a high converting caption using:
{hook}
"""

    def build_reel_prompt(self, idea: str, strategy: dict) -> str:

        return f"""
Platform: {strategy.get('platform')}
Audience: {strategy.get('target_audience')}
Sales Angle: {strategy.get('sales_angle')}

Create a short-form video script based on:
{idea}
"""

    def build_poster_prompt(self, concept: str, strategy: dict) -> str:

        return f"""
Platform: {strategy.get('platform')}
Audience: {strategy.get('target_audience')}
Sales Angle: {strategy.get('sales_angle')}

Design a promotional poster based on:
{concept}
"""

    def build_all(self, hooks: list, reels: list, posters: list, strategy: dict) -> dict:

        return {
            "hook_prompts": [
                self.build_hook_prompt(h, strategy) for h in hooks
            ],
            "reel_prompts": [
                self.build_reel_prompt(r, strategy) for r in reels
            ],
            "poster_prompts": [
                self.build_poster_prompt(p, strategy) for p in posters
            ],
        }