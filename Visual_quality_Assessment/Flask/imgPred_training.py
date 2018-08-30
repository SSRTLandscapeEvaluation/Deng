# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 22:50:46 2018

@author: Ao
"""

import pickle
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import preprocessing

'''用极端随机森林训练图像分类器'''
class ERFTrainer(object):
    def __init__(self,X,label_words):
        self.le=preprocessing.LabelEncoder()
        self.clf=ExtraTreesClassifier(n_estimators=100,max_depth=16,random_state=0)
        y=self.encode_labels(label_words)
        self.clf.fit(np.asarray(X),y)
        with open('clf.pkl', 'wb') as f:
            pickle.dump(self.clf, f)
    '''对标签编码，及训练分类器'''
    def encode_labels(self,label_words):
        return np.array(self.le.transform(label_words),dtype=np.float64)
    
    '''对位置数据的预测分类'''
    def classify(self,X):
        label_nums=self.clf.predict(np.asarray(X))
        label_words=self.le.inverse_transform([int(x) for x in label_nums])
        return label_words
    
if __name__ == "__main__":
    with open(r'feature_map.pkl','rb') as f:
        feature_map = pickle.load(f)
#    print(feature_map[0])
    label_words=[x['object_class'] for x in feature_map]
#    print(label_words)
    dim_size=feature_map[0]['feature_vector'].shape[1]
#    print(dim_size)
    X=[np.reshape(x['feature_vector'],(dim_size,)) for x in feature_map]
#    print(X[:2])
    erf=ERFTrainer(X,label_words)
    with open('erf.pkl','wb') as f:
        pickle.dump(erf,f) 