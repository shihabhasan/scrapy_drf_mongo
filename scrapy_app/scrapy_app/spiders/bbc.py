# -*- coding: utf-8 -*-
import scrapy

from scrapy_app.items import ScrapyAppItem

class BbcSpider(scrapy.Spider):
    name = "bbc"
    allowed_domains = ["bbc.com"]
    start_urls = ['http://bbc.com/']

    def parse(self, response):
        for article in response.css('div.media__content'):
            item = ScrapyAppItem()
            item['article_title'] = article.css('h3.media__title > a.media__link::text').extract_first().strip()
            item['article_tag'] = article.css('a.media__tag::text').extract_first()

            url = article.css('h3.media__title > a.media__link::attr(href)').extract_first()
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details, meta=item)

    def parse_details(self, response):
        item = response.meta
        article_heading = response.css("div.story-body > h1.story-body__h1::text").extract_first()
        article_text = response.css("div.story-body > div.story-body__inner > p::text").extract()
        article_url = response.url
        item['article_heading']=article_heading
        item['article_text']=article_text
        item['article_url']=article_url

        yield item





