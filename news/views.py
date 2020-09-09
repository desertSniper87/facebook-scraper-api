from django.http import JsonResponse
from facebook_scraper import get_posts
from rest_framework import views
from rest_framework.response import Response
from rest_framework.utils import json

from news.serializers import NewsSerializer


class NewsView(views.APIView):
    def get(self, request):
        page_name = 'DailyProthomAlo'
        posts = get_posts(page_name)

        return Response([post for post in posts])


