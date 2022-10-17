# -*- coding: utf-8 -*-
"""
Created on Thur Sept 22 

@author: Arijit
"""


from PIL import Image  
import numpy
from Utilites import add,bit2strings



original_image = Image.open('stegoimg.PNG') 
im=original_image.copy()
a=numpy.asarray(im) 
img_arr=numpy.copy(a)
key=int(input("Enter Key:"))
Data=[]
check=0
for i in range(im.height):
    for j in range(im.width):
        Data.append(add(img_arr[i][j],4))
        check+=1
        if(check==key):
            break
    if(check==key):
        break




Data2=[]
for i in range(0,key,4):
    Data2.append("".join(Data[i:i+4]))
print(bit2strings(Data2))
