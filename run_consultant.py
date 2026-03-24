from app.growth.growth_orchestrator import GrowthOrchestrator
from app.data.google_maps_client import GoogleMapsClient
from app.data.instagram_finder import InstagramFinder
from app.reporting.pdf_builder import PDFReportBuilder
from app.analysis.analysis_engine import AnalysisEngine


def run():

    print("=== AI Marketing Consultant System ===\n")

    # ---------------------------
    # INPUT
    # ---------------------------
    client_input = {
        "name": "Nusr-Et Steakhouse Doha",
        "core_problem": "low customer acquisition",
        "lead_tier": "high"
    }

    # ---------------------------
    # GOOGLE DATA
    # ---------------------------
    google_client = GoogleMapsClient()
    google_data = google_client.get_place_data(client_input["name"])

    rating = google_data.get("rating", 0)
    reviews = google_data.get("reviews", 0)

    # ---------------------------
    # INSTAGRAM
    # ---------------------------
    instagram_finder = InstagramFinder(api_key="d73e7006625d69fb60e0aa7daef0da018513f08de467114fe01804a4b6e633ad")
    instagram_data = instagram_finder.get_instagram_data(client_input["name"])

    instagram_link = instagram_data.get("link", "Not found")
    followers = instagram_data.get("followers")
    followers_text = f"{followers:,}" if followers else "Not publicly available"

    # ---------------------------
    # COMPETITORS
    # ---------------------------
    competitors = google_client.get_competitors(
        query="steakhouse",
        location="Doha",
        limit=3
    )

    # ---------------------------
    # ANALYSIS
    # ---------------------------
    analysis = AnalysisEngine.analyze(
        name=client_input["name"],
        rating=rating,
        reviews=reviews,
        location="Doha",
        instagram_followers=followers,
        competitors=competitors
    )

    # ---------------------------
    # ORCHESTRATOR
    # ---------------------------
    orchestrator = GrowthOrchestrator()

    growth_report = orchestrator.run(
        name=client_input["name"],
        core_problem=client_input["core_problem"],
        lead_tier=client_input["lead_tier"],
        social_status=instagram_link,
        rating=rating,
        reviews=reviews
    )

    # ---------------------------
    # PDF BUILDER
    # ---------------------------
    filename = f"clients/{client_input['name']}_growth_report.pdf"
    builder = PDFReportBuilder(filename)

    builder.add_cover_page(client_input["name"])
    builder.add_title(f"{client_input['name']} Growth Report")

    # ---------------------------
    # SNAPSHOT
    # ---------------------------
    builder.add_section(
        "Business Snapshot",
        f"""
<b>Business:</b> {client_input["name"]}<br/>
<b>Location:</b> Doha<br/>
<b>Rating:</b> {rating} ⭐<br/>
<b>Reviews:</b> {reviews}<br/>
<b>Market Average:</b> {analysis['avg_market_rating']} ⭐
"""
    )

    # ---------------------------
    # MARKET POSITION
    # ---------------------------
    builder.add_section(
        "Market Position",
        f"""
Current rating: {rating} ⭐<br/>
Market average: {analysis['avg_market_rating']} ⭐<br/><br/>

<b>Position:</b> {analysis['position']}
"""
    )

    # ---------------------------
    # COMPETITORS
    # ---------------------------
    comp_list = "<br/>".join([f"- {c['name']} → ⭐ {c['rating']} ({c['reviews']})" for c in competitors])

    builder.add_section(
        "Market Competitors",
        comp_list
    )

    # ---------------------------
    # GROWTH (بيع)
    # ---------------------------
    builder.add_section(
        "Growth Opportunity",
        f"""
Clear opportunity to increase revenue within 90 days.<br/><br/>

By improving visibility and conversion strategy,
this business can realistically achieve:<br/>
<b>{analysis['growth']}</b>
"""
    )

    # ---------------------------
    # 🔥 REVENUE LEAKAGE
    # ---------------------------
    builder.add_section(
        "Revenue Leakage",
        f"""
<b>⚠️ Critical Revenue Loss</b><br/><br/>

Your business is currently losing approximately 
<b>${analysis['revenue_loss_range']}</b> per day.<br/><br/>

This is driven by low visibility compared to competitors,
resulting in <b>{analysis['lost_customers_range']} potential customers</b>
choosing other restaurants daily.<br/><br/>

<b>Over 30 days:</b><br/>
<b>${int(analysis['avg_order_value']) * 30 * int(analysis['lost_customers_range'].split('-')[0])}+ </b><br/><br/>

This is not a marketing issue — this is a direct revenue leak.
"""
    )

    # ---------------------------
    # RISK
    # ---------------------------
    builder.add_section(
        "Risk Analysis",
        """
If no action is taken, competitors will continue capturing
market demand daily.<br/><br/>

This will lead to:
- Reduced visibility<br/>
- Lower customer acquisition<br/>
- Ongoing revenue loss<br/><br/>

The longer this continues, the harder it becomes to recover.
"""
    )

    # ---------------------------
    # STRATEGY
    # ---------------------------
    strategy_text = "<br/>".join([f"- {k}: {v}" for k, v in growth_report.strategic_overview.items()])
    builder.add_section("Strategy", strategy_text)

    # ---------------------------
    # MONTHLY PLAN
    # ---------------------------
    monthly_text = "<br/>".join([f"- {item}" for item in growth_report.monthly_plan_snapshot])
    builder.add_section("Monthly Plan", monthly_text)

    # ---------------------------
    # EXECUTION
    # ---------------------------
    execution_text = "<br/>".join([f"- {item}" for item in growth_report.execution_priorities])
    builder.add_section("Execution Priorities", execution_text)

    # ---------------------------
    # 🚀 CTA
    # ---------------------------
    builder.add_section(
        "Next Step",
        """
This report clearly shows a measurable revenue loss.<br/><br/>

If you want to recover this lost revenue within the next 30–60 days,
the next step is to implement a structured growth strategy.<br/><br/>

We can start immediately and track results within weeks.
"""
    )

    # ---------------------------
    # BUILD
    # ---------------------------
    builder.build()

    print(f"\n✅ PDF Generated: {filename}")


if __name__ == "__main__":
    run()