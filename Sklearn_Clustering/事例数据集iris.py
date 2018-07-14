# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 17:05:42 2018

@author: Ao
"""

from sklearn import datasets
from sklearn.cross_validation import train_test_split
iris=datasets.load_iris()
digits=datasets.load_digits()
#dir(iris)
#print(dir(digits))
#print(dir(iris))
#print(digits.data)
#print(digits.data[0])
#print(len(digits.data[0]))
#print(digits.target_names)
#print(digits.target)
#print(digits.images)
#print(digits.DESCR)
#print(iris)
#print(iris.feature_names)
#print(iris.target_names)
#print(iris.data)
print(iris.data.shape)
X=iris.data[:,[2,3]]
print(X.shape)
#print(X)
y=iris.target
print(y.shape)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)
print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)
#print(X_train,X_test,y_train,y_test)