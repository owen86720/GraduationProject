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

url='http://datacenter.taichung.gov.tw/swagger/OpenData/f6c18e09-6258-11e8-ab2d-00155d021202'


html=urllib.request.urlopen(url).read() 
html=html.decode('utf-8') 

r=re.compile(r'(Info.*)') 
Infos=re.findall(r,html)


for str1 in Infos:
	Info = str1.split('\"')
	if ( len(Info) >= 3 ) :	
		tokm = Info[3].split(',')
		Etokm = tokm[0]
		Ntokm = tokm[1]
		fromkm = Info[5].split(',')
		Efromkm = fromkm[0]
		Nfromkm = fromkm[1]
		ID = Info[19]
		#print ID
		cursor.execute("select * from RoadInfo where ID='%s'"%(ID))
		result = cursor.fetchall()
		print( len(result))
		if (len(result)==0):
			#print('insert..',routeid,value,datacollecttime)
			cursor.execute("INSERT INTO RoadInfo(Etokm,Ntokm,Efromkm,Nfromkm,ID) VALUES('%f','%f','%f','%f','%s')"%(float(Etokm),float(Ntokm),float(Efromkm),float(Nfromkm),ID))
			db.commit()

db.close()
#cursor.close()
print ('爬取数据并插入mysql数据库完成...')
