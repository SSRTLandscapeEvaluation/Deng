# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:40:59 2018

@author: Ao
"""

import matplotlib.pyplot as plt
import numpy as np
rng=np.random.RandomState(0)
#print(rng.rand(50))
x = 10*rng.rand(50)
y=x**2 +rng.randn(50)
plt.scatter(x,y);

from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept=True)
#print(model)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1,
                 normalize=False)

print(x.shape)#一维数组
X=x[:, np.newaxis]#升维
print(X.shape)#二维数组

model.fit(X,y)#训练模型
#print(model.fit(X,y))

model.coef_#斜率
print(model.coef_)

model.intercept_#截距
#print(model.intercept_)

xfit=np.linspace(0,10)
print(xfit)
Xfit=xfit[:,np.newaxis]
yfit=model.predict(Xfit)#测试模型

plt.scatter(x,y)
plt.scatter(xfit,yfit)