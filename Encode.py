# -*- coding: utf-8 -*-
"""
Created on Thur Sept 22 

@author: Arijit
"""
import cv2
from email.mime import image
from PIL import Image  
import numpy
from Utilites import add,string2bits,buck,change
from SkinDetection import skind

def encode(msg,nob):
    ig='cat.png'#input("Enter Image name with extension/Image path:")
    img_arr = cv2.imread(ig)
    #print(img_arr.flags["WRITEABLE"])
    h=img_arr.shape[0]
    w=img_arr.shape[1]
    #print(h,w)
    bucket=buck(nob)
    #print(bucket)
    msg_bin=list(string2bits(msg))
    f=open("msg.txt","w")
    for m in msg_bin:
        f.write(m) 
    msg_arr=[]
    for i in range(0,len(msg_bin)-1,2):
        msg_arr.append("".join(msg_bin[i:i+2]))
    
    print(msg_arr)
    cord=skind(ig,1)
    #for c in cord:
        #print(img_arr[c[0]][c[1]])
    #print(cord)
    j=0
    i=0
    k=0
    rgb=0
    msg_index=0
    flag=False
    for k in range(len(msg_arr)):
        i=cord[k][0]
        j=cord[k][1]
        print(f"i={i} j={j}")
        
        
        for rgb in range(0,3):
            if(msg_index==len(msg_arr)):
                flag=True
                break
            t=img_arr[i][j][rgb]
            #print(f"{i}{j}{rgb}")
            t=list(format(t,"b"))
            t=t[-nob:]
            t="".join(t)
            print(f"IMG OLD={img_arr[i][j][rgb]} ",end=" ") 
            c=change(int(t,2),msg_arr[msg_index],bucket[msg_arr[msg_index]],nob)
            
           # print(f"IMG OLD={img_arr[i][j][rgb]} {format(img_arr[i][j][rgb],'b')}",end=" ")
            #print(f"DATA={msg_arr[k]},ImgPixel={t},chnage Needed={c} " ,end=" ")
            
            if(c!=-1):
                c=list(format(c,'0'+str(nob)+'b'))
                #print(c)
                c="".join(c)
                t=img_arr[i][j][rgb]

                t=list(format(t,"b"))
                t=t[:-nob]
                t="".join(t)
                t=t+c
                img_arr[i][j][rgb]=int(t,2)
            msg_index+=1
            print(f"IMG NEW={img_arr[i][j][rgb]} {add(img_arr[i][j][rgb],nob)} ")
           
        if(flag):
            break
               
            #print(f"DATA NEW={add(img_arr[i][j],nob)} ",end=" ")
           #print(f"  IMG NEW={img_arr[i][j][rgb]}  {format(img_arr[i][j][rgb],'b')}")
        
        
       
        


    cv2.imwrite('stegoimg.PNG',img_arr)
    print('\n\nKEY=',len(msg_arr))
    

        
