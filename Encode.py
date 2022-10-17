# -*- coding: utf-8 -*-
"""
Created on Thur Sept 22 

@author: Arijit
"""
from email.mime import image
from PIL import Image  
import numpy
from Utilites import add,string2bits,buck,change


nob=int(input("Number Of Bits:"))
ig='cat.jpg'#input("Enter Image name with extension/Image path:")
original_image = Image.open(ig) 
im=original_image.copy()
im=im.convert("L")

a=numpy.asarray(im) 
img_arr=numpy.copy(a)
#print(img_arr.flags["WRITEABLE"])
h=im.height
w=im.width

bucket=buck(nob)
print(bucket)

msg=input("Enter Secrect Messgae:")
msg_bin=list(string2bits(msg))
msg_arr=[]
for i in range(0,len(msg_bin)-1,2):
    msg_arr.append("".join(msg_bin[i:i+2]))
#print(msg_arr)



j=0
i=0
k=0
for k in range(len(msg_arr)):
    
    t=img_arr[i][j]
    
    t=list(format(t,"b"))
    t=t[-nob:]
    t="".join(t)
    
    c=change(int(t,2),msg_arr[j],bucket[msg_arr[k]],nob)
    print(f"IMG OLD={img_arr[i][j]} ",end=" ")
    if(c!=-1):
        c=list(format(c,'0'+str(nob)+'b'))
        #print(c)
        c="".join(c)
        t=img_arr[i][j]
    
        t=list(format(t,"b"))
        t=t[:-nob]
        t="".join(t)
        t=t+c
        img_arr[i][j]=int(t,2)
    print(f"IMG NEW={img_arr[i][j]}")
    j=j+1
    if(j==w):
        j=0
        i=i+1
    

        
             



im=Image.fromarray(numpy.asarray(img_arr))
im=im.save('stegoimg.PNG')
print('\n\nKEY=',len(msg_arr))


  
