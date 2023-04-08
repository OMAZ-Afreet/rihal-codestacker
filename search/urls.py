from django.urls import path

from . import views as v

urlpatterns = [
  path('', v.search),
  path('stop-words/', v.list_stop_words),
  path('count-word/<int:id>/<str:word>/', v.count_word),
  path('top5/<int:id>/', v.top_5_words),
]
