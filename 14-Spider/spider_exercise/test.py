import requests
import random
from lxml import etree


def get_html(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        # "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        # "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
        "Referer":
        "https://www.mzitu.com/"
    }

    rsp = requests.get(url=url, headers=headers)
    html = etree.HTML(rsp.text)
    return html


url = "https://www.mzitu.com/page/1/"
html = get_html(url)
img_src = html.xpath('//div[@class="postlist"]/ul/li/a/@href')
for img_url in img_src:
    print(img_url)
