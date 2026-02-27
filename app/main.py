from app.agents.brand_diagnostic_agent import BrandDiagnosticAgent
from app.agents.strategy_agent import StrategyAgent
from app.agents.creative_agent import CreativeAgent
from app.agents.analytics_agent import AnalyticsAgent
from app.agents.report_agent import ReportAgent
from app.services.pdf_generator import PDFGenerator


def run():

    restaurant = {
        "name": "Burger Zone",
        "type": "Burger Restaurant",
        "target_audience": "Youth 18-30",
        "offer": "Burger + Fries for 29 QAR",
        "location": "Doha"
    }

    brand_agent = BrandDiagnosticAgent()
    strategy_agent = StrategyAgent()
    creative_agent = CreativeAgent()
    analytics_agent = AnalyticsAgent()
    report_agent = ReportAgent()
    pdf_generator = PDFGenerator()

    print("Running Brand Diagnostic...")
    brand_data = brand_agent.run(restaurant)

    print("Running Strategy...")
    strategy = strategy_agent.run(brand_data)

    print("Running Creative...")
    creative = creative_agent.run(brand_data)

    print("Running Analytics...")
    kpis = analytics_agent.run(brand_data)

    print("Generating Final Report...")
    final_report = report_agent.run(brand_data)

    pdf_path = pdf_generator.generate(final_report, restaurant["name"])

    print("Done.")
    print("Saved at:", pdf_path)


if __name__ == "__main__":
    run()