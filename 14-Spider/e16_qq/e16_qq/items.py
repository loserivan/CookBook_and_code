# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class E16QqItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QqItem(scrapy.Item):
    '''
    定义需要爬取的信息
    '''
    recruit_post_name = scrapy.Field()  # 招收岗位名称
    location_name = scrapy.Field()  # 工作地点
    category_name = scrapy.Field()  # 职业类别
    responsibility = scrapy.Field()  # 工作职责
