#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy

class QuotesSpider(scrapy.Spider):

    name = "quotes"
    start_urls = [
        'http://blog.csdn.net/github_33644920',
    ]

    def parse(self, response):
        for quote in response.css('div.article_item'):
            title = quote.css('a[href*=details]::text').extract_first().replace("\r\n","").strip()
            view_num = quote.css('span.link_view::text').extract_first().replace("(","").replace(")","").strip()
            yield {
                'article_title': title,
                'view_num': view_num
            }

        next_page = response.css('div.pagelist strong+a::attr("href")').extract_first()
        print "guoshijie",next_page
        next_url ="http://blog.csdn.net"+next_page
        print next_url
        if next_url is not None:
            yield response.follow(next_url, self.parse)
