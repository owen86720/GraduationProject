from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation
import datetime
import time
from keras.layers.normalization import BatchNormalization
from preprocessForsingle import preprocess
from getData import getData
import numpy

def single(routeid):
    data , MinValue= getData(routeid)
    if(len(data)<50):
        return 0
    #print('total:',len(data_df),'train:',len(train_df),'test:',len(test_df))
######
    Features , Label ,TestFeatures , TestLabel, Label_NUM = preprocess(data)
###### building model
    model = Sequential()
    model.add(Dense(units=32,input_dim=3,kernel_initializer='uniform'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))

    model.add(Dense(units=32,kernel_initializer='uniform'))
    #model.add(BatchNormalization())
    model.add(Activation('relu'))
    #model.add(Dense(units=16,kernel_initializer='uniform',activation='relu'))
    #model.add(Dense(units=16,kernel_initializer='uniform',activation='relu'))
    #model.add(Dense(units=4,kernel_initializer='uniform',activation='relu'))
    #model.add(Dense(units=1,kernel_initializer='uniform',activation='sigmoid'))
######

###### training

    model.add(Dense(units=Label_NUM,kernel_initializer='uniform'))
    #model.add(BatchNormalization())
    model.add(Activation('softmax'))
    model.compile(loss='binary_crossentropy',optimizer='Adagrad',metrics=['accuracy'])
    train_history = model.fit(x=Features,y=Label,validation_split=0.5,epochs=50,batch_size=50,verbose=2)
######
    path = 'models/' + routeid + '.h5'
    model.save(path)

'''
###### Predict
    all_probability = model.predict(TestFeatures[:5])
    print("probaility:\n",all_probability)
    for p in all_probability:
        pro = 0
        temp = MinValue
        #print("sum:",sum(p))
        for i in p:
            #print("i:",i,"temp:",temp)
            pro = pro + i*temp
            temp += 1
        #print("pro:",pro)
    #print('real:\n',TestLabel[:5])
    return pro
######
    #scores = model.evaluate(x=TestFeatures,y=TestLabel)
    #print ('scores:',scores[1])
    #endtime = time.time()
#print('spend:',round(endtime-starttime),'s')
'''
