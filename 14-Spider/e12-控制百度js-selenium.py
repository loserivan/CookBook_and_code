'''
通过selenium模拟对页面元素的控制
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches',
                                       ['enable-automation'])
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.baidu.com")

# 通过js来控制网页内容
# 编写js
# 然后通过execute_script执行

# 美化输入框，输入框id：kw
js = "var q=document.getElementById(\'kw\'); q.style.border=\'2px solid red\';"
# 执行代码
driver.execute_script(js)

time.sleep(3)
driver.save_screenshot("redbaidu.png")

# js隐藏相应元素，隐藏logo
img = driver.find_element_by_xpath('//*[@id="lg"]/img')
driver.execute_script('$(arguments[0]).fadeOut()', img)

# 滑动滚动条到最底下
js = "$('.scroll_top').click( function(){$('html, body').animate({scrollTop: '0px'}, 800)} );"

# 查看网页快照
time.sleep(3)
driver.save_screenshot("nullbaidu.png")

# error:未解决。。。。
# ERROR:device_event_log_impl.cc(208)]
# [18:03:02.139] Bluetooth:
# bluetooth_adapter_winrt.cc:1074 Getting Default Adapter failed.
