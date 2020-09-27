import scrapy


class XcdlSpider(scrapy.Spider):
    name = 'xcdl'
    allowed_domains = ['www.xicidaili.com']
    start_urls = ['https://www.xicidaili.com/']

    def parse(self, response):
        pass
