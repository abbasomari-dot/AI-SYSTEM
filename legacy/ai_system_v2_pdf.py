# ==========================================
# AI MARKETING SYSTEM V2.2 (PDF GENERATOR)
# ==========================================

import os
import time
import json
from openai import OpenAI

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

# ==========================================
# LOAD API KEY
# ==========================================

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found.")

client = OpenAI(api_key=api_key)

print("\n=== AI MARKETING SYSTEM V2.2 (PDF MODE) ===\n")

# ==========================================
# RESTAURANT INPUT
# ==========================================

restaurant = {
    "name": "Burger Zone",
    "type": "Burger Restaurant",
    "target_audience": "Youth 18-30",
    "offer": "Burger + Fries for 29 QAR",
    "location": "Doha"
}

# ==========================================
# AI GENERATOR (STRUCTURED)
# ==========================================

def generate_ai_marketing_plan(data):

    prompt = f"""
Return ONLY valid JSON.

Structure:

{{
  "strategy": {{
      "positioning": "",
      "tone": "",
      "marketing_channels": ""
  }},
  "instagram_reel": {{
      "hook": "",
      "script": ""
  }},
  "poster": {{
      "headline": "",
      "cta": ""
  }},
  "budget_strategy": "",
  "kpis": []
}}

Restaurant:
Name: {data['name']}
Type: {data['type']}
Target Audience: {data['target_audience']}
Offer: {data['offer']}
Location: {data['location']}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You generate structured JSON marketing plans only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return json.loads(response.choices[0].message.content)


# ==========================================
# PDF GENERATOR
# ==========================================

def generate_pdf(report_data, restaurant_name):

    file_name = f"{restaurant_name.replace(' ', '_')}_Marketing_Report.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    normal_style = styles["Normal"]

    elements.append(Paragraph(f"{restaurant_name} - Marketing Strategy Report", title_style))
    elements.append(Spacer(1, 0.4 * inch))

    # Strategy Section
    elements.append(Paragraph("1. Strategy", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph(f"Positioning: {report_data['strategy']['positioning']}", normal_style))
    elements.append(Paragraph(f"Tone: {report_data['strategy']['tone']}", normal_style))
    elements.append(Paragraph(f"Channels: {report_data['strategy']['marketing_channels']}", normal_style))
    elements.append(Spacer(1, 0.4 * inch))

    # Instagram Reel
    elements.append(Paragraph("2. Instagram Reel", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph(f"Hook: {report_data['instagram_reel']['hook']}", normal_style))
    elements.append(Paragraph(f"Script: {report_data['instagram_reel']['script']}", normal_style))
    elements.append(Spacer(1, 0.4 * inch))

    # Poster
    elements.append(Paragraph("3. Poster Concept", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph(f"Headline: {report_data['poster']['headline']}", normal_style))
    elements.append(Paragraph(f"CTA: {report_data['poster']['cta']}", normal_style))
    elements.append(Spacer(1, 0.4 * inch))

    # Budget
    elements.append(Paragraph("4. Budget Strategy", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph(report_data["budget_strategy"], normal_style))
    elements.append(Spacer(1, 0.4 * inch))

    # KPIs
    elements.append(Paragraph("5. KPIs", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    kpi_list = [ListItem(Paragraph(kpi, normal_style)) for kpi in report_data["kpis"]]
    elements.append(ListFlowable(kpi_list, bulletType="bullet"))

    doc.build(elements)

    return file_name


# ==========================================
# EXECUTION PIPELINE
# ==========================================

start_time = time.time()

report = generate_ai_marketing_plan(restaurant)
pdf_file = generate_pdf(report, restaurant["name"])

end_time = time.time()

print("PDF Generated:", pdf_file)
print("Execution Time:", round(end_time - start_time, 2), "seconds")
print("\n=== V2.2 PDF COMPLETED 🚀 ===")