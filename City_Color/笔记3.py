# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 17:54:55 2018

@author: Ao
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#np.set_printoptions(threshold=np.inf)
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
dirpath=r'J:\Deng\City_Color\test'
imgPath=r'J:\Deng\City_Color\test\IMG_20160704_200653_01.jpg'
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
print(len(lum_imgSmall[0,:]))
h,w,d=lum_imgSmall.shape
print(h,w,d)
pixData=np.reshape(lum_imgSmall,(h*w, d))
#print(pixData[:,0])
'''
def getPixData(img):
    lum_img=mpimg.imread(img)
#    print(lum_img)
    lum_imgSmall=misc.imresize(lum_img,0.1)
    h,w,d=lum_imgSmall.shape
    pixData=np.reshape(lum_imgSmall,(h*w, d))
    return lum_imgSmall,pixData#lum_imgSmall是缩放后的三维数组，pixData是降维后的数组

dirpath=r'D:\python\Deng\City_Color\test'
#imgPath=r'J:\Deng\City_Color\test\IMG_20160704_200653_01.jpg'
fileType=['jpg']
fileInfo=filePath(dirpath,fileType)
fileInfoKeys=list(fileInfo.keys())
img=fileInfo[fileInfoKeys[0]]
imgPathList=[os.path.join(fileInfoKeys[0],i) for i in img]
imgInfo=[(getPixData(img)) for img in imgPathList]
#print(imgPathList)
#

#print((imgInfo[0])[1].shape)



def cityColorThemes(imgInfo):
    #设置聚类参数，实验中仅使用了Kmeans算法，其他算法执行尝试
    default_base = {'quantile': .3,
                    'eps': .3,
                    'damping': 0.9,
                    'preference': -200,
                    'n_neighbors': 10,
                    'n_clusters': 7} 
    #定义参数字典


    datasets=[((i[1],None),{ }) for i in imgInfo]#基于pixData的图像数据，用于聚类计算
#    print(datasets)
#   imgInfo=[(getPixData(img)) for img in imgPathList]
    imgList=[i[0] for i in imgInfo]#基于lum_imgSmall的数据图像，用于图像显示，imgInfo为图像列表，
#    print(imgList)
    #官方聚类案例中对于datasets的配置
    
    
    themes=np.zeros((default_base['n_clusters'], 3))#建立0占位的数组，用于后面主题数据的追加。n_clusters是提取主题色的色彩聚类数量，此处为7，轴2为3，(7,3)，是RGB的数值
    (img,pix)=imgInfo[0]#可以一次性提取元素索引相同的值，img就是lum_imgSmall，而pix是pixData，lum_imgSmall是缩放后的三维数组，pixData是降维后的数组
#    print(len(img))
#    print('\n')
#    print(pix.shape)
#    print('\n')
    pixV,pixH=pix.shape#V是一张图像里的所有像素点个数，H是每个像素对应了R，G，B三种值
#    print(pixV)
    pred=np.zeros((pixV))#0值占位，
    plt.figure(figsize=(6*3+3, len(imgInfo)*2))#设置图标大小，根据图象的数量来设置高度
    plt.subplots_adjust(left= .02, right=.98, bottom=.001, top=.96, wspace=.3, hspace=.3)
    plot_num=1
    
#    print('*x*'+'\n')
#    print(enumerate(datasets))
#    print('*x**'+'\n')
    for i_dataset, (dataset, algo_params) in enumerate(datasets):#循环pixData数据，即将预测的每个图像数据。enumerate()函数将可迭代队象组成一个索引序列，可以同时获取索引和值，其中i_dataset为索引，从0开始
#        print(i_dataset)
        params=default_base.copy()
        #print(params)
        params.update(algo_params)#替换原来的，更新数据
        #print(params)
        X, y = dataset#用于机器学习的数据一般包括特征数据和类标，此次实验为无监督分类的聚类，没有类标，并将其在前文中设置为None对象
        
        Xstd = StandardScaler().fit_transform(X)#只用于二维显示，不用于聚类计算
 
#        print('***'+'\n')
#        print(Xstd)
#        print('***'+'\n')
        '''
        ***参数设定Start***
        '''
        two_means = cluster.MiniBatchKMeans(n_clusters=params['n_clusters'])
        
        spectral = cluster.SpectralClustering(n_clusters=params['n_clusters'],
                                              eigen_solver='arpack',affinity="nearest_neighbors")
        dbscan = cluster.DBSCAN(eps=params['eps'])
        affinity_propagation = cluster.AffinityPropagation(damping=params['damping'],
                                                           preference=params['preference'])
        birch = cluster.Birch(n_clusters=params['n_clusters'])
        gmn = mixture.GaussianMixture(n_components=params['n_clusters'],covariance_type='full')
        km=cluster.KMeans(n_clusters=params['n_clusters'])
        '''
        ***参数设定END***
        '''
        
        clustering_algorithms=(
#                ('Kmeans', km),
                ('MiniBatchKMeans', two_means),
#                ('AffinityPropagation', affinity_propagation),
#                ('MeanShift', ms),
#                ('SpectralClusterig', spectral),
#                ('Ward', ward),
#                ('AgglcmerativeClustering', average_linkage),
#                ('DBSCAN',dbscan),
#                ('birch',birch),
#                ('GaussianMixture',gmn)
                )
#        print('***'+'\n')
#        print(len(clustering_algorithms))
#        print('***'+'\n')
#循环算法
        for name, algorithm in clustering_algorithms:
#            print('***'+'\n')
#            print(name)
#            print('***'+'\n')
#            print(algorithm)
#            print('***'+'\n')
            t0=time.time()
#            print (time.asctime(time.localtime(time.time())))
            with warnings.catch_warnings():
                warnings.filterwarnings(
                        "ignore",
                        message="the number of connected ,spectral embedding"+"may not work as expected",
                        category = UserWarning)
                algorithm.fit(X)
            quantize=np.array(algorithm.cluster_centers_,dtype=np.uint8)#提取聚类的中心，定义为主题色
            themes=np.vstack((themes,quantize))#数据追加主题色
            t1=time.time()
            
            if hasattr(algorithm, 'labels'):
                y_pred = algorithm.labels_.astype(np.int)
            else:
                y_pred = algorithm.predict(X)
            
            pred=np.vstack((pred, y_pred))
            
            figWidth = (len(clustering_algorithms)+2)*3
            plt.subplot(len(datasets), figWidth, plot_num)
            plt.imshow(imgList[i_dataset])
            plt.subplot(len(datasets), figWidth, plot_num+1)
            if i_dataset == 0:
                plt.title(name, size=18)
            colors = np.array(list(islice(cycle(['#377eb8','#ff7f00','#4daf4a',
                                             '#f781bf','#a65628','#984ea3',
                                             '#999999','#e41a1c','#dede00']),
                                             int(max(y_pred)+1))))
            plt.scatter(Xstd[:, 0], Xstd[:, 1], s=10, color=colors[y_pred])
            plt.xlim(-2.5,2.5)
            plt.ylim(-2.5,2.5)
            plt.xticks(())
            plt.yticks(())
            plt.text(.99,.01,('%.2fs' % (t1 - t0)).lstrip('0'),
                 transform=plt.gca().transAxes,size=15,
                 horizontalalignment ='right')
            '''
            配置主题色子图参数配置
            '''
            plt.subplot(len(datasets), figWidth, plot_num+2)
            t=1
            pale=np.zeros(imgList[i_dataset].shape, dtype=np.uint8)
            h,w,_=pale.shape
            ph=h/len(quantize)
            for y in range(h):
                pale[y,::] = np.array(quantize[int(y/ph)], dtype=np.uint8)
            plt.imshow(pale)
            t+=1
            plot_num+=3
    plt.show()
    return themes,pred


cityColorThemes(imgInfo)