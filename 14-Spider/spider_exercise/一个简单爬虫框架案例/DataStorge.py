class DataStorge(object):
    """数据存储器"""
    def __init__(self):
        self.datas = []

    def add_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def save_data(self):
        pass
