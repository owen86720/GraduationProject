from keras.models import load_model
from single import single
from getData import getData
import numpy as np
import os
import pandas as pd
from preprocess import preprocess
from sklearn import preprocessing
def predict(routeid,C,time,rainfall):
    path = '/home/user/GraduationProject/models/' + routeid + '.h5'
    if(os.path.isfile(path)):
        model = load_model(path)
        data , MinValue = getData(routeid)
        test = pd.Series([C,time,rainfall,MinValue])
        newdata = pd.DataFrame([list(test)],columns=["C","datacollecttime","rainfall","value"])
        data = pd.concat([data,newdata])
        Features ,Label ,Label_NUM= preprocess(data)
        #scores = model.evaluate(x=Features,y=Label)
        #print ('scores:',scores[1])

        p = model.predict(Features[-1:])
        temp = MinValue*10
        pro = 0
        for i in p[0]:
            #print("i:",i,"temp:",temp)
            pro = pro + i*temp
            temp += 10
        print(routeid,pro)
    else:
        print(routeid,"NULL")
    print(" ")


