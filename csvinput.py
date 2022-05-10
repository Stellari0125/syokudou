import pandas as pd
from collections import defaultdict
import re
import os
import pymysql

db = pymysql.connect(host='localhost',
                    user='root',
                    password='123456',
                    port=3306,
                    database='arrivalgoodslist')
    # print("connect success")
cur = db.cursor()
cur.execute('DROP TABLE IF EXISTS CXPaiGu')
Creat='CREATE TABLE CXPaiGu(tunhuodi CHAR(20),' \
    ' paigu CHAR(20), ' \
    'cn CHAR(20) NOT NULL, ' \
    'bing CHAR(20))'
cur.execute(Creat)
    # print('success')

# 读排表

SourFilePath = 'D:\\python\\syokudou\\testfiles\\'  # 读整个文件夹
filenames = os.listdir(SourFilePath)  # 获得排表表名
for files in filenames:  # 对于每一张表进行操作
     tungu = re.split(r'-|-|.csv', files)  # 划分csv文件名字符串，获得囤谷地和该表所排的谷
     tunhuodi = tungu[1]  # 囤货地
     paigu = tungu[2]  # 该表的排谷

     data = pd.read_csv(SourFilePath + files, encoding='utf-8')  # 打开csv文件

     firstline = list(data.columns.values)  # 获得csv文件第一行 柄名
     bings = firstline[1:]  # 第一个一般是没用的cn 从第二个开始是柄名

     pair = []  # 创建列表
     for index, row in data.iterrows():  # 每一行读取
         for bing in bings:  # 判断柄名的数量
             if str(row[bing]) != 'nan':  # 柄数量不为空
                 cn = data.iloc[index, 0]  # 获得cn 第一列
                 bingnm = bing + str(row[bing])  # 把柄名和数量合起来
                 tmptup = (tunhuodi, paigu, cn, bingnm)  # 获得排谷信息的元组
                 pair.append(tmptup)

     for tup in pair:
        #     0-囤货地 1-谷名 2-cn 3-柄名+数量 写入mysql
        Inser = 'insert into CXPaiGu(tunhuodi,paigu,cn,bing) value (%s,%s,%s,%s)'
        value = (tup[0], tup[1], tup[2], tup[3])
        cur.execute(Inser, value)
        db.commit()
