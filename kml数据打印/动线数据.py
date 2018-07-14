#-*-coding:utf-8-*-
"""
Created on Tue Sep19

@author:Ball Ball
"""
import matplotlib.pyplot as plt

from pylab import mpl #解决matplotlib中文显示问题，matpllotlib提供的pylab的模块
mpl.rcParams['font.sans-serif'] = ['SimHei']#可在交互式解释器中，直接输入mpl.rcParams查看参数

filePath='D:\python\data.txt'
f=open(filePath,'r')
dataList=[]
while True:
    line=f.readline().split()#line 是一个列表
#    print(line)
    if len(line)!=0:
        dataList.append(line)
    if not line:break

print(dataList)	
itemName = dataList.pop(0)
#print(itemName)

temp_A=[i[1]for i in dataList]
humi_A=[i[2]for i in dataList]
lightItem_A=[i[3] for i in dataList]
timeline=[int(i[-3])*3600+int(i[-2])*60+int(i[-1])for i in dataList]
relativeTimeline=[i-timeline[0]for i in timeline]#将时间转化为相对时间

#print(temp_A,humi_AlightItem_A,relativeTimeline]

legend=plt.plot(relativeTimeline,temp_A,'r--',relativeTimeline,humi_A,'b--',relativeTimeline,lightItem_A,'y--')
#print(legend)
plt.xlabel(r'时间线')
plt.ylabel(r'测量值')
plt.legend([legend[0],legend[1],legend[2]],["temp_A","humi_A","lightItem_A"],bbox_to_anchor=(1,0.5))
plt.show()

f.close()











