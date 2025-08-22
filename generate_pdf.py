# generate_pdf.py
from fpdf import FPDF
import os


def generate_report(name, suggestions, filename="career_report.pdf"):
    """
    Generate a beautifully styled PDF report from a name and LLM-generated suggestions (string).
    Handles both structured and free-form LLM output.
    """
    pdf = FPDF()
    pdf.add_page()

    # Define font paths
    font_dir = "fonts"
    regular_font = os.path.join(font_dir, "DejaVuSans.ttf")
    bold_font = os.path.join(font_dir, "DejaVuSans-Bold.ttf")

    # Add custom font if available
    if os.path.exists(regular_font) and os.path.exists(bold_font):
        pdf.add_font("DejaVu", "", regular_font, uni=True)   # Regular
        pdf.add_font("DejaVu", "B", bold_font, uni=True)     # Bold
        pdf.set_font("DejaVu", size=12)
    else:
        print("⚠️ DejaVu font not found! Using Helvetica.")
        pdf.set_font("helvetica", size=12)

    # Background color: soft cream
    pdf.set_fill_color(255, 248, 240)
    pdf.rect(0, 0, 210, 297, 'F')

    # Title
    pdf.set_text_color(255, 153, 153)
    pdf.set_font("DejaVu" if os.path.exists(regular_font) else "helvetica", "B", 16)
    pdf.cell(0, 20, f"Career Report for {name.title()}", ln=True, align='C')
    pdf.ln(5)

    # Subtitle
    pdf.set_text_color(68, 68, 68)
    pdf.set_font("DejaVu" if os.path.exists(regular_font) else "helvetica", "", 13)
    pdf.cell(0, 10, "Your Future, Predicted with Love by Pookie 💖", ln=True, align='C')
    pdf.ln(15)

    # Divider
    pdf.set_draw_color(255, 153, 153)
    pdf.line(30, pdf.get_y(), 180, pdf.get_y())
    pdf.ln(10)

    # Section Title: Career Matches
    pdf.set_font("DejaVu" if os.path.exists(bold_font) else "helvetica", "B", 14)
    pdf.set_text_color(255, 105, 180)
    pdf.cell(0, 10, "🎯 Your Top 3 Career Matches", ln=True)
    pdf.ln(8)

    # Reset font and color
    pdf.set_text_color(68, 68, 68)
    pdf.set_font("DejaVu" if os.path.exists(regular_font) else "helvetica", "", 12)

    # Process suggestions line by line
    lines = suggestions.strip().split('\n')
    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            continue

        # Detect if it's a numbered career line (e.g. "1. Data Scientist")
        if clean_line[0].isdigit() and '.' in clean_line.split('.')[0]:
            # Job title line
            pdf.set_font("DejaVu" if os.path.exists(bold_font) else "helvetica", "B", 13)
            pdf.set_text_color(255, 105, 180)
            pdf.cell(0, 8, clean_line, ln=True)
            pdf.set_font("DejaVu" if os.path.exists(regular_font) else "helvetica", "", 12)
            pdf.set_text_color(68, 68, 68)
        else:
            # Tip or explanation line
            pdf.multi_cell(0, 7, f"💡 {clean_line}")
            pdf.ln(2)

    # Divider
    pdf.ln(8)
    pdf.set_draw_color(255, 153, 153)
    pdf.line(30, pdf.get_y(), 180, pdf.get_y())
    pdf.ln(10)

    # Pookie Says Section
    pdf.set_font("DejaVu" if os.path.exists(bold_font) else "helvetica", "B", 14)
    pdf.set_text_color(255, 153, 153)
    pdf.cell(0, 10, "💖 Pookie Says:", ln=True)

    pdf.set_font("DejaVu" if os.path.exists(regular_font) else "helvetica", "", 12)
    pdf.set_text_color(68, 68, 68)

    pookie_message = (
        f"{name.title()}, you're not just a student — you're a future AI leader. "
        "You built a CNN, deployed ML apps, and inspired others. "
        "Keep going, pookiee — the world is watching!"
    )
    pdf.multi_cell(0, 7, pookie_message)
    pdf.ln(10)

    # Save PDF
    pdf.output(filename)
    return filename