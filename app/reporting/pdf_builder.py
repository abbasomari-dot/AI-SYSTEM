from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

import matplotlib.pyplot as plt
import os


class PDFReportBuilder:

    def __init__(self, filename):
        self.doc = SimpleDocTemplate(filename, pagesize=A4)
        self.elements = []
        self.styles = getSampleStyleSheet()

        # Styles
        self.title_style = ParagraphStyle(
            name="Title",
            fontSize=22,
            leading=26,
            spaceAfter=20,
            alignment=1
        )

        self.heading_style = ParagraphStyle(
            name="Heading",
            fontSize=16,
            leading=20,
            spaceAfter=10,
            textColor=colors.HexColor("#2E4053")
        )

        self.body_style = ParagraphStyle(
            name="Body",
            fontSize=11,
            leading=16,
            spaceAfter=8
        )

    # ---------------------------
    # COVER PAGE
    # ---------------------------
    def add_cover_page(self, name):
        self.elements.append(Spacer(1, 200))
        self.elements.append(Paragraph(name, self.title_style))
        self.elements.append(Spacer(1, 20))
        self.elements.append(Paragraph("Growth Strategy Report", self.heading_style))
        self.elements.append(PageBreak())

    # ---------------------------
    # TITLE
    # ---------------------------
    def add_title(self, text):
        self.elements.append(Paragraph(text, self.title_style))
        self.elements.append(Spacer(1, 20))

    # ---------------------------
    # SECTION
    # ---------------------------
    def add_section(self, title, content):
        self.elements.append(Paragraph(title, self.heading_style))
        self.elements.append(Paragraph(content, self.body_style))
        self.elements.append(Spacer(1, 15))

    # ---------------------------
    # CHART
    # ---------------------------
    def add_chart(self, rating, reviews):

        plt.figure()
        plt.bar(["Rating", "Reviews/100"], [rating, reviews / 100])
        plt.title("Performance Overview")

        chart_path = "chart.png"
        plt.savefig(chart_path)
        plt.close()

        self.elements.append(Spacer(1, 20))
        self.elements.append(Image(chart_path, width=400, height=250))
        self.elements.append(Spacer(1, 20))

    # ---------------------------
    # KPI TABLE
    # ---------------------------
    def add_kpi_table(self, kpis):

        data = [["KPI", "Target"]]

        for k, v in kpis.items():
            data.append([k, v])

        table = Table(data)

        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.black),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ]))

        self.elements.append(Spacer(1, 10))
        self.elements.append(table)
        self.elements.append(Spacer(1, 20))

    # ---------------------------
    # BUILD
    # ---------------------------
    def build(self):
        self.doc.build(self.elements)