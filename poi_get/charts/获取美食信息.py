# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:58:43 2017

@author: RichieBall
"""
#百度地图POI数据采集, http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi 
#POI,  http://lbsyun.baidu.com/index.php?title=lbscloud/poitags 
from urllib.request import urlopen
from urllib import parse
import json  #json数据格式
import csv  #csv数据格式
import conversionofCoordi as cc  #百度坐标转换为GPS84坐标系
#import time

#leftBottom=[108.776852,34.186027]   #百度地图坐标拾取系统  http://api.map.baidu.com/lbsapi/getpoint/index.html 
#rightTop=[109.129275,34.382171]

leftBottom=[108.789929,34.177257]  
rightTop=[109.137753,34.394395]

partition=4
urlRoot=' http://api.map.baidu.com/place/v2/search? ' #行政区划区域检索: http://api.map.baidu.com/place/v2/search?query=ATM 机&tag=银行&region=北京&output=json&ak=您的ak //GET请求
#urlRootDetail=' http://api.map.baidu.com/place/v2/detail? ' #地点详情检索服务: http://api.map.baidu.com/place/v2/detail?uid=5a8fb739999a70a54207c130& ;output=json&scope=2&ak=您的密钥 //GET请求
poiName='美食'
AK='vxCvnNy8lMZdZNl0ugq4MlujIW4H3TKD' #百度地图API，注册后获取。 http://lbsyun.baidu.com/ 
fileName="baiduMapPoiSpotDetail2.csv"
#fileJsonName="baiduMapPoiSpotDetail2.json"
csvFile=open(fileName,'w')
jsonFile=open(fileJsonName,'w')

'''数据采集，并分别存储为csv和json两种数据格式'''
def scrapingData(leftBottom,rightTop,partition,urlRoot,poiName,AK,csvFile):
    xDis=(rightTop[0]-leftBottom[0])/partition  #分片范围，确保数据下载量
    yDis=(rightTop[1]-leftBottom[1])/partition
    jsonDic=[]  #提取采集数据，用于json数据格式的文件存储
    writer=csv.writer(csvFile)    #csv写入数据
    num=0  
    for i in range(partition):  
        for j in range(partition):
            leftBottomCoordi=[leftBottom[0]+i*xDis,leftBottom[1]+j*yDis]  #定义左下角坐标
            #rightTopCoordi=[rightTop[0]+i*xDis,rightTop[1]+j*yDis]
            rightTopCoordi=[leftBottom[0]+(i+1)*xDis,leftBottom[1]+(j+1)*yDis]  #定义右上角坐标
            #print(leftBottomCoordi,rightTopCoordi)
            for p in range(20):   #逐次采集 
                query={  #参数设置可以查看百度数据采集API说明  http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi 
                   'query':poiName,
                   'page_size':'20', 
                   'page_num':str(p),
                   'scope':2,  #此参数设置为2时，即采集detail详细信息，设置为1是仅采集基本信息
                   'bounds':str(leftBottomCoordi[1]) + ',' + str(leftBottomCoordi[0]) + ','+str(rightTopCoordi[1]) + ',' + str(rightTopCoordi[0]),
                   'output':'json',  #设置采集的格式
                   'ak':AK,                   
                }
                #url=urlRoot+'query=' + parse.urlencode(query) + '&page_size=20&page_num=' + str(p) + '&scope=1&bounds=' + str(leftBottomCoordi[1]) + ',' + str(leftBottomCoordi[0]) + ','+str(rightTopCoordi[1]) + ',' + str(rightTopCoordi[0]) + '&output=json&ak=' + AK;     
                url=urlRoot+parse.urlencode(query)
                #print(url)
                #time.sleep(0.1)
                data=urlopen(url)
#                print(data)
                responseJson=json.loads(data.read())  #读取采集的数据，该数据为json格式，因此调用json库方法              
                #print(responseJson.get("message"))  #查看采集信息是否成功
                if responseJson.get("message")=='ok':
                    results=responseJson.get("results")     
                    #print(results)
                    csvRow=[]
                    for row in range(len(results)):  
                        #print(results[row])
                        subData=results[row]
                        orgiCoordi=[subData.get('location').get('lng'),subData.get('location').get('lat')]
                        converCoordiGCJ=cc.bd09togcj02(orgiCoordi[0], orgiCoordi[1])  #转换百度坐标系为GPS84
                        converCoordiGPS84=cc.gcj02towgs84(converCoordiGCJ[0],converCoordiGCJ[1])
                        #csvRow=[subData.get('name'),subData.get('location').get('lat'),subData.get('location').get('lng'),subData.get('address')]
                        csvRow=[subData.get('name'),converCoordiGPS84[0],converCoordiGPS84[1],subData.get('uid'),subData]
                        #print(csvRow)
                        writer.writerow(csvRow)  #写入csv格式
                        writer.writerow([subData])
                        jsonDic.append(subData)
                        #jsonData=json.dumps([subData])
                        #jsonFile.write(jsonData)                        
            num+=1
            print("第"+str(num)+"个区域写入csv/json文件")
    json.dump(jsonDic,jsonFile)  #写入json格式
    jsonFile.write('\n') 

try:
    scrapingData(leftBottom,rightTop,partition,urlRoot,poiName,AK,csvFile)
finally:
    csvFile.close()
    jsonFile.close()