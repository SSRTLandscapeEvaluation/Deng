# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:23:23 2018

@author: Ao
"""

def scrapingBatch(poiNameClassify):
    for idData,(poiName,fileSubName) in enumerate(poiNameClassify.items()):
        fileName="poi_"+str(idData)+"_"+fileSubName
        csvFilePath=fileName+".csv"
        jsonFilePath=fileName+".json"
        csvFile=open(csvFilePath,'w')
        jsonFile=open(jsonFilePath,'w')
        scrapingData(leftBottom,rightTop,partition,urlRoot,poiRoot,poiName,AK,csFile,jsonFile)
        csvFile.close()
        jsonFile.close()
        print(str(idData)+"_"+poiName)
if __name__=="__main__":
    leftBottom=[  ,  ]
    rightTop=[   ,   ]
    
    partition=2
    urlRoot='http://api.map.baidu.com/place/v2/search?'










poiNameClassify={
        "美食":"delicacy",
        "酒店":"hotel",
        "购物":"delicacy",
        "生活服务":"delicacy",
        "丽人":"delicacy",
        "旅游景点":"delicacy",
        "休闲娱乐":"delicacy",
        "运动健身":"delicacy",
        "教育培训":"delicacy",
        "文化传媒":"delicacy",
        "医疗":"delicacy",
        "汽车服务":"delicacy",
        "交通设施":"delicacy",
        "金融":"delicacy",
        "房地产":"delicacy",
        "公司企业":"delicacy",
        "政府机构":"delicacy",
        }
count=0
print(poiNameClassify.items())
for idx,(name,nameID) in enumerate(poiNameClassify.items()):
    print(idx)
    print(name,nameID)