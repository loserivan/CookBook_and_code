import random
import time

import scrapy

from lianjiaspider.settings import REQUEST_HEADERS
# from lianjiaspider.items import LianjiaspiderItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    # start_urls = ['http://lianjia.com/']

    # 重写start_requests()方法, 定义url地址
    def start_requests(self):
        start_urls = [
            'https://cd.lianjia.com/zufang/jinniu/',
            'https://cd.lianjia.com/zufang/pidou/'
        ]
        for start_url in start_urls:
            yield scrapy.Request(url=start_url, headers=REQUEST_HEADERS,
                                 callback=self.parse, dont_filter=True)

    def parse(self, response):
        # print(response.body.decode('utf8'))
        infos = response.xpath('//div[@class="content__list--item--main"]')
        for info in infos:
            # 房屋标题
            titles = info.xpath('.//p[1]/a/text()').extract()
            title = titles[0].strip().replace(' ', '')
            # 房屋详情链接
            hrefs = info.xpath('.//p[1]/a/@href').extract()
            href = 'https://cd.lianjia.com/' + hrefs[0]
            # 房屋所在小区
            try:
                housing_estates = info.xpath('.//p[2]/a/text()').extract()
                housing_estate = '-'.join(housing_estates)
            except:
                housing_estate = None
            time.sleep(random.choice([1, 2, 3, 4]))
            yield scrapy.Request(url=href, callback=self.detail_parse,
                                 dont_filter=True, headers=REQUEST_HEADERS,
                                 meta={'title': title,
                                       'href': href,
                                       'housing_estate': housing_estate})

    def detail_parse(self, response):
        # 信息提取
        infos = response.xpath('//div[@class="content clear w1150"]')

        for info in infos:
            # 住建局房源核验码
            try:
                verification_codes = info.xpath('.//div/i/text()').extract()
                verification_code = verification_codes[1].split('：')[-1].strip()
            except:
                verification_code = None
            print(verification_code)


            # # 数据存储
            # item = LianjiaspiderItem()
            # item['title'] = response.meta['title']
            # item['href'] = response.meta['href']
            # item['housing_estate'] = response.meta['housing_estate']
            #
            # yield item

        # 图片信息处理


