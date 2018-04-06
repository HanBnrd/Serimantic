from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


"""
Names
"""
class NameList(APIView):

    def get(self, request, *args, **kwargs):
        name_id = kwargs.get('id')
        if name_id == 'all':
            names = Name.objects.all()
            serializer = NameSerializer(names, many=True)
            return Response(serializer.data)
        else:
            name = Name.objects.get(id=name_id)
            serializer = NameSerializer(name)
            return Response(serializer.data)

    def post(self):
        pass


"""
Keywords
"""
class KeywordList(APIView):

    def get(self, request, *args, **kwargs):
        keyword_id = kwargs.get('id')
        if keyword_id == 'all':
            keywords = Keyword.objects.all()
            serializer = KeywordSerializer(keywords, many=True)
            return Response(serializer.data)
        else:
            keyword = Keyword.objects.get(id=keyword_id)
            serializer = KeywordSerializer(keyword)
            return Response(serializer.data)

    def post(self):
        pass


"""
Tags
"""
class TagList(APIView):

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self):
        pass

# Tags filtered by name
class NameFilter(APIView):

    def get(self, request, *args, **kwargs):
        series = kwargs.get('series')
        series_id = Name.objects.get(name=series).id
        tags = Tag.objects.filter(name_id=series_id)
        keywords = set()
        for tag in tags:
            keywords.add(tag.keyword)
        serializer = KeywordSerializer(keywords, many=True)
        return Response(serializer.data)

# Tags filtered by keyword
class KeywordFilter(APIView):

    def get(self, request, *args, **kwargs):
        keyword = kwargs.get('keyword')
        keyword_id = Keyword.objects.get(keyword=keyword).id
        tags = Tag.objects.filter(keyword_id=keyword_id)
        names = set()
        for tag in tags:
            names.add(tag.name)
        serializer = NameSerializer(names, many=True)
        return Response(serializer.data)
