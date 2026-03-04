# app/growth/revenue/comparative_impact_engine.py

from dataclasses import dataclass
from typing import Dict


@dataclass
class ComparativeImpact:
    impacts: Dict[str, float]
    best_lever: str
    best_annual_increase: float


class ComparativeImpactEngine:

    @staticmethod
    def calculate(
        avg_order_value: float,
        monthly_customers: int,
        current_frequency: float,
        improvement_rate: float
    ) -> ComparativeImpact:

        current_monthly = (
            monthly_customers
            * current_frequency
            * avg_order_value
        )

        impacts = {}

        # ---------------------------
        # Realistic Weights
        # ---------------------------
        weights = {
            "Customer Frequency Increase": 1.0,
            "Average Order Value Increase": 0.8,
            "Conversion Rate Improvement": 0.6,
            "High-Ticket Upsell Strategy": 1.2,
        }

        # ---------------------------
        # Frequency
        # ---------------------------
        freq_rate = improvement_rate * weights["Customer Frequency Increase"]
        new_frequency = current_frequency * (1 + freq_rate)
        freq_monthly = monthly_customers * new_frequency * avg_order_value
        impacts["Customer Frequency Increase"] = (
            (freq_monthly - current_monthly) * 12
        )

        # ---------------------------
        # AOV
        # ---------------------------
        aov_rate = improvement_rate * weights["Average Order Value Increase"]
        new_aov = avg_order_value * (1 + aov_rate)
        aov_monthly = monthly_customers * current_frequency * new_aov
        impacts["Average Order Value Increase"] = (
            (aov_monthly - current_monthly) * 12
        )

        # ---------------------------
        # Conversion
        # ---------------------------
        conv_rate = improvement_rate * weights["Conversion Rate Improvement"]
        conv_monthly = current_monthly * (1 + conv_rate)
        impacts["Conversion Rate Improvement"] = (
            (conv_monthly - current_monthly) * 12
        )

        # ---------------------------
        # Upsell
        # ---------------------------
        upsell_rate = improvement_rate * weights["High-Ticket Upsell Strategy"]
        upsell_monthly = current_monthly * (1 + upsell_rate)
        impacts["High-Ticket Upsell Strategy"] = (
            (upsell_monthly - current_monthly) * 12
        )

        # ---------------------------
        # Best Lever
        # ---------------------------
        best_lever = max(impacts, key=impacts.get)
        best_value = impacts[best_lever]

        return ComparativeImpact(
            impacts=impacts,
            best_lever=best_lever,
            best_annual_increase=best_value
        )