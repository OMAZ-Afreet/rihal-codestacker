from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .forms import PDFForm


@api_view(["POST"])
def upload_pdf(req, *args, **kwargs):
    pass