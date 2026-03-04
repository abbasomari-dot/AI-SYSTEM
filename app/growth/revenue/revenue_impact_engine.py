# app/growth/revenue/revenue_impact_engine.py

from dataclasses import dataclass


@dataclass
class RevenueImpact:
    current_monthly_revenue: float
    projected_monthly_revenue: float
    monthly_increase: float
    yearly_increase: float
    impact_summary: str


class RevenueImpactEngine:

    @staticmethod
    def calculate(
        primary_lever: str,
        avg_order_value: float,
        monthly_customers: int,
        current_frequency: float,
        improvement_rate: float
    ) -> RevenueImpact:

        # الإيراد الحالي
        current_monthly = (
            monthly_customers
            * current_frequency
            * avg_order_value
        )

        # تطبيق التحسين حسب الرافعة
        if primary_lever == "Customer Frequency Increase":
            new_frequency = current_frequency * (1 + improvement_rate)
            projected_monthly = (
                monthly_customers
                * new_frequency
                * avg_order_value
            )

        elif primary_lever == "Average Order Value Increase":
            new_aov = avg_order_value * (1 + improvement_rate)
            projected_monthly = (
                monthly_customers
                * current_frequency
                * new_aov
            )

        elif primary_lever == "Conversion Rate Improvement":
            projected_monthly = current_monthly * (1 + improvement_rate)

        elif primary_lever == "High-Ticket Upsell Strategy":
            projected_monthly = current_monthly * (1 + improvement_rate * 1.2)

        else:
            projected_monthly = current_monthly * (1 + improvement_rate)

        monthly_increase = projected_monthly - current_monthly
        yearly_increase = monthly_increase * 12

        summary = (
            f"If we improve {primary_lever.lower()} by "
            f"{int(improvement_rate * 100)}%, "
            f"monthly revenue could increase by "
            f"${monthly_increase:,.0f}, "
            f"adding approximately "
            f"${yearly_increase:,.0f} annually."
        )

        return RevenueImpact(
            current_monthly_revenue=current_monthly,
            projected_monthly_revenue=projected_monthly,
            monthly_increase=monthly_increase,
            yearly_increase=yearly_increase,
            impact_summary=summary
        )