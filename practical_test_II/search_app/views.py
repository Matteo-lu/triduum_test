from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from search_app.models import Search
from search_app.serializers import SearchAppSerializer
from rest_framework.decorators import api_view

from django.db.models import Count

# Create your views here.
@api_view(['GET', 'POST'])
def search_list(request):
    if request.method == 'GET':
        searches = Search.objects.all()

        keyword = request.GET.get('keyword', None)
        if keyword is not None:
            searches = Search.filter(name_icontains=keyword)
    
        searches_serializer = SearchAppSerializer(searches, many=True)
        return JsonResponse(searches_serializer.data, safe=False)

    elif request.method == 'POST':
        searches_data = JSONParser().parse(request)
        searches_serializer = SearchAppSerializer(data=searches_data)
        if searches_serializer.is_valid():
            searches_serializer.save()
            return JsonResponse(searches_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(searches_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def search_info(request):
    if request.method == 'GET':
        count = Search.objects.values_list('keyword').annotate(keyword_count=Count('keyword')).order_by('-keyword_count')
        print(count)
