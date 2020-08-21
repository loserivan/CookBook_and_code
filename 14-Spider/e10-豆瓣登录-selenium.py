'''
利用selenium模拟登录豆瓣
需要输入验证码
分析：
1. 保存页面成快照
2. 等待用户手动输入验证码
3. 继续自动执行提交等动作
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001'
driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)

# 生成快照，查看验证码