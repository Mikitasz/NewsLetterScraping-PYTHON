
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor, Pt
from docx.shared import Inches
from docx import Document

import docx

class Word_docx:
    def __init__(self,images_folder,item_link,titlestext,item_main_text) -> None:
        self._images_folder = images_folder
    
        self._item_link=item_link
 
        self._titlestext=titlestext
        self._item_main_text=item_main_text
     
        self.main_text_font_size=16

    def add_hyperlink(self,paragraph, text, url):

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
    def word_format(self):

        document = Document()
        title = document.add_paragraph(self._titlestext)
        text = document.add_paragraph(str(self._item_main_text)[33:-49])
        link = document.add_paragraph("Link: ")
        paragraphs = document.paragraphs
        print(paragraphs)
        self.add_hyperlink(link,self._item_link,self._item_link)
        run = title.runs[0]
        font = run.font
        font.color.rgb = RGBColor(0, 0, 0)  # RGB values for black
        title.alignment = 0  # 0 for left-align 
        font.size = Pt(self.main_text_font_size)  # Font size 16 pointss

        document.save('example_document.docx')
    
