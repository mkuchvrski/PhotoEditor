from pickle import EMPTY_DICT
from PIL import Image, ImageEnhance, ImageFilter
import os


path = './img'
pathOut = '/editedImgs'

for filename in os.listdir(path):

    #get an image from the folder
    img = Image.open(f"{path}/{filename}")

    #turn photo to black and white and rotate upside down
    edit = img.filter(ImageFilter.SHARPEN).convert("L").rotate(180)

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    #get name without .jpg
    clean_name = os.path.splitext(filename)[0]
    
    #save image in new directory
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
