# -*- coding: utf-8 -*-
import scrapy


class QuotesToscrapeSpider(scrapy.Spider):
    name = 'quotes-toscrape'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
