from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    ListFlowable,
    ListItem,
    HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime


class PDFGenerator:

    def generate(self, report_data, project_name):

        file_name = f"reports/{project_name.replace(' ', '_')}_Report.pdf"
        doc = SimpleDocTemplate(file_name, pagesize=A4)

        elements = []
        styles = getSampleStyleSheet()

        title_style = styles["Heading1"]
        section_style = styles["Heading2"]
        normal_style = styles["Normal"]

        # COVER PAGE
        elements.append(Spacer(1, 2 * inch))
        elements.append(Paragraph("Strategic Marketing Report", title_style))
        elements.append(Spacer(1, 0.5 * inch))
        elements.append(Paragraph(f"Client: {project_name}", styles["Heading2"]))
        elements.append(Spacer(1, 0.3 * inch))
        elements.append(Paragraph(f"Date: {datetime.now().strftime('%B %Y')}", normal_style))
        elements.append(Spacer(1, 0.5 * inch))
        elements.append(HRFlowable(width="100%", thickness=2, color=colors.black))
        elements.append(PageBreak())

        # EXECUTIVE SUMMARY
        elements.append(Paragraph("Executive Summary", section_style))
        elements.append(Spacer(1, 0.3 * inch))
        elements.append(Paragraph(report_data["executive_summary"], normal_style))
        elements.append(PageBreak())

        # STRATEGIC POSITIONING
        elements.append(Paragraph("Strategic Positioning", section_style))
        elements.append(Spacer(1, 0.3 * inch))
        elements.append(Paragraph(report_data["strategy"]["positioning"], normal_style))
        elements.append(Spacer(1, 0.3 * inch))
        elements.append(Paragraph(f"Brand Tone: {report_data['strategy']['tone']}", normal_style))
        elements.append(Spacer(1, 0.2 * inch))
        elements.append(Paragraph(f"Primary Channels: {report_data['strategy']['marketing_channels']}", normal_style))
        elements.append(PageBreak())

        # GAP ANALYSIS
        elements.append(Paragraph("Strategic Gap Analysis", section_style))
        elements.append(Spacer(1, 0.3 * inch))

        elements.append(Paragraph("Strengths", styles["Heading3"]))
        strengths = [
            ListItem(Paragraph(item, normal_style))
            for item in report_data["strategy"]["gap_analysis"]["strengths"]
        ]
        elements.append(ListFlowable(strengths, bulletType="bullet"))
        elements.append(Spacer(1, 0.3 * inch))

        elements.append(Paragraph("Weaknesses", styles["Heading3"]))
        weaknesses = [
            ListItem(Paragraph(item, normal_style))
            for item in report_data["strategy"]["gap_analysis"]["weaknesses"]
        ]
        elements.append(ListFlowable(weaknesses, bulletType="bullet"))
        elements.append(Spacer(1, 0.3 * inch))

        elements.append(Paragraph("Growth Opportunities", styles["Heading3"]))
        opportunities = [
            ListItem(Paragraph(item, normal_style))
            for item in report_data["strategy"]["gap_analysis"]["growth_opportunity"]
        ]
        elements.append(ListFlowable(opportunities, bulletType="bullet"))
        elements.append(PageBreak())

        # 90-DAY GROWTH ROADMAP
        elements.append(Paragraph("90-Day Growth Roadmap", section_style))
        elements.append(Spacer(1, 0.3 * inch))

        for month, tasks in report_data["strategy"]["growth_roadmap"].items():
            elements.append(Paragraph(month.replace("_", " ").title(), styles["Heading3"]))
            roadmap_items = [
                ListItem(Paragraph(task, normal_style))
                for task in tasks
            ]
            elements.append(ListFlowable(roadmap_items, bulletType="bullet"))
            elements.append(Spacer(1, 0.4 * inch))

        elements.append(PageBreak())

        # CREATIVE PLAN
        elements.append(Paragraph("Creative Plan", section_style))
        elements.append(Spacer(1, 0.3 * inch))
        elements.append(Paragraph("Reel Hook:", styles["Heading3"]))
        elements.append(Paragraph(report_data["creative"]["reel_hook"], normal_style))
        elements.append(Spacer(1, 0.3 * inch))
        elements.append(Paragraph("Reel Script:", styles["Heading3"]))
        elements.append(Paragraph(report_data["creative"]["reel_script"], normal_style))
        elements.append(Spacer(1, 0.3 * inch))
        elements.append(Paragraph("Poster Headline:", styles["Heading3"]))
        elements.append(Paragraph(report_data["creative"]["poster_headline"], normal_style))
        elements.append(Spacer(1, 0.2 * inch))
        elements.append(Paragraph("Call To Action:", styles["Heading3"]))
        elements.append(Paragraph(report_data["creative"]["poster_cta"], normal_style))
        elements.append(PageBreak())

        # KPIs
        elements.append(Paragraph("Performance KPIs", section_style))
        elements.append(Spacer(1, 0.3 * inch))
        kpis = [
            ListItem(Paragraph(kpi, normal_style))
            for kpi in report_data["kpis"]
        ]
        elements.append(ListFlowable(kpis, bulletType="bullet"))

        doc.build(elements)

        return file_name