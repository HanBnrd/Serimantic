from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.db.models import Count
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
class NameFromId(APIView):

    def get(self, request, *args, **kwargs):
        name_id = kwargs.get('id')
        name = Name.objects.get(id=name_id)
        serializer = NameSerializer(name)
        return Response(serializer.data)

# Name from name
class NameFromName(APIView):

    def get(self, request, *args, **kwargs):
        name_name = kwargs.get('name')
        name = Name.objects.get(name=name_name)
        serializer = NameSerializer(name)
        return Response(serializer.data)

# Name from keyword
class NameFromKeyword(APIView):

    def get(self, request, *args, **kwargs):
        keyword = kwargs.get('keyword')
        keyword_id = Keyword.objects.get(keyword=keyword).id
        tags = Tag.objects.filter(keyword_id=keyword_id)
        names = set()
        for tag in tags:
            names.add(tag.name)
        serializer = NameSerializer(names, many=True)
        return Response(serializer.data)

# Name from keyword ids
class NameFromKeywordIds(APIView):

    def get(self, request, *args, **kwargs):
        keyword_set = kwargs.get('keywordids')
        keyword_ids = keyword_set.split('&')
        names = Name.objects.all()
        for keyword_id in keyword_ids:
            for name in Name.objects.all():
                if not Tag.objects.filter(name_id=name.id,keyword_id=keyword_id):
                    names = names.exclude(id=name.id)
        serializer = NameSerializer(names, many=True)
        return Response(serializer.data)


"""
Keywords
"""
class KeywordList(APIView):

    def get(self, request):
        keywords = Keyword.objects.all()
        serializer = KeywordSerializer(keywords, many=True)
        return Response(serializer.data)

    def post(self):
        pass

# Keywords from id
class KeywordFromId(APIView):

    def get(self, request, *args, **kwargs):
        keyword_id = kwargs.get('id')
        keyword = Keyword.objects.get(id=keyword_id)
        serializer = KeywordSerializer(keyword)
        return Response(serializer.data)

# Tags filtered by name
class KeywordFromName(APIView):

    def get(self, request, *args, **kwargs):
        name = kwargs.get('name')
        name_id = Name.objects.get(name=name).id
        tags = Tag.objects.filter(name_id=name_id)
        keywords = set()
        for tag in tags:
            keywords.add(tag.keyword)
        serializer = KeywordSerializer(keywords, many=True)
        return Response(serializer.data)

# Most frequent keywords
class KeywordFrequent(APIView):

    def get(self, request, *args, **kwargs):
        n = int(kwargs.get('n'))
        tags = Tag.objects.values_list('keyword_id').annotate(keyword_count=Count('keyword_id')).order_by('-keyword_count')
        keywords = set()
        for cpt in range(n):
            keyword = Keyword.objects.get(id=tags[cpt][0])
            keywords.add(keyword)
        serializer = KeywordSerializer(keywords, many=True)
        return Response(serializer.data)

# Random keywords
class KeywordRandom(APIView):

    def get(self, request, *args, **kwargs):
        n = int(kwargs.get('n'))
        tags = Tag.objects.values_list('keyword_id').order_by('?')
        keywords = set()
        for cpt in range(n):
            keyword = Keyword.objects.get(id=tags[cpt][0])
            keywords.add(keyword)
        serializer = KeywordSerializer(keywords, many=True)
        return Response(serializer.data)


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
