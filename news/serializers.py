from rest_framework import serializers
from rest_framework.serializers import Serializer


class SingleNewsSerializer(Serializer):
    post_id = serializers.IntegerField()
    text = serializers.CharField()
    time = serializers.DateTimeField()
    image = serializers.URLField()

class NewsSerializer(Serializer):
    news = SingleNewsSerializer(many=True)