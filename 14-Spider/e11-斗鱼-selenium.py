'''
https://www.douyu.com/directory/all
分析：
1. 利用selenium得到页面内容
2. 利用xpath或者beuatifulsoup等在页面中提取信息
'''
from selenium import webdriver
from bs4 import BeautifulSoup


class Douyu:
    # 初始化方法
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.douyu.com/directory/all'

    def douyu(self):
        self.driver.get(self.url)

        while True:
            soup = BeautifulSoup(self.driver.page_source, 'xml')

            # 提取页面信息。标题，主播名，人气值等
            titles = soup.find_all('h3', {'class': 'DyListCover-intro'})
            popularity_values = soup.find_all('span',
                                              {'class': 'DyListCover-hot'})
            anchors = soup.find_all('h2', {'class': 'DyListCover-user'})

            for title, popularity_value, anchor in zip(titles,
                                                       popularity_values,
                                                       anchors):
                print("房间：{}".format(title.get_text().strip()))
                print("热度：{}".format(popularity_value.get_text().strip()))
                print('主播：{}'.format(anchor.get_text().strip()))
                print("---" * 20)

    def destory(self):
        self.driver.quit()


if __name__ == "__main__":
    douyu = Douyu()
    douyu.setUp()
    douyu.douyu()
    douyu.destory()
