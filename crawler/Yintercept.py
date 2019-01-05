#!/usr/bin/env python
# coding=utf-8
import urllib.request
import re
import pymysql
import datetime 
print('connecting to MYSQL...')
db = pymysql.connect(host="localhost",user="root",passwd="max",db="project")
cursor = db.cursor()
print('connected !')

cursor.execute("select * from RoadInfo")
results = cursor.fetchall()
for cols in results:
    if(cols[3]==cols[4]):
        continue
    else:
        Yintercept = -1*(cols[5]*cols[3]-cols[1])
        cursor.execute("update RoadInfo set Yintercept = '%lf' where ID = '%s'"%(Yintercept,cols[0]))
        print("insert...",Yintercept)
        db.commit()

db.close()
cursor.close()
print ('爬取数据并插入mysql数据库完成...')
