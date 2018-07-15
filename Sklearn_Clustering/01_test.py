# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 14:49:44 2018

@author: Ao
"""

import numpy as np
from sklearn.svm import SVC
rng=np.random.RandomState(0)
X=rng.rand(10,10)
print(X)

y=rng.binomial(1,0.5,10)
#print(y)
X_test=rng.rand(5,10)
clf=SVC()
clf.set_params(kernel='linear').fit(X,y)
#print(clf.set_params(kernel='linear').fit(X,y))
clf.predict(X_test)
print(clf.predict(X_test))
print(X_test)