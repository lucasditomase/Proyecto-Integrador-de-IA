from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader
base=Path(__file__).resolve().parents[1]
source=(base/'PROPUESTA_PARA_ENTREGA.md').read_text()
output=base/'output/pdf/PROPUESTA_PARA_ENTREGA.pdf'
output.parent.mkdir(parents=True,exist_ok=True)
styles={
 'title':ParagraphStyle('title',fontName='Times-Roman',fontSize=25,leading=28,textColor=HexColor('#142a37'),spaceAfter=12),
 'subtitle':ParagraphStyle('subtitle',fontName='Helvetica',fontSize=9,leading=13,textColor=HexColor('#64716f'),spaceAfter=14),
 'heading':ParagraphStyle('heading',fontName='Helvetica-Bold',fontSize=12,leading=15,textColor=HexColor('#116c62'),spaceBefore=13,spaceAfter=6,keepWithNext=True),
 'body':ParagraphStyle('body',fontName='Helvetica',fontSize=10.3,leading=14.2,textColor=HexColor('#233641'),spaceAfter=8),
 'bullet':ParagraphStyle('bullet',fontName='Helvetica',fontSize=10.1,leading=13.7,textColor=HexColor('#233641'),leftIndent=12,firstLineIndent=-9,spaceAfter=5),
}
def markup(t):
 t=t.replace('→',' > ').replace('—','-').replace('–','-')
 t=escape(t)
 return re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
def footer(c,doc):
 w,h=A4
 c.setStrokeColor(HexColor('#d9dfd8'));c.line(45,39,w-45,39)
 c.setFont('Helvetica',8);c.setFillColor(HexColor('#64716f'))
 c.drawString(45,26,'INTELIGENCIA ARTIFICIAL 2026  /  PROPUESTA DE TRABAJO INTEGRADOR')
 c.drawRightString(w-45,26,str(doc.page))
 c.setFillColor(HexColor('#116c62'));c.rect(45,h-30,32,3,fill=1,stroke=0)
story=[]
for block in source.strip().split('\n\n'):
 if block.startswith('# '):story.append(Paragraph(markup(block[2:]),styles['title']))
 elif block.startswith('**Trabajo integrador'):story.append(Paragraph(markup(block).replace('\n','<br/>'),styles['subtitle']))
 elif block.startswith('## '):
  if block.startswith('## Qué contenidos'):story.append(PageBreak())
  story.append(Paragraph(markup(block[3:]),styles['heading']))
 elif block.startswith('- ') or re.match(r'^\d+\. ',block):
  for line in block.splitlines():story.append(Paragraph(markup(line),styles['bullet']))
 else:story.append(Paragraph(markup(block.replace('\n',' ')),styles['body']))
doc=SimpleDocTemplate(str(output),pagesize=A4,rightMargin=45,leftMargin=45,topMargin=43,bottomMargin=51,title='Aula: asistente para preparar exámenes multiple choice',author='Proyecto integrador de Inteligencia Artificial')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
r=PdfReader(output)
print('PDF:',output,'Páginas:',len(r.pages))
for i,p in enumerate(r.pages,1): print(i,len(p.extract_text()),'caracteres')
