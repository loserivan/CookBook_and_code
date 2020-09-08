from pymongo import MongoClient


class MongoAPi(object):
    '''MongoDB数据库接口''''
    def __init__(self, db_ip, db_port, db_name, table_name):
        self.db_ip = db_ip
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        self.connect = MongoClient(host=self.db_ip, port=db_port)

        self.db = self.connect[self.db_name]
        self.table = self.db[self.table_name]

    def get_one(self, query):
        '''
        获取一条数据

        query: 查询条件
        '''
        return self.table.find_one(query, property={"_id": False})

    def get_all(self, query):
        '''获取多条数据'''
        return self.table.find(query)

    def add(self, kv_dict):
        '''添加数据'''
        return self.table.insert(kv_dict)

    def delete(self, query):
        '''删除数据'''
        return self.table.delete_many(query)

    def check(self, query):
        '''查看表中是否有匹配的文档. 有: 返回True; 没有: 返回False'''
        ret = self.table.find_one(query)
        if ret is not None:
            return True
        else:
            return False

    def update(self, query, kv_dict):
        '''更新数据, 如果没有匹配文档, 新建(插入)'''
        self.table.update_one(query, {'$set': kv_dict}, upsert=True)
