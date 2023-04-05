from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import resolve1


def parse_pdf(path: str) -> tuple[int, str]:
    text = StringIO()
    
    with open(path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        resource_manager = PDFResourceManager(caching=True)
        device = TextConverter(resource_manager, text, laparams=LAParams())
        interpreter = PDFPageInterpreter(resource_manager, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    return resolve1(doc.catalog['Pages'])['Count'], text.getvalue()