import requests
from lxml import etree
'''
扇贝单词：
1. 把python单词列表下载下来
2. 练习xpath
'''


class Shanbei:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'user-agent':
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/75.0.3770.100 Safari/537.36'
        }
        self.pase()

    def request_xpath(self, url):
        response = requests.get(url, headers=self.headers)
        return etree.HTML(response.text)

    def get_text(self, text):
        if text:
            return text
        else:
            return ''

    def pase(self):
        word_dict = {}
        for page in range(1, 4):
            # https://www.shanbay.com/wordlist/110521/232414/?page=2
            url = self.base_url + '?page=%s' % page
            # url = self.base_url+f'?page={page}'
            # print(url)
            # 获取xpath对象
            html = self.request_xpath(url)
            word_lsit = html.xpath(
                '//table[@class="table table-bordered table-striped"]/tbody/tr'
            )
            for site in word_lsit:
                word_en_list = site.xpath('//td[@class="span2"]/strong/text()')
                word_zh_list = self.get_text(
                    site.xpath('//td[@class="span10"]/text()'))
                for i, word in enumerate(word_en_list):
                    word_en = (word_en_list[i])
                    word_zh = self.get_text(word_zh_list[i])
                    # print(word_en,word_zh)
                    word_dict[word_en] = word_zh

        print(word_dict)


if __name__ == '__main__':
    base_url = 'https://www.shanbay.com/wordlist/110521/232414/'
    Shanbei(base_url)
