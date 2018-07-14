# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:49:15 2018

@author: Ao
"""

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
from scipy import misc

'''显示一个文件夹下所有图片，便于查看。'''
#imgPath :图片目录
#imgList :图片列表
#nrows :行数

#首先将文件夹下的图片名做成一个列表，需要遍历目录

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