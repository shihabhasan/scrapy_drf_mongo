# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.db import models

from mongoengine import *

# Create your models here.

class ScrapyItems(Document):
    article_title = StringField()
    article_tag = StringField()
    article_heading = StringField()
    article_text = StringField()
    article_url = StringField()
    def __str__(self):
        return self.article_title
