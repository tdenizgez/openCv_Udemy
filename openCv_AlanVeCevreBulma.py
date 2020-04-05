# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:47:51 2020

@author: tdenizgez
"""


import cv2

img = cv2.imread(r"C:/Users/tdenizgez/Desktop/OpenCv/Dosyalar/contour.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255,cv2.THRESH_BINARY)
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
area = cv2.contourArea(cnt) 
print(area)
M = cv2.moments(cnt)
print(M['m00'])#--> Alanı Vermekte 

perimeter = cv2.arcLength(cnt,True)
print(perimeter)


"""

cv2.imshow("original",img)
cv2.imshow("gray",gray)
cv2.imshow("thresh",thresh)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""