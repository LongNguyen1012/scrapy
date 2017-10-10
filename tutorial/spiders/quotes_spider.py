# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:49:47 2017

@author: Long Nguyen
"""

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log("This is a log")
        yield {
            'author_name':response.css('small.author::text').extract_first(),
            'text':response.css('span.text::text').extract_first(),
            'tags':response.css('a.tag::text').extract()
        }