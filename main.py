from Encode import encode
import random
from Extract import extract
import cv2
from Utilites import generate_msg
global nob
while(True):
    ch=int(input("\n1.Encode\n2.Extract\n3.Random Insertion\nEnter Choice:"))
    if(ch==1):
        nob=int(input("Enter Number Of Bits in LSB(3to8):")) 
        msg=input("Enter Secrect Message:")
        encode(msg,nob)
    elif(ch==2):
        print(extract(nob))
    elif(ch==3):
        nob=random.randint(3,8)
        img = cv2.imread('cat.png')
        msg=generate_msg(round(img.shape[0] * img.shape[1] *0.009))
        print(f'Encoding Message Using {nob} of bits')
        print(extract(nob,encode(msg,nob)))

    else:
        break