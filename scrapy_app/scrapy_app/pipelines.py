# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class ScrapyAppPipeline(object):
#     def process_item(self, item, spider):
#         return item

import pymongo

class MongoPipeline(object):

    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'bbc_articles')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        bbcDict={}
        if item['article_text'] != []:
            bbcDict['article_title']=item['article_title']
            bbcDict['article_tag']=item['article_tag']
            bbcDict['article_heading']=item['article_heading']
            bbcDict['article_text']=" ".join(item['article_text'])
            bbcDict['article_url']=item['article_url']
            self.db[self.collection_name].insert_one(dict(bbcDict))
            return item