# -*- coding: utf-8 -*-

"""
Created on Wed Mar 21 14:38:01 2018

@author: 嗷~~
"""

import os
import matplotlib.pyplot as plt
import re
import numpy as np
import KmlData as KD

#print(KD.kmlSub)
def is_outlier(points, threshold = 3.5):
    if len(points.shape) == 1:
        points=points[:,None]#转换为二维数组
#        print("变成了二维数组")
    else :
        print("error")
    median = np.median(points, axis=0)#数组中位数
    diff = np.sum((points-median)**2, axis=-1)#计算方差
    diff = np.sqrt(diff)#标准差
    med_abs_deviation=np.median(diff)#中位数绝对值偏差
    # compute modified Z-score
    modified_z_score=0.6745 * diff / med_abs_deviation
    print(modified_z_score)
    return modified_z_score > threshold #判断，返回布尔值
kmlSubval = KD.kmlSub['kmldata.kml']    #需要改进算法，自动提取键所对应的值
#print(kmlSubval)
#kmlcoordinates = KD.kmlSub
'''
打印路径
'''
coordi2 = []
for i in kmlSubval:
#    print(i)
#    i=str(i)
#    print(i)
#    i=i.strip('[').strip(']')
#    print(i)
#    i=i.split('\n')
#    print(i)
#    print(len(i))
#    del i[2]
#    print(i)#去除高程
    try:    
        coordi2.append(i) 
    except:
        print('ValueError')

#print(coordi2)
#print()



def main():
    coordiArray=np.array(coordi2)
#print(coordiArray)
#ax = plt.subplots()
#print(coordiArray[:,0])
#ax=plt.subplots()
#for k in coordiArray:    
    plt.plot(coordiArray[:,0],coordiArray[:,1],'r-',lw=0.5,markersize=5)
#plt.axis([0,120,0,40])
#plt.Widget(20)
#plt.set_figheight(10)
#plt.set_figwidth(10)
    plt.show()
    print(coordiArray.shape)
    coordiZ=coordiArray[:,2]
    coordiArrayClean = coordiArray[~is_outlier(coordiZ,threshold=1.2)]
    print(coordiArrayClean.shape,coordiArray.shape)
    print(coordiArrayClean)
    plt.plot(coordiArrayClean[:,0],coordiArrayClean[:,1],'r-',lw=0.5,markersize=5)

    plt.show()

main()

















