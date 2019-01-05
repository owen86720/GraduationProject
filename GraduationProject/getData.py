import pymysql
import pandas as pd

def getData(routeid):
    db = pymysql.connect(host="",port=,user="",passwd="",db="") #連線至data server
    cursor = db.cursor()
    cursor.execute("select * from Data where routeid = '%s'"%(routeid))
    results = cursor.fetchall()
    db.close()
    cursor.close()
    #print(results)
    #if(results[0][0]==0):
        #return False
    value = []
    collecttime = []
    C = []
    rainfall = []
    small=100
    for record in results:
        temp = round(record[2]/10)
        #print temp
        if(temp<small):
            small = temp
        value = value + [temp]
        temp = record[3]
        #print('ori:',temp)
        hour = int(temp.strftime("%H"))
        mins = int(temp.strftime("%M"))
        #print(hour*24+mins)
        collecttime = collecttime + [(hour*60 + mins)]
        C = C +[record[8]]
        rainfall = rainfall + [record[9]]

######create DataFrame
    data_dict = { "value":value,"datacollecttime":collecttime,"C":C,"rainfall":rainfall}
    #data_dict = { "value":value,"C":C,"rainfall":rainfall}
    data_df = pd.DataFrame(data_dict)
    #data_df = pd.get_dummies(data=data_df,columns=["value"])
    #return data_df , len(data_df.columns)-3,small
    return data_df ,small
    
