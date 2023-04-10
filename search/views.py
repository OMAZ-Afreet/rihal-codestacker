import json 

from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.decorators import api_view

from pdf_search.paginate import paginate
from pdf.models import PDF
from .models import PDFSearch
from .serializers import SearchSerializer, PDFSearchSerializer, AdvancedSearchSerializer
from .algorithms import count_word_algo, top_5_words_algo
# from .utils import bench
from .stop_words import STOP_WORDS
from .caches import set_top5_cache, check_top5_cache, MONTH
from .advanced import ADVANCE_SEARCH_MODES, match_search


@api_view(["POST"])
def search(req, *args, **kwargs):
    ser = SearchSerializer(data=req.data)
    if ser.is_valid():
        s = ser.validated_data['search']
        result = PDFSearch.objects.filter(sentence__iregex=fr'\m{s}\M')
        if r:=paginate(result, req):
            return Response({'page': f'{r[0].number} of {r[1]}', 'results': PDFSearchSerializer(r[0], many=True).data})
        return Response(PDFSearchSerializer(result, many=True).data)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def advanced_search(req, *args, **kwargs):
    ser = SearchSerializer(data=req.data)
    if ser.is_valid():
        s = ser.validated_data['search']
        valid, mode, result = match_search(s)
        if valid:
            return Response(AdvancedSearchSerializer({'results': result, 'count': len(result), 'mode': mode}).data)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@cache_page(timeout=MONTH)
def count_word(req, id, word, *args, **kwargs):
    if not PDF.objects.filter(id=id).exists():
        return Response({'error': f'pdf file with ID:{id} NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)
    result = PDFSearch.objects.filter(pdf_id=id, sentence__iregex=fr'\m{word}\M').values_list('sentence', flat=True)
    sentences = list(result)
    # c = bench(count_word_algo, word, sentences)
    return Response({'pdf_ID': id, 'word': word.lower(), 'count': count_word_algo(word, sentences), 'sentences': sentences})


@api_view(["GET", "POST"])
def top_5_words(req, id, *args, **kwargs):
    words = req.data.get('ignore', None)
    top = req.data.get('top', None)
    
    is_cached, cached_result = check_top5_cache(id, words, top)
    
    if is_cached:
        return Response(json.loads(cached_result))
    else:
        if not PDF.objects.filter(id=id).exists():
            return Response({'error': f'pdf file with ID:{id} NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)
        sen_gen = (s for s in PDFSearch.objects.filter(pdf_id=id).values_list('sentence', flat=True))
        result = top_5_words_algo(sen_gen, words, top)
        res = {i[0]:i[1] for i in result}
        set_top5_cache(id, words, top, res)
        return Response(res)


@api_view(["GET"])
def list_stop_words(req, *args, **kwargs):
    return Response({'stop_words': STOP_WORDS})


@api_view(["GET"])
def list_advance_modes(req, *args, **kwargs):
    return Response({'Available Advance Search Modes': ADVANCE_SEARCH_MODES})