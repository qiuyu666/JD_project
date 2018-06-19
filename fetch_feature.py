# -*- coding:utf-8 *-*
# @Time    : 2017/11/22 0022 15:04
# @Author  : LQY
# @File    : fetch_feature.py
# @Software: PyCharm Community Edition
# -*- coding: utf-8 -*-

from datetime import datetime

import numpy as np
import get_feature as ff
import pandas as pd
import os


def get_feature(s1_date, s11_date, e1_date, s2_date, e2_date, s3_date, e3_date,path,resultpath):

      test11 = {}  # 特征提取需要的字典
      # file = open('E:\8-22_Ubi_data\data_deal\user_for_7model_7','r')
      file = open(path, 'r')
      i=0
      for line in file.readlines():
            if i==1:
                line = line.split(',')
                test11[line[0]] = line[1]
            i=1

      # s1_date=datetime(2014,11,1)
      # s11_date=time(2014,11,1)
      # e1_date=datetime(2014,11,7)
      # s2_date=datetime(2014,11,8)
      # e2_date=datetime(2014,11,14)
      # s3_date=datetime(2014,11,15)
      # e33_date=datetime(2014,11,21)
      # e34_date=datetime(2014,11,22)
      # e3_date=datetime(2014,11,28)

      os.chdir("E:\JD\data")

      fileadd = 't_comment.csv'
      name = ['shop_id', 'bad_num_all_sum','cmmt_num_all_sum','dis_num_all_sum','good_num_all_sum','mid_num_all_sum',
                    'bad_num_all_min', 'cmmt_num_all_min', 'dis_num_all_min', 'good_num_all_min', 'mid_num_all_min',
                    'bad_num_all_max', 'cmmt_num_all_max','dis_num_all_max', 'good_num_all_max', 'mid_num_all_max',
                    'bad_num_all_mean', 'cmmt_num_all_mean', 'dis_num_all_mean','good_num_all_mean', 'mid_num_all_mean',
                   'bad_num_all_var', 'cmmt_num_all_var', 'dis_num_all_var', 'good_num_all_var','mid_num_all_var',
              'bad_num_all_median', 'cmmt_num_all_median', 'dis_num_all_median', 'good_num_all_median', 'mid_num_all_median']

      ff.fetchfeature(fileadd, test11, 6, pcol=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                      process=['sum','sum','sum','sum','sum','min','min','min','min','min','max','max','max','max','max',
                     'mean','mean','mean','mean','mean','var','var','var','var','var','median','median','median','median','median'], timecol=0, rename=name, out_name=2,
                      start_date=s1_date, end_date=e3_date,result_path=resultpath)
      name = ['shop_id', 'bad_num_1_sum', 'cmmt_num_1_sum', 'dis_num_1_sum', 'good_num_1_sum', 'mid_num_1_sum',
            'bad_num_1_min',
              'cmmt_num_1_min', 'dis_num_1_min', 'good_num_1_min', 'mid_num_1_min',
                                                                         'bad_num_1_max', 'cmmt_num_1_max',
              'dis_num_1_max', 'good_num_1_max', 'mid_num_1_max',
                                                     'bad_num_1_mean', 'cmmt_num_1_mean', 'dis_num_1_mean',
              'good_num_1_mean', 'mid_num_1_mean',
                                   'bad_num_1_var', 'cmmt_num_1_var', 'dis_num_1_var', 'good_num_1_var',
              'mid_num_1_var',
              'bad_num_1_median', 'cmmt_num_1_median', 'dis_num_1_median', 'good_num_1_median',
              'mid_num_1_median']

      ff.fetchfeature(fileadd, test11, 6, pcol=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                      process=['sum','sum','sum','sum','sum','min','min','min','min','min','max','max','max','max','max',
                     'mean','mean','mean','mean','mean','var','var','var','var','var','median','median','median','median','median'], timecol=0,
                      rename=name, out_name=3,
                      start_date=s11_date, end_date=e1_date, result_path=resultpath)
      name = ['shop_id', 'bad_num_2_sum', 'cmmt_num_2_sum', 'dis_num_2_sum', 'good_num_2_sum', 'mid_num_2_sum',
            'bad_num_2_min',
              'cmmt_num_2_min', 'dis_num_2_min', 'good_num_2_min', 'mid_num_2_min',
                                                                         'bad_num_2_max', 'cmmt_num_2_max',
              'dis_num_2_max', 'good_num_2_max', 'mid_num_2_max',
                                                     'bad_num_2_mean', 'cmmt_num_2_mean', 'dis_num_2_mean',
              'good_num_2_mean', 'mid_num_2_mean',
                                   'bad_num_2_var', 'cmmt_num_2_var', 'dis_num_2_var', 'good_num_2_var',
              'mid_num_2_var',
              'bad_num_2_median', 'cmmt_num_2_median', 'dis_num_2_median', 'good_num_2_median',
              'mid_num_2_median']
      ff.fetchfeature(fileadd, test11, 6, pcol=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                      process=['sum','sum','sum','sum','sum','min','min','min','min','min','max','max','max','max','max',
                     'mean','mean','mean','mean','mean','var','var','var','var','var','median','median','median','median','median'], timecol=0,
                      rename=name, out_name=4,
                      start_date=s2_date, end_date=e2_date, result_path=resultpath)

      name = ['shop_id', 'bad_num_3_sum', 'cmmt_num_3_sum', 'dis_num_3_sum', 'good_num_3_sum', 'mid_num_3_sum',
            'bad_num_3_min',
              'cmmt_num_3_min', 'dis_num_3_min', 'good_num_3_min', 'mid_num_3_min',
                                                                         'bad_num_3_max', 'cmmt_num_3_max',
              'dis_num_3_max', 'good_num_3_max', 'mid_num_3_max',
                                                     'bad_num_3_mean', 'cmmt_num_3_mean', 'dis_num_3_mean',
              'good_num_3_mean', 'mid_num_3_mean',
                                   'bad_num_3_var', 'cmmt_num_3_var', 'dis_num_3_var', 'good_num_3_var',
              'mid_num_3_var',
              'bad_num_3_median', 'cmmt_num_3_median', 'dis_num_3_median', 'good_num_3_median',
              'mid_num_3_median']
      ff.fetchfeature(fileadd, test11, 6, pcol=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                      process=['sum','sum','sum','sum','sum','min','min','min','min','min','max','max','max','max','max',
                     'mean','mean','mean','mean','mean','var','var','var','var','var','median','median','median','median','median'], timecol=0,
                      rename=name, out_name=5,
                      start_date=s3_date, end_date=e3_date, result_path=resultpath)


      fileadd = 't_ads.csv'
      name = ['shop_id','charge_all_sum','consume_all_sum','charge_all_min','consume_all_min',
              'charge_all_max','consume_all_max','charge_all_mean','consume_all_mean',
              'charge_all_var','consume_all_var','charge_all_median','consume_all_median']
      ff.fetchfeature(fileadd,test11,3,pcol=[1,2,1,2,1,2,1,2,1,2,1,2],process=['sum','sum','min','min','max','max',
                     'mean','mean','var','var','median','median'],timecol=0,
                      rename=name,out_name=6,start_date=s1_date, end_date=e3_date,result_path=resultpath)
      name = ['shop_id', 'charge_1_sum', 'consume_1_sum', 'charge_1_min', 'consume_1_min',
              'charge_1_max', 'consume_1_max', 'charge_1_mean', 'consume_1_mean',
              'charge_1_var', 'consume_1_var', 'charge_1_median', 'consume_1_median']
      ff.fetchfeature(fileadd, test11, 3, pcol=[1,2,1,2,1,2,1,2,1,2,1,2],process=['sum','sum','min','min','max','max',
                     'mean','mean','var','var','median','median'], timecol=0,
                      rename=name, out_name=7, start_date=s11_date, end_date=e1_date, result_path=resultpath)
      name = ['shop_id', 'charge_2_sum', 'consume_2_sum', 'charge_2_min', 'consume_2_min',
              'charge_2_max', 'consume_2_max', 'charge_2_mean', 'consume_2_mean',
              'charge_2_var', 'consume_2_var', 'charge_2_median', 'consume_2_median']
      ff.fetchfeature(fileadd, test11, 3, pcol=[1,2,1,2,1,2,1,2,1,2,1,2],process=['sum','sum','min','min','max','max',
                     'mean','mean','var','var','median','median'], timecol=0,
                      rename=name, out_name=8,  start_date=s2_date, end_date=e2_date, result_path=resultpath)
      name = ['shop_id', 'charge_3_sum', 'consume_3_sum', 'charge_3_min', 'consume_3_min',
              'charge_3_max', 'consume_3_max', 'charge_3_mean', 'consume_3_mean',
              'charge_3_var', 'consume_3_var', 'charge_3_median', 'consume_3_median']
      ff.fetchfeature(fileadd, test11, 3, pcol=[1,2,1,2,1,2,1,2,1,2,1,2],process=['sum','sum','min','min','max','max',
                     'mean','mean','var','var','median','median'], timecol=0,
                      rename=name, out_name=9, start_date=s3_date, end_date=e3_date, result_path=resultpath)




      fileadd='t_product.csv'
      name=['shop_id','product_all_count']
      ff.fetchfeature(fileadd, test11, 4, pcol=[5],
                      process=['count'], timecol=0,
                      rename=name, out_name=10, start_date=s1_date, end_date=e3_date, result_path=resultpath)
      name = ['shop_id', 'product_1_count']
      ff.fetchfeature(fileadd, test11, 4, pcol=[5],
                      process=['count'], timecol=0,
                      rename=name, out_name=11, start_date=s11_date, end_date=e1_date, result_path=resultpath)
      name = ['shop_id', 'product_2_count']
      ff.fetchfeature(fileadd, test11, 4, pcol=[5],
                      process=['count'], timecol=0,
                      rename=name, out_name=12, start_date=s2_date, end_date=e2_date, result_path=resultpath)
      name = ['shop_id', 'product_3_count']
      ff.fetchfeature(fileadd, test11, 4, pcol=[5],
                      process=['count'], timecol=0,
                      rename=name, out_name=13,start_date=s3_date, end_date=e3_date, result_path=resultpath)



      fileadd='t_order.csv'

      name = ['shop_id', 'sale_amt_all_sum', 'offer_amt_all_sum', 'offer_cnt_all_sum', 'rtn_cnt_all_sum',
              'rtn_amt_all_sum','ord_cnt_all_sum','product_all_sum','user_cnt_all_sum',
              'sale_amt_all_min', 'offer_amt_all_min', 'offer_cnt_all_min', 'rtn_cnt_all_min',
              'rtn_amt_all_min', 'ord_cnt_all_min', 'product_all_min', 'user_cnt_all_min',

            'sale_amt_all_max', 'offer_amt_all_max', 'offer_cnt_all_max', 'rtn_cnt_all_max',
              'rtn_amt_all_max', 'ord_cnt_all_max', 'product_all_max', 'user_cnt_all_max',

              'sale_amt_all_mean', 'offer_amt_all_mean', 'offer_cnt_all_mean', 'rtn_cnt_all_mean',
              'rtn_amt_all_mean', 'ord_cnt_all_mean', 'product_all_mean', 'user_cnt_all_mean',

              'sale_amt_all_var', 'offer_amt_all_var', 'offer_cnt_all_var', 'rtn_cnt_all_var',
              'rtn_amt_all_var', 'ord_cnt_all_var', 'product_all_var', 'user_cnt_all_var',

              'sale_amt_all_median', 'offer_amt_all_median', 'offer_cnt_all_median', 'rtn_cnt_all_median',
              'rtn_amt_all_median', 'ord_cnt_all_median', 'product_all_median', 'user_cnt_all_median'



              ]

      ff.fetchfeature(fileadd, test11,4,
                      pcol=[1, 2, 3, 5,6,7,8,9, 1, 2, 3, 5,6,7,8,9, 1, 2, 3, 5,6,7,8,9, 1, 2, 3, 5,6,7,8,9,
                            1, 2, 3, 5,6,7,8,9, 1, 2, 3,5,6,7,8,9],
                      process=['sum', 'sum', 'sum', 'sum', 'sum','sum', 'sum', 'sum' ,'min', 'min', 'min', 'min', 'min', 'min', 'min', 'min',
                               'max', 'max',
                               'max', 'max', 'max','max', 'max', 'max',
                               'mean', 'mean', 'mean', 'mean', 'mean','mean', 'mean', 'mean',
                               'var', 'var', 'var', 'var', 'var','var', 'var', 'var', 'median',
                               'median', 'median', 'median', 'median','median', 'median', 'median'], timecol=0,
                      rename=name, out_name=14,
                      start_date=s1_date, end_date=e3_date, result_path=resultpath)
      name = ['shop_id', 'sale_amt_1_sum', 'offer_amt_1_sum', 'offer_cnt_1_sum', 'rtn_cnt_1_sum',
              'rtn_amt_1_sum', 'ord_cnt_1_sum', 'product_1_sum', 'user_cnt_1_sum',
              'sale_amt_1_min', 'offer_amt_1_min', 'offer_cnt_1_min', 'rtn_cnt_1_min',
              'rtn_amt_1_min', 'ord_cnt_1_min', 'product_1_min', 'user_cnt_1_min',

              'sale_amt_1_max', 'offer_amt_1_max', 'offer_cnt_1_max', 'rtn_cnt_1_max',
              'rtn_amt_1_max', 'ord_cnt_1_max', 'product_1_max', 'user_cnt_1_max',

              'sale_amt_1_mean', 'offer_amt_1_mean', 'offer_cnt_1_mean', 'rtn_cnt_1_mean',
              'rtn_amt_1_mean', 'ord_cnt_1_mean', 'product_1_mean', 'user_cnt_1_mean',

              'sale_amt_1_var', 'offer_amt_1_var', 'offer_cnt_1_var', 'rtn_cnt_1_var',
              'rtn_amt_1_var', 'ord_cnt_1_var', 'product_1_var', 'user_cnt_1_var',

              'sale_amt_1_median', 'offer_amt_1_median', 'offer_cnt_1_median', 'rtn_cnt_1_median',
              'rtn_amt_1_median', 'ord_cnt_1_median', 'product_1_median', 'user_cnt_1_median'

              ]

      ff.fetchfeature(fileadd, test11,4,
                      pcol=[1, 2, 3, 5,6,7,8,9, 1, 2, 3, 5,6,7,8,9, 1, 2, 3, 5,6,7,8,9, 1, 2, 3, 5,6,7,8,9,
                            1, 2, 3, 5,6,7,8,9, 1, 2, 3,5,6,7,8,9],
                      process=['sum', 'sum', 'sum', 'sum', 'sum','sum', 'sum', 'sum' ,'min', 'min', 'min', 'min', 'min', 'min', 'min', 'min',
                               'max', 'max',
                               'max', 'max', 'max','max', 'max', 'max',
                               'mean', 'mean', 'mean', 'mean', 'mean','mean', 'mean', 'mean',
                               'var', 'var', 'var', 'var', 'var','var', 'var', 'var', 'median',
                               'median', 'median', 'median', 'median','median', 'median', 'median'], timecol=0,
                      rename=name, out_name=15,
                      start_date=s11_date, end_date=e1_date, result_path=resultpath)
      name = ['shop_id', 'sale_amt_2_sum', 'offer_amt_2_sum', 'offer_cnt_2_sum', 'rtn_cnt_2_sum',
              'rtn_amt_2_sum', 'ord_cnt_2_sum', 'product_2_sum', 'user_cnt_2_sum',
              'sale_amt_2_min', 'offer_amt_2_min', 'offer_cnt_2_min', 'rtn_cnt_2_min',
              'rtn_amt_2_min', 'ord_cnt_2_min', 'product_2_min', 'user_cnt_2_min',

              'sale_amt_2_max', 'offer_amt_2_max', 'offer_cnt_2_max', 'rtn_cnt_2_max',
              'rtn_amt_2_max', 'ord_cnt_2_max', 'product_2_max', 'user_cnt_2_max',

              'sale_amt_2_mean', 'offer_amt_2_mean', 'offer_cnt_2_mean', 'rtn_cnt_2_mean',
              'rtn_amt_2_mean', 'ord_cnt_2_mean', 'product_2_mean', 'user_cnt_2_mean',

              'sale_amt_2_var', 'offer_amt_2_var', 'offer_cnt_2_var', 'rtn_cnt_2_var',
              'rtn_amt_2_var', 'ord_cnt_2_var', 'product_2_var', 'user_cnt_2_var',

              'sale_amt_2_median', 'offer_amt_2_median', 'offer_cnt_2_median', 'rtn_cnt_2_median',
              'rtn_amt_2_median', 'ord_cnt_2_median', 'product_2_median', 'user_cnt_2_median'

              ]
      ff.fetchfeature(fileadd, test11,4,
                      pcol=[1, 2, 3, 5,6,7,8,9, 1, 2, 3, 5,6,7,8,9, 1, 2, 3, 5,6,7,8,9, 1, 2, 3, 5,6,7,8,9,
                            1, 2, 3, 5,6,7,8,9, 1, 2, 3,5,6,7,8,9],
                      process=['sum', 'sum', 'sum', 'sum', 'sum','sum', 'sum', 'sum' ,'min', 'min', 'min', 'min', 'min', 'min', 'min', 'min',
                               'max', 'max',
                               'max', 'max', 'max','max', 'max', 'max',
                               'mean', 'mean', 'mean', 'mean', 'mean','mean', 'mean', 'mean',
                               'var', 'var', 'var', 'var', 'var','var', 'var', 'var', 'median',
                               'median', 'median', 'median', 'median','median', 'median', 'median'], timecol=0,
                      rename=name, out_name=16,
                      start_date=s2_date, end_date=e2_date, result_path=resultpath)

      name = ['shop_id', 'sale_amt_3_sum', 'offer_amt_3_sum', 'offer_cnt_3_sum', 'rtn_cnt_3_sum',
              'rtn_amt_3_sum', 'ord_cnt_3_sum', 'product_3_sum', 'user_cnt_3_sum',
              'sale_amt_3_min', 'offer_amt_3_min', 'offer_cnt_3_min', 'rtn_cnt_3_min',
              'rtn_amt_3_min', 'ord_cnt_3_min', 'product_3_min', 'user_cnt_3_min',

              'sale_amt_3_max', 'offer_amt_3_max', 'offer_cnt_3_max', 'rtn_cnt_3_max',
              'rtn_amt_3_max', 'ord_cnt_3_max', 'product_3_max', 'user_cnt_3_max',

              'sale_amt_3_mean', 'offer_amt_3_mean', 'offer_cnt_3_mean', 'rtn_cnt_3_mean',
              'rtn_amt_3_mean', 'ord_cnt_3_mean', 'product_3_mean', 'user_cnt_3_mean',

              'sale_amt_3_var', 'offer_amt_3_var', 'offer_cnt_3_var', 'rtn_cnt_3_var',
              'rtn_amt_3_var', 'ord_cnt_3_var', 'product_3_var', 'user_cnt_3_var',

              'sale_amt_3_median', 'offer_amt_3_median', 'offer_cnt_3_median', 'rtn_cnt_3_median',
              'rtn_amt_3_median', 'ord_cnt_3_median', 'product_3_median', 'user_cnt_3_median'

              ]
      ff.fetchfeature(fileadd, test11,4,
                      pcol=[1, 2, 3, 5,6,7,8,9, 1, 2, 3, 5,6,7,8,9, 1, 2, 3, 5,6,7,8,9, 1, 2, 3, 5,6,7,8,9,
                            1, 2, 3, 5,6,7,8,9, 1, 2, 3,5,6,7,8,9],
                      process=['sum', 'sum', 'sum', 'sum', 'sum','sum', 'sum', 'sum' ,'min', 'min', 'min', 'min', 'min', 'min', 'min', 'min',
                               'max', 'max',
                               'max', 'max', 'max','max', 'max', 'max',
                               'mean', 'mean', 'mean', 'mean', 'mean','mean', 'mean', 'mean',
                               'var', 'var', 'var', 'var', 'var','var', 'var', 'var', 'median',
                               'median', 'median', 'median', 'median','median', 'median', 'median'], timecol=0,
                      rename=name, out_name=17,
                      start_date=s3_date, end_date=e3_date, result_path=resultpath)


