import cv2
import numpy as np
arr=[[[122,255,344]]]
arr=np.array(arr)
cv2.imwrite('singel.png',arr)
print(arr)