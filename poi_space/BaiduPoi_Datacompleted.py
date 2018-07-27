# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:58:43 2017

@author: Richie
"""
#百度地图POI数据采集,http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi
#POI, http://lbsyun.baidu.com/index.php?title=lbscloud/poitags
from urllib.request import urlopen
from urllib import parse
#from bs4 import BeautifulSoup
import json
#import pymysql
import csv
import conversionofCoordi as cc
#import os
#import numpy as np
#import time
#conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='#',db='mysql',charset='utf8')
#cur=conn.cursor()
#cur.execute("USE scraping")




def scrapingData(leftBottom,rightTop,partition,urlRoot,poiName,AK,csvFile,jsonFile):
    xDis=(rightTop[0]-leftBottom[0])/partition
    yDis=(rightTop[1]-leftBottom[1])/partition
    jsonDic=[]
    writer=csv.writer(csvFile)
    num=0
    for i in range(partition):
        for j in range(partition):
            leftBottomCoordi=[leftBottom[0]+i*xDis,leftBottom[1]+j*yDis]
            #rightTopCoordi=[rightTop[0]+i*xDis,rightTop[1]+j*yDis]
            rightTopCoordi=[leftBottom[0]+(i+1)*xDis,leftBottom[1]+(j+1)*yDis]
            #print(leftBottomCoordi,rightTopCoordi)
            for p in range(20):    
                query={
                   'query':poiName,
                   'page_size':'20', 
                   'page_num':str(p),
                   'scope':2,
                   'bounds':str(leftBottomCoordi[1]) + ',' + str(leftBottomCoordi[0]) + ','+str(rightTopCoordi[1]) + ',' + str(rightTopCoordi[0]),
                   'output':'json',
                   'ak':AK,                   
                }
                #url=urlRoot+'query=' + parse.urlencode(query) + '&page_size=20&page_num=' + str(p) + '&scope=1&bounds=' + str(leftBottomCoordi[1]) + ',' + str(leftBottomCoordi[0]) + ','+str(rightTopCoordi[1]) + ',' + str(rightTopCoordi[0]) + '&output=json&ak=' + AK;     
                url=urlRoot+parse.urlencode(query)
                #print(url)
                data=urlopen(url)
#                print(data)
                responseJson=json.loads(data.read())                
#                print(responseJson.get("message"))
                if responseJson.get("message")=='ok':
                    results=responseJson.get("results")     
                    #print(results)
                    csvRow=[]
                    for row in range(len(results)):  
                        subData=results[row]
                        orgiCoordi=[subData.get('location').get('lng'),subData.get('location').get('lat')]
                        converCoordiGCJ=cc.bd09togcj02(orgiCoordi[0], orgiCoordi[1])
                        converCoordiGPS84=cc.gcj02towgs84(converCoordiGCJ[0],converCoordiGCJ[1])
                        #csvRow=[subData.get('name'),subData.get('location').get('lat'),subData.get('location').get('lng'),subData.get('address')]
                        csvRow=[subData.get('name'),converCoordiGPS84[0],converCoordiGPS84[1],subData.get('uid'),subData]
                        #print(csvRow)
                        writer.writerow(csvRow)
                        writer.writerow([subData])
                        jsonDic.append(subData)
            num+=1
            print("第"+str(num)+"个区域写入csv文件")
    json.dump(jsonDic,jsonFile)
    jsonFile.write('\n')

def scrapingBatch(poiNameClassify):
    for idData,(poiName,fileSubName) in enumerate(poiNameClassify.items()):
        fileName="poi_"+str(idData)+"_"+fileSubName
        csvFilePath=fileName+".csv"
        jsonFilePath=fileName+".json"
        csvFile=open(csvFilePath,'w')
        jsonFile=open(jsonFilePath,'w')
        scrapingData(leftBottom,rightTop,partition,urlRoot,poiName,AK,csvFile,jsonFile)
        csvFile.close()
        jsonFile.close()
        print(str(idData)+"_"+poiName)
 
if __name__=="__main__":
    leftBottom=[108.774279,34.171116]
    rightTop=[109.129577,34.387793]
    partition=2
    urlRoot='http://api.map.baidu.com/place/v2/search?'
    poiNameClassify={
            "美食":"delicacy",
            "酒店":"hotel",
            "购物":"shopping",
            "生活服务":"lifeService",
            "丽人":"beauty",
            "旅游景点":"spot",
            "休闲娱乐":"entertaiment",
            "运动健身":"sports",
            "教育培训":"education",
            "文化传媒":"media",
            "医疗":"medicalTreatment",
            "汽车服务":"carService",
            "交通设施":"trafficFacilities",
            "金融":"finance",
            "房地产":"realEstate",
            "公司企业":"corporation",
            "政府机构":"goveenment",
            }
    #poiName='旅游景点'
    AK='Xa040VZ1nm3sw9nGWcRHjik7nIY5STa4'
    #fileName="baiduMapPoiLandscape.csv"
    #fileJsonName="baiduMapPoiLandscape.json"
    #csvFile=open(fileName,'wt',encoding='utf-8')
    #csvFile=open(fileName,'w')
    #jsonFile=open(fileJsonName,'w')
    try:
        scrapingBatch(poiNameClassify)
    finally:
#        csvFile.close() 
#        jsonFile.close() 
        print("Finished!")