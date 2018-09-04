# -*- coding: utf-8 -*-
'''
Created on Wed Feb  7 02:35:31 2018

@author: RichieBall-caDesign设计(cadesign.cn)
'''
import pandas as pd
import sqlite3
from scipy import misc
import matplotlib.image as mpimg
import os
from config import DevConfig

fileName_1=r'D:\python\Deng\Visual_quality_Assessment\Flask\static\images\imagesA\PhotoInfo.csv'  #记录所拍摄图像的信息文件，不同的手机app，获取信息的存储方式不同，例如前文在基于GPS调研与数据读取部分
#fileName_2=r'static/images/imagesA/2017.12.15-lmk-S-WTSolutions-GPS.csv'
imresizeFN=r'D:\python\Deng\Visual_quality_Assessment\Flask\static\images\imresize' #用于存储调整图像大小后的图像路径

'''读取存储图像信息文件为dataframe格式'''
def csvReading(fileName):
    csvData=pd.read_csv(fileName)  #读取存储有图像信息的csv文件，并存储到dataframe中
    return csvData

'''调整图像大小并存储，及返回需要的图像信息'''
def getPixData(imgInfo):  #调整图像大小，便于网页显示
    imgPath=imgInfo['imagename']
    #print(imgPath)
    #print("sssssssssssssssss")
    pathTemp=[]
    for img in imgPath:
        print(type(img))
        print("sssssssssssssssss")
        try:
            imgrepath=os.path.join('D:\python\Deng\Visual_quality_Assessment\Flask\static\images\imagesA',img)
            print(imgrepath)
            lum_img=mpimg.imread(imgrepath)  # 读取图像为数组，值为RGB格式0-255

        except:
            print('aaaaaaaaaaaa')
            pass
        lum_imgSmall = misc.imresize(lum_img, 0.3)  # 传入图像的数组，调整图片大小。scipy.misc.imresize(*args, **kwds)：This function is only available if Python Imaging Library (PIL) is installed.使用pip install Pillow安装
        misc.imsave(os.path.join(imresizeFN,img),lum_imgSmall) #存储调整大小的图像，用于下一步的图像识别，以及减小网页显示的压力
        pathTemp.append(imresizeFN+img[:-4]+'.JPG')
    #print(pathTemp)
    imgInfo['imagename']=pathTemp
    return imgInfo

if __name__ == "__main__":
    fn_1 = csvReading(fileName_1)
    #fn_2 = csvReading(fileName_2)
    imageFN = pd.concat([fn_1]) #手机app拍摄图像时，信息存储在了两个文件中，需要分别读取后并合并
    imageFN.columns = ['imagename', 'time', 'long', 'lat'] #为方便编程，修改framedata的列索引为英文
    imgInfo=getPixData(imageFN)
    # print(imgInfo)
    conn=sqlite3.connect(DevConfig().DATABASE) #连接数据库
    imgInfo.to_sql('imagesinfodf',conn)  #将dataframe数据存储到SQlite数据库中，表结构根据framedata索引自动建立