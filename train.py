# -*- coding:utf-8 *-*
# @Time    : 2017/11/23 0023 21:23
# @Author  : LQY
# @File    : train.py
# @Software: PyCharm Community Edition

import numpy as np
import pandas
import xgboost
import matplotlib.pylab as plt
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


def load_data(path):

    df = pandas.read_csv(path)
    label = df.sale_amt_3m
    data = df.drop(['sale_amt_3m'], axis=1)

    return (data, label)

def evalerror(preds, df):
    label = df.get_label()
    diff = 0
    for i in range(len(preds)):
        diff += np.abs(preds[i] - label[i])
    return 'wame', float(diff / sum(label))

def xgb(train, test):

    X_train, X_val, y_train, y_val = train_test_split (train[0], train[1], train_size=0.8)

    dtrain = xgboost.DMatrix(X_train, y_train)
    dval = xgboost.DMatrix(X_val, y_val)
    dtest = xgboost.DMatrix(test)

    params = {}
    params["booster"] = "gbtree"
    params["objective"] = "reg:linear"  # 线性回归
    #params["objective"] = "binary:logistic"  # 逻辑回归
    params["eta"] = 0.01  # 0.1
    params["gamma"] = 0  # 树的叶子节点上作进一步分区所需的最小损失减少,越大越保守，一般0.1、0.2这样子
    params["max_depth"] = 6  # 默认为6 # 构建树的深度，越大越容易过拟合
    params["min_child_weight"] = 1  # 这个参数默认是 1，是每个叶子里面 h 的和至少是多少，对正负样本不均衡时的 0-1 分类而言，假设 h 在 0.01 附近，min_child_weight 为 1 意味着叶子节点中最少需要包含 100 个样本。
    # #这个参数非常影响结果，控制叶子节点中二阶导的和的最小值，该参数值越小，越容易 overfitting
    params["silent"] = 1  # 设置成1则没有运行信息输出，最好是设置为0
    params['alpha'] = 0.1  # L1 正则项参数
    #params['lambda'] = 2  # 控制模型复杂度的权重值的L2正则化项参数，参数越大，模型越不容易过拟合
    #params['eval_metric '] = evalerror(y_val,X_val)
    num_round = 800

    watchlist = [(dtrain, 'train'), (dval, 'val')]
    plst = list (params.items ())  # Using 5000 rows for early stopping.
    print ("训练开始\n")

    bst = xgboost.train (plst, dtrain, num_boost_round=num_round, evals=watchlist, feval=evalerror,early_stopping_rounds=30)
    #model = xgb.train(params, xgb_train, num_boost_round=100, evals=watchlist, feval=evalerror, early_stopping_rounds=5)
    limit = bst.best_iteration
    y_pred = bst.predict(dtest, ntree_limit=limit)

    return y_pred






if __name__ == '__main__':

     test = pandas.read_csv('E:\\JD\\data\\april_samples.csv')
    test = test.drop(['sale_amt_3m'],axis=1)
    result=pandas.read_csv('E:\\JD\\Sales_Forecast.csv',header=0)
    result=result.drop(['sale_amt_3m'],axis=1)

    print(train[0].columns)

    y_pred = xgb(train=train, test=test)

    df = pandas.DataFrame(y_pred)
    #result = result.drop([1])
    df=pandas.concat([result,df],axis=1)
    df.to_csv('E:\\JD\\data\\pre_result.csv', header=None, index=None)
    print(y_pred.shape)
    # for i in range(len(y_pred)):
    #     y_pred[i] = 1 if y_pred[i] > 0.5 else 0
    # print(metrics.classification_report