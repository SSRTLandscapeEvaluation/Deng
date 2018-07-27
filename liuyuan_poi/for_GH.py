# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:59:36 2018

@author: Ao
"""
from urllib.request import urlopen
from urllib import parse
#from bs4 import BeautifulSoup
import json
#import pymysql
import csv
import conversionofCoordi as cc
import os
import numpy as np
import time


filePath = r'D:\python\Deng\liuyuan_poi\baiduMapPoiLandscape.csv'
f = open(filePath,'r')
csvReader=csv.reader(f)
List =[]
for row in csvReader :
    print(row)
#    i=2
#    if i%2 == 0 :
#    i+=1
    LIST=row.split(',')
    print(LIST)