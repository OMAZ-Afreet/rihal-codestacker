from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('account/', include('account.urls')),
    path('pdf/', include('pdf.urls')),
    path('search/', include('search.urls')),
    path('docs/', include('docs.urls')),
]


handler404 = "home.views._404"