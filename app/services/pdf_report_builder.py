from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
import os


class PDFReportBuilder:

    def __init__(self, client_name, report):
        self.client_name = client_name
        self.report = report

    # ---------------------------
    # Dynamic Pie Calculation
    # ---------------------------
    def _calculate_opportunity_split(self):
        rating = float(self.report.overview.split("holds a ")[1].split(" rating")[0])
        reviews = int(self.report.overview.split("over ")[1].split(" reviews")[0])

        # Logic (واقعي)
        if rating >= 4.5 and reviews >= 800:
            return (75, 25)
        elif rating >= 4.0:
            return (65, 35)
        else:
            return (50, 50)

    def build(self):

        os.makedirs("clients", exist_ok=True)
        file_path = f"clients/{self.client_name}_growth_report.pdf"

        styles = getSampleStyleSheet()

        # Styles
        title_style = ParagraphStyle(
            'title',
            parent=styles['Title'],
            textColor=colors.HexColor("#111111"),
            spaceAfter=25
        )

        section_style = ParagraphStyle(
            'section',
            parent=styles['Heading2'],
            textColor=colors.HexColor("#0B5394"),
            spaceAfter=10
        )

        body_style = ParagraphStyle(
            'body',
            parent=styles['BodyText'],
            leading=14
        )

        story = []

        # ---------------------------
        # Title
        # ---------------------------
        story.append(Paragraph(f"{self.client_name} Growth Intelligence Report", title_style))

        # ---------------------------
        # Overview
        # ---------------------------
        overview_table = Table([[Paragraph(self.report.overview, body_style)]])
        overview_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F7F7F7")),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ]))
        story.append(overview_table)
        story.append(Spacer(1, 15))

        # ---------------------------
        # Insight
        # ---------------------------
        story.append(Paragraph("Key Insight", section_style))
        story.append(Paragraph(self.report.insight, body_style))
        story.append(Spacer(1, 15))

        # ---------------------------
        # Opportunity
        # ---------------------------
        story.append(Paragraph("Opportunity", section_style))
        story.append(Paragraph(self.report.opportunity, body_style))
        story.append(Spacer(1, 15))

        # ---------------------------
        # Action Plan
        # ---------------------------
        action_rows = [[Paragraph(f"• {a}", body_style)] for a in self.report.action_plan]

        action_table = Table(action_rows)
        action_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#EAF1FB")),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#0B5394")),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))

        story.append(Paragraph("Action Plan", section_style))
        story.append(action_table)
        story.append(Spacer(1, 20))

        # ---------------------------
        # Revenue
        # ---------------------------
        weekly = self.report.revenue['weekly']
        monthly = self.report.revenue['monthly']
        yearly = self.report.revenue['yearly']

        revenue_text = (
            f"<b>Weekly:</b> ${weekly[0]} - ${weekly[1]}<br/>"
            f"<b>Monthly:</b> ${monthly[0]} - ${monthly[1]}<br/>"
            f"<b>Yearly:</b> ${yearly[0]} - ${yearly[1]}"
        )

        revenue_table = Table([[Paragraph(revenue_text, body_style)]])
        revenue_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#E6F4EA")),
            ('BOX', (0, 0), (-1, -1), 1, colors.green),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ]))

        story.append(Paragraph("Revenue Impact", section_style))
        story.append(revenue_table)
        story.append(Spacer(1, 20))

        # ---------------------------
        # Bar Chart
        # ---------------------------
        drawing = Drawing(400, 220)
        chart = VerticalBarChart()

        chart.x = 50
        chart.y = 50
        chart.height = 120
        chart.width = 300

        chart.data = [[weekly[1], monthly[1], yearly[1]]]
        chart.categoryAxis.categoryNames = ['Weekly', 'Monthly', 'Yearly']

        chart.valueAxis.valueMin = 0
        chart.valueAxis.valueMax = yearly[1] * 1.2

        chart.barWidth = 25
        chart.groupSpacing = 15

        drawing.add(chart)
        story.append(drawing)

        story.append(Spacer(1, 20))

        # ---------------------------
        # Pie Chart (Dynamic)
        # ---------------------------
        captured, missed = self._calculate_opportunity_split()

        pie_drawing = Drawing(400, 200)
        pie = Pie()

        pie.x = 150
        pie.y = 20
        pie.width = 120
        pie.height = 120

        pie.data = [captured, missed]
        pie.labels = [
            f'Captured ({captured}%)',
            f'Missed ({missed}%)'
        ]

        pie.slices.strokeWidth = 0.5

        pie_drawing.add(pie)

        story.append(Paragraph("Market Opportunity", section_style))
        story.append(pie_drawing)

        # ---------------------------
        # Build
        # ---------------------------
        doc = SimpleDocTemplate(file_path)
        doc.build(story)

        return file_path