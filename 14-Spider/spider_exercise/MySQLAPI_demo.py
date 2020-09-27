"""
python连接mysqldemo
1.连接数据库 pymysql MySQLdb
2.查询记录
3.增加记录
4.更改记录
5.删除记录
6......
"""
__author__ = "Ivan"

import pymysql


class MySQLDemo(object):
    """MySQLAPI"""
    def __init__(self, host, username, password, dbname):
        """初始化,设置数据库连接参数"""
        self.conn = pymysql.connect(host, username, password,
                                    dbname, charset='utf8')
        self.cursor = self.conn.cursor()

    def get_all(self, sql):
        """查询全部数据,参数:sql查询语句"""
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            return False

    def get_one(self, sql):
        """查询单条数据"""
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            return results
        except Exception as e:
            print(e)
            return False

    def insert(self, table_name, data):
        """插入数据,参数:table_name; data(字典)"""
        if len(data.keys()) == 1:
            sql = 'insert into {}({}) values'.format(
                table_name, data.keys[0]
            ).replace("'", '') + '({})'.format(data.values()[0])
        else:
            sql = 'insert into {}{} values'.format(
                table_name, tuple(data.keys())
            ).replace("'", '') + str('{}'.format(tuple(data.values())))
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return int(self.cursor.lastrowid)
        except Exception as e:
            self.conn.rollback()
            return False

    def update(self, table_name, data, restrication_str):
        """更新记录"""
        data_str = ''
        for item in data.items():
            data_str += '{}="{}",'.format(item[0], item[1])
        values = data_str[:-1]
        sql = 'update {} set {} where {}'.format(table_name, data_str,
                                                 restrication_str)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return  self.cursor.rowcount
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False

    def query(self, sql):
        """执行一条sql语句"""
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return int(self.cursor.lastrowid)
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False

    def delete(self):
        """删除一条记录"""
        sql = ''
        pass

    def delete_tab(self, table_name):
        """删除表"""
        pass

    def format_tab(self, table_name):
        """格式化表"""
        sql = 'trncate table table_name'
        pass
