from django.http import FileResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

from search.models import PDFSearch
from .models import PDF
from .serializers import UploadPDFSerializer, PDFSerializer, NewPDFSerializer
from .tasks import parse_pdf_task, delete_pdf_object


@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def upload_pdf(req, *args, **kwargs):
    ser = UploadPDFSerializer(data=req.data)
    if ser.is_valid(raise_exception=True):
        files = ser.validated_data.pop('file')
        pdfs = []
        for f in files:
            if PDF.objects.filter(pdf_file=f.name).exists():
                return Response({'error': f'file: {f.name} already exists!'})
            pdf = PDF.objects.create(pdf_file=f, size=f.size)
            pdfs.append(pdf)
            parse_pdf_task.delay(pdf.id, pdf.pdf_file.name)
        return Response({'success': 'file/s uploaded.', 'file/s': NewPDFSerializer(pdfs, many=True).data})
    else:
        return Response({'failed': ser.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_parsing_status(req, id, *args, **kwargs):
    try:
        p = PDF.objects.only('pdf_file', 'parsing_status').get(id=id)
        return Response({'file': p.pdf_file.name, 'parsing_status': p.parsing_status})
    except PDF.DoesNotExist:
        return Response({'error': f'pdf file with ID:{id} NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def list_pdf(req, *args, **kwargs):
    p = PDF.objects.all()
    return Response(PDFSerializer(p, many=True).data)


@api_view(["GET"])
def get_pdf(req, id, *args, **kwargs):
    try:
        p = PDF.objects.get(id=id)
        return Response(PDFSerializer(p).data)
    except PDF.DoesNotExist:
        return Response({'error': f'pdf file with ID:{id} NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def download_pdf(req, id, *args, **kwargs):
    try:
        p = PDF.objects.get(id=id)
        res = FileResponse(p.pdf_file, filename=p.pdf_file.name, as_attachment=True)
        return res
    except PDF.DoesNotExist:
        return Response({'error': f'pdf file with ID:{id} NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)



@api_view(["GET"])
def list_pdf_sentences(req, id, *args, **kwargs):
    try:
        p = PDF.objects.only('id', 'pdf_file').get(id=id)
        sentences = PDFSearch.objects.filter(pdf=p).values_list('sentence', flat=True).order_by('id')
        return Response({'id': p.id, 'name': p.pdf_file.name, 'sentences': list(sentences)})
    except PDF.DoesNotExist:
        return Response({'error': f'pdf file with ID:{id} NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def delete_pdf(req, id, *args, **kwargs):
    try:
        p = PDF.objects.get(id=id)
        p.delete()
        delete_pdf_object.delay(p.pdf_file.name)
        return Response({'success': f'pdf: {p.pdf_file.name} DELETED'})
    except PDF.DoesNotExist:
        return Response({'error': f'pdf file with ID:{id} NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)











# from .forms import PDFForm
#from django.shortcuts import render

# def t(req):
#     if req.method == 'POST':
#         form = PDFForm(req.POST, req.FILES)
#         if form.is_valid():
#             print(type(form.cleaned_data['pdf_file']))
#             return render(req, 'pdf/index.html', {'form': form})
#     else:
#         form = PDFForm()
#         return render(req, 'pdf/index.html', {'form': form})
# from django.core.files.uploadedfile import InMemoryUploadedFile