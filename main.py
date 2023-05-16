from Encode import encode
from Extract import extract
global nob
while(True):
    ch=int(input("\n1.Encode\n2.Extract\n3.Exit\nEnter Choice:"))
    if(ch==1):
        nob=int(input("Enter Number Of Bits in LSB(3to8):")) 
        msg=input("Enter Secrect Message:")
        mode=False
        if msg=='RI':
            mode=True
        s=encode(msg,nob,mode)
    elif(ch==2):
        print('\nSECRET MESSAGE :'+extract(nob))
    else:
        break