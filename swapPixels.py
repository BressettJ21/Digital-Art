# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:14:47 2020

@author: jackb
"""

from PIL import Image
import random

im = Image.open('images/flowers-wall.jpg')
w, h = im.size
pixels = im.load()

#Scale is the numerator percent of pixels swapped

scale = 15      #Note: 50 will be half of the pixels



#Loop over the specified number of pixels
numPixels = w*h*scale//100
for _ in range(numPixels):
    #Get pairs of random coordinates

    col1 = random.randint(0, w - 1)
    row1 = random.randint(0, h - 1)

    col2 = random.randint(0, w - 1)
    row2 = random.randint(0, h - 1)
    
    #Capture particular pixels
    x = pixels[col1, row1]
    y = pixels[col2, row2]

    #Swap pixels
    pixels[col2, row2],pixels[col1, row1] = x,y




im.show()