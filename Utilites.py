# -*- coding: utf-8 -*-
"""
Created on Thur Sept 22 

@author: Arijit
"""
from re import I
import random

def add(n,nob): #returns Binary addition of last nob bits
    b=format(n,"b")
   
    x=(list(b))[::-1]
    x=x[:nob]
  
    n1=x.count('1')
    if(n1==0 or n1==4 or n1==8):
        s='00'
    elif(n1==1 or n1==5):
        s='01'
    elif(n1==2 or n1==6):
        s='10'
    elif(n1==3 or n1==7):
        s='11'
    return s
def bit2strings(b=None): 
    return ''.join([chr(int(x,2)) for x in b])

def string2bits(s=""):
    return "".join([bin(ord(x)) [2:].zfill(8) for x in s])

def buck(nob): #returns dictionary of bucket containing 00 01 10 11
    bucket={}
    for i in range(0,2**nob):
        try:
            bucket[add(i,nob)].append(i)
        except:
            bucket[add(i,nob)]=[]
            bucket[add(i,nob)].append(i)
            
    return bucket
def change(pixel,data,temp,nob): #returns the change requried in last 4 bits of the number in the corresponding pixel 
    if(add(pixel,nob)==data):
        #print("No Chnage")
        return -1
    else:
        l=0
        r=len(temp)-1
        
        
        diff=1000
        e=''
        pp=list(((format(pixel,"b"))))
        pp=pp[-nob:]
        pp="".join(pp)
        pp=int(pp,2)
       
        for i in temp:
            x=abs(i-pp)
            if(x<diff):
                diff=x
                e=i
        return e
def generate_msg(N):
    arr=[]
    arrn=[]
    arrs=[]
    for i in range(33,42):
        arrs.append(chr(i))
    for i in range(ord('A'),ord('Z')):
        arr.append(chr(i))
    for i in range(0,10):
        arrn.append(i)
    x=""
    for i in range(N):
        ch=random.randint(0,2)
        if(ch==1):
            r=random.randint(0,1)
            if(r):
                x=x+random.choice(arr)
            else:
                x=x+random.choice(arr).lower()
        elif(ch==2):
            x=x+str(random.choice(arrn))
        else:
            x=x+random.choice(arrs)
    x=list(x)

        
    for b in range(100):
        i=random.randint(0, len(x)-1)
        j=random.randint(0, len(x)-1)
        x[i],x[j]=x[j],x[i]    
    return ("".join(x))


def PSNR(img1, img2, max_value=255):
    img1=Image.open(img1)
    img2=Image.open(img2)
    mse = np.mean((np.array(img1, dtype=np.float32) - np.array(img2, dtype=np.float32)) ** 2)
    if mse == 0:
        return 100
    return 20 * np.log10(max_value / (np.sqrt(mse)))
