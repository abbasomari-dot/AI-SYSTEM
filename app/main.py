from app.agents.brand_diagnostic_agent import BrandDiagnosticAgent
from app.agents.strategy_agent import StrategyAgent
from app.agents.creative_agent import CreativeAgent
from app.agents.analytics_agent import AnalyticsAgent
from app.agents.report_agent import ReportAgent
from app.services.pdf_generator import PDFGenerator


def get_user_input():
    print("\n=== AI CONSULTING ENGINE ===\n")

    name = input("Project / Restaurant Name: ")
    business_type = input("Business Type: ")
    audience = input("Target Audience: ")
    offer = input("Main Offer / Value Proposition: ")
    location = input("Location: ")

    return {
        "name": name,
        "type": business_type,
        "target_audience": audience,
        "offer": offer,
        "location": location
    }


def run():

    data = get_user_input()

    print("\nRunning Brand Diagnostic...")
    brand_agent = BrandDiagnosticAgent()
    brand_result = brand_agent.run(data)

    print("Running Strategy...")
    strategy_agent = StrategyAgent()
    strategy_result = strategy_agent.run(brand_result)

    print("Running Creative...")
    creative_agent = CreativeAgent()
    creative_result = creative_agent.run(strategy_result)

    print("Running Analytics...")
    analytics_agent = AnalyticsAgent()
    analytics_result = analytics_agent.run(creative_result)

    print("Generating Final Report...")
    report_agent = ReportAgent()
    final_report = report_agent.run(analytics_result)

    pdf = PDFGenerator()
    file_path = pdf.generate(final_report, data["name"])

    print("\nDone.")
    print(f"Saved at: {file_path}")


if __name__ == "__main__":
    run()