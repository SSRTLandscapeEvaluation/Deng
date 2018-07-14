# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:09:24 2018

@author: Ao
"""

import os
import matplotlib.pyplot as plt
import re
import numpy as np
import csv
from pylab import mpl
from itertools import groupby
mpl.rcParams['font.sans-serif'] = ['SimHei']
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
fileInfo=filePath(dirpath,fileType)
'''打开csv文件并提取其中的美食评分 '''
def open_csv_getEatingscore(fileInfo):
    for key in fileInfo.keys():
        for val in fileInfo[key]:
            with open(val,'r') as csvfile:#打开文件
                csvList=[]#原始csv数据
                csvClean=[]#清理csv数据
                Eatingscore=[]
                Pricescore=[]
                for row in csvfile:#按行读取csv
                    row=row.strip()#移除空格
                    csvList.append(row)
                csvList = csvList[::]
                for i in csvList:
                    i=re.findall(r'\"(.+?)\"',i)#根据观察，提取csv中“”中的值，其为一个字典
                    csvClean.append(i)
                csvClean=csvClean[::]
                print(csvClean[0])
                print(len(csvClean[0]))
                for j in csvClean:
                    try:
                        j= eval(j[0])
                        detail_info=j['detail_info']
                        if 'overall_rating' in detail_info:
                            Eatingscore.append(detail_info['overall_rating'])
                            price = []
                            if 'price' in detail_info:
                                price.append(detail_info['overall_rating'])
                                price.append(detail_info['price'])
                                Pricescore.append(price)
                    except Exception as ex:
                        print ("为空，错误")
                Eatingscore=Eatingscore[::2]
                Pricescore=Pricescore[::2]
                Eatingscore = [ float(x) for x in Eatingscore ]             
    return Eatingscore

def open_csv_getpricescore(fileInfo):
    for key in fileInfo.keys():
        for val in fileInfo[key]:
            with open(val,'r') as csvfile:#打开文件
                csvList=[]#原始csv数据
                csvClean=[]#清理csv数据
                Eatingscore=[]
                Pricescore=[]
                for row in csvfile:#按行读取csv
                    row=row.strip()#移除空格
                    csvList.append(row)
                csvList = csvList[::]
                for i in csvList:
                    i=re.findall(r'\"(.+?)\"',i)#根据观察，提取csv中“”中的值，其为一个字典
                    csvClean.append(i)
                csvClean=csvClean[::]
                print(csvClean[0])
                print(len(csvClean[0]))
                for j in csvClean:
                    try:
                        j= eval(j[0])
                        detail_info=j['detail_info']
                        if 'overall_rating' in detail_info:
                            Eatingscore.append(detail_info['overall_rating'])
                            price = []
                            if 'price' in detail_info:
                                price.append(detail_info['overall_rating'])
                                price.append(detail_info['price'])
                                Pricescore.append(price)
                    except Exception as ex:
                        print ("为空，错误")
                Eatingscore=Eatingscore[::2]
                Pricescore=Pricescore[::2]              
    return Pricescore
a=open_csv_getEatingscore(fileInfo)
b=open_csv_getpricescore(fileInfo)
print(a,b)
def draw_a(a):
    plt.hist(a)
    plt.title('美食评分的柱状图')

def draw_b(b):
    x = [e[0] for e in b]
    x = [float(o) for o in x ]
    y = [i[1] for i in b]
    y = [float(p) for p in y ]
    '''
    配置散点图与直方图，来源《python数据科学手册》p235
    '''
    fig = plt.figure(figsize=(10,10))
    grid = plt.GridSpec(5,2,hspace=0.2,wspace=0.2)
    main_ax = fig.add_subplot(grid[:-1,1:])
    main_ax.scatter(x,y,s=3)
    plt.xlabel('评分')
    plt.ylabel('价格')
    plt.title('美食评与价格分布')

def draw_c(a):
    plt.figure()   
    plt.boxplot(a,labels = ['评分'])
    plt.title('美食评分箱型图')
    plt.savefig('美食评分箱型图')
def sort(a):
    a = a
    result = [[],[],[],[],[]]
    for item in a:
            if item < 1:
                result[0].append(item)
            elif 1 < item < 2:
                result[1].append(item)
            elif 2 < item < 3:
                result[2].append(item)
            elif 3 < item < 4:
                result[3].append(item)
            else:
                result[4].append(item)
    sizes = [len(result[0]),len(result[1]),len(result[2]),len(result[3]),len(result[4])]
    labels = ['0-1分','1-2分','2-3分','3-4分','4-5分']            
    plt.pie(sizes,labels=labels,labeldistance = 1.1,autopct ='%3.1f%%',shadow = False,startangle = 50,pctdistance = 0.6)


plt.show()    
draw_a(a)
draw_b(b)
draw_c(a)
sort(a)
