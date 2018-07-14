# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:09:24 2018

@author: Ao
"""

import os
'''
读取文件
'''
dirpath="D:\python\Deng\poi_get\charts"
fileType=["csv"]
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
