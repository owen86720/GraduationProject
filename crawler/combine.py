import pandas as pd
import numpy
import pymysql
import datetime
import time

db = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="max",db="project")
cursor = db.cursor()
batch = 50000
rounds = 1
while(rounds):
    rounds-=1
    cursor.execute("select count(1) from Data")
    results = cursor.fetchall()
    print (results[0][0])
    count = results[0][0]
    cursor.execute("select * from RoadSpeed where ID > %d and datacollecttime < DATE_SUB(NOW(),INTERVAL 1 DAY) limit %s"%(count,batch))
    results = cursor.fetchall()
    for record in results:
        routeid = record[1]
        value = record[2]
        collecttime = record[3]
        temp = collecttime
        cursor.execute("select * from RoadInfo where ID ='%s'"%(record[1]))
        roadinfo = cursor.fetchall()
        for info in roadinfo:
            Ntokm = info[1]
            Nfromkm = info[2]
            Etokm = info[3]
            Efromkm = info[4]
        mins = int(collecttime.strftime("%M"))
        mins = round(mins/10)*10
        if(mins == 60):
            mins = 0
        temp=temp.replace(minute=mins,second=0)
        cursor.execute("SELECT time ,tempataturec , rainfall, MIN(ABS(TIMESTAMPDIFF(MINUTE,time,'%s'))) as MinDiff from Weather Group by time ,tempataturec,rainfall order by MinDiff limit 1"%(temp))
        temp = cursor.fetchall()
        C = temp[0][1]
        rainfall = temp[0][2]
        print('Insert...',routeid,value,collecttime,Ntokm,Nfromkm,Etokm,Efromkm,C,rainfall)
        sql="INSERT INTO Data(routeid,value,datacollecttime,Ntokm,Nfromkm,Etokm,Efromkm,tempataturec,rainfall) VALUE('" + routeid + "','" + str(value) + "','" + str(collecttime) + "','" + str(Ntokm) + "','" + str(Nfromkm) + "','" + str(Etokm) + "','" + str(Efromkm) + "','" + str(C) + "','" + str(rainfall) + "')"
        #print(sql)
        cursor.execute(sql)
        db.commit()
    #break
db.close()
cursor.close()
