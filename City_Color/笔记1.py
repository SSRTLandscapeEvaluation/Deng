# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:55:40 2018

@author: Ao
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
import os
import numpy as np

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

dirpath=r'D:\python\Deng\City_Color\test'
imgPath=r'D:\python\Deng\City_Color\test\IMG_20160704_200653_01.jpg'
fileType=['jpg']
fileInfo=filePath(dirpath,fileType)
print(fileInfo)
fileInfoKeys=list(fileInfo.keys())
#print(fileInfoKeys)
img=fileInfo[fileInfoKeys[0]]
#print(img)
imgPathList=[os.path.join(fileInfoKeys[0],i) for i in img]
#print(imgPathList)
lum_img=mpimg.imread(imgPathList[0])
#print(lum_img)
lum_imgSmall=misc.imresize(lum_img,0.2)
print(lum_imgSmall)
h,w,d=lum_imgSmall.shape
print(h,w,d)
pixData=np.reshape(lum_imgSmall,(h*w, d))
#print(pixData[:,0])
