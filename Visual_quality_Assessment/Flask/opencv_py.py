# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 21:37:16 2018

@author: Ao
"""
import cv2
import numpy as np
import os

import matplotlib.pyplot as plt

rootDirectory = r'D:\python\Deng\Visual_quality_Assessment\horizontal_testImg'
inputImg_edge = r'D:\python\Deng\Visual_quality_Assessment\horizontal_testImg\toilet.jpg'
imgA=r'D:\python\Deng\Visual_quality_Assessment\horizontal_testImg\toilet.jpg'
imgB=r'D:\python\Deng\Visual_quality_Assessment\horizontal_testImg\tower.jpg'

#检测边
def edgeDetection(inputImg_edge):
    imgEdge=cv2.imread(inputImg_edge,cv2.IMREAD_GRAYSCALE)
    sobelHorizontal=cv2.Sobel(imgEdge,cv2.CV_64F,1,0,ksize=5)
    """
    help(cv2.Sobel)
    help(cv2.Sobel)
    Help on built-in function Sobel:

    Sobel(...)
    Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst

    .   @param src input image.
    .   @param dst output image of the same size and the same number of channels as src .
    .   @param ddepth output image depth, see @ref filter_depths "combinations"; in the case of
    .   8-bit input images it will result in truncated derivatives.
    .   @param dx order of the derivative x.
    .   @param dy order of the derivative y.
    .   @param ksize size of the extended Sobel kernel; it must be 1, 3, 5, or 7.
    .   @param scale optional scale factor for the computed derivative values; by default, no scaling is
    .   applied (see #getDerivKernels for details).
    .   @param delta optional delta value that is added to the results prior to storing them in dst.
    .   @param borderType pixel extrapolation method, see #BorderTypes
    .   @sa  Scharr, Laplacian, sepFilter2D, filter2D, GaussianBlur, cartToPolar
    """
    sobelVertical=cv2.Sobel(imgEdge,cv2.CV_64F,0,1,ksize=5)#索贝尔滤波器
    laplacian=cv2.Laplacian(imgEdge,cv2.CV_64F)
    canny=cv2.Canny(imgEdge,50,240)
    
#    print(imgEdge)
    cv2.namedWindow('img')
#    cv2.imshow('original',imgEdge)
#    cv2.imshow('sobel horizontal',sobelHorizontal)#输出显示图像
#    cv2.imwrite(os.path.join(rootDirectory,'sobel horizontal.jpg'),sobelHorizontal)
    cv2.imshow('laplacian',laplacian)
    cv2.imwrite(os.path.join(rootDirectory,'laplacian.jpg'),laplacian)
    
    cv2.waitKey()

#检测棱角
def cornerDetection(inputImg_edge):
    imgCorners=cv2.imread(inputImg_edge)
    imgGray=cv2.cvtColor(imgCorners,cv2.COLOR_BGR2GRAY)
    imgGray=np.float32(imgGray)
    imgHarris=cv2.cornerHarris(imgGray,7,5,0.04)
    print(imgHarris.max(),imgHarris.shape)
    imgHarris=cv2.dilate(imgHarris,np.ones((1,1)))
    print(imgCorners[300:500])
    imgCorners[imgHarris>0.01*imgHarris.max()]=[40,74,236]#定义阈值，显示重要的棱角
    cv2.imshow('harris corners',imgCorners)
    cv2.imwrite(os.path.join(rootDirectory,'harris corners.jpg'),imgCorners)
    cv2.waitKey()


#sift 尺寸不变特征点检测
def siftDetection(inputImg_edge):
    imgSift=cv2.imread(inputImg_edge)
    imgGray=cv2.cvtColor(imgSift,cv2.COLOR_BGR2GRAY)
    print(imgGray.shape)
    sift=cv2.xfeatures2d.SIFT_create()
    keypoints=sift.detect(imgGray,None)
    print(keypoints[:3],len(keypoints))
    for k in keypoints[:3]:
        print(k.pt,k.size,k.octave,k.response,k.class_id,k.angle)
        """
        关键点信息包含：
        k.pt关键点坐标
        k.size关键点直径大小
        k.octave从高斯金字塔的哪一层得到的数据
        k.response响应程度，
        k.class_id对图像进行分类
        k.angle角度，关键点方向
        """
    des = sift.compute(imgGray,keypoints)
    print(type(keypoints),type(des))
    print(des[0][:2])
    print(des[1][:2])
    print(des[1].shape)
    imgSift=np.copy(imgSift)
    cv2.drawKeypoints(imgSift,keypoints,imgSift,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    """
    help(cv2.drawKeypoints)
    """
    cv2.imshow('sift features',imgSift)
    cv2.imwrite(os.path.join(rootDirectory,'sift feature.jpg'),imgSift)
    cv2.waitKey()

#star特征点提取
def starDetection(inputImg_edge):
    imgStar=cv2.imread(inputImg_edge)
#    imgGray=cv2.cvtColor(imgSift,cv2.COLOR_BGR2GRAY)
    star=cv2.xfeatures2d.StarDetector_create()
    keypoints=star.detect(imgStar)
#    print(len(keypoints),keypoints)
    cv2.drawKeypoints(imgStar,keypoints,imgStar,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('star features',imgStar)
    cv2.imwrite(os.path.join(rootDirectory,'star feature.jpg'),imgStar)
    cv2.waitKey()

#sift图像匹配
def matchSift(imgA,imgB):
    img1 = cv2.imread(imgA,0)
    img2 = cv2.imread(imgB,0)
    sift=cv2.xfeatures2d.SIFT_create()
    kp1,des1 = sift.detectAndCompute(img1,None)
    kp2,des2 = sift.detectAndCompute(img2,None)
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    """
    """
    print(type(matches),matches[:2],(matches[0][0].distance,matches[0][1].distance))
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
    imgM = cv2.drawMatchesKnn(img1,kp1, img2,kp2,good[0:int(1*len(good))],None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    fig, ax = plt.subplots(figsize=(50,30))
    ax.imshow(imgM),plt.show()
    

if __name__ == "__main__":
#    cornerDetection(inputImg_edge)
#    edgeDetection(inputImg_edge)    
#    siftDetection(inputImg_edge)
#    starDetection(inputImg_edge)
    matchSift(imgA,imgB)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    