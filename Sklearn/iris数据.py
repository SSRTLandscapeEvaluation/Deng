# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:09:01 2018

@author: Ao
"""
from sklearn import datasets
import seaborn as sns
iris =datasets.load_iris()
iris.head()
from sklearn.cross_validation import train_test_split
Xtrain,Xtest,ytrain,ytest = train_test_split(X_iris,y_iris,random_state=1)

from sklearn.naive_bayes import GaussianNB  #选择模型类
model = GaussianNB()
model.fit(Xtrain,ytrain)
y_model = model.predict(Xtest)