# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:49:47 2017

@author: Long Nguyen
"""

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    allowed_domains = ["https://www.yellowpages.com/los-angeles-ca/attorneys?refinements=bbb_grade_display%3A1"]
    start_urls = ["https://www.yellowpages.com/los-angeles-ca/attorneys?refinements=bbb_grade_display%3A1"]

    def parse(self, response):
        for result in response.css("div.result"):
            item = {
                'company_name':result.css('span[itemprop="name"]::text').extract_first(),
                'rating':result.css('span.bbb-rating extra-rating::text').extract_first(),
                'street':result.css('span.street-address::text').extract_first(),
                'locality':result.css('span.locality::text').extract_first(),
                'region"':result.css('span[itemprop="addressRegion"]::text').extract_first(),
                'zip':result.css('span[itemprop="postalCode"]::text').extract_first(),
                'phone':result.css('span[itemprop="telephone"]::text').extract_first(),
                'tags':result.css('div.categories').extract(),
                'comment':result.css('p.body with-avatar::text').extract_first()
            }
        
        yield item