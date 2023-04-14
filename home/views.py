from django.shortcuts import render
from django.http import JsonResponse



def index(request, *args, **kwargs):
    return render(request, 'index.html')


def _404(req, *args, **kwargs):
    return JsonResponse({
        "404 not found": f"This url doesn't exists. Please check {req.scheme}://{req.get_host()}/docs/ for full documentation and available routes."
    })