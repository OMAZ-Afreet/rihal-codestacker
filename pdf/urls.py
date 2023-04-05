from django.urls import path

from . import views as v

urlpatterns = [
    path('upload/', v.upload_pdf),
    path('parsing-status/<int:id>/', v.get_parsing_status),
    # path('', v.t),
]
