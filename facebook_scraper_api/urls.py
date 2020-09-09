from django.contrib import admin
from django.urls import path, include

from news.views import NewsView

urlpatterns = [
    path('', NewsView.as_view(), name='news-view'),
    path('admin/', admin.site.urls),
]
