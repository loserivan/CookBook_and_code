import scrapy
import json
from e16_qq.items import QqItem


class QqSpider(scrapy.Spider):

    name = 'qq'
    # 设置只能爬取腾讯域名的信息
    allowed_domains = ['careers.tencent.com']
    baseURL = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageSize=10&pageIndex='
    offset = 1
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        # 下载的结果自动放在response内储存
        contents = json.loads(response.text)
        posts = contents['Data']['Posts']
        item = QqItem()
        for post in posts:
            item['recruit_post_name'] = post['RecruitPostName']
            item['location_name'] = post['LocationName']
            item['category_name'] = post['CategoryName']
            item['responsibility'] = post['Responsibility']
            yield item
        if self.offset < 10:
            self.offset += 1
            yield scrapy.Request(self.baseURL + str(self.offset),
                                 callback=self.parse)
