import re
from StegoAlgo import encode,extract
import os,numpy
from PIL import Image
from math import log10, sqrt
import numpy as np
import random
from Utilites import generate_msg,PSNR
import csv


path=os.getcwd()
img_path=path+'/Image/'
stego_path=path+'/Stego/'
IMAGES=os.listdir(img_path)
IMAGES.sort()

global nob
nob=6
im=Image.open(img_path+IMAGES[0])
msg_size=(im.height*im.width)//4 

msgx=generate_msg(msg_size)
f=open("msg.txt","w")
f.write(msgx)
f.close()

f=open("extracted_msg.txt","w")
f.truncate(0)
f.close()

f=open("PSNR_INFO.txt","w")
f.write('Image Name'+'     '+'  PSNR  ')
f.close()

#msg="ARIJIT BANERJEE"
for nob in range(3,9):
    for img in IMAGES:
        x=encode(msgx,nob,img_path,img,stego_path)
        #print(img,'Encoding DONE')

    STEGO=os.listdir(stego_path)
    STEGO.sort()
    #print(IMAGES)
    #print(STEGO)

    for img in STEGO:
        f=open("extracted_msg.txt","a")
        f.write(extract(nob,x,stego_path+img)+'\n')
        f.close()
    f=open("PSNR_INFO.txt","a")
    f.write('\n'+"----------------------No of LSB Bits Used----------------------: "+str(nob)+'\n')
    f.close()
    print("No of LSB Bits Used : ",nob)
    for i in range(len(IMAGES)):
        f=open("PSNR_INFO.txt","a")
        f.write(IMAGES[i]+' '+str(PSNR(img_path+IMAGES[i],stego_path+STEGO[i]))+'\n')
        f.close()
        print(f"{IMAGES[i]} {PSNR(img_path+IMAGES[i],stego_path+STEGO[i])}")







