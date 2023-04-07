from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import PDFSearch
from .serializers import SearchSerializer, PDFSearchSerializer
from .algorithms import count_word_algo

@api_view(["GET"])
def search(req, *args, **kwargs):
    ser = SearchSerializer(data=req.data)
    if ser.is_valid():
        s = ser.validated_data['search']
        result = PDFSearch.objects.filter(sentence__icontains=s)
        return Response(PDFSearchSerializer(result, many=True).data)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)



import time
@api_view(["GET"])
def count_word(req, id, word, *args, **kwargs):
    result = PDFSearch.objects.filter(pdf_id=id, sentence__iregex=fr'\b{word}\b').values_list('sentence', flat=True)
    sentences = list(result)
    return Response({'pdf_ID': id, 'word': word, 'count': count_word_algo(word, sentences), 'sentences': sentences})
