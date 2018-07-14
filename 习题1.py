# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 21:25:04 2018

@author: D
"""

a=['cow','pig','horse']
b=['dog','cat','gold fish']
c=['lion','elephant','gorilla']
w=a+b+c
for x in range(len(w)):
    print("{0}:{1}".format(x,w[x]))
