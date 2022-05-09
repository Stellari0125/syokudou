import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='arrivalgoodslist',
                     charset='utf8')
cursor = db.cursor()
# 创建表
sql_createTb = """
"""
