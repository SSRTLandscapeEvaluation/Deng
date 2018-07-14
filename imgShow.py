# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:49:15 2018

@author: 嗷~~
"""

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as mpc
from mpl_toolkits.mplot3d import Axes3D
import math
from scipy import misc
import numpy as np

#注意
from PIL import ImageFile  
ImageFile.LOAD_TRUNCATED_IMAGES = True  #出现“IOError: image file is truncated (n bytes not processed)”错误的解决办法

#dirpath='C:\Users\Ao\Desktop\fwc' 
#imgPath='C:\Users\Ao\Desktop\fwc' 
'''
 A以文件夹名为键，值为包含该文件夹下所有文件名的列表。文件类型可以自行定义
'''

def filePath(dirpath,fileType):
    fileInfo={}
    i=0
    for dirpath,dirNames,fileNames in os.walk(dirpath):
        i+=1
       # print(1,'\n')
#        print(dirpath,'\n',dirNames,'\n',fileNames,'\n')
        if fileNames:
            tempList = [f for f in fileNames if f.split('.')[-1] in fileType]
#            if not tempList:
#                print(i,"NULL")
#            print(tempList)
            if tempList:
                fileInfo.setdefault(dirpath,tempList)
    return fileInfo
#fileInfo是一个字典，路径为键，文件名为值
'''B显示一个文件夹下所有图片，便于查看。并作为进一步图片处理分析的基础，关注后续相关实验'''
def imgShow(imgPath,imgList,nrows):    
    ncols=math.ceil(len(imgList)/nrows)
    fig,axes=plt.subplots(ncols,nrows,sharex=True,sharey=True,figsize=(10,10))   #布局多个子图，每个子图显示一幅图像，size是图形的显示大小
    ax=axes.flatten()  #降至1维，便于循环操作子图
    
#    print(ax)
    for i in range(len(imgList)):#i可以理解为一个序号
        img=os.path.join(imgPath,imgList[i])#获取图像路径
        lum_img=mpimg.imread(img)#读取图像为数组，值为RGB格式0-255
#        print(lum_img)
        lum_imgSmall=misc.imresize(lum_img,0.3)#传入图像数组，调整图像大小，指分辨率，不是显示大小
#        print(lum_img.shape,lum_imgSmall.shape)
        #lum_img=lum_img[:,:,]
        #print(lum_img.shape,lum_img)
        ax[i].imshow(lum_imgSmall)
        ax[i].set_title(i+1)
    fig.tight_layout()
    fig.suptitle("images show",fontsize=14,fontweight='bold',y=1.02)
    plt.show()

'''C将像素RGB颜色投射到色彩空间中，直观感受图像颜色的分布'''
def imageColorPoints(imgPath,imgList,nrows):
    ncols=math.ceil(len(imgList)/nrows)
    fig = plt.figure()
    for i in range(len(imgList)):
    #for i in range(24):
        #print(1)
        ax=fig.add_subplot(nrows,ncols,i+1,projection='3d')
        #for i in range(len(imgList)):
        img=os.path.join(imgPath,imgList[i])
        lum_img=mpimg.imread(img)
        lum_imgSmall=misc.imresize(lum_img,0.01)#调整大小后分辨率为原来的0.01倍
#        print(lum_imgSmall)
#        print(lum_imgSmall[:,:,0],lum_imgSmall[:,:,1],lum_imgSmall[:,:,2])
        ax.scatter(lum_imgSmall[:,:,0],lum_imgSmall[:,:,1],lum_imgSmall[:,:,2],c=(lum_imgSmall/255).reshape(-1,3),marker='+')
        #用rgb的三个分量值作为颜色的空间坐标，并显示其颜色。设置颜色时，需要将0-255缩放至0-1区间内
        ax.set_xlabel('r',labelpad=10)
        ax.set_ylabel('g',labelpad=10)
        ax.set_zlabel('b',labelpad=10)
        ax.set_title(i+1)
        fig.set_figheight(a)
        fig.set_figwidth(b)
#    plt.subplots_adjust(wspace=0.4,hspace=0.2,top=0.9,bottom=0.1)
    fig.tight_layout()
    plt.show()
'''建立图像颜色HSV各分量的直方图，分析颜色色彩分布情况'''
def imageColorHist(imgPath,imgList,nrows):
    ncols=math.ceil(len(imgList)/nrows)#4
    fig,axes=plt.subplots(ncols,nrows,sharex=True,sharey=True,figsize=(15,20))
    ax=axes.flatten()
#    print(ax)
    num_bins = 30    #设置直方图的bin参数，及柱数量
    totalH=np.array([])
    totalS=np.array([])
    totalV=np.array([])
#    print(imgList)
    for i in range(len(imgList)):
#        print(i)
        img=os.path.join(imgPath,imgList[i])
        lum_img=mpimg.imread(img)
        lum_imgSmall=misc.imresize(lum_img, 0.1)
        lum_imgSmallHSV=mpc.rgb_to_hsv(lum_imgSmall/255)
        
        
#RGB空间结构不符合人们对于颜色相似性的主观判断，因此将其转换为HSV空间，更接近人对于颜色的主观认识。

        ax[i].hist(lum_imgSmallHSV[...,0].flatten(), num_bins, normed=1)
        fig.set_figheight(a)
        fig.set_figwidth(b)  #提取H色调分量
#        print(toralH.shape,lum_imgSmallHSV[...,0].reshape(-1))
        totalH=np.append(totalH,lum_imgSmallHSV[...,0].reshape(-1))#疑问！！！！！！！！！！！！！！！！！！！！！！！！！
        totalS=np.append(totalS,lum_imgSmallHSV[...,1].reshape(-1))
        totalV=np.append(totalV,lum_imgSmallHSV[...,2].reshape(-1))
        ax[i].set_title(i+1)
    fig.tight_layout()
    fig.suptitle("images HSVshow",fontsize=14,fontweight='bold',y=1.02)
    
#    print(lum_imgSmallHSV[...,0].reshape(-1))    
    totalStat,(totalAXH,totalAXS,totalAXV)=plt.subplots(ncols=3,figsize=(10, 3))
    totalAXH .hist(totalH*360,num_bins,normed=1,facecolor='y')
    totalAXS.hist(totalS*100,num_bins,normed=1,facecolor='k')
    totalAXV.hist(totalV*100,num_bins,normed=1,facecolor='g')
    
    plt.show()

if __name__=="__main__":
    dirpath=r"D:\python\陕北照片"
    fileType=['jpg']
     fileInfo=filePath(dirpath,fileType)
#    print(fileInfo)
    
    filePathKeys=list(fileInfo.keys())
    print(filePathKeys)
    imgPath=filePathKeys[0]
    
    imgList=fileInfo[filePathKeys[0]]
#    print(len(imgList))
    a=10
    b=10
    nrows=4
    imgShow(imgPath,imgList,nrows)
    imageColorPoints(imgPath,imgList,nrows)
    imageColorHist(imgPath,imgList,nrows)
 
