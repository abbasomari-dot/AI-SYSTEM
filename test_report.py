from app.growth.growth_orchestrator import GrowthOrchestrator
from app.services.pdf_report_builder import PDFReportBuilder


# Generate Report
report = GrowthOrchestrator.run(
    name="Test Restaurant",
    lead_tier="A",
    core_problem="Low visibility",
    social_status="Weak",
    rating=4.6,
    reviews=850
)

# Print to terminal
print("OVERVIEW:\n", report.overview)
print("\nINSIGHT:\n", report.insight)
print("\nOPPORTUNITY:\n", report.opportunity)
print("\nACTION PLAN:")
for step in report.action_plan:
    print("-", step)


# Generate PDF
pdf_builder = PDFReportBuilder("Test Restaurant", report)
file_path = pdf_builder.build()

print("\nPDF Generated at:", file_path)