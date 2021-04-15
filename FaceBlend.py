# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 12:31:24 2020

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
       ims.append(Image.open('MyFaces/Artsy/{}.jpg'.format(image)).resize((800,753)))
       ws.append(ims[i].size[0]), hs.append(ims[i].size[1]) 
       pixels = ims[i].load()
       pixelsList.append(pixels)
       i += 1
       imagesUsed += image 
       
    return ims, ws, hs, pixelsList, imagesUsed
    





def swapPixels(images,scale):
    #Load in other images to swap pixels
    ims, ws, hs, pixelsList, imagesUsed = getLists(images)
    
    #Seperate and copy base image
    baseImage = ims.pop(0).copy()
    
    #Get Base Dimensions
    w,h = baseImage.size
    
    #Get pixels from baseImage
    originalPixels = baseImage.load()
    
    #Loop over the specified number of pixels
    numPixels = w*h*scale//100
    
    for _ in range(numPixels):
            
        #Get pair of random coordinates
        col = random.randint(0, w - 1)
        row = random.randint(0, h - 1)

    
        #Capture particular pixel
        x = pixelsList[1][col, row]
            
        #Replace pixels
        originalPixels[col, row] = x
            
        
    return baseImage, imagesUsed

def main():
    #What images to swap from
    images = ["SurprisedPink", "SadBlue"]     #Note: your main image is the first image
    description = ""
    for i in range(len(images)):
        description = description + images[i] 
    
    ProcessedImages = []
    #Scale is the numerator percent of pixels swapped
    scale = 1      #Note: 50 will be half of the pixels
    
    #newImage, imagesUsed = swapPixels(images,scale)
    
    #path = "MyFaces/overlapped/{}{}.png".format(str(scale), imagesUsed)

    #newImage.save(path)
    
    
    numFrames = 30

    for i in range(numFrames):
        if i < numFrames//2:
            scale += 8
            print("nasty", scale)
            currentIm, imagesUsed = swapPixels(images,scale)
            ProcessedImages.append(currentIm)
        else:
            scale -= 8
            print("flip", scale)
            currentIm, imagesUsed = swapPixels(images,scale)
            ProcessedImages.append(currentIm)



    #save Gif

    currentIm.save('gifs/DoubleExposure{}{}.gif'.format(description, str(numFrames)),
               save_all=True,
               append_images=ProcessedImages,
               duration=20,
               loop=0)
 
main()
