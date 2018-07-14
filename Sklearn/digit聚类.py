# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:43:55 2018

@author: Ao
"""
#from sklearn import datasets
from sklearn.datasets import load_digits
digits=load_digits()
digits.images.shape

'''可视化前一百张图像'''
import matplotlib.pyplot as plt
fig, axes = plt.subplots(10,10,figsize=(8,8),#子图个数10x10，大小8x8
                          subplot_kw={'xticks':[],'yticks':[]},#大概是轴的标尺，无
                          gridspec_kw=dict(hspace=0.1,wspace=0.1))#子图间隔

for i,ax in enumerate(axes.flat):

    ax.imshow(digits.images[i],cmap='binary',interpolation='nearest')
    ax.text(0.05,0.05,str(digits.target[i]),
             transform=ax.transAxes,color='green')
     