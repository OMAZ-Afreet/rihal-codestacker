from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

from .models import PDF
from .serializers import UploadPDFSerializer, PDFSerializer, NewPDFSerializer
from .tasks import parse_pdf
from .utils import local_save


@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def upload_pdf(req, *args, **kwargs):
    ser = UploadPDFSerializer(data=req.data)
    if ser.is_valid(raise_exception=True):
        files = ser.validated_data.pop('file')
        pdfs = []
        for f in files:
            # if PDF.objects.filter(pdf_file=f.name).exists():
            #     return Response({'error': f'file: {f.name} already exists!'})
            # pdf = PDF.objects.create(pdf_file=f, size=f.size)
            # pdfs.append(pdf)
            path = local_save(f)
            parse_pdf.delay(1, path)
        return Response({'success': 'file/s uploaded.', 'file/s': NewPDFSerializer(pdfs, many=True).data})
    else:
        return Response({'failed': ser.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_pdf_info(req):
    parse_pdf.delay(2)
    return Response()










# from .forms import PDFForm
#from django.shortcuts import render

# def testo(req):
#     if req.method == 'POST':
#         form = PDFForm(req.POST, req.FILES)
#         if form.is_valid():
#             print(type(form.cleaned_data['pdf_file']))
#             return render(req, 'pdf/index.html', {'form': form})
#     else:
#         form = PDFForm()
#         return render(req, 'pdf/index.html', {'form': form})
# from django.core.files.uploadedfile import InMemoryUploadedFile