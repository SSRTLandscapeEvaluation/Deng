# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 10:43:30 2018

@author:  Ao
"""
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn import svm #调入算法，Support Vector Machines支持向量机
import matplotlib.pyplot as plt
digits=datasets.load_digits()
clf=svm.SVC(gamma=0.001,C=100)#实例化算法为clf。SCV是svm的一种类型，用于分类。而SVR用于回归。参数设置通过help(svm)查看
'''
**训练**
'''
clf.fit(digits.data[:-1],digits.target[:-1])#给出数据集的特征数据，和特征数据所对应的类标
#print(clf.fit(digits.data[:-1],digits.target[:-1]))
'''
**测试**
'''
clf.predict(digits.data[-1:])#根据训练数据获取模型，预测未知类型的特征数据
#print(clf.predict(digits.data[-1:]))
dir(digits)
#print(dir(digits))

plt.figure(1,figsize=(3,3))
#print(plt.figure(1,figsize=(3,3)))
plt.imshow(digits.images[-1],cmap=plt.cm.gray_r,interpolation='nearest')
print(plt.imshow(digits.images[-1],cmap=plt.cm.gray_r,interpolation='nearest'))


'''
**保存模型**——————joblib库
'''
from sklearn.externals import joblib
joblib.dump(clf,'digits_test.pkl')


'''
**调用**
'''
clf2=joblib.load('digits_test.pkl')





















