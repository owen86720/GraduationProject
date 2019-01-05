#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup
import pymysql

print('connecting...')
db = pymysql.connect('127.0.0.1','root','max','project')
print('connected!')
cursor = db.cursor()


hdrs = {'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}

url = "https://www.cwb.gov.tw/V7/observe/24real/Data/46749.htm"

r = requests.get(url, headers = hdrs)
soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), 'lxml')
trs = soup.find_all('tr')   # 获取全部tr标签成为一个列表
for tr in trs: 
    tds = tr.find_all('td')        
    if len(tds) != 0 :
        ths = tr.find_all('th')# 获取每个tr标签里的属性style
        time = ths[0].text
        cursor.execute("select * from Weather where time=str_to_date(\'2018/%s\','%%Y/%%m/%%d %%H:%%i')"%(time))
        result = cursor.fetchall()
        if(len(result)==0):
            td = [x for x in tds]   # 获取的列表
            tempataturec = 0
            if(td[0].text!='-'):
                tempataturec = float(eval(td[0].text))
            #print (type(tempataturec))
            weather = td[2].text
            #wind = td[3].text
            windspeed = td[4].text
            gust = td[5].text
            visibility = td[6].text
            #humid = td[7].text
            #pressure = td[8].text
            rainfall = float(eval(td[9].text))
            #sunhours = td[10].text
     
            print('insert...',time,tempataturec,weather,windspeed,gust,visibility,rainfall)
     
            cursor.execute("INSERT INTO Weather(time,tempataturec,weather,windspeed,gust,visibility,rainfall) VALUES(str_to_date( \'2018/%s\' , '%%Y/%%m/%%d %%H:%%i'),'%f','%s','%s','%s','%s','%f')"%(time,tempataturec,weather,windspeed,gust,visibility,rainfall))
            db.commit()
     

db.close()
cursor.close()
print ('爬取数据并插入mysql数据库完成...')
