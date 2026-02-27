class AnalyticsAgent:

    def run(self, data):

        kpis = [
            "Increase engagement rate by 20% within 60 days",
            "Grow followers by 30% in 3 months",
            "Improve customer retention via targeted campaigns"
        ]

        return {
            **data,
            "kpis": kpis
        }