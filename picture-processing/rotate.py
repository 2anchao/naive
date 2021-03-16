# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 14:42:03 2018

@author: Alex
"""

import os
import time
from PIL import Image
import numpy as np

def alter(path,object):
    s = os.listdir(path)
    count = 1
    for i in s:
        document = os.path.join(path,i)#作用是目录地址分别和每一个图片名字结合
        img = Image.open(document)#打开目录下的一个个图片     
        for i in range(1,4):#定义次数为3的循环（1，2，3）
            count+=1
            resize_image=img.resize((299,299),Image.ANTIALIAS)#将旋转后的图片变为299x299，Image.ANTIALIAS是表示高品质改尺寸
            rotate_resize_image=resize_image.rotate(i*90)#3次分别旋转了90，180，270度
            listStr = [str(int(time.time())), str(count)]#具体不清楚，作用是给前面处理过的图片命名
            fileName = ''.join(listStr)
            print(count)
            rotate_resize_image.save(object+os.sep+'%s.jpg' % fileName)#储存图片
            continue
alter("C:/Users/Alex/Desktop/cutnormal/",'C:/Users/Alex/Desktop/rotatecutnormal/')#这是需要传入的实参
