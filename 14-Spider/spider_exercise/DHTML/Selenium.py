from selenium import webdriver
import time
# from selenium.webdriver.common.keys import keys

# headless模式(无界面)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920x1080') # 设置窗口大小

# 创建浏览器对象
driver = webdriver.Chrome(chrome_options=chrome_options)

# get方法访问网站
driver.get("https://www.baidu.com")

# # 生成当前页面快照
# driver.save_screenshot('index.png')

# 模拟百度搜索
# id='kw' 输入"美女",点击操作
driver.find_element_by_id('kw').send_keys(u'美女')

# id='su'
driver.find_element_by_id('su').click()

time.sleep(1)

driver.save_screenshot('girl.png')

# 打印当前页面源码
print(driver.page_source)

# 获取当前页面url,cookies
print(driver.current_url)
print(driver.get_cookies())

driver.close()
