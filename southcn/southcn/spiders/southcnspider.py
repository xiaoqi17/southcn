# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime, timedelta
import time

from southcn.items import SouthcnItem


class SouthcnspiderSpider(scrapy.Spider):
    name = "southcnspider"
    allowed_domains = ["http://epaper.southcn.com/"]
    start_urls = ['http://epaper.southcn.com/']

    def parse(self,response):
        now = datetime.now()
        for i in range(0, 367):
            yestoday = now - timedelta(days=i)
            url = 'http://epaper.southcn.com/nfdaily/html/'+yestoday.strftime('%Y-%m/%d')+'/node_2.htm'
            yield scrapy.Request(url, meta={'yestoday':yestoday},callback=self.parse_urls, dont_filter=True)

    def parse_urls(self, response):
        yestoday = response.meta["yestoday"]
        sels = response.css('#btdh li')
        for sel in sels:
            item = SouthcnItem()
            links = sel.css('a::attr(href)').extract()[0]
            link = 'http://epaper.southcn.com/nfdaily/html/'+yestoday.strftime('%Y-%m/%d')+'/'+links
            item['text_url'] = link
            yield scrapy.Request(link,meta={'item': item},callback=self.parse_text, dont_filter=True)

    def parse_text(self,response):
        sels = response.css('#article')
        for sel in sels:
            item = response.meta['item']
            item['title'] = sel.css('h1::text').extract()[0]
            item['text_time'] = sel.css('#pubtime_baidu::text').extract()[0]
            item['text'] = sel.css('p::text').extract()
            yield item

