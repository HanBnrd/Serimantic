"""Serimantic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views as viewsAPI
from spa import views as viewsSPA

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    # Name API
    url(r'^api/tv/all', viewsAPI.NameList.as_view()),
    # Name from id
    url(r'^api/tv/id/(?P<id>.*)/$', viewsAPI.NameListId.as_view()),
    # Name from name
    url(r'^api/tv/name/(?P<name>.*)/$', viewsAPI.NameListName.as_view()),
    # Keyword API
    url(r'^api/keyword/(?P<id>.*)/$', viewsAPI.KeywordList.as_view()),
    # Tag API
    url(r'^api/tag/all', viewsAPI.TagList.as_view()),
    # Tag from name
    url(r'^api/tag/name/(?P<name>.*)/$', viewsAPI.NameFilter.as_view()),
    # Tag from keyword
    url(r'^api/tag/keyword/(?P<keyword>.*)/$', viewsAPI.KeywordFilter.as_view()),
    # Series recommendation from name
    url(r'^api/recommendation/(?P<series>.*)/$', viewsAPI.Recommendation.as_view()),
    # SPA
    url(r'^', viewsSPA.index, name="index"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
