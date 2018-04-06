from rest_framework import serializers
from api.models import *

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
