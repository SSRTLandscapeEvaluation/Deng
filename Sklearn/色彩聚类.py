# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 00:10:55 2018

@author: Ao
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:28:41 2017
 
@author: RichieBall-caDesign设计(cadesign.cn)
"""
print(__doc__)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy.random import rand
from scipy import misc
 
from sklearn import cluster, datasets, mixture
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler
 
import os
import time
import warnings
from itertools import cycle, islice
import json
 
'''A以文件夹名为键，值为包含该文件夹下所有文件名的列表。文件类型可以自行定义 '''
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
 
'''B读取图像为RGB数组，并调整图像大小，减少计算时间。调整图像数组形状为2维，用于下一步骤的聚类计算'''
def getPixData(img):
        lum_img=mpimg.imread(img)  #读取图像为数组，值为RGB格式0-255
        lum_imgSmall=misc.imresize(lum_img, 0.2)  #传入图像的数组，调整图片大小
        h, w, d=lum_imgSmall.shape
        pixData=np.reshape(lum_imgSmall, (h*w, d))  #调整数组形状为2维
        return lum_imgSmall,pixData
 
'''C聚类的方法提取图像主题色，并打印图像、聚类预测类的二维显示和主题色带'''
def cityColorThemes(imgInfo):    
    #设置聚类参数，本实验中仅使用了KMeans算法，其它算法可以自行尝试
    default_base = {'quantile': .3,
                    'eps': .3,
                    'damping': .9,
                    'preference': -200,
                    'n_neighbors': 10,
                    'n_clusters': 7}    
    datasets=[((i[1],None),{}) for i in imgInfo] #基于pixData的图像数据，用于聚类计算
    imgList=[i[0] for i in imgInfo]  #基于lum_imgSmall的图像数据，用于图像显示
#    print(datasets[0])
    #官方聚类案例中对于dataset的配置，此处留作记录，可以对比官方案例中配置的变化
#    datasets = [
#            (noisy_circies,{'damping': .77,'preference': -240,'quantile': .2,'n_clusters': 2}),
#            (noisy_moons,{'damping': .75,'preference': -220,'n_clusters':2}),
#            (varied,{'eps': .18,'n_neighbors':2}),
#            (aniso,{'eps': .15,'n_neighbor':2}),
#            (blobs,{}),
#            (no_atructure,{})
#            ]
    themes=np.zeros((default_base['n_clusters'],3))   #建立0站位的数组，用于后期主题数组的追加，'n_clusters'为提取主题色的聚类数量，此处为7，轴为3，是色彩RGB的值
    (img,pix)=imgTnfo[0] #可以一次性提取元素索引值相同的值，img就是lum_imgSmall,而pix是pixData
    pixV,pixH=pix.shape#获取pixData的数据形状，用于pred预测初始值建立
    
    
    
    
    
    
    
    
    
    
    
    plt.show()
    return themes,pred
 
'''D显示所有图像主题色，获取总体印象'''
def cityColorImpression(themes):  
    n_samples=themes.shape[0]
'''跟随课程自行补全代码'''      
    plt.show()
 
'''E保存文件。因为对于大量数据聚类计算花费时间较长，因此建议将数据存储在文件中，以备之后调用。savingData()函数将文件存储为json数据格式''' 
def savingData(data,savingPath,name):
    jsonFile=open(os.path.join(savingPath,str(time.time())+r'_cityColorImpression_%s.json'%name),'w')
    json.dump(data.tolist(),jsonFile)  #将numpy数组转换为列表后存储为json数据格式
    jsonFile.close()
    
if __name__ == "__main__":
    savingPath=r"D:\MUBENAcademy\pythonSystem\code"
#    dirpath=r"D:\digit-x\southernInternship"
    dirpath=r'D:\r_academiccommunication\GPSToolBox\export'
    fileType=["jpg","png"] 
    fileInfo=filePath(dirpath,fileType)
#    print(fileInfo)
    filePathKeys=list(fileInfo.keys())
    selection=2 #选择待分析图像文件夹索引
    imgPath=filePathKeys[selection]  
#    print(imgPath)  #通过打印路径核实所选文件夹是否正确
    imgList=fileInfo[filePathKeys[selection]]
    imgPathList=[os.path.join(imgPath,i) for i in imgList]
    imgInfo=[(getPixData(img)) for img in imgPathList]    
#    print(imgPathList)
#    print(imgInfo[0][1])
'''图像主题色显示与印象'''    
    themes,pred=cityColorThemes(imgInfo)
    cityColorImpression(themes)
'''存储数据'''    
    nameThemes=r'themes'
    savingData(themes,savingPath,nameThemes)
    namePred=r'pred'
    savingData(pred,savingPath,namePred)