from django.shortcuts import render
from django.http import JsonResponse

from .schemas import SCHEMA

def docs(request, *args, **kwargs):
    return render(request, 'docs.html')

def docs_v2(request, *args, **kwargs):
    return render(request, 'docs_v2.html')

def schema(req, *args, **kwargs):
    return JsonResponse(SCHEMA)