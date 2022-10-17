# -*- coding: utf-8 -*-
"""
Created on Thur Sept 22 

@author: Arijit
"""

from traceback import print_tb
from PIL import Image  
import numpy




ig='cat.jpg'#input("Enter Image name with extension/Image path:")
original_image = Image.open(ig) 
im=original_image.copy()
im=im.convert("L")

a=numpy.asarray(im) 
img_arr=numpy.copy(a)
#print(img_arr.flags["WRITEABLE"])
h=im.height
w=im.width
print(h,w)
i=0
j=0
while(True):
    print(img_arr[i][j] ,end=" ")
    j=j+1
    if(j==w):
        j=0
        i=i+1
        print("\n")
    


