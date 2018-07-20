# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 20:24:53 2018

@author: Administrator
"""
'''
 # 简单的生成器函数
def my_gen():
     n=1
     print("first")
     # yield区域
     yield n

     n+=1
     print("second")
     yield n

     n+=1
     print("third")
     yield n

 a=my_gen()
 print("next method:")
 # 每次调用a的时候，函数都从之前保存的状态执行
 print(next(a))
 print(next(a))
 print(next(a))

 print("for loop:")
 # 与调用next等价的
 b=my_gen()
 for elem in my_gen():
     print(elem)
     '''
def my_gen():
     n=1
     print("first")
     # yield区域
     yield n

     n+=1
     print("second")
     yield n

     n+=1
     print("third")
     yield n

def m2y_gen():
     n=1
     print("f")
     # yield区域
     yield n

     n+=1
     print("s")
     yield n

     n+=1
     print("t")
     yield n

a=my_gen()
b=m2y_gen()
print("next method:")
print(next(b))
