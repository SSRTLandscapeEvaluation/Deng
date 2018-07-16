# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:50:29 2018

@author: Ao
"""
import time 
import warnings

import numpy as np
import matplotlib.pyplot as plt

from sklearn import cluster,datasets,mixture
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler
from itertools import cycle,islice

np.random.seed(0)

#==================
#
#
#==================
n_samples = 1500
noisy_circles = datasets.make_circles(n_samples=n_samples, factor=.5,
                                      noise=.05)
noisy_moons = datasets.make_moons(n_samples=n_samples,noise = .05)

