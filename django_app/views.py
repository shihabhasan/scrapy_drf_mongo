# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import ScrapyItems
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response

class BbcApiView(APIView):
    def get(self, request):
        all_articles = ScrapyItems.objects.all()
        serializer = ScrapyItemsSerializer(all_articles, many=True)
        return Response(serializer.data)

class TitleApiView(APIView):
    def get(self, request):
        all_titles = ScrapyItems.objects.all()
        serializer = ArticleTitleSerializer(all_titles, many=True)
        return Response(serializer.data)

class HeadingApiView(APIView):
    def get(self, request):
        all_titles = ScrapyItems.objects.all()
        serializer = ArticleHeadingSerializer(all_titles, many=True)
        return Response(serializer.data)

class TagApiView(APIView):
    def get(self, request):
        all_tags = ScrapyItems.objects.all()
        serializer = ArticleTagSerializer(all_tags, many=True)
        return Response(serializer.data)

class ArticleApiView(APIView):
    def get(self, request, n):
        all_tags = ScrapyItems.objects.all()
        serializer = ScrapyItemsSerializer(all_tags, many=True)
        return Response(serializer.data[int(n)])

class TagDetailsApiView(APIView):
    def get(self, request, tag_name):
        all_tags = ScrapyItems.objects.filter(article_tag=tag_name)
        serializer = ScrapyItemsSerializer(all_tags, many=True)
        return Response(serializer.data)

class TitleDetailsApiView(APIView):
    def get(self, request, title):
        all_tags = ScrapyItems.objects.filter(article_title=title)
        serializer = ScrapyItemsSerializer(all_tags, many=True)
        return Response(serializer.data)

class HeadingDetailsApiView(APIView):
    def get(self, request, heading):
        all_tags = ScrapyItems.objects.filter(article_heading=heading)
        serializer = ScrapyItemsSerializer(all_tags, many=True)
        return Response(serializer.data)