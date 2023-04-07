from django.urls import path

from . import views as v

urlpatterns = [
  path('', v.search),
  path('count-word/<int:id>/<str:word>/', v.count_word),
]
