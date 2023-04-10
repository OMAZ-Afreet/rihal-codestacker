from django.urls import path

from .views import sign_up, test_access

urlpatterns = [
    path('sign-up/', sign_up),
    path('', test_access),
    
]
