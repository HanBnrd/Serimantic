from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from src.processing import recommendation


"""
Names
"""
class NameList(APIView):

    def get(self, request):
        names = Name.objects.all()
        serializer = NameSerializer(names, many=True)
        return Response(serializer.data)

    def post(self):
        pass

# Name from id
class NameListId(APIView):

    def get(self, request, *args, **kwargs):
        name_id = kwargs.get('id')
        name = Name.objects.get(id=name_id)
        serializer = NameSerializer(name)
        return Response(serializer.data)

# Name from name
class NameListName(APIView):

    def get(self, request, *args, **kwargs):
        name_name = kwargs.get('name')
        name = Name.objects.get(name=name_name)
        serializer = NameSerializer(name)
        return Response(serializer.data)


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
        name = kwargs.get('name')
        name_id = Name.objects.get(name=name).id
        tags = Tag.objects.filter(name_id=name_id)
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


"""
Recommendation
"""
class Recommendation(APIView):

    def get(self, request, *args, **kwargs):
        series = kwargs.get('series')
        rec = recommendation(series)
        name = Name.objects.get(name=rec)
        serializer = NameSerializer(name)
        return Response(serializer.data)
