'''
MongoDB属于更加适合爬虫的数据库

MongoDB 是一个基于分布式文件存储的数据库。由 C++ 语言编写。
旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。

MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关
系数据库当中功能最丰富，最像关系数据库的。

概念:
SQL术语/概念	MongoDB术语/概念	 解释/说明
database	    database	        数据库
table	        collection	        数据库表/集合
row	            document	        数据记录行/文档
column	        field	            数据字段/域
index	        index	            索引
table           joins	 	        表连接,MongoDB不支持
primary key	    primary key	        主键,MongoDB自动将_id字段设置为主键
'''
import pymongo

# # 插入文档
# client = pymongo.MongoClient('localhost', 27017)
# db = client.TBTL_tea
# post = {
#     'name': 'liudana',
#     'sex': 'm',
#     'age': '18',
#     'class': ['database', 'python', 'java', 'math', '数据分析'],
#     'income': '1000000'
# }

# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
# print("post id is: ", post_id)

# 连接mongodb数据库
client = pymongo.MongoClient()

# 获取数据库
db = client.TBTL_tea

# 获取集合
std = db.posts

# 获取数据
datas = std.find()
print(datas, type(datas))

for data in datas:
    print(data['name'])
    # 获取集合中的字段属性
    print(data.keys())
