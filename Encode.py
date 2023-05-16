# -*- coding: utf-8 -*-
"""
Created on Thur Sept 22 

@author: Arijit
"""
import cv2
from email.mime import image
from PIL import Image  
import numpy
from Utilites import add,string2bits,buck,change,generate_msg
from SkinDetection import skind,detect_pixel
def encode(msg,nob,mode):
    ###TESTING

    sucess_cord=[]

    ####
    ig='cat.png'#input("Enter Image name with extension/Image path:")
    img_arr = cv2.imread(ig)
    #print(img_arr.flags["WRITEABLE"])
    h=img_arr.shape[0]
    w=img_arr.shape[1]
    cord=skind(ig,1)
    MAX=(len(cord)*3*2)//8
    bucket=buck(nob)
  
    ####
    if mode:
     msg=generate_msg(MAX)
    ####
    msg_gen=open("msg_gen.txt","w")
    msg_gen.write(msg)
    msg_gen.close()

    msg_bin=list(string2bits(msg))
    f=open("msg.txt","w")
    for m in msg_bin:
        f.write(m) 
    msg_arr=[]
    for i in range(0,len(msg_bin)-1,2):
        msg_arr.append("".join(msg_bin[i:i+2]))
    
    #print(msg_arr)

    #print("SKIN PIXEL")
    #for c in range(12):
        #print(cord[c])
    #print(cord)
    LL=0
    j=0
    i=0
    k=0
    rgb=0
    msg_index=0
    flag=False
    while(k<len(cord)):
        i=cord[k][0]
        j=cord[k][1]
        #print(f"i={i} j={j}")
        
        #print(f"TRYING COORDINATES {i},{j}   MSG_BITS={msg_arr[msg_index]} {msg_arr[msg_index+1]} {msg_arr[msg_index+2]}")
        for rgb in range(0,3):
            
            if(msg_index==len(msg_arr)):
                flag=True
                break
            #print(f"MSGBIT{msg_index}:{msg_arr[msg_index]}")
            t=img_arr[i][j][rgb]
            #print(f"{i}{j}{rgb}")
            t=list(format(t,"b"))
            t=t[-nob:]
            t="".join(t)
            #print(f"IMG OLD={img_arr[i][j][rgb]} ",end=" ") 
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
            #print(f"IMG NEW={img_arr[i][j][rgb]} {add(img_arr[i][j][rgb],nob)} ")
        if(not(detect_pixel(img_arr[i][j]))):
           # print('Falied',i,j)
            #print(f"IMG NEW={img_arr[i][j]}")
            if(msg_index!=0):
                msg_index-=3
            
        else:
            #print(f"Sucess COORDINATES {i},{j}")
            sucess_cord.append([i,j])
            LL+=6
         
        if(flag):
            break
               
            #print(f"DATA NEW={add(img_arr[i][j],nob)} ",end=" ")
           #print(f"  IMG NEW={img_arr[i][j][rgb]}  {format(img_arr[i][j][rgb],'b')}")
        
        k+=1
       
    print(f"Message Length={LL//8}  Max Length={MAX}")
    msg_gen=open("msg_gen.txt","a")
    msg_gen.write(msg[:LL//8])
    msg_gen.close()

    cv2.imwrite('stegoimg.PNG',img_arr)
    ####
    #img_arr = cv2.imread('stegoimg.PNG')
    #for i in range(len(sucess_cord)):
        #print(sucess_cord[i][0],sucess_cord[i][1],img_arr[sucess_cord[i][0]][sucess_cord[i][1]])
    ####
    print('\n\nKEY=',LL//2)

   

        
