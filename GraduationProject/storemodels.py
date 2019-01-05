import pymysql
from single import single
import paramiko
import os
'''
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="120.108.205.165",port="3389",username="max",password="a28572756")
'''
db = pymysql.connect(host="",port=,user="root",passwd="max",db="project") # 連線至data server
cursor = db.cursor()
cursor.execute("select ID , done from RoadInfo");
results = cursor.fetchall()
print(results)   
count = 0

for cols in results:
    if(cols[1]==None):
        path = '/home/user/GraduationProject/models/' + cols[0] + '.h5'
        if(os.path.isfile(path)):
            print(cols[0],'is exist')
        else:
            count += 1
            single(cols[0])
        cursor.execute("UPDATE RoadInfo set done = '1' where ID = '%s'"%(cols[0]))
        db.commit()
    #if(count%10==0):
    #    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('sudo sh /GraduationProject/restart.sh')
    #single(cols[0])
db.close()
cursor.close()
