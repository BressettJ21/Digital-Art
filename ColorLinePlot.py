# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:33:37 2020

@author: jackb
"""

from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

im = Image.open('images/flowers-wall.jpg')
w, h = im.size
pixels = im.load()
print(pixels[2,3])
reds = []
greens = []
blues = []
def stripAllPixels(colNums,rowNums):
    #Slice Pixels into three color lists
    for i in range(rowNums):
        for j in range(colNums):
            red, green, blue = pixels[j,i]
            reds.append(red), greens.append(green), blues.append(blue)
    return reds,greens,blues

#colNums,rowNums = 4,4
#reds,greens,blues = stripAllPixels(colNums,rowNums)

avgRedRow = []
avgGreenRow = []
avgBlueRow = []
for i in range(h):
    for j in range(w):
        red, green, blue = pixels[j,i]
        reds.append(red), greens.append(green), blues.append(blue)
    avgRedRow.append(np.average(reds)),avgGreenRow.append(np.average(greens)),avgBlueRow.append(np.average(blues))
    reds = []
    greens = []
    blues = []
    


# Put data into Pandas Df
df=pd.DataFrame({'x': [i for i in range(len(avgRedRow))], 'Reds': avgRedRow, 'Greens': avgGreenRow, 'Blues': avgBlueRow})
 
# multiple line plot
plt.plot( 'x', 'Reds', data=df, marker='', color='red', linewidth=2)
plt.plot( 'x', 'Greens', data=df, marker='', color='green', linewidth=2)
plt.plot( 'x', 'Blues', data=df, marker='', color='blue', linewidth=2)
plt.legend()