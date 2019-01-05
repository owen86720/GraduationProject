import pymysql
import sys
from load import predict
from single import single
from getArea import getArea
if(sys.argv[1]>sys.argv[2]):
    Maxx=sys.argv[1]
    Minx=sys.argv[2]
else:
    Maxx=sys.argv[2]
    Minx=sys.argv[1]
if(sys.argv[3]>sys.argv[4]):
    Maxy=sys.argv[3]
    Miny=sys.argv[4]
else:
    Maxy=sys.argv[4]
    Miny=sys.argv[3]
inarea,count = getArea(Minx,Maxx,Miny,Maxy)
time = sys.argv[5]
print(inarea)
print("[[")
for route in inarea:
    predict(route,25,time,0)
print("]]")