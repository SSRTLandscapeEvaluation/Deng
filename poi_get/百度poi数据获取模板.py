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

#conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='#',db='mysql',charset='utf8')
#cur=conn.cursor()
#cur.execute("USE scraping")
 
leftBottom=[108.776852,34.186027]
rightTop=[109.129275,34.382171]
partition=2
urlRoot='http://api.map.baidu.com/place/v2/search?'
poiName='丽人'
AK='Xa040VZ1nm3sw9nGWcRHjik7nIY5STa4'
fileName="baiduMapPoiLandscape2.csv"
#csvFile=open(fileName,'wt',encoding='utf-8')
csvFile=open(fileName,'w')

def scrapingData(leftBottom,rightTop,partition,urlRoot,poiName,AK,csvFile):
    xDis=(rightTop[0]-leftBottom[0])/partition
    yDis=(rightTop[1]-leftBottom[1])/partition
    
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
                   'scope':1,
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
                #print(responseJson)
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
                        csvRow=[subData.get('name'),converCoordiGPS84[0],converCoordiGPS84[1],subData.get('address')]
                        #print(csvRow)
                        writer.writerow(csvRow)
            num+=1
            print("第"+str(num)+"个区域写入csv文件")
#cur.close()
#conn.close()
try:
    scrapingData(leftBottom,rightTop,partition,urlRoot,poiName,AK,csvFile)
finally:
    csvFile.close()