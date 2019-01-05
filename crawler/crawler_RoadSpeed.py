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

url='http://datacenter.taichung.gov.tw/swagger/OpenData/18a1b191-6249-11e8-ab2d-00155d021202'


html=urllib.request.urlopen(url).read() 
html=html.decode('utf-8') 

r=re.compile(r'(Info.*)') 
Infos=re.findall(r,html)
for str1 in Infos:
	Info = str1.split('\"')
	if ( len(Info) >= 3 ) :	
		routeid = Info[1]
		value = Info[5]     
		datacollecttime = Info[9]
		cursor.execute("select * from RoadSpeed where datacollecttime='%s' and routeid='%s'"%(datacollecttime,routeid))
		result = cursor.fetchall()
		#print (len(result))
		if (len(result)==0):
			print('insert..',routeid,value,datacollecttime)
			cursor.execute("INSERT INTO RoadSpeed(routeid,value,datacollecttime) VALUES('%s','%d',str_to_date( \' %s \' , '%%Y/%%m/%%d %%H:%%i:%%s'))"%(routeid,int(value,10),datacollecttime))
			db.commit()

db.close()
cursor.close()
print ('Finished')
