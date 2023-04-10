from django.urls import path, include

urlpatterns = [
    path('account/', include('account.urls')),
    path('pdf/', include('pdf.urls')),
    path('search/', include('search.urls')),
]
