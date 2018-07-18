# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:59:16 2018

@author: Ao
"""
#print(_doc_)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
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
***
part A
以文件夹名为键，值包含文件夹下所有文件名的列表，文件类型自定义
***
'''

#dirpath="D:\python\Deng\poi_get\charts"
#fileType=[" "]
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

'''
***
part B
读取图像rgb数组，并调整图像大小，减少计算时间，调整图像数组为2维，用于下一步的计算
***
'''

def getPixData(img):
    lum_img=mpimg.imread(img)
    print(lum_img)
    lum_imgSmall=misc.imresize(lum_img,0.3)
    h,w,d=lum_imgSmall.shape
    pixData=np.reshape(lum_imgSmall,(h*w, d))
    return lum_imgSmall,pixData

'''
***
part C
聚类的方法提取图像主题色，并打印图像、聚类预测的二位显示和主题色
***
'''
def cityColorThemes(imgInfo):
    #设置聚类参数，实验中仅使用了Kmeans算法，其他算法执行尝试
    default_base = {'quantile': .3,
                    'eps': .3,
                    'damping': 0.9,
                    'preference': -200,
                    'n_neighbors': 10,
                    'n_cluster': 7}
    datasets=[((1[1],None),()) for i in imgInfo]#基于pixData的图像数据，用于聚类计算
    imgList=[i[0] for i in imgInfo]#基于lum_imgSmall的数据图像，用于图像显示，imgInfo为图像列表
#   print(datasets[0])
    #官方聚类案例中对于datasets的配置
    
    
    themes=np.zeros((default_base['n_clusters'], 3))#建立0占位的数组，用于后面主题数据的追加。n_clusters是提取主题色的色彩聚类数量，此处为7，轴2为3，是RGB的数值
    (img,pix)=imgInfo[0]#可以一次性提取元素索引相同的值，img就是lum_imgSmall，而pix是pixData
    pixV,pixH=pix.shape
    pred=np.zeros((pixV))
    plt.figure(figsize=(6*3+3, len(imgInfo)*2))#设置图标大小，根据图象的数量来设置高度
    plt.subplots_adjust(left= .02, right=.98, bottom=.001, top=.96, wspace=.3, hspace=.3)
    plot_num=1
    
    for i_dataset, (dataset, algo_params) in enumerate(datasets):#循环pixData数据，即将预测的每个图像数据。enumerate()函数将可迭代队象组成一个索引序列，可以同时获取索引和值，其中i_dataset为索引，从0开始
        print(i_dataset)
        params=default_base.copy()
        #print(params)
        params.update(algo_params)
        #print(params)
        X, y = dataset#用于机器学习的数据一般包括特征数据和类标，此次实验为无监督分类的聚类，没有类标，并将其在前文中设置为None对象
        #print(X.shape,X)
        Xstd = StandardScaler().fit_transform(X)
        
        two_means = cluster.MiniBatchKMeans(n_clusters=params['n_clusters'])
        
        spectral = cluster.SpectralClustering(n_clusters=params['n_clusters'],
                                              eigen_solver='arpack',affinity="nearest_neighbors")
        dbscan = cluster.DBSCAN(eps=params['eps'])
        dffinity_propagation = cluster.AffinityPropagation(damping=params['damping'],
                                                           preference=params['preference'])
        birch = cluster.Birch(n_clusters=params['n_clusters'])
        qmm = mixture.GaussianMixture(n_components=params['n_cluster'],covariance_type='full')
        km=cluster.KMeans(n_clusters=params['n_clusters'])
        
        
        clustering_algorithms=(
                ('KMeans',km),
                )
        for name, algorithm in clustering_algorithms:
            t0=time.time()
            with warnings.catch_warning():
                warnings.filterwarnings(
                        "ignore",
                        massage="the number of connected ,spectral embedding"+"may not work as expected",
                        cateqory = UserWarning)
                algorithm.fit(X)
            quantize=np.array(algorithm.cluster_centers_,dtype=np.uint8)
            themes=np.vstack((themes,quantize))
            t1=time.time()
            
            if hasattr(algorithm,'labels'):
                y_pred = algorithm.labels_.astype(np.int)
            else:
                y_pred = algorithm.prediot(X)
            
            pred=np.vstack((pred, y_pred))
            
            figWidth = (len(clustering_algorithms)+2)*3
            plt.subplot(len(datasets), figWidth, plot_num+1)
            if i_dataset == 0:
                plt.title(name, size=18)
            colors = np.array(list(islice(cycle(['#377eb8','#ff7f00','#4daf4a',
                                             '#f781bf','#a65628','#984ea3',
                                             '#999999','#e41a1c','#dede00']),int(max(y_pred)+1))))
            plt.scatter(Xstd[:, 0], Xstd[:, 1], s=10, color=colors[y_pred])
            plt.xlim(-2.5,2.5)
            plt.ylim(-2.5,2.5)
            plt.xticks(())
            plt.yticks(())
            plt.text(.99,.01,('%.2fs' % (t1 - t0)).lstrip('0'),
                 transform=plt.gca().transAxes,size=15,
                 horizontalalignment ='right')
            



















