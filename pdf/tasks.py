import re
from itertools import islice

from celery import shared_task
from celery.utils.log import get_task_logger

from search.models import PDFSearch
from .models import PDF
from .pdf_parser import parse_pdf
from .exceptions import PDFTaskUpdateFailed
from .utils import get_file, delete_file

logger = get_task_logger(__name__)

RE = re.compile(r'(?<!Dr)(?<!Mr)(?<!Mrs)(?<!\b\d)\s*[.!?\n]\s+')

def log_msg(id: int, err: Exception):
    logger.error(
        f'''
            PDF_ID: {id},
            
            Exception: {type(err)},
            
            args: {err.args}
        '''
        )


@shared_task
def parse_pdf_task(id: int, path: str):
    try:
        p, text = parse_pdf(path)
        
        raw_sentences = re.split(RE, text)
        # generator for a valid sentence
        sentences = (PDFSearch(pdf_id=id, sentence=s.replace("\n", " ")) for s in raw_sentences if s)
        
        batch_size = 100
        while True:
            batch = list(islice(sentences, batch_size))
            if not batch:
                break
            PDFSearch.objects.bulk_create(batch, batch_size)
        
        i = PDF.objects.filter(id=id).update(number_of_pages=p, parsing_status='DONE')
        
        if i != 1:
            raise PDFTaskUpdateFailed('pdf record was not updated: parsing status may be inaccurate!')
    except PDFTaskUpdateFailed as pe:
        PDFSearch.objects.filter(pdf_id=id).delete()
        log_msg(id, pe)
    except Exception as e:
        PDF.objects.filter(id=id).update(parsing_status='FAILED')
        log_msg(id, e)




@shared_task
def delete_pdf_object(path: str):
    try:
        delete_file(path)
    except Exception as e:
        log_msg(path, e)