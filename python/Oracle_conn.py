#!/usr/bin/env python
# encoding: utf-8
'''
@author: yichao
@contact: yichao1994@hotmail.com
@file: Oracle_conn.py
@time: 2019/5/21 20:31
@desc:
'''


import cx_Oracle                                          #引用模块cx_Oracle
conn = cx_Oracle.connect('scott/oracle@localhost/orcl')    #连接数据库
c = conn.cursor()                                           #获取cursor
x =c.execute('select sysdate from dual')                   #使用cursor进行各种操作
data = x.fetchone()
print(data)
c.close()                                                 #关闭cursor
conn.close()