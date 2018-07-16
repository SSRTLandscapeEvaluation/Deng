# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 17:06:55 2018

@author: Ao
"""
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
import matplotlib as mpl
import matplotlib.pyplot as plt
X=[[1,2],[2,4],[4,5],[3,2],[3,1]]
y=[0,0,1,1,2]
#XX=[[2,4]]
classif=OneVsRestClassifier(estimator=SVC(random_state=0))
classif.fit(X,y).predict(X)
#print(classif.fit(X,y).predict(XX))

x_plt = [i[0] for i in X]
y_plt = [i[1] for i in X]
print(x_plt,y_plt)
plt.plot(x_plt,y_plt,'o',color='black')

'''
y=LabelBinarizer().fit_transform(y)
print(y)
classif.fit(X,y).predict(X)
print(classif.fit(X,y).predict(X))

'''
from sklearn.preprocessing import MultiLabelBinarizer
y = [[0,1],[0,2],[1,3],[0,2,3],[2,4]]
y=MultiLabelBinarizer().fit_transform(y)
print(y)
classif.fit(X,y).predict(X)
print(classif.fit(X,y).predict(X))