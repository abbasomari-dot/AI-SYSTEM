from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os


class PDFReportBuilder:

    def __init__(self, client_name, data):
        self.client_name = client_name
        self.data = data

    def build(self):

        os.makedirs("clients", exist_ok=True)

        file_path = f"clients/{self.client_name}_growth_report.pdf"

        styles = getSampleStyleSheet()

        story = []

        story.append(Paragraph(f"{self.client_name} Growth Strategy Report", styles['Title']))
        story.append(Spacer(1, 20))

        story.append(Paragraph("Executive Summary", styles['Heading2']))
        story.append(Paragraph(self.data["recommendation"], styles['BodyText']))
        story.append(Spacer(1, 20))

        story.append(Paragraph("Business Diagnosis", styles['Heading2']))
        story.append(Paragraph(f"Rating: {self.data['rating']}", styles['BodyText']))
        story.append(Paragraph(f"Reviews: {self.data['reviews']}", styles['BodyText']))
        story.append(Paragraph(f"Core Problem: {self.data['core_problem']}", styles['BodyText']))
        story.append(Spacer(1, 20))

        story.append(Paragraph("Growth Strategy", styles['Heading2']))
        story.append(Paragraph(f"Primary Strategy: {self.data['primary_lever']}", styles['BodyText']))
        story.append(Paragraph(f"Campaign Framework: {self.data['campaign_type']}", styles['BodyText']))
        story.append(Paragraph(f"Content Strategy: {self.data['offer_strategy']}", styles['BodyText']))
        story.append(Spacer(1, 20))

        story.append(Paragraph("90 Day Action Plan", styles['Heading2']))
        story.append(Paragraph(f"Month 1: {self.data['month1']}", styles['BodyText']))
        story.append(Paragraph(f"Month 2: {self.data['month2']}", styles['BodyText']))
        story.append(Paragraph(f"Month 3: {self.data['month3']}", styles['BodyText']))

        doc = SimpleDocTemplate(file_path)

        doc.build(story)

        return file_path