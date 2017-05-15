"""scrapy_drf_mongo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from django_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.BbcApiView.as_view()),
    url(r'^home$', views.BbcApiView.as_view()),
    url(r'^title$', views.TitleApiView.as_view()),
    url(r'^heading$', views.HeadingApiView.as_view()),
    url(r'^tag$', views.TagApiView.as_view()),
    url(r'^n=(?P<n>[0-9]+)$', views.ArticleApiView.as_view()),
    url(r'^tag=(?P<tag_name>.*)$', views.TagDetailsApiView.as_view()),
    url(r'^title=(?P<title>.*)$', views.TitleDetailsApiView.as_view()),
    url(r'^heading=(?P<heading>.*)$', views.HeadingDetailsApiView.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)