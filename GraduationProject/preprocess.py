import pandas as pd
import numpy
from sklearn import preprocessing

def preprocess(data_df):

    data_df = pd.get_dummies(data=data_df,columns=["value"])
    #print(data_df)
    
    
    
    Label_NUM = len(data_df.columns)-3

###### dataframe to array
    ndarray = data_df.values
    #numpy.random.shuffle(ndarray)
    Label = ndarray[:,3:]
    Features = ndarray[:,:3]
    #print('features:',features)
    #print("label:",Features)
######

###### Normalized features

    minmax_scale = preprocessing.MinMaxScaler(feature_range=(0,1))
    scaledFeatures = minmax_scale.fit_transform(Features)
    scaledLabel = minmax_scale.fit_transform(Label)
    #print(scaledFeatures)
    #print("scaledlabel:",label)

######
    return scaledFeatures , scaledLabel , Label_NUM
