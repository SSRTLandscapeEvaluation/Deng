# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 18:59:44 2017 
@author: RichieBall-caDesign设计(cadesign.cn)
"""
import os
import matplotlib.pyplot as plt
import re
import numpy as np

dirpath=r"D:\python\kmlPhotos"
 
'''A以文件夹名为键，值为包含该文件夹下所有文件名的列表。文件类型可以自行定义 '''
fileType=["jpg"] 
kmlType=["kml"]
def filePath(dirpath,fileType):
    fileInfo={}
    i=0
    for dirpath,dirNames,fileNames in os.walk(dirpath):
        i+=1
       # print(1,'\n')
#        print(dirpath,'\n',dirNames,'\n',fileNames,'\n')
        if fileNames:
            tempList = [f for f in fileNames if f.split('.')[-1] in fileType]
#            if not tempList:
#                print(i,"NULL")
#            print(tempList)
            if tempList:
                fileInfo.setdefault(dirpath,tempList)
    return fileInfo  
        
fileInfo=filePath(dirpath,fileType)
kmlInfo=filePath(dirpath,kmlType)
#kmlInfo.pop((list(kmlInfo.keys())[0]))
print(fileInfo)
print(kmlInfo)

'''B提取文件名包含的信息，本次实验中文件名格式为'20170719093319_30.242473-120.09893-49.2_.jpg'，可以提取出日期、经度、维度、高程和文件类型。以字典形式存储，便于后期数据处理'''
def coordiExtraction(fileInfo):
    coordiInfo={} #定义以文件夹为键，以tempDic子字典为值的字典
    for key in fileInfo.keys():
#        print(key) 
        tempDic = {}#d定义子字典，以文件名为键，提取的各类信息列表为值
        for val in fileInfo[key]:
#            print(val)
            valList=re.split('[_-]',val)
            if ' ' in valList:
                valList.remove(' ')
                valList[3]=-float(valList[3])
            valList[0]=int(valList[0])
            valList[1]=float(valList[1])
            valList[2]=float(valList[2])
            valList[3]=float(valList[3])
#            print(valList)
            tempDic.setdefault(val,valList)
#            print(tempDic)
        coordiInfo.setdefault(key,tempDic)
#        print(coordiInfo)
    return coordiInfo
coordiInfo=coordiExtraction(fileInfo)
#print(coordiInfo)
coordiSubKey=list(coordiInfo.keys())[0] #本次实验提取一个文件夹为进一步的实验对象
#print(coordiSubKey)
coordiSub=coordiInfo[coordiSubKey]
#print(coordiSubKey,'\n',coordiSub)


'''C提取.kml文件中的坐标信息'''
def kmlCoordi(kmlInfo):    
    kmlCoordiInfo={}
    pat=re.compile('<coordinates>(.*?)</coordinates>') 
    '''正则表达式函数，将字符串转换为模式对象.号匹配除换行符之外的任何字符串，但只匹配一个字母，增加*？字符代表匹配前面表达式的0个
    或多个副本，并匹配尽可能少的副本'''
    for key in kmlInfo.keys():
        tempDic={}
        for val in kmlInfo[key]:#提取一个kml文件
            f=open(os.path.join(key,val),'r',encoding='UTF-8')#kml文件中含有中文
            content=f.read().replace('\n',' ')#移除换行，从而可以根据模式对象提取标示符间的内容，同时忽略换行
#            print(content)    
            coordiInfo = pat.findall(content)#采集coordinates内的数据
#            print(coordiInfo)
            coordiInfoStr=' ' #设置一个空集
            for i in coordiInfo :
                coordiInfoStr = coordiInfoStr + i#将每一段的坐标数据叠合在一个数据中
#            print(coordiInfoStr)
                
            coordiInfoStrip=coordiInfoStr.replace(' ',',')#删除数据的空格
            coordiInfoStrip=coordiInfoStrip.replace(',,,,,,,,,,,,,,,,,,,,,',',')
#            a=type(coordiInfoStrip)
#            print(coordiInfoStrip)

            coordiInfoList=coordiInfoStrip.strip(',').split(',')#制表符已经被移除
#            print(coordiInfoList)
            n = 3
            coordiInfoList=[coordiInfoList[i:i + n] for i in range(0, len(coordiInfoList), n)]
#            print(coordiInfoList)
            coordi=[]
            for i in coordiInfoList:
#                coordiSplit=i.split(',')
#                print(coordiSplit)
#                coordiSplit=i.remove[2]
                temp=[]
                for j in i:
                    try:
                        temp.append(float(j))
                    except ValueError:
                        print("ValueError")                    
                if len(temp) == 3:
                    coordi.append(temp)
            f.close()
            tempDic.setdefault(val,coordi)
        kmlCoordiInfo.setdefault(key,tempDic)
        
    return kmlCoordiInfo
kmlCoordiInfo=kmlCoordi(kmlInfo)
#print(kmlCoordiInfo)#两层字典，第一层为{路径:{子字典}}，第二层为{文件名:坐标}
kmlSub=kmlCoordiInfo[coordiSubKey]
#print(kmlSub)#提取子字典
#print(len(list(kmlSub.keys())))
#'''
#D读取经纬度坐标，根据.kml文件打印成路径,同时定位图片位置并显示高程变化 
def researchPath(coordiSub,kmlSub):
    coordiValues=list(coordiSub.values())        
    coordiValuesArray=np.array(coordiValues) #将存储了值(子列表)的列表转化为numpy的数组
#    print(coordiValuesArray)
    kmlSubValues=list(kmlSub.values())#[0]
    kmlSubArray=np.array(kmlSubValues)
#    print(coordiValuesArray.shape)
    print(kmlSubArray)
#    print('\n','数组的维数/秩=',coordiValuesArray.ndim,'\n','数组的维度/轴=',coordiValuesArray.shape,'\n','数组元素的总个数=',coordiValuesArray.size,'\n','数组中每个元素的字节大小=',coordiValuesArray.itemsize,'\n','数据类型=',coordiValuesArray.dtype)
#    print(kmlSubArray)
    fig,ax=plt.subplots()
    for i in kmlSubArray:
        ax.plot(i[:,0],i[:,1],'b-',lw=0.7,markersize=5)
#        print(i)
#    ax.plot(kmlSubArray[:,0],kmlSubArray[:,1],'r-',lw=0.7,markersize=2)
    for k in coordiValuesArray:
        ax.plot(k[:,1],k[:,2],'r-',lw=0.7,markersize=10)
#    ax.plot(coordiValuesArray[:,2],coordiValuesArray[:,1],'r+-',lw=0.5,markersize=5)
#    cm=plt.cm.get_cmap('hot')
#    sc=ax.scatter(coordiValuesArray[:,1],coordiValuesArray[:,2],c=coordiValuesArray[:,3],s=50,alpha=0.8,cmap=cm)   
#    fig.colorbar(sc)
    ax.set_xlabel('lng')
    ax.set_ylabel('lat')
#    print(coordiValues[0][1],coordiValues[0][2])
    ax.annotate('origin',xy=(coordiValues[0][2],coordiValues[0][1]),xycoords='data',xytext=(coordiValues[0][2]+0.015, coordiValues[0][1]-0.006),fontsize=15,arrowprops=dict(facecolor='black',shrink=0.05))
    fig.text(0.50,0.92,'research path',fontsize=10,color='gray',horizontalalignment='center',va='top',alpha=0.5)    
    fig.set_figheight(50)
    fig.set_figwidth(50)
    plt.show()
researchPath(coordiSub,kmlSub)


#'''











