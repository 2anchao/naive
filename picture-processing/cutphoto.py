# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 14:42:03 2018

@author: Alex
"""

import os
import time
from PIL import Image
import numpy as np

def cut_image(image):  
    width,height=image.size#得到我们图片的尺寸
    item_width=int(width/3)  #宽除以3
    item_height=int(height/3)#高除以3
    box_list=[]  #定义一个空的列表
    cout=0  
    for j in range(0,3):  
        for i in range(0,3):  
            cout+=1  
            box=(i*item_width,j*item_height,(i+1)*item_width,(j+1)*item_height)  #区域由一个4元组定义，表示为坐标是 (left, upper, right, lower)，j=0，i=0时，截取九宫格左上角，j=0，i=1时，朝右移动一下
            box_list.append(box)#九个box加到了list  
    print(cout)  
    image_list=[image.crop(box) for box in box_list]#得到所有用九宫格切出来的图片  
    return image_list
def alter(path,object):
    s = os.listdir(path)
    count=1
    for i in s:
        document = os.path.join(path,i)#作用是目录地址分别和每一个图片名字结合
        img = Image.open(document)#打开目录下的一个个图片
        cuted_img_list=cut_image(img)#调用前面的cut_image函数
        for cuted_img in cuted_img_list:#遍历list里面的所有图片并命名
            count += 1
            listStr = [str(int(time.time())), str(count)]
            fileName = ''.join(listStr)
            print(count)
            cuted_img.save(object+os.sep+'%s.jpg' % fileName)#储存图片
            continue
alter("C:/Users/Alex/Desktop/normal/",'C:/Users/Alex/Desktop/cutnormal/')#这是需要传入的实参
