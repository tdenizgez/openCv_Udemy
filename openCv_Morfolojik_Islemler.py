# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:56:36 2020

@author: tdenizgez
"""

import cv2
import numpy as np

"""
https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html
 Morphological transformations are some simple operations based on the image shape. 
 It is normally performed on binary images.
 It needs two inputs, one is our original image, second one is called structuring element or kernel
 which decides the nature of operation. 
 Two basic morphological operators are Erosion and Dilation.
 Then its variant forms like Opening, Closing, Gradient etc also comes into play.

"""

img = cv2.imread("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\heli.jpg",0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations=1) #Resme inceltme islemi gerceklestirir


kernel_1 = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations=1) #Resme kalınlaştırma islemi gerceklestirir

cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)

cv2.waitKey()
cv2.destroyAllWindows()