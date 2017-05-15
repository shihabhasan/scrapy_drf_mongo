# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

class ScrapyAppItem(scrapy.Item):
    # define the fields for your item here like:
    article_title = Field()
    article_tag = Field()
    article_heading = Field()
    article_text = Field()
    article_url = Field()
