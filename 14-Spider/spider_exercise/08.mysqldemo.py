# python操作mysql创建数据表
import pymysql
# try:
#     # 获取一个数据库连接，注意：如果是utf-8类型，需要定制数据库
#     # 打开数据库连接
#     '''
#     host='localhost'数据库服务器地址
#     user='root' 登录数据库用户
#     password='root' 用户密码
#     db='test'   连接的数据库名称
#     port=3306 数据库端口号
#     '''
#     db = pymysql.connect(host='localhost',
#                          user='root',
#                          password='root',
#                          db='test',
#                          port=3306)
#     # 创建游标，对数据进行操作，使用cursor()方法
#     cursor = db.cursor()
#     # 使用execute()执行sql语句
#     cursor.execute('DROP TABLES IF EXISTS HELLO')
#     # 使用预处理语句创建表
#     sql = """create table HELLO(
#         FIRST_NAME CHAR(20) NOT NULL,
#         LAST_NAME CHAR(20),
#         AGE INT,
#         SEX CHAR(1),
#         INCOME FLOAT
#     )"""
#     cursor.execute(sql)
#     db.close()
# except:
#     print('创建失败~~')

# # 数据库插入操作
# db = pymysql.connect('localhost', 'root', 'root', 'test')
# # 利用cursor()创建游标对象
# cursor = db.cursor()
# # sql语句
# # sql = 'insert into BJTLXY(FIRST_NAME, LAST_NAME, AGE, SEX, INCOM)'
# # 'VALUES("liu", "dana", 18, "M", "100000"), ("huang", "laoban", '
# # '19, "M", "99999")'
# # 为了防止sql注入
# sql = "INSERT INTO BJTLXY(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) \
#     VALUES ('%s', '%s', '%d', '%c', '%f')" % ('liu', 'dana', 18, 'M', '100000')
# try:
#     cursor.execute(sql)
#     # 提交
#     db.commit()
#     print('执行成功!')
# except Exception:
#     db.rollback()
#     print('执行失败')
# db.close()

# 数据库查询操作
try:
    db = pymysql.connect('localhost', 'root', 'root', 'test', 3306)
    cursor = db.cursor()
    cursor.execute('select * from bjtlxy')
    datas = cursor.fetchall()
    for data in datas:
        print(data)
    cursor.close()
    db.close()
except Exception as e:
    print('查询失败')
    print(e)
'''
fetchall():获取全部返回结果
fechone():获取下一个查询结果集
rowcount: 只读属性,返回执行语句的影响的行数
'''