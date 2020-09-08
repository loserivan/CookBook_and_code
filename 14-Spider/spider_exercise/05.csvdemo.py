'''
CSV(Comma-Separated Value)逗号分隔值
CSV文件由任意的数据记录组成，记录间以某种换行符分割，每行记录由换行符组合
'''
import csv
headers = ['ID', 'UserName', 'Age', 'City']
rows = [(1001, 'dana', 18, 'Beijing'), (1002, 'huanglaoban', 28, 'Cengdu'),
        (1003, 'yitengjun', 'Nane', 'Jinan')]
with open('test.csv', 'w', newline="") as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
