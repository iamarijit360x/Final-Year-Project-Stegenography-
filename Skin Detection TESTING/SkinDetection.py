import cv2
import numpy as np
def detect(img):
    img=cv2.imread(img)
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #skin color range for hsv color space 
    HSV_mask = cv2.inRange(img_HSV, (0, 15, 0), (17,170,255)) 
    HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

    #converting from gbr to YCbCr color space
    img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    #skin color range for hsv color space 
    YCrCb_mask = cv2.inRange(img_YCrCb, (0, 135, 85), (255,180,135)) 
    YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

    #merge skin detection (YCbCr and hsv)
    global_mask=cv2.bitwise_and(YCrCb_mask,HSV_mask)
    global_mask=cv2.medianBlur(global_mask,3)
    global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4,4), np.uint8))


    HSV_result = cv2.bitwise_not(HSV_mask)
    YCrCb_result = cv2.bitwise_not(YCrCb_mask)

 
    global_mask=cv2.bitwise_not(global_mask)



    #show results
    # cv2.imshow("1_HSV.jpg",HSV_result)
    # cv2.imshow("2_YCbCr.jpg",YCrCb_result)
    # cv2.imshow("3_global_result.jpg",global_result)
    # cv2.imshow("Image.jpg",img)
    # Convert the image to grayscale

    cv2.imwrite("3_global_result.jpg",global_mask)

    #_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
    f=open('c.txt',"w")
    #cv2.imwrite("img"+str(r)+".png",thresh)
    color_value=[]
    coordinates = np.column_stack(np.where(global_mask == 0))
    for cord in coordinates:   
        x=cord[0]
        y=cord[1]
        #print(img[x][y][0])
        #f.write(str(img[x][y])+'\n')
        color_value.append(img[x][y])
    f=open('RANGE.txt',"w")
    min_max=[]
    temp=color_value[0][0]
    min=255
    max=0
    for r in color_value:
        if(r[0]==temp):
            if(r[1]<min):
                min=r[1]
            elif(r[1]>max):
                max=r[1]
        else:
            min_max.append([min,max])
            print(f"R={temp} G-{min,max}")
            #f.write(str(temp)+' '+str(min)+','+str(max)+'\n')
            min=255
            max=0
            temp=temp + 1

        
    f=open('RANGE_GB.txt',"w")
    max=0
    min=255
    temp=color_value[0][1]
    temp_r=555
    for r in color_value:
        if(temp_r!=r[0]):
            f.write('------------------------------------------------------'+'\n')
            #print(f"R={r[0]}")
            f.write('R='+str(r[0])+'\n')
           
            temp_r=r[0]
        
        if(temp==r[1]):
            if(r[2]>max):
                max=r[2]
            if(r[2]<min):
                min=r[2]
        else:
            #print(f"G={temp} B-{min,max}")
            f.write('G='+str(temp)+' B-'+str(min)+','+str(max)+'\n')
            max=0
            min=255
            temp=r[1]
            



    
    
        
        
    


detect('test.png')