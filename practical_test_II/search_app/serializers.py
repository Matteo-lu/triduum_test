from rest_framework import serializers
from search_app.models import Search

class SearchAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ['id', 'keyword', 'created_at', 'results']
