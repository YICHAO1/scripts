#!/usr/bin/python3

import pymysql

# 打开数据库连接
# 数据库IP 用于名称 用户密码 数据库DB名称
db = pymysql.connect("localhost", "xxxx", "xxxx", 'world')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("select * from city where CountryCode = 'CHN'")

# 使用 fetchone() 方法获取单条数据
# data = cursor.fetchone()
# 使用 fetchall() 方法获取所有数据，为元组
data = cursor.fetchall()

# 分条进行显示
for city in data:
    print(city)

print("The number of citys belong to CHN: ", len(data))
# 关闭数据库连接
db.close()