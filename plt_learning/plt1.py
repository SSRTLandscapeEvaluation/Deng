# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 01:10:38 2018

@author: 嗷~~
"""
import matplotlib.pyplot as plt 
#import matplotlib as plt
import numpy as np

fig = plt.figure()
#ax = plt.axes()
fig,ax=plt.subplots(2)

x = np.linspace(0,10,100)
#ax.plot(x,np.sin(x))
ax[0].plot(x,np.sin(x))
ax[1].plot(x,np.cos(x))


fig = plt.figure()
ax = plt.axes()


x = np.linspace(0,10,100)
#ax.plot(x,np.sin(x))
ax.plot(x,np.sin(x),x,np.cos(x))
ax.plot(x,np.cos(x))

plt.show() 