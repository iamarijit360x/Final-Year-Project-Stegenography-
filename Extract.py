# -*- coding: utf-8 -*-
"""
Created on Thur Sept 22 

@author: Arijit
"""

import cv2
from PIL import Image  
import numpy
from Utilites import add,bit2strings
from SkinDetection import skind
def extract(nob):
    ig='stegoimg.PNG'
    #nob=int(input("Number Of Bits:"))
    img_arr = cv2.imread('stegoimg.PNG') 
    key=int(input("Enter Key:"))
    Data=[]
    check=0
    h=img_arr.shape[0]
    w=img_arr.shape[1]
   
   
    cord=skind(ig,2)
    print(len(cord))
    ###
    #for i in range(key):
        #print(cord[i])
    ###
    rgb=0
    check=0
    flag=False
    for k in range(len(cord)):
        i=cord[k][0]
        j=cord[k][1]
        #print(f"I={i},J={j}")
        
        for rgb in range(0,3):
            #print(f"IMG={img_arr[i][j][rgb]} {format(img_arr[i][j][rgb],'b')} Add_return={add(img_arr[i][j][rgb],nob)}")
            #print(f"IMG ={img_arr[i][j][rgb]}")
            Data.append(add(img_arr[i][j][rgb],nob))
            check+=1
            if(check==key):
                flag=True
                break
        if(flag):
            break

    f=open("msg.txt","a")
    f.write("\n-----\n")
    


    Data2=[]
    for i in range(0,key,4):
        Data2.append("".join(Data[i:i+4]))

    for m in Data2:
        f.write(m) 

    f=open("msg_rec.txt","w")
    msg=(bit2strings(Data2))
    f.write(msg)
    return msg
