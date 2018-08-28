# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 01:29:22 2018

@author: Ao
"""

import math
import numpy as np

def gussoinBlur(sigma,kernalN):
#    g=pow(math.e,-(pow(x,2)+pow(y,2))/(2*pow(sigma,2)))/(2*math.pi*pow(sigma,2))#二维高斯函数
    kernal=np.ones((kernalN,kernalN,2))
    print(kernal)
    coordi=[i for i in range(-math.floor(kernalN/2),math.floor(kernalN/2)+1)]
    
    coordiArrayRow = np.array(coordi)
    coordiArrayCol=np.array(coordi[::-1]).reshape((-1,1))
    print(coordiArrayRow,coordiArrayCol)
    kernalS=np.dstack((kernal[...,0]*coordiArrayRow,kernal[...,1]*coordiArrayCol))
    print(kernalS)
    g=pow(math.e,-(pow(kernalS[...,0],2)+pow(kernalS[...,1],2))/(2*pow(sigma,2)))/(2*math.pi*pow(sigma,2))#二维高斯函数
    print(g)
    return g

if __name__ == "__main__":
    gussoinBlur(1.5,3)