class BrandDiagnosticAgent:

    def run(self, data):

        executive_summary = f"""
        {data['name']} operates as a {data['type']} in {data['location']}, targeting {data['target_audience']}.

        Market Position:
        The business demonstrates a clear product-market fit through its core offering: {data['offer']}. 
        However, its current digital positioning may not fully reflect its competitive potential.

        Strategic Opportunity:
        By strengthening brand visibility, content consistency, and digital engagement strategy, 
        there is significant opportunity to increase customer acquisition and retention.

        Recommended Direction:
        Implement a structured social media growth framework focusing on positioning, 
        performance-driven content, and targeted promotional campaigns.

        Expected Outcome:
        With disciplined execution, measurable growth in engagement, foot traffic, 
        and brand perception can be achieved within 60–90 days.
        """

        return {
            **data,
            "executive_summary": executive_summary.strip()
        }