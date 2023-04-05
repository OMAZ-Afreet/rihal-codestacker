from django.urls import path, include

urlpatterns = [
    path('pdf/', include('pdf.urls'))
]
