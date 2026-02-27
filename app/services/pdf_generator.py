from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus import ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch


class PDFGenerator:

    def generate(self, report_data, restaurant_name):

        file_name = f"reports/{restaurant_name.replace(' ', '_')}_Report.pdf"
        doc = SimpleDocTemplate(file_name, pagesize=A4)

        elements = []
        styles = getSampleStyleSheet()

        elements.append(Paragraph(f"{restaurant_name} Marketing Report", styles["Heading1"]))
        elements.append(Spacer(1, 0.4 * inch))

        elements.append(Paragraph("Executive Summary", styles["Heading2"]))
        elements.append(Paragraph(report_data["executive_summary"], styles["Normal"]))
        elements.append(Spacer(1, 0.4 * inch))

        elements.append(Paragraph("Strategy", styles["Heading2"]))
        elements.append(Paragraph(report_data["strategy"]["positioning"], styles["Normal"]))
        elements.append(Paragraph(report_data["strategy"]["tone"], styles["Normal"]))
        elements.append(Paragraph(report_data["strategy"]["marketing_channels"], styles["Normal"]))
        elements.append(Spacer(1, 0.4 * inch))

        elements.append(Paragraph("Creative Plan", styles["Heading2"]))
        elements.append(Paragraph(report_data["creative"]["reel_hook"], styles["Normal"]))
        elements.append(Paragraph(report_data["creative"]["reel_script"], styles["Normal"]))
        elements.append(Paragraph(report_data["creative"]["poster_headline"], styles["Normal"]))
        elements.append(Paragraph(report_data["creative"]["poster_cta"], styles["Normal"]))
        elements.append(Spacer(1, 0.4 * inch))

        elements.append(Paragraph("KPIs", styles["Heading2"]))
        kpis = [ListItem(Paragraph(kpi, styles["Normal"])) for kpi in report_data["kpis"]]
        elements.append(ListFlowable(kpis, bulletType="bullet"))

        doc.build(elements)

        return file_name