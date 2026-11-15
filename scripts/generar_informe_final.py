"""Construye el PDF de entrega a partir de docs/INFORME_FINAL_AULA.md."""
from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/INFORME_FINAL_AULA.md"
OUTPUT = ROOT / "output/pdf/INFORME_FINAL_AULA.pdf"
INK = HexColor("#192e3b")
ACCENT = HexColor("#14685c")
MUTED = HexColor("#4b616a")
LINE = HexColor("#cfded8")
PALE = HexColor("#edf5f1")

styles = {
    "cover": ParagraphStyle("cover", fontName="Times-Bold", fontSize=46, leading=48,
                            textColor=INK, spaceBefore=12, spaceAfter=3, keepWithNext=True),
    "subtitle": ParagraphStyle("subtitle", fontName="Times-Roman", fontSize=22, leading=26,
                               textColor=INK, spaceAfter=12, keepWithNext=True),
    "meta": ParagraphStyle("meta", fontName="Helvetica", fontSize=10, leading=14.5,
                           textColor=MUTED, spaceAfter=11, keepWithNext=True),
    "page": ParagraphStyle("page", fontName="Times-Bold", fontSize=25, leading=29,
                           textColor=INK, spaceAfter=10, keepWithNext=True),
    "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=11.5, leading=15,
                              textColor=ACCENT, spaceBefore=9, spaceAfter=5, keepWithNext=True),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10.6, leading=14.5,
                           textColor=INK, spaceAfter=7),
    "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=9.8, leading=13.1,
                           textColor=INK),
}


def markup(value):
    escaped = escape(value)
    with_links = re.sub(
        r"\[([^\]]+)\]\((https://[^ )]+)\)",
        r'<link href="\2" color="#14685c"><u>\1</u></link>',
        escaped,
    )
    return re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", with_links)


def make_table(block, width):
    lines = block.splitlines()
    rows = [[cell.strip() for cell in line.strip("|").split("|")]
            for line in [lines[0], *lines[2:]]]
    fractions = {2: (0.36, 0.64), 3: (0.32, 0.34, 0.34)}[len(rows[0])]
    data = [
        [Paragraph(("<b>" + markup(cell) + "</b>") if i == 0 else markup(cell), styles["cell"])
         for cell in row]
        for i, row in enumerate(rows)
    ]
    table = Table(data, colWidths=[width * part for part in fractions], repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PALE),
        ("LINEBELOW", (0, 0), (-1, -1), 0.45, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


def running_text(canvas, document):
    page_width, page_height = A4
    left, right = 48, page_width - 48
    canvas.setFillColor(ACCENT)
    canvas.rect(left, page_height - 29, 26, 3, stroke=0, fill=1)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawString(left + 36, page_height - 30, "TRABAJO INTEGRADOR")
    canvas.drawRightString(right, page_height - 30, "UCA / INTELIGENCIA ARTIFICIAL")
    canvas.setStrokeColor(LINE)
    canvas.line(left, 43, right, 43)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(left, 29, "AULA  /  SEGUNDO SEMESTRE DE 2026")
    canvas.drawRightString(right, 29, str(document.page))


def main():
    document = SimpleDocTemplate(
        str(OUTPUT), pagesize=A4, leftMargin=48, rightMargin=48,
        topMargin=49, bottomMargin=54,
        title="Aula - Informe final de Inteligencia Artificial",
        author="Lucas Di Tomase y Pablo Margewka",
        subject="Universidad Católica Argentina - Ingeniería Informática - Segundo semestre de 2026",
    )
    story = []
    first = True
    for block in SOURCE.read_text(encoding="utf-8").strip().split("\n\n"):
        if block == "<!-- pagebreak -->":
            story.append(PageBreak())
            first = False
        elif block.startswith("# "):
            title, subtitle = block.splitlines()
            story.append(Paragraph(markup(title[2:]), styles["cover"]))
            story.append(Paragraph(markup(subtitle[3:]), styles["subtitle"]))
        elif block.startswith("@"):
            metadata = [markup(line.split(" ", 1)[1]) for line in block.splitlines()]
            metadata[-1] = "<b>" + metadata[-1] + "</b>"
            story.append(Paragraph("<br/>".join(metadata), styles["meta"]))
        elif block.startswith("### "):
            story.append(Paragraph(markup(block[4:]), styles["section"]))
        elif block.startswith("## "):
            story.append(Paragraph(markup(block[3:]), styles["subtitle" if first else "page"]))
        elif block.startswith("|"):
            story.extend((make_table(block, document.width - 12), Spacer(1, 7)))
        else:
            story.append(Paragraph(markup(block.replace("\n", " ")), styles["body"]))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    document.build(story, onFirstPage=running_text, onLaterPages=running_text)
    print(OUTPUT)


if __name__ == "__main__":
    main()
