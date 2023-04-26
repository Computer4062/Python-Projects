# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlerPipeline:
    def process_item(self, item, spider):
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