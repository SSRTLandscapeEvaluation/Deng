
from PIL import Image
import os


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


def CuttingImg(imgPathList):
    for i in imgPathList:
        
        img = Image.open(i) #打开当前路径图像
        
        box1 = (0, 100, 1080, 1820)    #设置图像裁剪区域
        
        image1 = img.crop(box1)   #图像裁剪
        
        image1.save(i)  #存储当前区域
    
if __name__ == "__main__" :    
    dirpath1=r"D:\python\rePhotos\CityWall\IN"
    dirpath2=r"D:\python\rePhotos\CityWall\OUT"    
    dirpath3=r"D:\python\rePhotos\MuslimStreet" 
    dirpathAll=[dirpath1,dirpath2,dirpath3]
    fileType=["JPG"]
    for dirpath in dirpathAll:
        fileInfo=filePath(dirpath,fileType)
#        print(fileInfo)
        fileInfo = filePath(dirpath,fileType)
#       print(type(fileInfo.keys()))
        fileInfoKeys=list(fileInfo.keys())
        imgPath=fileInfoKeys[0]
        imgList=fileInfo[fileInfoKeys[0]]
        imgPathList=[os.path.join(imgPath,i) for i in imgList]
        CuttingImg(imgPathList)