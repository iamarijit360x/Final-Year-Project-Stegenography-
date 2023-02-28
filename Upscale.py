import cv2
import time
import os,numpy
from PIL import Image
import numpy as np
from os import listdir

i = 1

path=os.getcwd()
img_path=path+'/HR/'
save_path = path + '/Output/'
IMAGES=os.listdir(img_path)
IMAGES.sort()

for img in IMAGES:
    if (img.endswith(".png")):
        imgK = os.path.join(img_path, img)
        imgR = cv2.imread(imgK)
        width = imgR.shape[1]
        height = imgR.shape[0]
        bicubic = cv2.resize(imgR,(width*4,height*4))

        super_res = cv2.dnn_superres.DnnSuperResImpl_create()

        start = time.time()
        super_res.readModel('FSRCNN_x4.pb')
        super_res.setModel('fsrcnn',4)
        fsrcnn_image = super_res.upsample(imgR)
        end = time.time()
        k = str(i)
        i = i+1
        print('Time taken in seconds by fsrcnn for image' + k, end-start)
        cv2.imwrite(os.path.join(save_path , 'fsrcnn_output' + k + '.jpg'),fsrcnn_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#     cv2.imshow('Image',img)
#     cv2.imshow('BICUBIC',bicubic)
#     cv2.imshow('FSRCNN',fsrcnn_image)
