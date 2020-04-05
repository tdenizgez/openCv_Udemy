# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:50:49 2020

@author: tdenizgez
"""

import cv2
import numpy as np


def nothing(x):
    pass



cv2.namedWindow("Tracbar")
cv2.resizeWindow("Tracbar",500,250)


cv2.createTrackbar("Lower-H","Tracbar",0,180,nothing)
cv2.createTrackbar("Lower-S","Tracbar",0,255,nothing)
cv2.createTrackbar("Lower-V","Tracbar",0,255,nothing)

cv2.createTrackbar("Upper-H","Tracbar",0,180,nothing)
cv2.createTrackbar("Upper-S","Tracbar",0,255,nothing)
cv2.createTrackbar("Upper-V","Tracbar",0,255,nothing)

cap = cv2.VideoCapture(0)

while 1:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lh = cv2.getTrackbarPos("Lower-H","Tracbar")
    ls = cv2.getTrackbarPos("Lower-S","Tracbar")
    lv = cv2.getTrackbarPos("Lower-V","Tracbar")
    
    uh = cv2.getTrackbarPos("Upper-H","Tracbar")
    us = cv2.getTrackbarPos("Upper-S","Tracbar")
    uv = cv2.getTrackbarPos("Upper-V","Tracbar")

    lower_color = np.array([lh,ls,lv])
    upper_color = np.array([uh,us,uv])

    mask  = cv2.inRange(hsv,lower_color,upper_color)
    
    cv2.imshow("original", frame)
    cv2.imshow("hsv",mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()