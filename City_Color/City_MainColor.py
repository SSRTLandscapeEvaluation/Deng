# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:59:16 2018

@author: Ao
"""

import numpy as np
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


'''
***part A
以文件夹名为键，值包含文件夹下所有文件名的列表，文件类型自定义
***
'''
