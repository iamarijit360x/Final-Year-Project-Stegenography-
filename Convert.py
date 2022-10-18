
import numpy,os
from PIL import Image  
path=os.getcwd()+'/Image/'
print(path)
IMAGES=(os.listdir(path))


def convert(ig,x,y):
    original_image = Image.open(ig)
    im=original_image.copy()
    im=im.convert("L")
    width, height = im.size   # Get dimensions

    left = (width - x)/2
    top = (height - y)/2
    right = (width + x)/2
    bottom = (height + y)/2

    # Crop the center of the image
    im = im.crop((left, top, right, bottom))
    os.remove(ig)
    im=im.save((ig[:-4])+'.PNG')

x=int(input("Enter Height:")) 
y=int(input("Enter Width:"))     
for img in IMAGES:
    convert(path+img,x,y)
    
