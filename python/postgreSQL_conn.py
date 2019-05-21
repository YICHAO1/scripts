#!/usr/bin/env python
# encoding: utf-8
'''
@author: yichao
@contact: yichao1994@hotmail.com
@file: postgreSQL_conn.py
@time: 2019/5/21 20:23
@desc:
'''

import psycopg2

# parameters
database_name="MyDB"
user="postgres"
passwd="postgres"
host="localhost"
port="5432"



# test sql
def pg_test():
    conn = psycopg2.connect(database=database_name, user=user, password=passwd, host=host, port=port)
    cur = conn.cursor()
    cur.execute("select * from mysch.mytab") # mysch means schema
    rows = cur.fetchall()  # all rows in table
    for line in rows:
        print(line) # print result
    cur.close()
    conn.close()
    return


if __name__ == '__main__':
    pg_test()