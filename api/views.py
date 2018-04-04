from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Lists all Names or create a new one
class NameList(APIView):

    def get(self, request):
        names = Name.objects.all()
        serializer = NameSerializer(names, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class KeywordList(APIView):

    def get(self, request):
        keywords = Keyword.objects.all()
        serializer = KeywordSerializer(keywords, many=True)
        return Response(serializer.data)

    def post(self):
        pass
