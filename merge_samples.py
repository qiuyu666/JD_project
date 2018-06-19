# -*- coding:utf-8 *-*
# @Time    : 2017/11/23 0023 21:29
# @Author  : LQY
# @File    : merge_samples.py
# @Software: PyCharm Community Edition

import os
import pandas as pd
import xgboost
import numpy as np
from pandas import DataFrame,Series
def merge_featue(path,labelpath,resultpath):
    #path = 'E:\\JD\\data\\generate_feature_8'
    paths=os.listdir(path)
    print paths
    a = pd.read_csv(labelpath, header=0)#lable文件
    print a.index
    for p in paths:
        b=pd.read_csv(path+'\\'+p,header=0,delimiter=',',index_col=['shop_id'])
        b.fillna(0)
        #print b.index
        a =pd.merge(a,b,left_on='shop_id',right_index=True,how='left')
    a.to_csv(resultpath,encoding = "utf-8",index=None)
# merge_featue('E:\\JD\\data\\generate_feature_8','E:\\JD\\august.csv','E:\\JD\\data\\august_samples.csv')
# merge_featue('E:\\JD\\data\\generate_feature_9','E:\\JD\\september.csv','E:\\JD\\data\\september_samples.csv')
# merge_featue('E:\\JD\\data\\generate_feature_10','E:\\JD\\october.csv','E:\\JD\\data\\october_samples.csv')
# merge_featue('E:\\JD\\data\\generate_feature_11','E:\\JD\\november.csv','E:\\JD\\data\\november_samples.csv')
# merge_featue('E:\\JD\\data\\generate_feature_12','E:\\JD\\december.csv','E:\\JD\\data\\december_samples.csv')
# merge_featue('E:\\JD\\data\\generate_feature_1','E:\\JD\\january.csv','E:\\JD\\data\\january_samples.csv')
#merge_featue('E:\\JD\\data\\generate_feature_1','E:\\JD\\january.csv','E:\\JD\\data\\january_samples.csv')

#merge_featue('E:\\JD\\data\\generate_feature_4','E:\\JD\\Sales_Forecast.csv','E:\\JD\\data\\april_samples.csv')
#


#合并模型
def concact_feature():
    # j = pd.read_csv('E:\wash_data\generate_feature_7\\for_7model_1107.csv', header=0, delimiter=',')
    # i = pd.read_csv('E:\wash_data\generate_feature_7\\for_7model_1114.csv', header=0, delimiter=',')
    # h=pd.read_csv('E:\wash_data\generate_feature_7\\for_7model_1121.csv',header=0, delimiter=',')
    # a=pd.read_csv('E:\\JD\\data\\august_samples.csv',header=0, delimiter=',')
    # b=pd.read_csv('E:\\JD\\data\\september_samples.csv',header=0, delimiter=',')
    c=pd.read_csv('E:\\JD\\data\\october_samples.csv',header=0, delimiter=',')
    d = pd.read_csv('E:\\JD\\data\\november_samples.csv', header=0, delimiter=',')
    e = pd.read_csv('E:\\JD\\data\\december_samples.csv', header=0, delimiter=',')
    f = pd.read_csv('E:\\JD\\data\\january_samples.csv', header=0, delimiter=',')
    #g = pd.read_csv('E:\wash_data\generate_feature_28\\for_28model_0117_test.csv', header=0, delimiter=',')
    # #d=pd.read_csv('E:\wash_data\\after_merge_feature\\7model\\for_7model_28.csv',header=0, delimiter=',')
    list=[c,d,e,f,]
    #list = [f, g]
    # a = pd.read_csv('E:\wash_data\\after_merge_feature\\14model\\for_14model_14.csv', header=0, delimiter=',')
    # b = pd.read_csv('E:\wash_data\\after_merge_feature\\14model\\for_14model_21.csv', header=0, delimiter=',')
    # # c = pd.read_csv('E:\wash_data\\after_merge_feature\\14model\\for_14model_28.csv', header=0, delimiter=',')
    # list=[a,b]
    # a = pd.read_csv('E:\wash_data\\after_merge_feature\\21model\\for_21model_21.csv', header=0, delimiter=',')
    # b = pd.read_csv('E:\wash_data\\after_merge_feature\\21model\\for_21model_28.csv', header=0, delimiter=',')
    # list = [a, b]
    result=pd.concat(list)
    result.to_csv('E:\\JD\\data\\samples_all.csv',header=True,index=None)
#concact_feature()
