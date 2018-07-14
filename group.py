# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 00:40:15 2018

@author: 嗷~~
"""

l = list(range(15))
n = 3
print([l[i:i + n] for i in range(0, len(l), n)])