# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 01:41:02 2022

@author: iamar
"""
from PIL import Image  
from PIL import Image, ImageChops,ImageOps
import numpy

ig="cat.jpg"
original_image = Image.open(ig) 
img1=original_image.copy()
img1=img1.convert("L")
img2=Image.open('stegoimg.PNG')
img3 = ImageChops.subtract(image1 = img1, image2 = img2)
img3=ImageOps.invert(img3)
img3.show()
arr=numpy.asarray(img3)

for i in range(60):
    print(arr[0][i])

  
