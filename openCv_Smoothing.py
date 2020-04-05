# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:20:21 2020

@author: tdenizgez
"""


import cv2
import numpy as np

img_filter = cv2.imread("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\filter.png")
img_median = cv2.imread("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\median.png")
img_bilateral = cv2.imread("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\bilateral.png")

blur =cv2.blur(img_filter,(5,5))
blur_g=cv2.GaussianBlur(img_filter, (3,3), 5)
blur_m = cv2.medianBlur(img_median,7)
blur_b = cv2.bilateralFilter(img_bilateral,9,95,95)


cv2.imshow("original1",img_filter)
cv2.imshow("blur_g",blur_g)

    
cv2.imshow("original2",img_median)
cv2.imshow("blur_m",blur_m)


cv2.imshow("original3",img_bilateral)
cv2.imshow("blur_b",blur_b)


cv2.waitKey(0)
cv2.destroyAllWindows()