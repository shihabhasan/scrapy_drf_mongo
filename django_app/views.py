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
        all_titles = ScrapyItems.objects.values_list('article_title')
        titleList=[]
        for title in all_titles:
            titleList.append(title)
        context = {"article_title": titleList}
        return Response(context)

class HeadingApiView(APIView):
    def get(self, request):
        all_heading = ScrapyItems.objects.values_list('article_heading')
        headingList=[]
        for heading in all_heading:
            headingList.append(heading)
        context = {"article_heading": headingList}
        return Response(context)

class TagApiView(APIView):
    def get(self, request):
        all_tags = ScrapyItems.objects.values_list('article_tag')
        tagList=[]
        for tag in all_tags:
            if tag not in tagList:
                tagList.append(tag)
        context={"article_tag": tagList}
        return Response(context)

class ArticleApiView(APIView):
    def get(self, request, n):
        n=int(n)
        all_items = ScrapyItems.objects.all()
        serializer = ScrapyItemsSerializer(all_items, many=True)
        if n>0 and n< len(all_items):
            return Response(serializer.data[n-1])
        if n<1:
            context={'Input Error': 'Provide provide positive integer value'}
            return Response(context)
        if n>(len(all_items)-1):
            context = {'Input Error': 'There are '+str(len(all_items)-1)+' articles. Maximum input value is '+str(len(all_items)-1) }
            return Response(context)

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