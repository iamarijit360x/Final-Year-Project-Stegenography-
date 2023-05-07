from Encode import encode
from Extract import extract
global nob
global s
while(True):
    ch=int(input("\n1.Encode\n2.Extract\n3.Exit\nEnter Choice:"))
    if(ch==1):
        nob=int(input("Enter Number Of Bits in LSB(3to8):")) 
        msg=input("Enter Secrect Message:")
        s=encode(msg,nob)
    elif(ch==2):
        print('SECRET MESSAGE :'+extract(nob,s))
    else:
        break