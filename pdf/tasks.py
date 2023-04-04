from celery import shared_task
from celery.utils.log import get_task_logger
from pdfminer.high_level import extract_text, extract_pages

from .models import PDF

logger = get_task_logger(__name__)

@shared_task
def parse_pdf(id, pdf):
    try:
        pass
    except Exception as e:
        logger.error(
        f'''
            PDF_ID: {id},
            
            Exception: {type(e)},
            
            args: {e.args}
        '''
        )