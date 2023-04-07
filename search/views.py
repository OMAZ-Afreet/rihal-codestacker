from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.decorators import api_view

from .models import PDFSearch
from .serializers import SearchSerializer, PDFSearchSerializer
from .algorithms import count_word_algo
from .utils import bench


@api_view(["GET"])
def search(req, *args, **kwargs):
    ser = SearchSerializer(data=req.data)
    if ser.is_valid():
        s = ser.validated_data['search']
        result = PDFSearch.objects.filter(sentence__icontains=s)
        return Response(PDFSearchSerializer(result, many=True).data)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
@cache_page(60 * 60 * 24 * 30)
def count_word(req, id, word, *args, **kwargs):
    result = PDFSearch.objects.filter(pdf_id=id, sentence__iregex=fr'\b{word}\b').values_list('sentence', flat=True)
    sentences = list(result)
    c = bench(count_word_algo, word, sentences)
    return Response({'pdf_ID': id, 'word': word.lower(), 'count': count_word_algo(word, sentences), 'sentences': sentences})









