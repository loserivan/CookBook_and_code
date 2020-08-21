# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class E16QqPipeline:
    def process_item(self, item, spider):
        return item


class QqPipline:
    def __init__(self):
        self.f = open('QQ.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # item(Itemd对象，被爬取的item)
        # 这个方法必须实现
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content)
        return item
