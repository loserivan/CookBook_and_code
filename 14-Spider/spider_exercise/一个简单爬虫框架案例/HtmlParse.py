import re
from bs4 import BeautifulSoup
from urllib import parse


class HtmlParse(object):
    """Html解析器"""
    def parse(self, page_url, html_cont):
        """
        解析页面内容,提取url和数据
        :param page_url: 下载页面的URL地址
        :param html_cont: 下载页面的内容
        :return:
        """
        if page_url is not None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'lxml', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        """
        提取新的url地址集合
        :param page_url: 下载页面的url
        :param soup: soup
        :return: 返回新的url集合
        """
        new_urls = set()
        # 提取符合要求的a标记
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))

        for link in links:
            # 提取href属性
            new_url = link['href']
            # 拼接完整URL地址
            new_ful_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_ful_url)

        return  new_urls

    def _get_new_data(self, page_url, soup):
        """
        提取有效数据
        :param page_url:
        :param soup
        :return:
        """
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_="...").find('h1')
        data['title'] = title.get_text()
        data['..'] = ...

        return data

