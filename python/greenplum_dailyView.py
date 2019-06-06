#!/usr/bin/python3 python
# encoding: utf-8
'''
@author: yichao
@contact: yichao1994@hotmail.com
@file: greenplum_dailyView.py
@time: 2019/5/23 10:12
@desc:
'''

import psycopg2
import pandas
from requests import post
import json
import datetime

head = {
    "source": "ADops",
    "token": "5HbhJ4Je",
    "title": "test",
    "content": "test",
    "content_html": "",
    "severity": 1,
    "product": "OPS"
}

# funcion to connect pg db
def db_conn(sqlText):
    conn = psycopg2.connect(database='postgres', user='xxxxxx',password='xxxxxx', host='xx.xx.xx.xx', port='5432')
    cur = conn.cursor()
    cur.execute(sqlText)
    rows = cur.fetchall()
    #print(rows)
    cur.close()
    conn.close()
    return rows

# to convert original data ro table style
def to_table(data, title):
    d = {}
    index = 0
    for t in title:
        d[t] = data[index]
        index = index + 1
    df = pandas.DataFrame(d)
    df = df[title]
    h = df.to_html(index=False)
    return h

# transpose data
def transpose(matrix):
        new_matrix = []
        for i in range(len(matrix[0])):
            matrix1 = []
            for j in range(len(matrix)):
                matrix1.append(matrix[j][i])
            new_matrix.append(matrix1)
        return new_matrix


# json head
def post_req(html_text):
    head["content_html"] = html_text
    return head


if __name__ == '__main__':
    data = db_conn("SELECT hostname,port,role,preferred_role,mode,status FROM gp_segment_configuration")
    down_num= db_conn("SELECT count(status) FROM gp_segment_configuration where status='d';")
    #print(down_num[0][0])
    #print(data)
    metadata = transpose(data)
    #print(metadata)
    title=['hostname','port','role','preferred_role','mode','status']
    #print(to_html(metadata, title))
    html_tab=to_table(metadata, title)
    html_text = html_tab + '<h2>'+str(datetime.date.today())+'故障节点数为： '+str(down_num[0][0])+'</h2>'
    json_text = post_req(html_text)
    json_text = json.dumps(json_text)
    #print(json_text)
    url= "http://oops.op.internal.gridsumdissector.com/apiv1/alert/"
    r = post(url, data=json_text)
    print(r.text)



