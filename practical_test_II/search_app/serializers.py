"""
Module containing serealizer class
"""


from rest_framework import serializers
from search_app.models import Search

class SearchAppSerializer(serializers.ModelSerializer):
    """
    Class to serialize search objects
    """
    class Meta:
        model = Search
        fields = ['id', 'keyword', 'created_at', 'results']
