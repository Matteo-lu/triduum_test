from django.urls import path
from search_app.views import search_list, search_info, search_by_id
from django.urls import re_path


urlpatterns = [
    re_path('search/?$', search_list),
    re_path('search/info/?$', search_info),
    path('search/<uuid:pk>', search_by_id)
]
