# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 02:39:48 2021

@author: abc
"""
"""
from scipy import misc
img = misc.array("C:/Users/abc/Desktop/image/test_image.jpg")
print(type(img))
"""

"""
from skimage import io , img_as_ubyte
img = img_as_ubyte(io.imread("C:/Users/abc/Desktop/image/test_image.jpg",as_gray=True))

print(img.dtype,img.shape)

print(img[0,0])

print(img[10:15,20:25])

mean_grey = img.mean()
max_value = img.max()
min_value = img.min()

print("Min ,Max and Mean are :",min_value,max_value,mean_grey)
"""

from skimage import io,img_as_ubyte
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt

img = img_as_ubyte(io.imread("C:/Users/abc/Desktop/image/test_image.jpg",as_gray=True))

flippedLR = np.fliplr(img)
flippedUD = np.flipud(img)

plt.subplot(2,1,1)
plt.imshow(img,cmap="Greys")
plt.subplot(2,2,3)
plt.imshow(flippedLR,cmap = "Blues")
plt.subplot(2,2,4)
plt.imshow(flippedUD,cmap = "hsv")











