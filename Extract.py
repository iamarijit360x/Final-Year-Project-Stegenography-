# -*- coding: utf-8 -*-
"""
Created on Thur Sept 22 

@author: Arijit
"""

import cv2
from PIL import Image  
import numpy
from Utilites import add,bit2strings

def extract(nob,key=""):
    #nob=int(input("Number Of Bits:"))
    img_arr = cv2.imread('stegoimg.PNG')
    if(key==""): 
        key=int(input("Enter Key:"))
    Data=[]
    check=0
    h=img_arr.shape[0]
    w=img_arr.shape[1]
    i=0
    j=0
    rgb=0
    while(True):
        print(f"IMG={img_arr[i][j][rgb]} {format(img_arr[i][j][rgb],'b')} Add_return={add(img_arr[i][j][rgb],nob)}")
        Data.append(add(img_arr[i][j][rgb],nob))
        check+=1
        rgb+=1
        if(rgb==3):
            rgb=0
            j=j+1
        if(j==w):
            j=0
            i=i+1
        
        if(check==key):
            break


    f=open("msg.txt","a")
    f.write("\n")
    


    Data2=[]
    for i in range(0,key,4):
        Data2.append("".join(Data[i:i+4]))

    for m in Data2:
        f.write(m) 
    return (bit2strings(Data2))
