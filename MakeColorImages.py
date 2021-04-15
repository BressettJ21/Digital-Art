# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:34:56 2020

@author: jackb
"""


from PIL import Image

width = 750
height = 750

colors = {"red":(255,0,0), "green":(0, 255, 0), "blue":(0,0,255), "yellow":(255,255,0), "purple":(255,0,255)}

for color in colors:
    image = Image.new("RGB", (width, height), colors[color])
    
    #Save with unique path
    path = "colors\{}.jpg".format(color)
    image.save(path)