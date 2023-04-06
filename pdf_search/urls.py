from django.urls import path, include

urlpatterns = [
    path('pdf/', include('pdf.urls')),
    path('search/', include('search.urls')),
]
