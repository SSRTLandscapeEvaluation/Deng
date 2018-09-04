# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 23:36:08 2018

@author: Ao
"""
import numpy as np
#import sqlite3
import pickle
import cv2
import os
from imgPred_training import ERFTrainer
import imgPred_buildFeatures as bf
import random 
#from sklearn.cluster import KMeans
from sklearn import preprocessing
'''创建图像识别/分类器'''
class ImageTagExtractor(object):
    
    def __init__(self, model_file, featK):
        with open(model_file,'rb') as f1:
            self.clf=pickle.load(f1)#读取储存的图像分类器模型
        
        with open(featK,'rb') as f2:
            self.kmeans,self.centroids=pickle.load(f2)#读取储存的聚类模型和聚类中心点
        
        '''对标签编码'''
        with open(r'feature_map.plk','rb') as f:
            self.feature_map = pickle.load(f)
        self.label_words = [x['object_class'] for x in self.feature_map]
        self.le = preprocessing.LabelEncoder()
        self.le.fit(self.label_words)
    
    def predict(self,img,scaling_size):
        img=bf.resize_image(img,scaling_size)
        feature_vector=bf.BagOfWords().construct_feature(img,self.kmeans,self.centroids)
        label_nums = self.clf.predict(np.asarray(feature_vector))
        image_tag = self.le.inverse_transform([int(x) for x in label_nums])[0]
        print(label_nums,image_tag)
        return image_tag

'''以文件夹名为键，值为包含该文件夹下所有文件名的列表。文件类型可以自行定义 '''
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
 
'''配置参数，随机抽取用于识别/分类的图像，验证模型预测结果'''
class predConfig(object):
    def __init__(self):
        self.model_file=r'clf.pkl'
        self.featK=r'featK.pkl'
        self.imgPred=r'D:\python\Deng\Visual_quality_Assessment\Flask\static\images\imaged'
        self.fileType = ["jpg","JPG"]
        self.selectNum = 3
        self.scaling_size =200
    
    def pred(self):
        fileInfo=filePath(self.imgPred, self.fileType)
        imgFNList = [key+r'/'+fn for key in fileInfo.keys() for fn in fileInfo[key]]
        rndImg=random.sample(imgFNList,random.randint(self.selectNum,len(imgFNList)))
        predInfo={fn:ImageTagExtractor(self.mode_file,self.featK).predict(cv2.imread(fn),self.scaling_size) for fn in rndImg}
        return predInfo

if __name__ == "__main__":
    predInfo=predConfig().pred()
    print(predInfo)