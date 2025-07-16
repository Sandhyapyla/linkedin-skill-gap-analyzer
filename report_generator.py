from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf_report(name, job_role, matched_skills, missing_skills, score, output_file="skill_report.pdf"):
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 50, "📊 Skill Gap Analysis Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 90, f"Name: {name}")
    c.drawString(50, height - 110, f"Job Role: {job_role}")
    c.drawString(50, height - 130, f"Skill Fit Score: {score}%")
    c.drawString(50, height - 150, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    y = height - 190
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "✅ Matched Skills:")
    c.setFont("Helvetica", 12)
    y -= 20
    for skill in sorted(matched_skills):
        c.drawString(70, y, f"- {skill}")
        y -= 15

    y -= 10
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "❌ Missing Skills:")
    c.setFont("Helvetica", 12)
    y -= 20
    for skill in sorted(missing_skills):
        c.drawString(70, y, f"- {skill}")
        y -= 15
        if y < 100:  # Handle page overflow
            c.showPage()
            y = height - 50

    c.save()