# get_feature(datetime(2016, 8, 1),datetime(2016, 8, 1),datetime(2016, 8, 10),datetime(2016, 8, 11),datetime(2016, 8, 20), datetime(2016, 8, 21),
#              datetime(2016, 8, 31),'E:\\JD\\august.csv','E:\\JD\\data\\generate_feature_8')
# get_feature(datetime(2016, 9, 1),datetime(2016, 9, 1),datetime(2016, 9,10),datetime(2016, 9, 11), datetime(2016, 9, 20),
#             datetime(2016, 9, 21),datetime(2016, 9, 30),'E:\\JD\\september.csv',
#             'E:\\JD\\data\\generate_feature_9')
# get_feature(datetime(2016, 8, 3),datetime(2016, 8, 3),datetime(2016, 9, 1),datetime(2016, 9, 2), datetime(2016, 10, 1),
#             datetime(2016, 10, 2),datetime(2016,10, 31),'E:\\JD\\october.csv',
#             'E:\\JD\\data\\generate_feature_10')
# get_feature(datetime(2016, 9, 2),datetime(2016, 9, 2),datetime(2016, 10,1),datetime(2016, 10, 2), datetime(2016, 10, 31),
#             datetime(2016, 11, 1),datetime(2016,11, 30),'E:\\JD\\november.csv',
#             'E:\\JD\\data\\generate_feature_11')
# get_feature(datetime(2016, 10, 3),datetime(2016, 10, 3),datetime(2016, 11, 1),datetime(2016, 11, 2), datetime(2016, 12, 1),
#             datetime(2016, 12, 2),datetime(2016,12, 31),'E:\\JD\\december.csv',
#             'E:\\JD\\data\\generate_feature_12')
# get_feature(datetime(2017, 11, 3),datetime(2017, 11, 3),datetime(2017, 12, 2),datetime(2017, 12, 3), datetime(2017, 1, 1),
#             datetime(2017, 1, 2),datetime(2017,1, 31),'E:\\JD\\january.csv',
#             'E:\\JD\\data\\generate_feature_1')
get_feature(datetime(2017, 1, 31),datetime(2017, 1, 31),datetime(2017, 3, 1),datetime(2017, 3, 2), datetime(2017, 3, 31),
             datetime(2017, 4, 1),datetime(2017,4, 30),'E:\\JD\\Sales_Forecast.csv',
             'E:\\JD\\data\\generate_feature_4')



