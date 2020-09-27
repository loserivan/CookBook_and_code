import scrapy


class BaiduspiderSpider(scrapy.Spider):
    # 爬虫名称
    name = 'baiduspider'
    # 爬虫允许域名
    allowed_domains = ['baidu.com']
    # 起始地址
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        with open('baidu.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode('utf-8'))
