# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:21:00 2018

@author: Ao
"""

import os
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
#from itertools import cycle,islice
import time
 
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import base
from sklearn import cluster,covariance, manifold
from scipy.stats import chi2_contingency
 


'''
A 以文件夹名为键，值为包含文件下的所有文件列表
'''

def filePath(dirpath,fileType):
    fileInfo={}
    i=0
    for dirpath,dirNames,fileNames in os.walk(dirpath):
        i+=1
        if fileNames:
            tempList = [f for f in fileNames if f.split('.')[-1] in fileType]
            if tempList:
                fileInfo.setdefault(dirpath,tempList)
    return fileInfo 

'''B展平函数列表'''

flatten_lst=lambda lst: [m for n_lst in lst for m in flatten_lst(n_lst)] if type(lst) is list else [lst]


'''
C提取分析所需数据，并转换为sklearn的bunch储存方法，统一格式，方便读取。注意poi行业分类类标