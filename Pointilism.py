# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:45:42 2020

@author: jackb
"""

from PIL import Image
import random

im = Image.open('images/CornellLeaveswithChapel.jpg')
w, h = im.size
pixels = im.load()

scale = 50
numPixels = w*h*scale//100



# Curruption by adding random pixels:

for _ in range(numPixels):
    #Create a random color to fill the pixel instead of only black. This will increase corruption in the image
    colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pixels[random.randint(0, w - 1), random.randint(0, h - 1)] = colors


im.show()
