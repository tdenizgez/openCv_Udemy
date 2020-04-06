# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:39:40 2020

@author: tdenizgez
"""


import cv2
import numpy as np

def nothing(x):
    pass


img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow("image")

# trackbar olusturma.
cv2.createTrackbar("R", "image", 0, 255, nothing) #Renk Kodu,windowAdi,renk araligi bas,renk araligi son,onChange
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)


while(True):
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")

    img[:] = [r,g,b]
    cv2.imshow("image",img)
    k= cv2.waitKey(1) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        break
    




