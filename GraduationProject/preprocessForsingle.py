import pandas as pd
import numpy
from sklearn import preprocessing

def preprocess(data_df):

    data_df = pd.get_dummies(data=data_df,columns=["value"])
    #print(data_df)
    Label_NUM = len(data_df.columns)-3
###### train data : test data = 8:2
    msk = numpy.random.rand(len(data_df)) <0.8
    train_df = data_df[msk]
    test_df = data_df[~msk]
###### dataframe to array
    ndarray = train_df.values
    numpy.random.shuffle(ndarray)
    Label = ndarray[:,3:]
    Features = ndarray[:,:3]
    ndarray = test_df.values
    numpy.random.shuffle(ndarray)
    TestLabel = ndarray[:,3:]
    TestFeatures = ndarray[:,:3]
    #print('features:',features)
    #print("label:",Features)
######

###### Normalized features

    minmax_scale = preprocessing.MinMaxScaler(feature_range=(0,1))
    scaledFeatures = minmax_scale.fit_transform(Features)
    scaledLabel = minmax_scale.fit_transform(Label)
    scaledTestFeatures = minmax_scale.fit_transform(TestFeatures)
    scaledTestLabel = minmax_scale.fit_transform(TestLabel)
    #print(scaledFeatures)
    #print("scaledlabel:",label)

######
    return scaledFeatures , scaledLabel ,scaledTestFeatures , scaledTestLabel, Label_NUM
