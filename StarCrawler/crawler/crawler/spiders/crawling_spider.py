import os
import pandas as pd
from scrapy import Item, Field, Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MyItem(Item):
    title = Field()
    price = Field()
    availability = Field()

class CrawlingSpider(Spider):
    name = "crawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        categories = response.css('ul.nav-list > li > ul > li > a::attr(href)').extract()
        for category in categories:
            yield response.follow(category, callback=self.parse_category)

    def parse_category(self, response):
        books = response.css('article.product_pod > h3 > a::attr(href)').extract()
        for book in books:
            yield response.follow(book, callback = self.parse_book)

    def parse_book(self, response):
        title = response.css(".product_main h1::text").get()
        price = response.css(".price_color::text").get()
        availability = response.css(".availability::text")[1].get().replace("\n", "").replace(" ", "")

        item = MyItem()
        item['title'] = title
        item['price'] = price
        item['availability'] = availability

        return item

class TextFilePipeline(object):
    def __init__(self):
        self.file = open("output.txt", 'w')

    def process_item(self, item, spider):
        line = "{} | {} | {}\n".format(item['title'], item['price'], item['availability'])
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()