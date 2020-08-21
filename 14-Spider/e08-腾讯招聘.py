import json
import requests
import time
'''
爬取腾讯招聘的网站："https://careers.tencent.com/search.html?index=1"
下载页面，发现要提取的网页元素并不在我们下载到的HTML之中
分析请求页面，获取它的js请求文件（除JS选项卡还有可能在XHR选项卡中）
发现数据存放在：https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1597755983531&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn
json数据，
解析数据，获取想要的信息。
'''
# 获取页面
t = int(time.time() * 1000)

data = {"timestamp": t, "pageIndex": "1", "pageSize": "10"}

url = "https://careers.tencent.com/tencentcareer/api/post/Query?"

response = requests.get(url, params=data)
# 获取数据为json数据
html = response.text
html = json.loads(html)
# print(type(html))
# print(html)

# 提取数据，posts为本页所有岗位信息列表
posts = html['Data']['Posts']

list = []

for post in posts:
    item = {}
    item['recruit_post_name'] = post['RecruitPostName']  # 招收岗位名称
    item['location_name'] = post['LocationName']  # 工作地点
    item['category_name'] = post['CategoryName']  # 职业类别
    item['responsibility'] = post['Responsibility']  # 工作职责
    # print(item)
    list.append(item)

# 保存到json文件
with open('tencent_recruit.json', 'w', encoding='utf-8') as f:
    json.dump(list, f, ensure_ascii=False, sort_keys=True, indent=4)
