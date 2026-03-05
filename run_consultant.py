from app.growth.growth_orchestrator import GrowthOrchestrator
from app.services.client_report_builder import ClientReportBuilder
from app.services.presentation_builder import PresentationBuilder
from app.services.pdf_report_builder import PDFReportBuilder

from app.leads.lead_pipeline import LeadPipeline
from app.leads.lead_dashboard import LeadDashboard

from app.intelligence.instagram_analyzer import InstagramAnalyzer


def run():

    print("\nAI Marketing Consultant System\n")

    pipeline = LeadPipeline()
    leads = pipeline.run()

    orchestrator = GrowthOrchestrator()
    instagram = InstagramAnalyzer()

    dashboard_leads = []

    for lead in leads:

        client_name = lead["name"]

        print(f"\nProcessing lead: {client_name}")

        # Instagram Analysis
        insta_data = instagram.analyze(client_name)

        client_input = {
            "core_problem": "low_repeat_customers",
            "social_status": "weak",
            "rating": lead["rating"],
            "reviews": lead["reviews"],
            "lead_tier": "B",
            "aov": 24,
            "monthly_customers": 1100,
            "frequency": 1.2
        }

        # Run strategy engine
        growth_report = orchestrator.run(
            core_problem=client_input["core_problem"],
            social_status=client_input["social_status"],
            rating=client_input["rating"],
            reviews=client_input["reviews"],
            lead_tier=client_input["lead_tier"]
        )

        # System results
        system_results = {

            "rating": client_input["rating"],
            "reviews": client_input["reviews"],
            "social_status": client_input["social_status"],
            "core_problem": client_input["core_problem"],

            "aov": client_input["aov"],
            "monthly_customers": client_input["monthly_customers"],
            "frequency": client_input["frequency"],
            "revenue_model": "standard",

            "primary_lever": growth_report.strategic_overview["Strategic Direction"],
            "best_lever": growth_report.strategic_overview["Campaign Framework"],
            "financial_impact": "Projected growth via engagement expansion",

            "annual_revenue_increase": "Estimated growth based on engagement strategy",
            "roi": "Projected positive ROI",
            "payback_period": "3-6 months",

            "campaign_type": growth_report.strategic_overview["Campaign Framework"],
            "offer_strategy": growth_report.strategic_overview["Content Structure"],
            "sales_angle": growth_report.strategic_overview["Growth Focus"],

            "hooks": growth_report.monthly_plan_snapshot,
            "reel_ideas": growth_report.execution_priorities,
            "poster_concepts": growth_report.monthly_plan_snapshot,
            "prompts": growth_report.execution_priorities,

            "conversion_probability": "Moderate",
            "performance_tier": client_input["lead_tier"],
            "recommendation": growth_report.executive_summary,

            "risk_score": "Low",
            "risk_warnings": [],

            "suitability_score": "High",
            "suitability_warnings": [],

            "reach": 2000,
            "engagement": 564,
            "clicks": 320,
            "conversions": 200,

            "month1": growth_report.monthly_plan_snapshot[0],
            "month2": growth_report.monthly_plan_snapshot[1],
            "month3": growth_report.monthly_plan_snapshot[2],

            # Instagram data
            "followers": insta_data["followers"],
            "posts": insta_data["posts"],
            "instagram_url": insta_data["instagram_url"]
        }

        # Markdown report
        report_builder = ClientReportBuilder(client_name, system_results)
        report_path = report_builder.save_report()

        print("Report generated:", report_path)

        # PowerPoint
        presentation = PresentationBuilder(client_name, system_results)
        ppt_path = presentation.save()

        print("Presentation generated:", ppt_path)

        # PDF
        pdf_builder = PDFReportBuilder(client_name, system_results)
        pdf_path = pdf_builder.build()

        print("PDF generated:", pdf_path)

        # Add to dashboard
        dashboard_leads.append({
            "name": client_name,
            "rating": lead["rating"],
            "reviews": lead["reviews"],
            "followers": insta_data["followers"],
            "posts": insta_data["posts"],
            "engagement_rate": insta_data["engagement_rate"],
            "lead_score": insta_data["instagram_score"],
            "instagram_url": insta_data["instagram_url"]
        })

    # Save dashboard
    dashboard = LeadDashboard()

    dashboard_path = dashboard.save(dashboard_leads)

    print("\nLead dashboard saved:", dashboard_path)


if __name__ == "__main__":
    run()