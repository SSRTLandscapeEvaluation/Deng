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
blobs = datasets.make_blobs(n_samples=n_samples,random_state=8)
no_structure = np.random.rand(n_samples,2),None

#
random_state = 170
X,y = datasets.make_blobs(n_samples=n_samples,random_state=random_state)
transformation = [[0.6,-0.6],[-0.4,0.8]]
X_aniso = np.dot(X,transformation)
ansio = (X_aniso,y)

#
varied = datasets.make_blobs(n_samples=n_samples,
                             cluster_std=[1.0,2.5,0.5],
                             random_state=random_state)

#==============
#Set up cluster paramters
#==============
plt.figure(figsize=9*2+3,12.5)
plt.subplots_adjust(left=.02, right=.98, bottom=.001, top=.96, wspace=.05,
                    hspace=.01)

plot_num = 1

default_base = {'quantile': .3,
                'eps': .3,
                'damping': .9,
                'preference': -200,
                'n_neighbors': 10,
                'n_cluster': 3}
datasets = [
    (noisy_circles, {'damping': .77, 'preference': -240,
                     'quantile': .2, 'n_clusters': 2}),
    (noisy_moons, {'damping': .75, 'preference': -220, 'n_clusters': 2}),
    (varied, {'eps': .18, 'n_neighbors': 2}),
    (aniso, {'eps': .15, 'n_neighbors': 2}),
    (blobs, {}),
    (no_structure, {})]

































