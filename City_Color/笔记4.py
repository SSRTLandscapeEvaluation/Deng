# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 17:57:29 2018

@author: Ao
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 09:11:20 2017
@author: Administrator
"""
import matplotlib.pyplot as plt
import matplotlib.image as mping
import numpy as np
from scipy import misc
#显示一张图片
img=r'D:\\python\\Deng\\City_Color\\test\\1.jpg'
wolf=mping.imread(img)
print(wolf.shape)
plt.imshow(wolf)
plt.axis('off')
#plt.show()
#显示图片的一个通道
wolf_1=wolf[:,:,0]
plt.imshow(wolf_1)
#plt.show()
# 此时会发现显示的是热量图，
#不是我们预想的灰度图，可以添加 cmap 参数，有如下几种添加方法：

plt.imshow(wolf_1,cmap='Greys_r')
#plt.show()