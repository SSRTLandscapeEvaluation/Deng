# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:59:16 2018

@author: Ao
"""

import numpy as np
from numpy.random import rand
from scipy import misc

from sklearn import cluster,datasets,mixture
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler

import os
import time
import warnings
from itertools import cycle, islice
import json


'''
***part A
以文件夹名为键，值包含文件夹下所有文件名的列表，文件类型自定义
***
'''
#dirpath="D:\python\Deng\poi_get\charts"
#fileType=["jpg"]
#'''
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
