# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:40:59 2018

@author: Ao
"""

import matplotlib.pyplot as plt
import numpy as np
rng=np.random.RandomState()
print(rng.rand(50))
x = 10*rng.rand(50)
y=2*x - 1 +rng.randn(50)
plt.scatter(x,y);

from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept=True)
#print(model)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1,
                 normalize=False)

print(x.shape)#一维数组
X=x[:, np.newaxis]#升维
print(X.shape)#二维数组

model.fit(X,y)
print(model.fit(X,y))

model.coef_
print(model.coef_)

model.intercept_
print(model.intercept_)

xfit=np.linspace(-1,11)
Xfit=xfit[:,np.newaxis]
yfit=model.predict(Xfit)

plt.scatter(x,y)
plt.scatter(xfit,yfit)