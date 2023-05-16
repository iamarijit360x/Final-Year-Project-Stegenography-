import cv2
import numpy as np
arr=[]
for i in range(0,255):
    for j in range(0,255):
        temp=[]
        for k in range(0,255):
            temp.append([i,j,k])
        arr.append(temp)
arr=np.array(arr)
cv2.imwrite('test.png',arr)
