'''
利用selenium模拟登录豆瓣
url = 'https://www.douban.com/
user: 19938467368
passward: Huawei12#$
如需要输入验证码
分析：
1. 保存页面成快照
2. 等待用户手动输入验证码
3. 继续自动执行提交等动作
'''
from selenium import webdriver

url = 'https://accounts.douban.com/'
driver = webdriver.Chrome()
driver.get(url)
# 等待(显性,隐性,强制)
driver.implicitly_wait(5)
driver.find_element_by_xpath(
    '//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()
driver.implicitly_wait(2)
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('19938467368')
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('Huawei12#$')
driver.find_element_by_xpath(
    '//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a').click()

driver.implicitly_wait(1)

print(driver.page_source)
