# import requests

# url = 'https://www.w3school.com.cn/json/index.asp'
# response = requests.get(url=url)
# content = response.text

# print(content)

from urllib import request
import gzip

response = request.urlopen('https://www.baidu.com/')
content = response.read().decode('utf-8')

print(content)
