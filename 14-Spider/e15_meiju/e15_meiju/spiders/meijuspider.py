import scrapy

# 导入需要的item
from e15_meiju.items import MeijuItem


# 定义spider
class MeijuSpider(scrapy.Spider):

    name = "meiju"

    start_urls = ["https://www.meijutt.tv/new100.html"]

    # 重写parse
    def parse(self, response):
        '''
        默认已经得到了网页
        反馈的内容用response表示
        其中包含需要的所有数据
        :param response:
        :return:
        '''
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')

        for movie in movies:
            '''
            每个movie都转换成一个item
            '''
            item = MeijuItem()
            item['name'] = movie.xpath('./h5/a/@title').extract()[0]
            item['href'] = movie.xpath('./h5/a/@href').extract()[0]

            tv = movie.xpath('./span[@class="mjtv"]/text()')
            if len(tv):
                item['tv'] = tv.extract()[0]
            else:
                item['tv'] = ""

            item['state'] = movie.xpath('./span/font/text()').extract()[0]
            item['time'] = movie.xpath('./div/font/text()').extract()[0]

            # item通过yield返回
            yield item
