from django.urls import path

from . import views as v

urlpatterns = [
    path('upload/', v.upload_pdf),
    path('get/', v.get_pdf_info),
    # path('', v.testo),
]
