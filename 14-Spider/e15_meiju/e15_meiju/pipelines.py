# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class E15MeijuPipeline:
    def process_item(self, item, spider):
        return item


class MeijuPipeline:
    '''
    次方法必须被实现
    用来处理item内容
    且必须返回一个item
    '''
    def __init__(self):
        self.file = open('meiju.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        '''
        此案例中只是把item值打印出来
        :param item:
        :param spider:
        :return item:
        '''
        with open('meiju.json', 'a', encoding='utf-8') as f:
            json.dump(dict(item),
                      f,
                      ensure_ascii=False,
                      sort_keys=True,
                      indent=4)

        return item

    def close_spider(self, spider):
        self.file.close()
