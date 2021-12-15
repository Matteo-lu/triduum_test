from django.urls import path
from search_app.views import search_list, search_info
from django.urls import re_path


urlpatterns = [
    re_path('search/?$', search_list),
    re_path('search/info/?$', search_info)
]
