# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:10:09 2020

@author: jackb
"""

from PIL import Image, ImageFilter
import random

def getLists(images):
    #Container for im objects
    ims = []
    ws = []
    hs = []
    pixelsList = []
    i = 0
    imagesUsed = ""
    for image in images:
       #Note: make sure image paths are correct
       ims.append(Image.open('colors/{}.jpg'.format(image)))
       ws.append(ims[i].size[0]), hs.append(ims[i].size[1]) 
       pixels = ims[i].load()
       pixelsList.append(pixels)
       i += 1
       imagesUsed += image 
       
    return ims, ws, hs, pixelsList, imagesUsed
    

def getEdgeImage(filename):
    image = Image.open('images/{}'.format(filename)) 
  
    # Converting the image to greyscale, as edge detection  
    # requires input image to be of mode = Greyscale (L) 
    image = image.convert("L") 
  
    # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES 
    image = image.filter(ImageFilter.FIND_EDGES)
    
    #Convert the image back into RGB to perform pixel swapping
    image = image.convert("RGB") 

    return image



def swapPixels(images, edgeImage, scale):
    #Load in other images to swap pixels
    ims, ws, hs, pixelsList, imagesUsed = getLists(images)
    #Load pixels from edge image
    w,h = edgeImage.size
    edgePixels = edgeImage.load()


    #Loop over the specified number of pixels
    numPixels = w*h*scale//100  
    for _ in range(numPixels):
        
        #Get pairs of random coordinates
        col1 = random.randint(0, w - 1)
        row1 = random.randint(0, h - 1)

        col2 = random.randint(0, w - 1)
        row2 = random.randint(0, h - 1)
    
        #Capture particular pixels
        x = edgePixels[col1, row1]
        if _ % 2 == 0:
            col2 = random.randint(0, ws[0] - 1)
            row2 = random.randint(0, hs[0] - 1)
            y = pixelsList[0][col2, row2]
        
        else:
            col2 = random.randint(0, ws[1] - 1)
            row2 = random.randint(0, hs[1] - 1)
            y = pixelsList[1][col2, row2]


        #Swap pixels
        pixelsList[_ % 2][col2, row2],edgePixels[col1, row1] = x,y
        
    return edgeImage, imagesUsed

def main():
    #What images to swap from
    images = ["green", "red"]
    
    #What image to extract edges
    filename = 'icewall.jpg'
    edgeImage = getEdgeImage(filename)
    
    #Scale is the numerator percent of pixels swapped
    scale = 1     #Note: 50 will be half of the pixels
    
    NewImage, imagesUsed = swapPixels(images,edgeImage,scale)
    
    path = "images\Convoluted{}{}{}".format(str(scale), imagesUsed,filename)
    NewImage.save(path)
    
main()
