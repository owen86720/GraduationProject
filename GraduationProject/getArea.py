import pymysql
def getArea(Minx,Maxx,Miny,Maxy):
    def SingleInArea(x,y):
        if( ((y<float(Maxy)) and (float(Miny)<y) ) and ((x<float(Maxx)) and (float(Minx)<x))):
            return True
        else:
            return False
    def CheckY(M,Yintercept,x1,x2):
        big = x1 if x1 > x2 else x2
        small = x1 if x1 < x2 else x2
        temp1 = (float(Maxy)-Yintercept)/M
        temp2 = (float(Miny)-Yintercept)/M
        if((temp1<big)and(temp1>small)and(temp2<big)and(temp2>small)and(((big<float(Maxx))and(big>float(Minx)))or((small<float(Maxx))and(small>float(Minx))))):
            return True
        else:
            return False
    def CheckX(M,Yintercept,y1,y2):
        big = y1 if y1 > y2 else y2
        small = y1 if y1 < y2 else y2
        temp1 = float(Maxx)*M+Yintercept
        temp2 = float(Minx)*M+Yintercept
        if((temp1<big)and(temp1>small)and(temp2<big)and(temp2>small)and(((big<float(Maxy))and(big>float(Miny)))or((small<float(Maxy))and(small>float(Miny))))):
            return True
        else:
            return False
    inarea = set()
    count =0
    db = pymysql.connect(host="120.108.205.165",port=3306,user="root",passwd="max",db="project")
    cursor = db.cursor()
    cursor.execute("select * from RoadInfo");
    results = cursor.fetchall()
    db.close()
    cursor.close()
    for cols in results:
        if(SingleInArea(cols[3],cols[1]))or(SingleInArea(cols[4],cols[2])):
            inarea.add(cols[0])
            count+=1
        else:
            if(cols[5]==None):
                big = cols[1] if cols[1]>cols[2] else cols[2]
                small = cols[1] if cols[1]<cols[2] else cols[2]
                if((big>float(Maxy))and(small<float(Miny))and(cols[3]<float(Maxx))and(cols[3]>float(Minx))):
                    inarea.add(cols[0])
                    count+=1
            elif(cols[5]==0):
                if(CheckX(cols[5],cols[6],cols[1],cols[2])):
                    inarea.add(cols[0])
                    count+=1
            else:
                if(CheckX(cols[5],cols[6],cols[1],cols[2])or CheckY(cols[5],cols[6],cols[3],cols[4])):
                    inarea.add(cols[0])
                    count+=1
                
    return inarea,count


