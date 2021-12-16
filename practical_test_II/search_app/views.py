"""
Module containing the endpint views for the API
"""


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
    """View to retrieve and create searches objects

    Returns:
        json: search objects representation with code response
    """
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
            return JsonResponse(
                searches_serializer.data, \
                    status=status.HTTP_201_CREATED
                )
        return JsonResponse(
            searches_serializer.errors, \
                status=status.HTTP_400_BAD_REQUEST
            )

@api_view(['GET'])
def search_info(request):
    """View to retrieve searches report

    Returns:
        json: report with formatted fields
    """
    if request.method == 'GET':
        inform = []
        count = Search.objects.values_list('keyword')\
            .annotate(keyword_count=Count('keyword'))\
            .order_by('-keyword_count')
        for i in range(0, len(count)):
            search = {}
            search["item"] = i
            search["keyword"] = count[i][0]
            search["search_number"] = count[i][1]
            search["last_date"] = Search.objects.filter(
                keyword=count[i][0])\
                    .order_by('-created_at').first().\
                        created_at.strftime("%c")
            search["first_date"] = Search.objects.filter(
                keyword=count[i][0]).order_by('-created_at').\
                    last().created_at.strftime("%c")
            search["results"] = Search.objects.filter(
                keyword=count[i][0])\
                    .order_by('-created_at').first().results
            inform.append(search)
        return JsonResponse(inform, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def search_by_id(request, pk):
    """
    View to retrieve, update and delete search by id
    """
    print("Entramos pa")
    try:
        search = Search.objects.get(id=pk)
    except Search.DoesNotExist:
        return JsonResponse(
                            {'message': 'The element does not exist'},
                            status=status.HTTP_404_NOT_FOUND
                            )
    if (request.method == 'GET'):
        search_serializer = SearchAppSerializer(search)
        return JsonResponse(search_serializer.data, safe=False)

    if (request.method == 'PUT'):
        for att, value in request.data.items():
            if (hasattr(search, att)):
                setattr(search, att, value)
        search_serializer = SearchAppSerializer(search)
        return JsonResponse(search_serializer.data, safe=False)

    if (request.method == 'DELETE'):
        search.delete()
        return JsonResponse(
                            {'message': 'Successfully deleted'}
                            )
