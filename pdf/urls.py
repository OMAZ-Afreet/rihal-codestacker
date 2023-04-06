from django.urls import path

from . import views as v

urlpatterns = [
    path('upload/', v.upload_pdf),
    path('list/', v.list_pdf),
    path('get/<int:id>/', v.get_pdf),
    path('download/<int:id>/', v.download_pdf),
    path('list-sentences/<int:id>/', v.list_pdf_sentences),
    path('delete/<int:id>/', v.delete_pdf),
    path('parsing-status/<int:id>/', v.get_parsing_status),
    path('<int:id>/get-page/<int:page>/', v.get_page_image),
    path('<int:id>/download-page/<int:page>/', v.download_page_image),
    
    # path('', v.t),
]
