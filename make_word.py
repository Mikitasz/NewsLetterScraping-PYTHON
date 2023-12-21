
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor, Pt
from docx.shared import Inches
from docx import Document
import docx
def add_hyperlink(paragraph, text, url):

    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

    hyperlink = docx.oxml.shared.OxmlElement('w:hyperlink')
    hyperlink.set(docx.oxml.shared.qn('r:id'), r_id, )

    new_run = docx.text.run.Run(
        docx.oxml.shared.OxmlElement('w:r'), paragraph)
    new_run.text = text

    hyperlink.append(new_run._element)
    paragraph._p.append(hyperlink)
    return hyperlink
def word_format(item_text,item_main_text,item_link):


    document = Document()
    
    title = document.add_paragraph(item_text)
    text = document.add_paragraph(item_main_text)
    link = document.add_paragraph("Link: ")
    paragraphs = document.paragraphs
    print(paragraphs)
    add_hyperlink(link, item_link, item_link)
   
    run = title.runs[0]
    font = run.font
    font.color.rgb = RGBColor(0, 0, 0)  # RGB values for black
    title.alignment = 0  # 0 for left-align 
    font.size = Pt(16)  # Font size 16 pointss

    document.save('example_document.docx')