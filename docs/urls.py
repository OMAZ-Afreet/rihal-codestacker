from django.urls import path

from .views import docs, docs_v2, schema

urlpatterns = [
    path('', docs),
    path('v2/', docs_v2),
    path('schema/', schema, name='schema')
]
