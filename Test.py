from Encode import encode
from Extract import extract
import numpy,os
path=os.getcwd()
img_path=path+'/Image'
stego_path=path+'/Stego'
IMAGES=os.listdir(img_path)
STEGo=os.listdir(stego_path)

global nob
nob=6
msg="ARIJIT BANERJEE CSE"
for img in IMAGES[1:]:
    x=encode(msg,nob,img_path,img,stego_path)
for img in STEGO[1:]:
    print('\nSecrect Message : '+extract(nob,x,stego_path+img+'_stego.PNG'))
    
