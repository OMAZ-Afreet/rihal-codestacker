from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes

from .models import PDFSearch
from .serializers import SearchSerializer, PDFSearchSerializer

@api_view(["GET"])
def search(req, *args, **kwargs):
    ser = SearchSerializer(data=req.data)
    if ser.is_valid():
        s = ser.validated_data['search']
        result = PDFSearch.objects.filter(sentence__icontains=s)
        return Response(PDFSearchSerializer(result, many=True).data)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)