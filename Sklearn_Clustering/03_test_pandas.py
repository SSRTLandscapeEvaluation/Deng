# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 17:06:55 2018

@author: Ao
"""
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
X=[[1,2],[2,4],[4,5],[3,2],[3,1]]
y=[0,0,1,1,2]
XX=[[2,4]]
classif=OneVsRestClassifier(estimator=SVC(random_state=0))
classif.fit(X,y).predict(XX)
print(classif.fit(X,y).predict(XX))
