from io import StringIO

from django.core.files.base import File

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import resolve1


def parse_pdf(pdf: File) -> tuple[int, str]:
    text = StringIO()
    
    with pdf as file:
        parser = PDFParser(file)
        doc = PDFDocument(parser)
        resource_manager = PDFResourceManager(caching=True)
        device = TextConverter(resource_manager, text, laparams=LAParams())
        interpreter = PDFPageInterpreter(resource_manager, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    return resolve1(doc.catalog['Pages'])['Count'], text.getvalue()


# from django.core.files.storage import default_storage
# def doit(file):
#     text = StringIO()
#     with file as in_file:
#         parser = PDFParser(in_file)
#         doc = PDFDocument(parser)
#         resource_manager = PDFResourceManager(caching=True)
#         device = TextConverter(resource_manager, text, laparams=LAParams())
#         interpreter = PDFPageInterpreter(resource_manager, device)
#         for page in PDFPage.create_pages(doc):
#             interpreter.process_page(page)

#     return resolve1(doc.catalog['Pages'])['Count'], text.getvalue()
