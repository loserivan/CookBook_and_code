"""
URL管理器

value:

    - 已经爬取的URL集合 old_urls
    - 尚未爬取的URL集合 new_urls

method:

    1.has_new_url() 判断是否有待取的URL地址
    2.add_new_url(url) add_new_urls(url) 添加新的url到尚未爬取的URL集合
    3.get_new_url() 获取一个尚未爬取的url地址
    4.new_url_size() 获取尚未爬取URL集合的大小
    5.old_url_size() 获取已经爬取的URL集合的大小

"""


class UrlManager(object):
    """URL管理器"""
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        """判断是否有待取的URL地址"""
        if self.new_url_size() != 0:
            return True
        else:
            return False

    def get_new_url(self):
        """
        获取一个尚未爬取的url地址
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        """
        添加一个新的url到尚未爬取的URL集合
        :parma url: 新的url, <str>
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        添加多个新的url到尚未爬取的URL集合
        :parma urls: 新的urls, Iterable
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        """获取尚未爬取URL集合的大小"""
        return len(self.new_urls)

    def old_url_size(self):
        """获取已经爬取的URL集合的大小"""
        return len(self.old_urls)