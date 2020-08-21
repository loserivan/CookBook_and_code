'''
https://search.douban.com/book/subject_search?search_text=python&cat=1001&start=0
使用selenium爬取页面
保存内容后用xpath进行分析
'''
import time
from selenium import webdriver
from lxml import etree


def get_web(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.save_screenshot('douban_reading.png')

    fn = 'douban_reading.html'
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    content_parse(fn)
    driver.quit()


def content_parse(fn):
    html = ''
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()
    # 生成xml树
    tree = etree.HTML(html)
    # 查找book
    books = tree.xpath('//div[@class="item-root"]')

    for book in books:
        book_name = book.xpath('.//div[@class="title"]/a/text()')
        print(book_name[0])


if __name__ == "__main__":
    url = "https://search.douban.com/book/subject_search?search_text=python&cat=1001&start=0"
    get_web(url)
