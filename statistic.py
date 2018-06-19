# -*- coding:utf-8 *-*
# @Time    : 2017/11/22 0022 15:51
# @Author  : LQY
# @File    : statistic.py
# @Software: PyCharm Community Editiont
import pandas as pd
import numpy as np
from datetime import datetime
from pandas import DataFrame
import get_feature as gf
def statistic_shop():
    df=pd.read_csv('E:\\JD\\t_sales_sum.csv')
    dic=dict(list(df.groupby('dt')))
    #print dic['2016-11-30']
    print dic.keys()
    i=1
    for key in dic:
        dic[key].to_csv('E:\\JD\\'+str(i)+'.csv',index=False)
        i+=1


#statistic_shop()
def get_sales_sum():
    test11={}
    path='E:\\JD\\1.csv'
    resultpath='E:\\JD\\data'
    s1_date=datetime(2016,7,1)
    e3_date=datetime(2016,9,30)
    file = open(path, 'r')
    for line in file.readlines():
        line = line.split(',')
        test11[line[1]] = line[2]
    fileadd='E:\\JD\\data\\t_order.csv'
    name=['shop_id','sale_amount','offer_amount','rtn_amount']
    gf.fetchfeature(fileadd, test11, 4, pcol=[1,2,6],
                    process=['sum','sum','sum'], timecol=0, rename=name, out_name='sales_sum',
                    start_date=datetime(2016,7,1), end_date=datetime(2016,9,30), result_path='E:\\JD\\data')
#get_sales_sum()
# raw_data = pd.read_csv('E:\\JD\\data\\t_order.csv', header=-1)
# keycol=4
# test11={}
# file = open('E:\\JD\\1.csv', 'r')
# for line in file.readlines(100):
#     line = line.split(',')
#     test11[line[1]] = line[2]
# #print raw_data
#raw_data[0]
# a = raw_data[keycol].astype(np.str)
# #print a
# raw_data.pop(keycol)
# print raw_data
# raw_data.insert(keycol, keycol, a)
# print raw_data
# data = raw_data[raw_data[keycol].isin(test11)]
# se=data[0]
# print type(se.values[0])
t=pd.read_csv('E:\\JD\\1.csv',header=0)
asu=pd.read_csv('E:\\JD\\data\\sales_sumresult.csv',header=0)
re=pd.merge(t,asu,how='left',left_on='shop_id',right_on='shop_id')
re.to_csv('E:\\JD\\data\\sales_sum_merge.csv')
