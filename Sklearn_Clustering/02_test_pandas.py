# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 15:06:57 2018

@author: Ao
"""
import numpy as np
import pandas as pd
df=pd.DataFrame([['urbanland','H',80,'class1'],['framland','M',100,'class2'],['forest','L',200,'class1']])
df.columns=['landUse','saftyLevel','gyrate_mn','classlabel']
print(df)
print('\n')

'''
**有序特征**
'''

saftyLevel_mapping={'H':3,'M':2,'L':1}
df['saftyLevel']=df['saftyLevel'].map(saftyLevel_mapping)
print(df)
print('\n')

'''
**替换回来**

inv_saftyLevel_mapping={v:k for k,v in saftyLevel_mapping.items()}
df['saftyLevel']=df['saftyLevel'].map(inv_saftyLevel_mapping)
print(df)

'''
'''
**替换class类**
'''

class_mapping={label:idx for idx,label in enumerate(np.unique(df['classlabel']))}
print(class_mapping)
df['classlabel']=df['classlabel'].map(class_mapping)
print(df)

'''
**替换回来**

inv_class_mapping={v:k for k,v in class_mapping.items()}
df['classlabel']=df['classlabel'].map(inv_class_mapping)
print(df)
'''

'''
***sklearn的LabelEncoder类***
'''
from sklearn.preprocessing import LabelEncoder
class_label = LabelEncoder()
y=class_label.fit_transform(df['classlabel'].values)
print(y)

'''
**独热编码**
'''
X=df[['landUse','saftyLevel','gyrate_mn']].values
#print(X)
X[:,0]=class_label.fit_transform(X[:,0])
print(X)
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features=[0])
ohe.fit_transform(X).toarray()
print(ohe.fit_transform(X).toarray())


























