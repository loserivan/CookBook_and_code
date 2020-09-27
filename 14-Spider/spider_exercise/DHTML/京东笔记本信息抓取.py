from selenium import webdriver
# 负责条件的发起,触发
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pymongo
import time

"""
设置等待
selenium主要提供显式等待和隐式等待
implicitly_wait方法(隐式等待)
WebDriverWait(显式等待)
参数:
    driver: 传入WebDriver的实例
    timeout: 超时时间,等待的最长时间(考虑隐式等待时间)
    poll_frequency=POLL_FREQUENCY: 调用until或者until_not方法的间隔时间,默认0.5s
    ignored_exceptions=None: 忽略异常,如果在调用until或until_not过程中抛出元组中的异常,
                        则不中断代码,继续等待,如果排除的是元组外的异常,则中断代码,抛出异常
"""
# headless模式(无界面)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')  # 设置窗口大小
# 启动浏览器
browser = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(browser, 10)
# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
db = client.jd_computer
collection = db.computer


def to_mongodb(data):
    """数据存储"""
    try:
        collection.insert_one(data)
        print('Insert the data successfully')
    except Exception as e:
        print(e)
        print('Insert the data failed')


def search():
    browser.get('https://www.jd.com/')
    try:
        # 查找搜索框与搜索按钮,输入信息后点击
        inputs = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#key'))
        )
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#search > div > div.form > button')
            )
        )
        # print(inputs)
        inputs[0].send_keys('笔记本')
        submit.click()
        # 查找笔记本按钮,销量排名按钮
        button1 = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '#J_selector > div:nth-child(2) > div > div.sl-value > '
                 'div.sl-v-list > ul > li:nth-child(1) > a')
            )
        )
        button1.click()
        button2 = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '#J_filter > div.f-line.top > div.f-sort > a:nth-child(2)')
            )
        )
        button2.click()
        # 获取总页数
        max_page = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR,
                 '#J_bottomPage > span.p-skip > em:nth-child(1) > b')
            )
        )
        return max_page[0].text
    except TimeoutException:
        search()


def next_page(page_num):
    """获取下一页"""
    try:
        # 滑动网页到底部,加载所有商品信息
        browser.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(10)
        html = browser.page_source
        parse_html(html)
        while page_num == 101:
            exit()
        # 查找下一页按钮,点击
        button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.pn-next')
            )
        )
        button.click()
        # 等待信息元素加载完成
        wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '#J_goodsList > ul > li:nth-child(60)')
            )
        )
        # 判断翻页是否成功
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'),
                str(page_num)
            )
        )
    except TimeoutException:
        return next_page(page_num)


def parse_html(html):
    """解析网页数据"""
    soup = BeautifulSoup(html, 'lxml')
    goods_info = soup.select('.gl-i-wrap')
    # 查看当前商品信息加载数量
    quantity = str(len(goods_info))
    print(quantity)
    for info in goods_info:
        data = {}
        # 获取商品标题信息
        title = info.select('.p-name.p-name-type-2 a em')[0].text.strip()
        data['title'] = title
        # 获取商品价格
        price = info.select('.p-price i')[0].text.strip()
        price = int(float(price))
        data['price'] = price
        # 获取商品的评论数
        commit = info.select('.p-commit strong')[0].text.strip()
        commit = commit.replace('条评价', '')

        if '万' in commit:
            commit.split('万')
            commit = int(float(commit[0]) * 10000)
        else:
            commit = int(float(commit.replace('+', '')))

        data['commit'] = commit
        # 获取店铺属性
        shop_property = info.select('.p-icons i')

        if len(shop_property) >= 1:
            mess = shop_property[0].text.strip()
            if mess == '自营':
                data['shop_property'] = '自营'
            else:
                data['shop_property'] = '非自营'
        else:
            data['shop_property'] = '非自营'

        to_mongodb(data)
        print(data)
        print('.........' * 10)


def main():
    print(type(search()))
    total = int(search())
    for i in range(2, total + 2):
        time.sleep(10)
        print('第', i - 1, '页: ')
        next_page(i)


if __name__ == '__main__':
    main()
