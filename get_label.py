# -*- coding:utf-8 *-*
# @Time    : 2017/11/24 0024 16:18
# @Author  : LQY
# @File    : get_label.py
# @Software: PyCharm Community Edition
import pandas as pd
import numpy as np
from datetime import datetime
def get_label(date1,date2):
    users=pd.read_csv('E:\\JD\\Sales_Forecast.csv',header=-1)

    orders=pd.read_csv('E:\\JD\\data\\t_order.csv',parse_dates=[0],header=-1)
    #print orders[0]
    data=orders[orders[0]>=date1]
    data =data[data[0]<=date2]
    a=data.groupby([4])[1].sum()#sale_amt
    #print a.index

    b=data.groupby([4])[6].sum()#rtn_amt

    c=data.groupby([4])[2].sum()#offer_amt
   #print a[3],b[3],c[3]
    all=-0.40190693*a-23.88246236*c+5.61020851*b+138648150
    pd.DataFrame(all).to_csv('E:\\JD\\label_result_1031.csv')
    #print all

#get_label(datetime(2016,11,1),datetime(2017,1,29))

def get_shop_mean():
    users = pd.read_csv('E:\\JD\\Sales_Forecast.csv', header=0,index_col='shop_id')
    f = pd.read_csv('E:\\JD\\t_sales_sum.csv',header=0,index_col='shop_id')
    f.drop(['date'])
    t=f.groupby(['shop_id'])['sale_amt_3m'].mean()
    for d in t.index:
        users.ix[d,'sale_amt_3m']=t[d]
    #print  users
    users.to_csv('E:\\JD\\shop_mean.csv',header=None)
#get_shop_mean()

def getmean():

    shop_mean=pd.read_csv('E:\\JD\\shop_mean.csv',header=-1,index_col=[0])
    result = pd.DataFrame(index=shop_mean.index,columns=['sales'])
    #print shop_mean
    xgresult = pd.read_csv('E:\\JD\data\\pre_result.csv',header=-1,index_col=[0])
    a=(shop_mean[1]+xgresult[1])/2
    result['sales']=a
    print result
    result.to_csv('E://JD//result_a.csv',header=None)

getmean()

