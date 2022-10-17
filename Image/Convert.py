
import numpy,os
from PIL import Image  
path=os.getcwd()
IMAGES=(os.listdir(path))


def convert(ig):
    original_image = Image.open(ig)
    im=original_image.copy()
    im=im.convert("L")
    os.remove(ig)
    im=im.save((ig[:-4])+'.PNG')

    
for img in IMAGES[1:]:
    convert(img)
    
