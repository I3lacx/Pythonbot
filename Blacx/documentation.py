#This is the manmade documentation where you can see some examples
#and how to use opencv or cv2
#The code is commented and different possibilites are written down
#some code is commented, this is just so you can switch easier between
#two options

#standard imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'C:\\Users\\Maxi\\Documents\\Programmieren\\Python\\opencv\\'

#with imread you can read an image from your work place into Python
#the last part is in which style so: (these are all variables for numbers)
#IMREAD_COLOR <- 1
#IMREAD_GRAYSCALE <- 0
#IMREAD_UNCHANGED <- -1
img = cv2.imread(path + "watch.jpg",cv2.IMREAD_GRAYSCALE) # <- 0


#with imshow you can show an image 'image' is the window name and img the image
cv2.imshow('image', img)
#program halts until key is pressed
cv2.waitKey(0)
#destroy all cv related windows
cv2.destroyAllWindows()

#you can show pictures using pyplot:
#NOTE: conversion from colors is different (BGR <-> RGB)
#use interplotation to avoid to cubic images
plt.imshow(img, cmap='gray', interpolation='bicubic')
#you can even paint a function onto the picture
plt.plot([50,100],[150,300],'c',linewidth=5)
plt.show()

#save the image as 'watchgray.png'
cv2.imwrite(path + 'watchgray.png', img)
