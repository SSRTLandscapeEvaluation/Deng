# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:23:44 2018

@author: Ao
"""

import os
import exifread
import csv
'''读取文件'''

#'''
def filePath(dirpath,fileType):
    fileInfo={}
    i=0
    for dirpath,dirNames,fileNames in os.walk(dirpath):
        i+=1
        if fileNames:
            tempList = [f for f in fileNames if f.split('.')[-1] in fileType]
            if tempList:
                fileInfo.setdefault(dirpath,tempList)
    return fileInfo


def exifread_infos(photo):
 
    #加载 ExifRead 第三方库  https://pypi.org/project/ExifRead/
    #获取照片时间、经纬度信息
    #photo参数：照片文件路径
    
    # Open image file for reading (binary mode) 
    f = open(photo, 'rb')
    # Return Exif tags
    tags = exifread.process_file(f)

    try:
        #拍摄时间
#        Time=tags["EXIF DateTimeOriginal"].printable
#        print(EXIF_Date)
        #纬度
        LatRef=tags["GPS GPSLatitudeRef"].printable
        Lat=tags["GPS GPSLatitude"].printable[1:-1].replace(" ","").replace("/",",").split(",")
        Lat=float(Lat[0])+float(Lat[1])/60+float(Lat[2])/float(Lat[3])/3600
        if LatRef != "N":
            Lat=Lat*(-1)
        #经度
        LonRef=tags["GPS GPSLongitudeRef"].printable
        Lon=tags["GPS GPSLongitude"].printable[1:-1].replace(" ","").replace("/",",").split(",")
        Lon=float(Lon[0])+float(Lon[1])/60+float(Lon[2])/float(Lon[3])/3600
#        print(Lon)
        if LonRef!="E":
            Lon=Lon*(-1)
        f.close()
    except :
        return "ERROR:请确保照片包含经纬度等EXIF信息。"
    else:
        return Lat,Lon

if __name__ == "__main__":
    dirpath="D:\python\Deng\Visual_quality_Assessment\Flask"
    fileType=["jpg","JPG"]
    fileInfo = filePath(dirpath,fileType)
#    print(type(fileInfo.keys()))
    fileInfoKeys=list(fileInfo.keys())
    imgPath=fileInfoKeys[0]
    imgList=fileInfo[fileInfoKeys[0]]
    imgPathList=[os.path.join(imgPath,i) for i in imgList]
#    print(imgPathList)
    csvFile = open('PhotoInfo.csv','w')
    fileHeader=["Name","Time","Latitude","Longtitude"]
    writer=csv.writer(csvFile)
    writer.writerow(fileHeader)
    for photo in imgPathList:
        print(photo)
        Lat , Lon = exifread_infos(photo)
        print(Lat,Lon)
        time=''
        row = [photo,time,Lat,Lon]
        writer.writerow(row)
        
    csvFile.close()    
        
    
    
    
    
    
    