"""
爬虫调度器
"""
from spider_exercise.一个简单爬虫框架案例.HtmlParse import HtmlParse
from spider_exercise.一个简单爬虫框架案例.DataStorge import DataStorge
from spider_exercise.一个简单爬虫框架案例.HtmlDownload import HtmlDownloader
from spider_exercise.一个简单爬虫框架案例.UrlManager import UrlManager


class SpiderScheduler(object):
    def __init__(self):
        self.manager = UrlManager()
        self.download = HtmlDownloader()
        self.parse = HtmlParse()
        self.storge = DataStorge()

    def crawl(self, root_url):
        # 添加入口URL
        self.manager.add_new_url(root_url)
        # 判断url管理器中是否有新的url地址
        # 判断爬取了多少个url
        while self.manager.has_new_url() and self.manager.old_url_size() < 100:
            try:
                # 从url管理器中获取新的url地址
                new_url = self.manager.get_new_url()
                # HTML下载器进行页面加载
                html = self.download.download(new_url)
                # HTML解析器解析数据
                new_urls, data = self.parse.parse(new_url, html)
                # 将获取的url添加到url管理器中
                self.manager.add_new_urls(new_urls)
                # 存储数据
                self.storge.save_data(data)
                print('已爬取{}个链接'.format(self.manager.old_url_size()))
            except Exception as e:
                print("crawl faild", e)


if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    spider = SpiderScheduler()
    spider.crawl(url)