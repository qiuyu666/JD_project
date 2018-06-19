# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 21:27:27 2017

@author: Mym
"""

import pandas as pd
from sklearn import linear_model
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import sklearn


# score with index

class SwI():
    def __init__(self, score, index):
        self.score = score
        self.index = index


def generate_complex_samples(data, result_dict, label):
    delay_list = []
    size_list = []
    for feature in result_dict:
        size_list.append(result_dict[feature][1])
        delay_list.append(result_dict[feature][2])
    s = max(size_list)
    d = max(delay_list)
    df = pd.DataFrame()

    for feature in result_dict:
        r = []
        a = data[feature]
        i = s + d
        days = result_dict[feature][1]
        if days == 0:
            continue
        delay = result_dict[feature][2]
        while len(a) - i >= label:
            r.append(a[i - delay - days:i - delay].sum())
            i = i + 1
        df[feature] = pd.Series(r)
    c = []
    a = data['copd']
    i = s + d
    days = label
    while len(a) - i >= label:
        c.append(a[i:i + label].sum())
        i = i + 1
    df['label'] = pd.Series(c)
    return df


def data_convert(df):  # 数据变换
    df['pm2.5'] = df['pm2.5'] / 100
    df['pm10'] = df['pm10'] / 100
    df['so2'] = df['so2'] / 100
    df['co'] = df['co'] / 10
    df['no2'] = df['no2'] / 100
    df['o3_8h'] = df['o3_8h'] / 10
    df['copd'] = df['copd'] / 10
    df['label'] = df['label'] / 10
    return df


def data_convert2(df):  # 归一化
    for col in list(df.columns[0:-1]):
        df[col] = (df[col] - df[col].min() + 0.1) / (df[col].max() - df[col].min())
    return df


def train_model(df, f_list):
    labels = df.iloc[:, -1]
    raw_train = df[f_list]

    train = pd.concat([raw_train, labels], axis=1)
    X1 = train[:round(df.shape[0] / 3 * 2)]
    X1 = sklearn.utils.shuffle(X1)

    X2 = train[round(df.shape[0] / 3 * 2):]

    label1 = X1.pop(df.columns[-1])
    label2 = X2.pop(df.columns[-1])
    reg = linear_model.BayesianRidge(alpha_1=1e-06,
                                     alpha_2=1e-06,
                                     compute_score=False,
                                     copy_X=True,
                                     fit_intercept=True,
                                     lambda_1=1e-06,
                                     lambda_2=1e-06,
                                     n_iter=3000,
                                     normalize=False,
                                     tol=0.0001,
                                     verbose=False)

    reg = linear_model.LinearRegression(fit_intercept=True)
    reg.fit(X1, label1)
    #    print(reg.coef_)
    y_pred = reg.predict(X2)
    y_true = label2

    true = np.array(y_true)
    true = true.tolist()
    pred = np.array(y_pred)
    pred = pred.tolist()

    #    score1 = metrics.r2_score(y_true,y_pred)
    #    score2 = metrics.mean_squared_error(y_true,y_pred)
    #    score3 = reg.score(X1,label1)
    corr = cal_correlation(df)
    return true, pred, corr, reg.coef_  # 返回回归系数


def cal_correlation(df):
    corr_matrix = np.corrcoef(df, rowvar=0)
    corr_matrix = pd.DataFrame(corr_matrix)
    corr_matrix.columns = df.columns
    corr_matrix.index = corr_matrix.columns
    return corr_matrix


if __name__ == "__main__":
    data = pd.read_csv('data/zigong_copd.csv', header=0, encoding='gb18030')
    data = pd.read_csv('data/nanhai_copd.csv', header=0, encoding='gb18030')
    label = 1
    aqi = 1
    level = 1
    pm25 = 1
    pm10 = 1
    co = 1
    o3 = 1
    so2 = 1
    no2 = 1
    delay = 1
    copd = 1

    df = generate_samples(data, aqi, level, pm25, pm10, so2, co, no2, o3, copd, label, delay)
    df.to_csv('zigong_better_analyse.csv', index=False)
    draw()
    df = data_convert2(df)
    f_list = list(df.columns[0:-1])
    true, pred, corr, reg_coef = train_model(df, f_list)
    print reg_coef
