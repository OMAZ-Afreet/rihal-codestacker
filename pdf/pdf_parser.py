from io import StringIO

import fitz

from .utils import get_file

#* Old implementation *#
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfinterp import resolve1


# def parse_pdf(pdf: File) -> tuple[int, str]:
#     text = StringIO()
    
#     with pdf:
#         parser = PDFParser(pdf)
#         doc = PDFDocument(parser)
#         resource_manager = PDFResourceManager(caching=True)
#         device = TextConverter(resource_manager, text, laparams=LAParams())
#         interpreter = PDFPageInterpreter(resource_manager, device)
#         for page in PDFPage.create_pages(doc):
#             interpreter.process_page(page)

#     return resolve1(doc.catalog['Pages'])['Count'], text.getvalue()


def parse_pdf(path: str) -> tuple[int, str]:
    text = StringIO()
    with get_file(path) as pdf:
        doc = fitz.open('pdf', pdf.read())
        for page in doc:
            text.write(page.get_text())
    
    return len(doc), text.getvalue()


def page_to_image(path: str, page_num: int, dpi=96):
    '''
    Possible error: ValueError if page_num out pf range
    '''
    if page_num <= 0:
        raise ValueError('invalid page number')

    pdf = get_file(path)
    doc = fitz.open('pdf', pdf.read())
    page = doc.load_page(page_num-1)
    
    return page.get_pixmap(dpi=dpi).tobytes()